# file-access-tracer

Processes XRootD `ofs.notify` events from standard input and emits newline-delimited JSON describing file read access.

XRootD starts the binary once and supplies events through a pipe. No separate service unit or FIFO is required.

## Requirements

- Go 1.22 or later (to build from source)
- XRootD with `ofs.notify` support (for production deployment)

## Installation

### From a release

Download the binary for the target platform from the [GitHub Releases](https://github.com/dynamic-entropy/file-access-tracer/releases) page, then install it on a path readable by the XRootD process (for example `/usr/local/bin/file-access-tracer`).

Release artifacts:

| Artifact | Platform |
|----------|----------|
| `file-access-tracer-linux-amd64` | Linux x86_64 |
| `file-access-tracer-linux-arm64` | Linux aarch64 |
| `file-access-tracer-darwin-amd64` | macOS (Intel) |
| `file-access-tracer-darwin-arm64` | macOS (Apple Silicon) |
| `SHA256SUMS` | SHA-256 checksums |

Releases are produced automatically when a version tag matching `v*` is pushed.

### From source

```bash
make build    # writes bin/file-access-tracer
make test
make release  # cross-compiled artifacts under dist/
```

## XRootD configuration

Enable notification for read opens and pipe events into the tracer:

```
ofs.notify openr | /usr/local/bin/file-access-tracer
```

To append JSON lines to a log file:

```
ofs.notify openr | /bin/sh -c '/usr/local/bin/file-access-tracer >>/var/log/xrootd/access.jsonl 2>>/var/log/xrootd/access.err'
```

See [`deploy/xrootd-ofs-notify.cfg`](deploy/xrootd-ofs-notify.cfg) for a configuration snippet.

## Output

One JSON object per accepted event is written to standard output. By default only `openr` events are accepted. Use `-events` to select a different set (comma-separated).

```bash
file-access-tracer -version
file-access-tracer -events openr,closer
```

Example output:

```json
{"tid":"local","event":"openr","path":"/data/file.root","is_write":false,"ts_access":"2026-07-14T02:00:00Z","storage":"xrootd"}
```

## Site validation campaign

The [`campaign/`](campaign/) directory tracks CMS RSE readiness for access capture (inventory, status, and validation procedure).

## License

See repository metadata.
