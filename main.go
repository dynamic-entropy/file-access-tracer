// file-access-tracer reads XRootD ofs.notify lines from stdin or a FIFO.
package main

import (
	"bufio"
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"log"
	"os"
	"os/signal"
	"strings"
	"syscall"
	"time"
)

// Set via -ldflags "-X main.version=..."
var version = "dev"

// NotifyEvent is one parsed ofs.notify line (default XRootD format).
type NotifyEvent struct {
	TID      string    `json:"tid"`
	Event    string    `json:"event"`
	Path     string    `json:"path"`
	IsWrite  bool      `json:"is_write"`
	TsAccess time.Time `json:"ts_access"`
	Storage  string    `json:"storage"`
	Raw      string    `json:"raw,omitempty"`
}

func main() {
	log.SetFlags(log.LstdFlags | log.Lmsgprefix)
	log.SetPrefix("file-access-tracer: ")

	if len(os.Args) < 2 {
		usage()
		os.Exit(2)
	}

	switch os.Args[1] {
	case "stdin":
		runStdin(os.Args[2:])
	case "fifo":
		runFIFO(os.Args[2:])
	case "version", "-version", "--version":
		fmt.Println(version)
	case "help", "-h", "--help":
		usage()
	default:
		fmt.Fprintf(os.Stderr, "unknown command %q\n", os.Args[1])
		usage()
		os.Exit(2)
	}
}

func usage() {
	fmt.Fprintf(os.Stderr, `file-access-tracer %s

Usage:
  file-access-tracer stdin [-events openr]
  file-access-tracer fifo -path /var/run/xrootd/ofs.notify.fifo [-events openr]
  file-access-tracer version

For read-access popularity, enable only openr in XRootD:

  ofs.notify openr >/var/run/xrootd/ofs.notify.fifo

See deploy/file-access-tracer.service for systemd.
`, version)
}

func runStdin(args []string) {
	fs := flag.NewFlagSet("stdin", flag.ExitOnError)
	events := fs.String("events", "openr", "comma-separated ofs.notify events to accept")
	_ = fs.Parse(args)
	consume(os.Stdin, parseEventFilter(*events))
}

func runFIFO(args []string) {
	fs := flag.NewFlagSet("fifo", flag.ExitOnError)
	path := fs.String("path", "", "path to ofs.notify FIFO (required)")
	events := fs.String("events", "openr", "comma-separated ofs.notify events to accept")
	_ = fs.Parse(args)
	if *path == "" {
		log.Fatal("-path is required")
	}

	// O_RDWR so open does not block waiting for the XRootD writer.
	f, err := os.OpenFile(*path, os.O_RDWR, 0)
	if err != nil {
		log.Fatalf("open fifo %s: %v", *path, err)
	}
	defer f.Close()

	sig := make(chan os.Signal, 1)
	signal.Notify(sig, syscall.SIGINT, syscall.SIGTERM)
	go func() {
		<-sig
		_ = f.Close()
	}()

	log.Printf("reading fifo %s (events=%s)", *path, *events)
	consume(f, parseEventFilter(*events))
}

func parseEventFilter(spec string) map[string]struct{} {
	out := make(map[string]struct{})
	for _, e := range strings.Split(spec, ",") {
		e = strings.TrimSpace(e)
		if e != "" {
			out[e] = struct{}{}
		}
	}
	if len(out) == 0 {
		out["openr"] = struct{}{}
	}
	return out
}

func consume(r io.Reader, allow map[string]struct{}) {
	sc := bufio.NewScanner(r)
	buf := make([]byte, 0, 64*1024)
	sc.Buffer(buf, 1024*1024)

	enc := json.NewEncoder(os.Stdout)
	var nOK, nSkip, nBad int
	for sc.Scan() {
		line := strings.TrimSpace(sc.Text())
		if line == "" {
			continue
		}
		ev, err := parseNotifyLine(line)
		if err != nil {
			nBad++
			log.Printf("parse error: %v (line=%q)", err, line)
			continue
		}
		if _, ok := allow[ev.Event]; !ok {
			nSkip++
			continue
		}
		nOK++
		if err := enc.Encode(ev); err != nil {
			log.Printf("encode: %v", err)
			return
		}
	}
	if err := sc.Err(); err != nil {
		log.Printf("read ended: %v (ok=%d skip=%d bad=%d)", err, nOK, nSkip, nBad)
		return
	}
	log.Printf("eof (ok=%d skip=%d bad=%d)", nOK, nSkip, nBad)
}

func parseNotifyLine(line string) (NotifyEvent, error) {
	// Default format: "<tid> <event> <path...>"
	tid, rest, ok := strings.Cut(line, " ")
	if !ok || tid == "" {
		return NotifyEvent{}, fmt.Errorf("missing tid")
	}
	event, path, ok := strings.Cut(strings.TrimLeft(rest, " "), " ")
	if !ok || event == "" || path == "" {
		return NotifyEvent{}, fmt.Errorf("missing event or path")
	}
	path = strings.TrimSpace(path)

	isWrite := event == "openw" || event == "closew" || event == "fwrite" || event == "create"
	return NotifyEvent{
		TID:      tid,
		Event:    event,
		Path:     path,
		IsWrite:  isWrite,
		TsAccess: time.Now().UTC(),
		Storage:  "xrootd",
		Raw:      line,
	}, nil
}
