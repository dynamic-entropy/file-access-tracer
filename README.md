# file-access-tracer

Go binary for XRootD `ofs.notify` read-access events → JSON (Kafka / Rucio traces later).

**Site deploy:** install one binary + one XRootD config line. XRootD starts and manages the process via a pipe.

## Build

```bash
make build          # → bin/file-access-tracer
make test
```

Cross-build for releases: `make release-linux`

## Deploy on an SE

1. Install the binary:

```bash
sudo make install
# or: sudo install -m 0755 bin/file-access-tracer /usr/bin/file-access-tracer
```

2. XRootD config (`deploy/xrootd-ofs-notify.cfg`):

```
ofs.notify openr | /usr/bin/file-access-tracer
```

3. Restart XRootD. Events are JSON lines on the tracer’s stdout.

## Host on GitHub

```bash
git tag v0.1.0 && git push origin v0.1.0
```

## CMS RSE validation campaign

See [`campaign/`](campaign/): `sites.csv` / `SITES.md` and place→read→verify procedure.
