<!-- path: .claude/reference-map.md -->

# Reference map — `dq-platform`

> Pinned to: dq-platform@4124478 (branch `main`)
> Living document. Revisit whenever the pin in
> [`references/dq-platform.lock`](../references/dq-platform.lock)
> moves enough to invalidate the layout below.
> `scripts/check-reference-pin.sh` warns when the SHA on this line
> diverges from the lock.

This is the **"you are here"** for the reference, kept short by hand
so any agent (Claude, Codex, future you) can orient in seconds. It is
**not** a [`/scout`](commands/scout.md) report — those are dated and
versioned under `studies/scout/`. It is **not** a study, a design, or
our architecture either.

## What dq-platform is

A monorepo Data Quality runtime: declarative YAML rule specifications,
authored per data entity with explicit ownership, compiled and
executed by a Go engine that integrates with a scheduler and emits
reports and alerts. The repo is organized as five logical workspaces
that share a `go.work` and a common ADR backbone
(ref: dq-platform@4124478 README.md).

## The five workspaces

| Workspace | What it owns | Where deep work lives |
|-----------|--------------|-----------------------|
| `engine/` | Go runtime: DSL schema source of truth, compilers, scheduler integration, reporting, alerting. | `engine/cmd/`, `engine/internal/` |
| `rules/`  | Declarative YAML rule specs per entity; owner metadata; governance workflow. | `rules/_schema/`, `rules/<domain>/` |
| `tools/`  | Auxiliary CLIs: linter, dry-run runner, manifest publisher, path-safe utilities, migrations. | `tools/{lint,dryrun,manifest,migrate,pathsafe}/` |
| `deploy/` | Kubernetes manifests, observability, dashboards, environment overlays. | `deploy/{base,overlays,observability,dashboards}/` |
| `docs/`   | Cross-workspace documentation: ADRs (MADR), architecture notes, glossary, governance, runbooks, security. | `docs/{adr,architecture,dev,runbooks,security}/` |

## Where to find what

- **AI agent contract** (hard rules R1–R8, principles P1–P6,
  slash-command catalog) — [`CLAUDE.md`](../references/dq-platform/CLAUDE.md).
  `AGENTS.md` at the root is a thin pointer to it.
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
- **Contributing** — `CONTRIBUTING.md`. The reference's own
  contribution flow (not ours — ours lives in this repo's
  `CONTRIBUTING.md`).
- **Studies (theirs)** — `studies/{critiques,decisions,foundation}/`.
  Their working notes; useful to triangulate intent behind an ADR.

## What this map is NOT

- **Not a scout.** A scout is dated, versioned in `studies/scout/`,
  and produces a capability map, vocabulary, and entry points for
  `/study`. This file is hand-maintained and intentionally tiny —
  enough to orient, no more.
- **Not a study.** A study mergulha on one topic. This file names
  things and locates them; it does not interpret them.
- **Not our architecture.** Our system designs live under
  `docs/system-design/`. This map only describes the *reference*.

## When to update this file

- After hydrating a new pin (`make refs-sync`) that meaningfully
  moves the layout — directories renamed, workspaces added or
  removed, ADRs renumbered.
- After a `/scout` that surfaces structure not captured here.
- Never as a side effect of unrelated work. Update it in its own
  commit, with a one-line reason — same discipline as moving the pin.
