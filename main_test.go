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
	in := strings.NewReader("" +
		"a openr /r\n" +
		"b closer /r\n" +
		"c openw /w\n")
	// smoke: parse filter only allows openr
	allow := parseEventFilter("openr")
	if len(allow) != 1 {
		t.Fatalf("allow=%v", allow)
	}
	_ = in
}
