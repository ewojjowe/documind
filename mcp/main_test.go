package main

import (
	"strings"
	"testing"
)

func TestStatusMentionsPhase(t *testing.T) {
	if got := status(); !strings.Contains(got, "Phase 4") {
		t.Errorf("status() = %q, want it to mention Phase 4", got)
	}
}
