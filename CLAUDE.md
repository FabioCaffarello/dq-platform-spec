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

```text
Learning   :  scout  →  study
                          │
                          ▼
Strategic  :            vision  →  brief
                                     │
                                     ▼
Execution  :                       system-design  →  spec  →  roadmap
```

Each artifact distills the one before it. The detail — what good
looks like, the traps, the template to fill — lives in the matching
command (`.claude/commands/<name>.md`) and skill
(`.claude/skills/<name>/SKILL.md`). The catalog is
[`.claude/skills/README.md`](.claude/skills/README.md).

You do not have to walk the whole chain every time. A small change
may be a spec straight from an existing system design. Let the work
decide how far back up the chain you reach — but never skip *forward*
(no spec without the architecture that frames it existing somewhere,
even briefly).

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
