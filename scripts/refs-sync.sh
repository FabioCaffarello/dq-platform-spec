#!/usr/bin/env bash
# path: scripts/refs-sync.sh
#
# Hydrate every reference declared in references/*.lock to its pinned ref.
#
# Usage:
#   scripts/refs-sync.sh          # sync all references
#   scripts/refs-sync.sh status   # show pinned vs. on-disk, no change
#   scripts/refs-sync.sh clean    # remove hydrated content (lockfiles stay)

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REFS_DIR="$ROOT/references"
MODE="${1:-sync}"

parse_lock() {
  local file="$1" name="" url="" ref="" sha=""
  while IFS= read -r line; do
    line="${line%%#*}"
    line="$(echo "$line" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
    [ -z "$line" ] && continue
    local key val
    key="$(echo "$line" | cut -d= -f1 | sed 's/[[:space:]]*$//')"
    val="$(echo "$line" | cut -d= -f2- | sed 's/^[[:space:]]*//')"
    case "$key" in
      name) name="$val" ;; url) url="$val" ;;
      ref)  ref="$val"  ;; sha) sha="$val" ;;
    esac
  done < "$file"
  echo "${name}|${url}|${ref}|${sha}"
}

iterate_locks() {
  shopt -s nullglob
  local found=0
  for lock in "$REFS_DIR"/*.lock; do
    found=1; "$1" "$lock"
  done
  if [ "$found" -eq 0 ]; then echo "No references/*.lock files found." >&2; exit 1; fi
}

do_sync() {
  local fields; fields="$(parse_lock "$1")"
  local name url ref
  name="$(echo "$fields" | cut -d'|' -f1)"
  url="$(echo  "$fields" | cut -d'|' -f2)"
  ref="$(echo  "$fields" | cut -d'|' -f3)"
  local dir="$REFS_DIR/$name"
  if [ -z "$name" ] || [ -z "$url" ] || [ -z "$ref" ]; then
    echo "ERROR: $1 missing name/url/ref" >&2; exit 1
  fi
  if [ ! -d "$dir/.git" ]; then
    echo "==> cloning $name from $url"; git clone "$url" "$dir"
  fi
  echo "==> syncing $name to ref '$ref'"
  git -C "$dir" fetch --tags --force origin
  git -C "$dir" checkout --quiet --detach "origin/$ref" 2>/dev/null \
    || git -C "$dir" checkout --quiet --detach "$ref"
  echo "    $name now at $(git -C "$dir" rev-parse HEAD)"
}

do_status() {
  local fields; fields="$(parse_lock "$1")"
  local name ref sha
  name="$(echo "$fields" | cut -d'|' -f1)"
  ref="$(echo  "$fields" | cut -d'|' -f3)"
  sha="$(echo  "$fields" | cut -d'|' -f4)"
  local dir="$REFS_DIR/$name"
  if [ -d "$dir/.git" ]; then
    echo "$name  pin=$ref  lock-sha=${sha:-<none>}  on-disk=$(git -C "$dir" rev-parse HEAD)"
  else
    echo "$name  pin=$ref  lock-sha=${sha:-<none>}  on-disk=<not hydrated>"
  fi
}

do_clean() {
  local fields; fields="$(parse_lock "$1")"
  local name; name="$(echo "$fields" | cut -d'|' -f1)"
  local dir="$REFS_DIR/$name"
  if [ -d "$dir" ]; then echo "==> removing $dir"; rm -rf "$dir"; fi
}

case "$MODE" in
  sync)   iterate_locks do_sync ;;
  status) iterate_locks do_status ;;
  clean)  iterate_locks do_clean ;;
  *) echo "usage: $0 [sync|status|clean]" >&2; exit 2 ;;
esac
