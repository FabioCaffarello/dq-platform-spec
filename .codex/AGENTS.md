<!-- path: .codex/AGENTS.md -->
<!-- audience: Codex CLI -->
<!-- status: thin pointer; the operating guide is ../CLAUDE.md -->

# Codex Entry Point — DQ Platform Spec

The authoritative guide is **[`../CLAUDE.md`](../CLAUDE.md)**. This
file exists because Codex looks for `.codex/AGENTS.md` by convention.

Before producing anything:

1. Read `../CLAUDE.md`.
2. `make refs-sync` if `../references/dq-platform/` is absent; do not
   bump the pin (that's a deliberate, separate change).
3. Pick the command matching your artifact under
   `../.claude/commands/`. Each loads its skill and template.

If this file and `../CLAUDE.md` ever disagree, `CLAUDE.md` wins.
