<!-- path: AGENTS.md -->
<!-- audience: any AI coding agent that reads AGENTS.md by convention -->
<!-- status: living document, kept in sync with CLAUDE.md -->

# Agents Entry Point — DQ Platform Spec

This is the cross-agent convention file. The full operating guide is
**[`CLAUDE.md`](./CLAUDE.md)** — read it before producing anything.

## In one breath

This is a spec-authoring workspace. You read a pinned reference
(`dq-platform`, vendored under `references/`) and distill it into the
documents that guide real development:

```text
study → system-design → spec → roadmap
```

Low ceremony, high quality. Quality comes from good templates and from
every document ending in an honest self-critique — not from gates.

## Before you start

1. Read `CLAUDE.md` (the chain, the seven principles, the commands).
2. `make refs-sync` if `references/dq-platform/` is absent. Never
   reason about the reference from memory.
3. Pick the command for the artifact you're making (`/study`,
   `/system-design`, `/spec`, `/roadmap`); each loads its skill and
   template.

## The three that matter most

- **Read before you reason** — hydrate and open the real files.
- **Distill, don't copy** — judge reference patterns on fit, in our
  terms.
- **Every document doubts itself** — the self-critique section is the
  quality mechanism.
