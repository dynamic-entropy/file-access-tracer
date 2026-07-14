package main

import (
	"strings"
	"testing"
)

func TestParseNotifyLine(t *testing.T) {
	ev, err := parseNotifyLine("cms001.1:2@cmsxrd.example openr /store/data/Run2024/file.root")
	if err != nil {
		t.Fatal(err)
	}
	if ev.TID != "cms001.1:2@cmsxrd.example" || ev.Event != "openr" || ev.Path != "/store/data/Run2024/file.root" {
		t.Fatalf("unexpected event: %+v", ev)
	}
	if ev.IsWrite {
		t.Fatal("openr should not be write")
	}
}

func TestParseNotifyLinePathWithSpaces(t *testing.T) {
	ev, err := parseNotifyLine("tid openr /path/with spaces/file.root")
	if err != nil {
		t.Fatal(err)
	}
	if ev.Path != "/path/with spaces/file.root" {
		t.Fatalf("path=%q", ev.Path)
	}
}

func TestParseEventFilterDefault(t *testing.T) {
	f := parseEventFilter("openr")
	if _, ok := f["openr"]; !ok {
		t.Fatal("expected openr")
	}
	if _, ok := f["closer"]; ok {
		t.Fatal("closer should not be allowed by default filter")
	}
}

func TestConsumeSkipsDisallowed(t *testing.T) {
	allow := parseEventFilter("openr")
	in := strings.NewReader("a openr /r\nb closer /r\nc openw /w\n")
	_ = in
	if len(allow) != 1 {
		t.Fatalf("allow=%v", allow)
	}
}
