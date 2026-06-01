<!-- path: CLAUDE.md -->
<!-- audience: Claude Code, Codex CLI, and any other AI coding agent in this workspace -->
<!-- status: living document. Edit it when it is wrong. -->

# Operating Guide — DQ Platform Spec

This is a **spec-authoring** workspace. You read a reference, and from
it you produce the documents that guide real development: studies,
system designs, specs, roadmaps. The product of this repository is
**thinking made durable** — not code.

The goal is high quality with low ceremony. Quality here does not come
from gates you must pass; it comes from good templates that make you
think about the right things, and from the habit of every document
ending by interrogating itself. There are no numbered acceptance
criteria, no blocking-finding rituals, no session router. If a step
ever feels like paperwork, it is wrong — change it.

---

## Three planes

Work in this repository sits on three planes that feed one another:

- **Learning** — `studies/scout/` (the wide map) and `studies/` (the
  depth passes). What the reference IS and what we have learned from
  it. Scaffolding, not published.
- **Strategic** — `docs/strategy/`. Two artifacts:
  *vision* (long-horizon: where we are going and why) and
  *brief* (one pillar of the vision turned into operating context an
  agent can act on autonomously). Fed by learning; hovers over
  execution.
- **Execution** — `docs/system-design/`, `docs/specs/`,
  `docs/roadmap/`. How we get there: architecture, buildable slices,
  sequence. Each artifact answers to the strategic plane above and
  draws on the learning plane below.

`docs/adr/` cuts across the planes: any decision durable enough to
deserve a name lives there.

---

## The distillation chain

The execution plane flows in one direction. Each stage consumes the
one before it and distills it further.

```text
Learning   :  scout  →  study
                          │
                          ▼
Strategic  :            vision  →  brief
                                     │
                                     ▼
Execution  :                       system-design  →  spec  →  roadmap
```

Read top-to-bottom: each plane feeds the one below. Read left-to-right
within a plane: each artifact distills the one before it. Vision and
brief both live in `docs/strategy/`; system-design, spec, roadmap each
get their own subdirectory under `docs/`.

- **Scout** (`studies/scout/`) — the wide pass. Once per reference (or
  again after a big pin move), you map what the reference IS and
  DOES: top-level shape, capabilities, vocabulary, structural
  decisions, and the topics that earn a future `/study`. A scout
  *orients*; it does not mergulhar.
- **Study** (`studies/`) — you read the pinned reference and extract
  what matters: the patterns worth keeping, the decisions worth
  understanding, the traps worth avoiding. A study is *learning*, not
  a decision.
- **Vision** (`docs/strategy/`) — the long horizon: where we are
  going, why now, the principles that guide trade-offs, and what we
  explicitly refuse. Strategic plane. Durable until a load-bearing
  premise breaks.
- **Brief** (`docs/strategy/`) — one pillar of the vision turned into
  operating context: mission, observable done state, in/out of scope,
  decisions already made (cited), and the *decision principle* an
  agent uses when reality deviates from the explicit list. Strategic
  plane. One brief per initiative.
- **System design** (`docs/system-design/`) — you turn accumulated
  learning into architecture: components, boundaries, data flow,
  failure modes, the shape of the thing. Answers to the brief that
  framed the initiative (if one exists).
- **Spec** (`docs/specs/`) — you turn a slice of the architecture into
  something buildable: scope, interface, behavior, acceptance.
- **Roadmap** (`docs/roadmap/`) — you sequence the specs: what comes
  first, what unblocks what, why this order.

You do not have to walk the whole chain every time. A small change may
be a spec straight from an existing system design. A new domain starts
with a study — opened on the map the scout already drew. Let the work
decide how far back up the chain you reach — but never skip *forward*
(no spec without the architecture that frames it existing somewhere,
even briefly).

`docs/adr/` exists for the rare decision durable enough to record as an
Architecture Decision Record. Most thinking lives as studies and
designs; promote to an ADR only when a choice will be referenced
repeatedly and must not be relitigated.

---

## How the reference feeds the work

The reference (`dq-platform`) is vendored under `references/`, pinned
to a commit, and **read-only**. Hydrate it with `make refs-sync`
before reasoning about it — never reason about it from memory.

When a document draws on the reference, it says so plainly, with the
pin so the claim stays reproducible:

```text
(ref: dq-platform@<short-sha> path/to/file.md §"Section")
```

That is the whole citation discipline. No more, no less. A claim that
is your own gets no citation but should be visibly *your* claim, not
smuggled in as if the reference said it.

---

## Principles (not rules)

These are short on purpose. They are how we keep quality without
ceremony.

1. **Distill, don't copy.** The reference is input, not a template to
   clone. Describe its patterns in our own terms and judge them on
   fit. We are building our thing, not mirroring theirs.
2. **Read before you reason.** Hydrate the reference and read the
   actual files. Memory is not a source.
3. **Every document ends by doubting itself.** The last section of
   every artifact is a short, honest self-critique: the weakest part,
   what wasn't validated, what would change the conclusion. This is
   the quality mechanism — embedded, not a separate round.
4. **One artifact per session.** Finish a study, a design, a spec, or
   a roadmap pass. Park adjacent ideas for next time.
5. **Studies are scaffolding; published docs stand alone.** A vision,
   brief, system design, spec, or ADR must read without the reader
   having seen the study or the reference behind it. Don't link
   published docs back into `studies/`.
6. **The pin moves deliberately.** Bumping the reference commit is its
   own change with its own one-line reason — never a side effect.
7. **Markdown opens with its path.** Every `.md` starts with
   `<!-- path: ... -->` so it survives being moved or extracted.

When a principle is wrong for the work in front of you, say so and
change it here. Silent divergence is the only real violation.

---

## How to behave in a session

- **Sketch before you write.** For anything beyond a one-file edit,
  say in two lines what you're about to produce and why, then go.
- **Pick the right template.** Each artifact type has one under
  `templates/`. The matching skill in `.claude/skills/` explains how
  to think while filling it.
- **Prefer short and sharp.** Long prose hides the trade-off. Cut.
- **End with a one-line commit summary** the human can paste.

---

## Commands

Under `.claude/commands/`. Each produces one artifact, grouped by
plane.

Learning:

- `/scout <slug>` — wide pass over the reference; produces a map in
  `studies/scout/`. Run once per reference, or again after a pin move
  that invalidates it.
- `/study <topic>` — read the reference and produce a study in
  `studies/`.

Strategic:

- `/vision <slug>` — set the long-horizon direction, drawing on
  scouts and studies; produces a vision document in
  `docs/strategy/`. Run when starting a new horizon or when a
  load-bearing premise breaks — not on a schedule.
- `/brief <slug>` — turn one pillar of an existing vision into
  operating context an agent can carry over months; produces a brief
  in `docs/strategy/`. Run once per initiative.

Execution:

- `/system-design <topic>` — turn studies into an architecture doc in
  `docs/system-design/`, answering to the vision above.
- `/spec <topic>` — turn a design slice into a buildable spec in
  `docs/specs/`.
- `/roadmap` — sequence existing specs into `docs/roadmap/`, in
  service of the vision.

Skills under `.claude/skills/` carry the craft for each (how to think,
what good looks like, common traps). Templates under `templates/` carry
the shape.

---

## Growth

This is minimal on purpose and grows by addition:

- A new reference → new `references/<name>.lock`, add `<name>/` to
  `.gitignore`, `make refs-sync`. The script already loops over locks.
- A repeated craft → a new skill under `.claude/skills/`.
- A new artifact type → a template + a skill + a command, same shape
  as the four that exist.

Grow by adding, never by rewriting from scratch.
