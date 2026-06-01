<!-- path: AGENTS.md -->
<!-- audience: any AI coding agent that reads AGENTS.md by convention -->
<!-- status: thin pointer; the operating guide is CLAUDE.md -->

# Agents Entry Point — DQ Platform Spec

The full operating guide is **[`CLAUDE.md`](./CLAUDE.md)** — read it
before producing anything. This file exists for agents that look for
`AGENTS.md` by convention.

## Before you start

1. Read `CLAUDE.md` (three planes, citation discipline, seven
   principles).
2. `make refs-sync` if `references/dq-platform/` is absent. Never
   reason about the reference from memory.
3. Pick the command for your artifact under `.claude/commands/`. Each
   loads its skill and template. Catalog:
   [`.claude/skills/README.md`](./.claude/skills/README.md).

## The three that matter most

- **Read before you reason** — hydrate and open the real files.
- **Distill, don't copy** — judge reference patterns on fit, in our
  terms.
- **Every document doubts itself** — the self-critique section is the
  quality mechanism.
