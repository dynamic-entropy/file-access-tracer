#!/usr/bin/env python3
"""Import CMS Rucio RSEs into campaign/sites.csv."""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from pathlib import Path

FIELDS = [
    "rse",
    "site",
    "tier",
    "storage_tech",
    "protocol_primary",
    "endpoint_url",
    "capture_method",
    "tracer_status",
    "last_probe_at",
    "last_probe_result",
    "probe_did",
    "notes",
    "contact",
]

# Prefer these schemes for probe reads (first match wins).
SCHEME_PREFERENCE = ("root", "xroot", "davs", "https", "gsiftp", "srm")


def infer_site(rse: str, attrs: dict) -> str:
    # Prefer PhEDEx/CMS site code over full RSE-like pnn when possible.
    pnn = str(attrs.get("pnn") or "")
    m = re.match(r"^(T[0-3]_[A-Z]{2}_[A-Za-z0-9-]+?)(?:_(?:Disk|Tape|Buffer|MSS|Temp|Test).*)?$", rse)
    if m:
        return m.group(1)
    m = re.match(r"^(T[0-3]_[A-Z]{2}_[A-Za-z0-9-]+?)(?:_(?:Disk|Tape|Buffer|MSS|Temp|Test).*)?$", pnn)
    if m:
        return m.group(1)
    if pnn:
        return pnn
    parts = rse.rsplit("_", 1)
    return parts[0] if len(parts) == 2 else rse


def infer_storage_tech(rse: str, attrs: dict, protocols: list[dict]) -> str:
    blob = " ".join(
        [
            rse.lower(),
            str(attrs.get("oidc_base_path", "")).lower(),
            str(attrs.get("CE_config.server", "")).lower(),
            " ".join(
                f"{p.get('hostname', '')} {p.get('prefix', '')} {p.get('impl', '')}"
                for p in protocols
            ).lower(),
        ]
    )
    if "eos" in blob or "eoscms" in blob:
        return "EOS"
    if "storm" in blob or "/stoRM" in blob:
        return "StoRM"
    if "dcache" in blob or "/pnfs/" in blob or "pnfs." in blob:
        return "dCache"
    if "xroot" in blob or any(p.get("scheme") in ("root", "xroot") for p in protocols):
        # root:// alone is ambiguous (EOS, StoRM, plain XRootD, dCache door)
        if any(
            (p.get("prefix") or "").startswith("/eos")
            or "eos" in (p.get("hostname") or "").lower()
            for p in protocols
        ):
            return "EOS"
        if any("/pnfs/" in (p.get("prefix") or "") for p in protocols):
            return "dCache"
        return "XRootD"
    if any(p.get("scheme") in ("davs", "https") for p in protocols):
        return "unknown"
    return "unknown"


def capture_method_for(tech: str) -> str:
    return {
        "EOS": "ofs.notify",
        "XRootD": "ofs.notify",
        "dCache": "dcache.kafka",
        "StoRM": "deferred",
    }.get(tech, "unknown")


def pick_protocol(protocols: list[dict]) -> tuple[str, str]:
    by_scheme = {p.get("scheme"): p for p in protocols if p.get("scheme")}
    for scheme in SCHEME_PREFERENCE:
        p = by_scheme.get(scheme)
        if not p:
            continue
        host = p.get("hostname") or ""
        port = p.get("port")
        prefix = p.get("prefix") or "/"
        if scheme in ("root", "xroot"):
            url = f"root://{host}:{port}/" if port else f"root://{host}/"
        elif scheme in ("davs", "https"):
            url = f"{scheme}://{host}:{port}{prefix}" if port else f"{scheme}://{host}{prefix}"
        elif scheme == "gsiftp":
            url = f"gsiftp://{host}:{port}{prefix}" if port else f"gsiftp://{host}{prefix}"
        elif scheme == "srm":
            url = f"srm://{host}:{port}{prefix}" if port else f"srm://{host}{prefix}"
        else:
            url = f"{scheme}://{host}"
        return scheme if scheme != "xroot" else "root", url
    return "", ""


def load_existing(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    with path.open(newline="") as f:
        return {row["rse"]: row for row in csv.DictReader(f) if row.get("rse")}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "campaign" / "sites.csv",
    )
    parser.add_argument(
        "--expression",
        default=None,
        help="Optional Rucio RSE expression filter",
    )
    args = parser.parse_args()

    from rucio.client import Client

    client = Client()
    existing = load_existing(args.output)

    rows: list[dict] = []
    raw = list(client.list_rses(rse_expression=args.expression) if args.expression else client.list_rses())
    names: list[str] = []
    for item in raw:
        if isinstance(item, dict):
            names.append(item["rse"])
        else:
            names.append(str(item))
    names = sorted(set(names))

    print(f"Fetching details for {len(names)} RSEs...", file=sys.stderr)
    errors = 0
    for i, rse in enumerate(names, 1):
        if i % 25 == 0 or i == len(names):
            print(f"  {i}/{len(names)}", file=sys.stderr)
        try:
            info = client.get_rse(rse)
            attrs = dict(client.list_rse_attributes(rse))
        except Exception as exc:  # noqa: BLE001
            errors += 1
            print(f"  skip {rse}: {exc}", file=sys.stderr)
            continue

        protocols = info.get("protocols") or []
        tech = infer_storage_tech(rse, attrs, protocols)
        scheme, url = pick_protocol(protocols)
        site = infer_site(rse, attrs)
        tier = attrs.get("tier", "")
        if tier == "" and site.startswith("T"):
            tier = site[1] if len(site) > 1 and site[1].isdigit() else ""

        prev = existing.get(rse, {})
        # Preserve manual campaign fields if already set.
        row = {
            "rse": rse,
            "site": site,
            "tier": str(tier),
            "storage_tech": prev.get("storage_tech") or tech,
            "protocol_primary": scheme,
            "endpoint_url": url,
            "capture_method": prev.get("capture_method")
            or capture_method_for(prev.get("storage_tech") or tech),
            "tracer_status": prev.get("tracer_status") or "not_started",
            "last_probe_at": prev.get("last_probe_at") or "",
            "last_probe_result": prev.get("last_probe_result") or "",
            "probe_did": prev.get("probe_did") or "",
            "notes": prev.get("notes") or "",
            "contact": prev.get("contact") or attrs.get("site_admins", "") or "",
        }
        # Re-derive capture_method if storage_tech was auto and method empty/unknown
        if not prev.get("capture_method"):
            row["capture_method"] = capture_method_for(row["storage_tech"])
        rows.append(row)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)

    from collections import Counter

    tech_counts = Counter(r["storage_tech"] for r in rows)
    print(f"Wrote {len(rows)} RSEs to {args.output} (errors={errors})", file=sys.stderr)
    for k, v in sorted(tech_counts.items()):
        print(f"  {k}: {v}", file=sys.stderr)
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
