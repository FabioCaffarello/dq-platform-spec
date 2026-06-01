#!/usr/bin/env bash
# path: scripts/check-reference-pin.sh
#
# Coherence check: the short SHA cited in .claude/reference-map.md
# must match the sha pinned in references/dq-platform.lock. Divergence
# means either the pin moved without refreshing the map, or the map
# was edited without bumping the pin.
#
# This is a WARNING, not a block. Pre-commit runs it when either file
# changes; the script always exits 0 and emits a clear message on
# stderr when the SHAs disagree. Move to exit 1 only if drift becomes
# a recurring problem.
#
# Usage:
#   scripts/check-reference-pin.sh
#
# Reads:
#   - .claude/reference-map.md  (line "> Pinned to: dq-platform@<sha>")
#   - references/dq-platform.lock  (line "sha = <40-char-sha>")

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MAP="$ROOT/.claude/reference-map.md"
LOCK="$ROOT/references/dq-platform.lock"

if [ ! -f "$MAP" ]; then
  echo "check-reference-pin: $MAP missing; nothing to check." >&2
  exit 0
fi
if [ ! -f "$LOCK" ]; then
  echo "check-reference-pin: $LOCK missing; nothing to check." >&2
  exit 0
fi

map_sha="$(grep -Eo 'dq-platform@[0-9a-f]{4,40}' "$MAP" | head -n 1 | cut -d@ -f2 || true)"
lock_sha="$(grep -E '^[[:space:]]*sha[[:space:]]*=' "$LOCK" \
           | head -n 1 | cut -d= -f2 | tr -d '[:space:]' || true)"

if [ -z "$map_sha" ]; then
  echo "check-reference-pin: WARNING — no 'dq-platform@<sha>' line found in $MAP." >&2
  exit 0
fi
if [ -z "$lock_sha" ]; then
  echo "check-reference-pin: WARNING — no 'sha = ...' line found in $LOCK." >&2
  exit 0
fi

# Compare on the shorter of the two prefixes; the map carries a short
# SHA by convention.
short_len="${#map_sha}"
lock_prefix="${lock_sha:0:$short_len}"

if [ "$map_sha" != "$lock_prefix" ]; then
  cat >&2 <<EOF
check-reference-pin: WARNING — pin drift between map and lock.

  reference-map.md   dq-platform@$map_sha
  dq-platform.lock   sha = $lock_sha

The reference-map's "you are here" no longer matches what
'make refs-sync' would hydrate. Either:
  - refresh .claude/reference-map.md against the current pin, or
  - bump the lock if the map was the correct one.

(This is a non-blocking warning. Fix it in its own commit.)
EOF
fi

exit 0
