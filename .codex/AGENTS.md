<!-- path: .codex/AGENTS.md -->
<!-- audience: Codex CLI -->
<!-- status: living document, kept in sync with CLAUDE.md -->

# Codex Entry Point — DQ Platform Spec

The authoritative guide is **[`../CLAUDE.md`](../CLAUDE.md)**. Everything
there applies to Codex exactly as to Claude Code. This file exists only
because Codex looks for `.codex/AGENTS.md` by convention.

This is a spec-authoring workspace. You distill a pinned reference into
study → system-design → spec → roadmap. Low ceremony; quality comes
from good templates and an honest self-critique ending every document.

Before producing anything:
1. Read `../CLAUDE.md`.
2. `make refs-sync` if `../references/dq-platform/` is absent; do not
   bump the pin (that's a deliberate, separate change).
3. Use the command matching your artifact; each loads its skill
   (`../.claude/skills/`) and template (`../templates/`).

If this file and `../CLAUDE.md` ever disagree, `CLAUDE.md` wins.
