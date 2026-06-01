#!/usr/bin/env python3
# path: scripts/build-index.py
#
# Regenerate .claude/state/index.yaml from artifact files. Auto-stages
# the result so the developer never has to remember `git add`. The
# index is derived state; this script is its single source of truth.
#
# Hard-fails on integrity violations (broken parent IDs) — those are
# real errors a developer must fix before committing.
#
# Run modes:
#   scripts/build-index.py        manual regeneration (also via `make index`)
#   pre-commit calls it the same way; the hook is non-blocking on
#   regeneration (auto-stages) and blocking on integrity violations.

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
INDEX_PATH = REPO / ".claude" / "state" / "index.yaml"
LOCK_PATH = REPO / "references" / "dq-platform.lock"

# Slug shape: lowercase alnum + dashes; starts with alnum.
SLUG = r"[a-z0-9][a-z0-9-]*"
ARTIFACT_ID_RE = re.compile(rf"^(scout|study|vision|brief|design|spec|roadmap|adr):{SLUG}$")
PILLAR_ID_RE = re.compile(rf"^pillar:{SLUG}:{SLUG}$")

# Header field line in a markdown blockquote: "> Field name: value"
HEADER_FIELD_RE = re.compile(r"^>\s*([A-Za-z][A-Za-z ]+):\s*(.*?)\s*$")

# Pillar declaration inside vision body:
#   <!-- pillar-id: <slug> -->
#   ### <heading>
# Blank lines between the comment and the heading are tolerated.
PILLAR_RE = re.compile(
    r"<!--\s*pillar-id:\s*(" + SLUG + r")\s*-->\s*\n+\s*###\s+(.+?)\s*(?:\n|$)",
    re.MULTILINE,
)

ARTIFACT_TYPE_SUFFIXES = {
    "vision": "-vision",
    "brief": "-brief",
    "roadmap": "-roadmap",
}


def yaml_str(s: str) -> str:
    """Emit a YAML string as JSON-escaped — safe for any character.

    JSON-style double-quoted strings are a strict subset of YAML
    strings, so this handles colons, quotes, backslashes, leading
    dashes, and anything else without a special case.
    """
    return json.dumps(s, ensure_ascii=False)


def read_pin() -> str:
    if not LOCK_PATH.exists():
        return "dq-platform@unknown"
    for line in LOCK_PATH.read_text().splitlines():
        m = re.match(r"^\s*sha\s*=\s*([0-9a-f]+)", line)
        if m:
            return f"dq-platform@{m.group(1)[:7]}"
    return "dq-platform@unknown"


def slug_for(path: Path, type_: str) -> str:
    stem = path.stem
    suffix = ARTIFACT_TYPE_SUFFIXES.get(type_)
    if suffix and stem.endswith(suffix):
        stem = stem[: -len(suffix)]
    return stem


def parse_header_fields(text: str) -> dict[str, str]:
    """Read the top blockquote header.

    Skips initial HTML comments and blank lines, then collects "> Key:
    value" lines until the first non-blockquote, non-blank line.
    """
    fields: dict[str, str] = {}
    in_header = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(">"):
            in_header = True
            m = HEADER_FIELD_RE.match(line)
            if m:
                key = m.group(1).strip().lower().replace(" ", "_")
                fields[key] = m.group(2).strip()
        elif not in_header:
            # Pre-header (path comment, blanks, title) — keep scanning.
            continue
        else:
            # First non-blockquote line after the header ends it.
            if stripped == "":
                continue
            break
    return fields


def parse_pillars(text: str, vision_slug: str) -> list[dict]:
    pillars: list[dict] = []
    for m in PILLAR_RE.finditer(text):
        pid = m.group(1).strip()
        heading = m.group(2).strip()
        pillars.append(
            {"id": f"pillar:{vision_slug}:{pid}", "heading": heading}
        )
    # Deterministic order: by stable ID. The vision file can rearrange
    # pillars without producing a diff in the index.
    pillars.sort(key=lambda p: p["id"])
    return pillars


def is_artifact_file(path: Path) -> bool:
    return path.suffix == ".md" and not path.name.startswith(".")


def collect_simple(dir_: Path, type_: str, parent_field: str | None = None) -> list[dict]:
    """For directories where each .md is one artifact of `type_`."""
    items: list[dict] = []
    if not dir_.exists():
        return items
    for path in sorted(dir_.iterdir()):
        if not is_artifact_file(path):
            continue
        if path.is_dir():
            continue
        items.append(build_artifact(path, type_, parent_field))
    return items


def build_artifact(path: Path, type_: str, parent_field: str | None) -> dict:
    text = path.read_text()
    fields = parse_header_fields(text)
    slug = slug_for(path, type_)
    rel_path = path.relative_to(REPO).as_posix()

    status = fields.get("status") or ("published" if type_ in ("scout", "study", "roadmap", "adr") else "draft")

    parent: str | None = None
    if parent_field:
        raw = fields.get(parent_field)
        if raw:
            # Strip backticks if present; the ID is bare.
            parent = raw.strip("`").strip()
            if not parent:
                parent = None

    artifact: dict = {
        "id": f"{type_}:{slug}",
        "type": type_,
        "path": rel_path,
        "status": status,
        "parent": parent,
    }
    if type_ == "vision":
        artifact["pillars"] = parse_pillars(text, slug)
    return artifact


def collect_strategy() -> list[dict]:
    items: list[dict] = []
    strategy_dir = REPO / "docs" / "strategy"
    if not strategy_dir.exists():
        return items
    for path in sorted(strategy_dir.iterdir()):
        if not is_artifact_file(path) or path.is_dir():
            continue
        stem = path.stem
        if stem.endswith("-vision"):
            items.append(build_artifact(path, "vision", parent_field=None))
        elif stem.endswith("-brief"):
            items.append(build_artifact(path, "brief", parent_field="vision_pillar"))
        # Other strategy files (if any) are ignored — they aren't part of
        # the chain. Flag silently rather than fail.
    return items


def collect() -> list[dict]:
    items: list[dict] = []
    items += collect_simple(REPO / "studies" / "scout", "scout")

    # studies/ (excluding the scout/ subdir)
    studies_dir = REPO / "studies"
    if studies_dir.exists():
        for path in sorted(studies_dir.iterdir()):
            if path.is_dir() or not is_artifact_file(path):
                continue
            items.append(build_artifact(path, "study", parent_field=None))

    items += collect_strategy()
    items += collect_simple(REPO / "docs" / "system-design", "design", parent_field="brief")
    items += collect_simple(REPO / "docs" / "specs", "spec", parent_field="design")
    items += collect_simple(REPO / "docs" / "roadmap", "roadmap")
    items += collect_simple(REPO / "docs" / "adr", "adr")

    items.sort(key=lambda a: a["id"])
    return items


def emit_yaml(artifacts: list[dict], reference_pin: str) -> str:
    lines: list[str] = []
    lines.append("# .claude/state/index.yaml")
    lines.append("# Generated by scripts/build-index.py — DO NOT EDIT BY HAND.")
    lines.append("# Pre-commit regenerates this file when artifacts change")
    lines.append("# and auto-stages it. Run `make index` to regenerate manually.")
    lines.append("schema_version: 1")
    lines.append(f"reference_pin: {yaml_str(reference_pin)}")
    if not artifacts:
        lines.append("artifacts: []")
    else:
        lines.append("artifacts:")
        for a in artifacts:
            lines.append(f"  - id: {yaml_str(a['id'])}")
            lines.append(f"    type: {yaml_str(a['type'])}")
            lines.append(f"    path: {yaml_str(a['path'])}")
            lines.append(f"    status: {yaml_str(a['status'])}")
            parent = a.get("parent")
            if parent is None:
                lines.append("    parent: null")
            else:
                lines.append(f"    parent: {yaml_str(parent)}")
            pillars = a.get("pillars")
            if pillars is not None:
                if not pillars:
                    lines.append("    pillars: []")
                else:
                    lines.append("    pillars:")
                    for p in pillars:
                        lines.append(f"      - id: {yaml_str(p['id'])}")
                        lines.append(f"        heading: {yaml_str(p['heading'])}")
    return "\n".join(lines) + "\n"


def check_integrity(artifacts: list[dict]) -> list[str]:
    """Every parent ID cited must exist as an artifact or pillar ID."""
    known: set[str] = set()
    for a in artifacts:
        known.add(a["id"])
        for p in a.get("pillars") or []:
            known.add(p["id"])

    errors: list[str] = []
    for a in artifacts:
        parent = a.get("parent")
        if parent is None:
            continue
        # Format sanity for the parent.
        if not (ARTIFACT_ID_RE.match(parent) or PILLAR_ID_RE.match(parent)):
            errors.append(
                f"{a['id']} ({a['path']}) cites parent {parent!r}, which is "
                f"not a valid ID shape (expected <type>:<slug> or "
                f"pillar:<vision-slug>:<pillar-slug>)"
            )
            continue
        if parent not in known:
            errors.append(
                f"{a['id']} ({a['path']}) cites parent {parent!r}, which "
                f"does not exist in the index"
            )
    return errors


def git_add(path: Path) -> None:
    """Best-effort git add; silent if not in a git context."""
    try:
        subprocess.run(
            ["git", "add", "--", str(path.relative_to(REPO))],
            cwd=str(REPO),
            check=True,
            capture_output=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass


def main() -> int:
    artifacts = collect()
    pin = read_pin()
    new_content = emit_yaml(artifacts, pin)

    old_content = INDEX_PATH.read_text() if INDEX_PATH.exists() else ""

    if new_content != old_content:
        INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
        INDEX_PATH.write_text(new_content)
        git_add(INDEX_PATH)
        print(
            f"build-index: regenerated {INDEX_PATH.relative_to(REPO)} "
            f"({len(artifacts)} artifact{'s' if len(artifacts) != 1 else ''})",
            file=sys.stderr,
        )

    errors = check_integrity(artifacts)
    if errors:
        print(
            "build-index: INTEGRITY FAILURE — parent IDs not found in index:",
            file=sys.stderr,
        )
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
