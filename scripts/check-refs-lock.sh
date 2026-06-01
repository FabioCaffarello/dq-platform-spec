#!/usr/bin/env bash
# path: scripts/check-refs-lock.sh
#
# Validate every references/*.lock declares at least name, url, and ref.
# These are the fields scripts/refs-sync.sh needs to hydrate a reference;
# missing any of them silently breaks `make refs-sync`.
#
# Usage:
#   scripts/check-refs-lock.sh                       # check all lockfiles
#   scripts/check-refs-lock.sh references/foo.lock   # check the given files

set -euo pipefail

if [ "$#" -gt 0 ]; then
  files=("$@")
else
  shopt -s nullglob
  files=(references/*.lock)
  shopt -u nullglob
fi

bad=0
for file in "${files[@]}"; do
  [ -f "$file" ] || continue

  missing=()
  for key in name url ref; do
    if ! grep -Eq "^[[:space:]]*${key}[[:space:]]*=[[:space:]]*[^[:space:]#]" "$file"; then
      missing+=("$key")
    fi
  done

  if [ "${#missing[@]}" -gt 0 ]; then
    echo "Lockfile missing required field(s): ${missing[*]}"
    echo "  $file"
    bad=1
  fi
done

if [ "$bad" -ne 0 ]; then
  echo
  echo "Each references/*.lock must declare name, url, and ref (sha is optional)."
  exit 1
fi
