#!/usr/bin/env bash
# path: scripts/check-path-header.sh
#
# Enforce the path-header rule from CLAUDE.md:
#   "Markdown opens with its path. Every .md starts with
#    <!-- path: ... --> so it survives being moved or extracted."
#
# Checks every tracked .md file (excluding references/) and fails if the
# first line is not exactly <!-- path: <some-path> -->. The contained
# path is informational; we do not require it to match the file location.
#
# Usage:
#   scripts/check-path-header.sh                 # check all tracked .md files
#   scripts/check-path-header.sh path/a.md ...   # check the given files

set -euo pipefail

# Pre-commit passes changed files as arguments. When run by hand without
# arguments, fall back to every tracked markdown file outside references/.
if [ "$#" -gt 0 ]; then
  files=("$@")
else
  mapfile -t files < <(git ls-files -- '*.md' ':!:references/**')
fi

header_re='^<!--[[:space:]]*path:[[:space:]]*[^[:space:]].*-->[[:space:]]*$'

bad=0
for file in "${files[@]}"; do
  # Skip anything under references/ even if pre-commit hands it to us.
  case "$file" in
    references/*) continue ;;
  esac
  [ -f "$file" ] || continue

  first_line="$(head -n 1 -- "$file" || true)"
  if ! printf '%s' "$first_line" | grep -Eq "$header_re"; then
    if [ "$bad" -eq 0 ]; then
      echo "Missing or malformed path-header on the first line."
      echo "Expected:  <!-- path: <relative/path/to/file.md> -->"
      echo
    fi
    printf '  %s:1: got %q\n' "$file" "$first_line"
    bad=1
  fi
done

if [ "$bad" -ne 0 ]; then
  echo
  echo "See CLAUDE.md, principle 7: 'Markdown opens with its path.'"
  exit 1
fi
