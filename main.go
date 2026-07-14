// file-access-tracer reads XRootD ofs.notify lines from stdin (piped by XRootD).
package main

import (
	"bufio"
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"log"
	"os"
	"strings"
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

	fs := flag.NewFlagSet("file-access-tracer", flag.ExitOnError)
	events := fs.String("events", "openr", "comma-separated ofs.notify events to accept")
	showVersion := fs.Bool("version", false, "print version and exit")
	fs.Usage = usage
	_ = fs.Parse(os.Args[1:])

	if *showVersion || (fs.NArg() == 1 && fs.Arg(0) == "version") {
		fmt.Println(version)
		return
	}
	if fs.NArg() > 0 {
		fmt.Fprintf(os.Stderr, "unexpected arguments: %v\n", fs.Args())
		usage()
		os.Exit(2)
	}

	consume(os.Stdin, parseEventFilter(*events))
}

func usage() {
	fmt.Fprintf(os.Stderr, `file-access-tracer %s

XRootD starts this binary once and pipes ofs.notify lines to stdin:

  ofs.notify openr | /usr/bin/file-access-tracer

Options:
  -events string   comma-separated events to accept (default "openr")
  -version         print version
`, version)
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
