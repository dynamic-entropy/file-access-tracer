# file-access-tracer

Go binary for XRootD `ofs.notify` read-access events → JSON (Kafka / Rucio traces later).

**Site deploy:** install one binary + one XRootD config line. XRootD starts and manages the process via a pipe.

## Release binaries (GitHub Actions)

Push a version tag; CI builds and attaches:

| Artifact | Platform |
|----------|----------|
| `file-access-tracer-linux-amd64` | Linux x86_64 |
| `file-access-tracer-linux-arm64` | Linux aarch64 |
| `file-access-tracer-darwin-amd64` | macOS Intel |
| `file-access-tracer-darwin-arm64` | macOS Apple Silicon |
| `SHA256SUMS` | checksums |

```bash
git tag v0.1.0
git push origin v0.1.0
# → https://github.com/dynamic-entropy/file-access-tracer/releases/tag/v0.1.0
```

## Install from a release (manual commands)

### Linux VM (e.g. local xrootd test)

```bash
VER=v0.1.0
ARCH=amd64   # or arm64 — run: uname -m  (x86_64→amd64, aarch64→arm64)

curl -fsSL -o /tmp/file-access-tracer \
  "https://github.com/dynamic-entropy/file-access-tracer/releases/download/${VER}/file-access-tracer-linux-${ARCH}"
sudo install -m 0755 /tmp/file-access-tracer /usr/local/bin/file-access-tracer
file-access-tracer -version
```

Point XRootD at the binary and capture JSON to a file (no helper script required):

```
ofs.notify openr | /bin/sh -c '/usr/local/bin/file-access-tracer >>/tmp/xrootd/access.jsonl 2>>/tmp/xrootd/access.err'
```

Then:

```bash
xrootd -c /tmp/xrootd/xrootd.cfg -l /tmp/xrootd/logs/xrootd.log -d
xrdfs root://localhost:1094/ cat /path/to/file
tail -f /tmp/xrootd/access.jsonl
```

### macOS (local smoke)

```bash
VER=v0.1.0
ARCH=arm64   # Intel Mac: amd64

curl -fsSL -o /tmp/file-access-tracer \
  "https://github.com/dynamic-entropy/file-access-tracer/releases/download/${VER}/file-access-tracer-darwin-${ARCH}"
chmod +x /tmp/file-access-tracer
printf '%s\n' 'local openr /tmp/demo.root' | /tmp/file-access-tracer
```

## Build from source

```bash
make build          # → bin/file-access-tracer
make test
make release        # → dist/* for all OS/arch above
```

## CMS RSE validation campaign

See [`campaign/`](campaign/): `sites.csv` / `SITES.md` and place→read→verify procedure.
