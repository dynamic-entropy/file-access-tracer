#!/usr/bin/env python3
"""Generate campaign/SITES.md from sites.csv for human-readable browsing."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

STATUS_EMOJI = {
    "validated": "✅",
    "instrumented": "🟡",
    "not_started": "⚪",
    "blocked": "🚫",
    "out_of_scope": "⬛",
}

PROBE_EMOJI = {
    "pass": "✅",
    "fail": "❌",
    "skip": "⏭️",
    "pending": "⏳",
    "": "—",
}


def status_cell(status: str) -> str:
    return f"{STATUS_EMOJI.get(status, '❓')} `{status}`"


def probe_cell(result: str) -> str:
    if not result:
        return "—"
    return f"{PROBE_EMOJI.get(result, '❓')} `{result}`"


def md_escape(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "campaign" / "sites.csv",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "campaign" / "SITES.md",
    )
    args = parser.parse_args()

    with args.input.open(newline="") as f:
        rows = list(csv.DictReader(f))

    by_status = Counter(r.get("tracer_status") or "" for r in rows)
    by_tech = Counter(r.get("storage_tech") or "" for r in rows)
    by_probe = Counter(r.get("last_probe_result") or "(none)" for r in rows)

    lines: list[str] = []
    lines.append("# CMS RSE access-capture status")
    lines.append("")
    lines.append(
        "Auto-generated from [`sites.csv`](sites.csv). "
        "The CSV is the source of truth for automation; this Markdown summary is derived for browsing."
    )
    lines.append("")
    lines.append("Regenerate: `python scripts/render_sites_md.py`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| tracer_status | count |")
    lines.append("|---------------|------:|")
    for k, v in sorted(by_status.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"| {status_cell(k)} | {v} |")
    lines.append("")
    lines.append("| storage_tech | count |")
    lines.append("|--------------|------:|")
    for k, v in sorted(by_tech.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"| `{k}` | {v} |")
    lines.append("")
    lines.append("| last_probe_result | count |")
    lines.append("|-------------------|------:|")
    for k, v in sorted(by_probe.items(), key=lambda kv: (-kv[1], kv[0])):
        label = k if k != "(none)" else ""
        lines.append(f"| {probe_cell(label)} | {v} |")
    lines.append("")
    lines.append("## Legend")
    lines.append("")
    lines.append("| Status | Meaning |")
    lines.append("|--------|---------|")
    lines.append("| ⚪ `not_started` | In inventory; no instrumentation yet |")
    lines.append("| 🟡 `instrumented` | Capture configured at site |")
    lines.append("| ✅ `validated` | place→read→capture probe passed |")
    lines.append("| 🚫 `blocked` | Cannot instrument yet |")
    lines.append("| ⬛ `out_of_scope` | Explicitly skipped |")
    lines.append("")

    # Full inventory table (compact columns)
    lines.append("## All RSEs")
    lines.append("")
    lines.append(
        "| status | rse | site | tier | tech | method | protocol | endpoint | probe |"
    )
    lines.append(
        "|--------|-----|------|------|------|--------|----------|----------|-------|"
    )
    for r in sorted(rows, key=lambda x: (x.get("tracer_status") or "", x.get("rse") or "")):
        lines.append(
            "| {status} | `{rse}` | {site} | {tier} | `{tech}` | `{method}` | `{proto}` | `{url}` | {probe} |".format(
                status=status_cell(r.get("tracer_status") or ""),
                rse=md_escape(r.get("rse") or ""),
                site=md_escape(r.get("site") or ""),
                tier=md_escape(r.get("tier") or ""),
                tech=md_escape(r.get("storage_tech") or ""),
                method=md_escape(r.get("capture_method") or ""),
                proto=md_escape(r.get("protocol_primary") or ""),
                url=md_escape(r.get("endpoint_url") or ""),
                probe=probe_cell(r.get("last_probe_result") or ""),
            )
        )
    lines.append("")

    # Sections per status for quick filtering in the UI
    for status in ("validated", "instrumented", "not_started", "blocked", "out_of_scope"):
        subset = [r for r in rows if (r.get("tracer_status") or "") == status]
        if not subset:
            continue
        lines.append(f"## {STATUS_EMOJI.get(status, '❓')} {status} ({len(subset)})")
        lines.append("")
        lines.append("| rse | site | tech | endpoint |")
        lines.append("|-----|------|------|----------|")
        for r in sorted(subset, key=lambda x: x.get("rse") or ""):
            lines.append(
                f"| `{md_escape(r.get('rse') or '')}` | {md_escape(r.get('site') or '')} | "
                f"`{md_escape(r.get('storage_tech') or '')}` | `{md_escape(r.get('endpoint_url') or '')}` |"
            )
        lines.append("")

    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {args.output} ({len(rows)} RSEs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
