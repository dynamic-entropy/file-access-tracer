APP := file-access-tracer
VERSION ?= $(shell git describe --tags --always --dirty 2>/dev/null || echo dev)
PREFIX ?= /usr
BINDIR ?= $(PREFIX)/bin

.PHONY: build install test clean release-linux

build:
	CGO_ENABLED=0 go build -ldflags="-s -w -X main.version=$(VERSION)" -o bin/$(APP) .

test:
	go test ./...

install: build
	install -d $(DESTDIR)$(BINDIR)
	install -m 0755 bin/$(APP) $(DESTDIR)$(BINDIR)/$(APP)
	install -d $(DESTDIR)/usr/share/file-access-tracer
	install -m 0644 deploy/xrootd-ofs-notify.cfg $(DESTDIR)/usr/share/file-access-tracer/xrootd-ofs-notify.cfg

release-linux:
	mkdir -p dist
	GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -ldflags="-s -w -X main.version=$(VERSION)" -o dist/$(APP)-linux-amd64 .
	GOOS=linux GOARCH=arm64 CGO_ENABLED=0 go build -ldflags="-s -w -X main.version=$(VERSION)" -o dist/$(APP)-linux-arm64 .

clean:
	rm -rf bin dist
