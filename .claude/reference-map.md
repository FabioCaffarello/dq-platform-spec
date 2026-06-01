<!-- path: .claude/reference-map.md -->
<!-- This file is NOT a scout, a study, or our architecture.
     A scout (studies/scout/) mergulha on capabilities and produces a
     dated map; this file only points at file locations a scout does
     not centralize (glossary, decision log, governance, ADR series).
     The high-level framing of dq-platform ("what it is", workspace
     table) lives in scouts — duplicating it here would bias future
     scouts toward repeating the existing framing. -->
<!-- Read by /study for file-level orientation. /scout does not open
     this map. Update in its own commit when the pin moves enough to
     invalidate a pointer below. -->

# Reference map — `dq-platform`

> Pinned to: dq-platform@4124478 (branch `main`)
> Living document. `scripts/check-reference-pin.sh` warns when the
> SHA on this line diverges from
> [`references/dq-platform.lock`](../references/dq-platform.lock).

## Where to find what

- **AI agent contract** (hard rules R1–R8, principles P1–P6,
  slash-command catalog) — `CLAUDE.md` at the reference root.
  `AGENTS.md` is a thin pointer to it. (Paths under `references/`
  are gitignored hydrated content; not linked from here so CI link
  checks stay clean.)
- **Architecture Decision Records** — `docs/adr/` (MADR-aligned).
  ADRs `0001–0013` cover Wave 1 (compatibility, identity, storage,
  failure scope, manifest publication, alerting, loader semantics)
  and Wave 2 (Git host, multi-agent contract, substrate posture,
  documentation language, tag conventions), plus Wave 3 phase
  sequencing.
- **Glossary** — `docs/glossary.md`. Authoritative definitions for
  reference-internal terms; consult before introducing your own.
- **Governance** — `docs/governance.md`. How decisions are taken and
  who owns what.
- **Decision log (state)** — `studies/foundation/06-decision-log.md`.
  Current state of every decision (open / in-progress / settled).
- **Kickoff** — `KICKOFF.md`. The framing document for the current
  wave of work.
- **Studies (theirs)** — `studies/{critiques,decisions,foundation}/`.
  Their working notes; useful to triangulate intent behind an ADR.
