# file-access-tracer

Go binary that reads XRootD `ofs.notify` events from a **FIFO** (recommended) or stdin and emits JSON access events. Used for SE read-access monitoring (Kafka / Rucio traces later).

## Build

```bash
cd file-access-tracer
make build          # → bin/file-access-tracer
make test
```

Or:

```bash
go build -o file-access-tracer .
```

Cross-build Linux release artifacts:

```bash
make release-linux  # → dist/file-access-tracer-linux-{amd64,arm64}
```

## Host on GitHub

This directory is meant to be its **own repo** (do not nest under the dCache/XRootD clones long-term).

```bash
cd file-access-tracer
git init
git add .
git commit -m "Initial file-access-tracer"
gh repo create file-access-tracer --public --source=. --remote=origin --push
```

Releases: push a tag; Actions builds Linux binaries and attaches them to the GitHub Release.

```bash
git tag v0.1.0
git push origin v0.1.0
```

Sites can then:

```bash
curl -fsSL -o file-access-tracer \
  https://github.com/dynamic-entropy/file-access-tracer/releases/download/v0.1.0/file-access-tracer-linux-amd64
sudo install -m 0755 file-access-tracer /usr/bin/file-access-tracer
```

## Deploy (systemd + XRootD)

1. Install binary and unit:

```bash
sudo make install
# or copy bin + deploy/file-access-tracer.service manually to /usr/bin and /etc/systemd/system/
sudo systemd-tmpfiles --create /usr/lib/tmpfiles.d/file-access-tracer.conf
sudo systemctl daemon-reload
sudo systemctl enable --now file-access-tracer
```

2. Point XRootD at the same FIFO (read opens only):

```
ofs.notify openr >/var/run/xrootd/ofs.notify.fifo
```

(see `deploy/xrootd-ofs-notify.cfg`)

3. Restart XRootD, then check:

```bash
journalctl -u file-access-tracer -f
```

Optional env overrides: `/etc/file-access-tracer/env` (`FIFO_PATH`, `EVENTS`).

## Why FIFO

Tracer lifecycle is independent of XRootD; restart the service without changing XRootD’s child process. Use `stdin` only for ad-hoc tests.

## CMS RSE validation campaign

See [`campaign/`](campaign/): inventory table (`sites.csv`) and place→read→verify procedure for all CMS Rucio RSEs.
