<!-- path: .claude/skills/spec-authoring/SKILL.md -->

# Skill — Spec authoring

A spec turns one slice of a system design into something buildable. It
is the artifact you hand to Claude Code, Codex, or a human and trust
them to implement without re-deriving the architecture.

## How to think

**One slice, not the whole design.** A system design may spawn many
specs. Each spec is the smallest coherent thing that can be built,
tested, and shipped on its own. If the scope needs the word "and" three
times, it's three specs.

**Specify behavior and contract; leave the how alone.** The implementer
owns the implementation. Your job is to make "did they build the right
thing?" answerable. Describe what it does observably, and the interface
it exposes — not the algorithm inside.

**Make acceptance checkable.** "Works correctly" is not acceptance.
"`validate(x)` returns an error when x is empty" is. If you can't write
the check, you haven't specified the behavior.

**State dependencies explicitly.** What must exist first? This is what
the roadmap consumes to sequence work. A spec with hidden dependencies
breaks the roadmap silently.

**The design must frame the slice.** Cite the parent in the header as
`> Design: design:<slug>`. Before writing, open that design and
confirm the slice is named in its `### Components` or
`### Boundaries and contracts` — by component name, boundary, or
clearly-bounded responsibility (synonyms and paraphrases count). A
spec written against a design that does not frame the slice is the
silent failure the coverage guard exists to catch; the right
discipline is to notice it before writing, not on the guard's stop.

## What good looks like

- The scope is one buildable slice with crisp in/out lists.
- Acceptance is a set of observable checks an implementer can self-test
  against.
- The interface is concrete enough to code against without guessing.
- The self-critique asks whether someone could build *exactly this* and
  still deliver the wrong thing.

## Traps

- **Mega-spec:** the whole system design crammed into one spec. Split
  it.
- **Process-as-acceptance:** "code reviewed, tests pass" — those are
  workflow, not acceptance. Acceptance is about the artifact's
  behavior.
- **Over-prescription:** dictating the implementation. You specify the
  contract; they own the code.
- **Under-specification:** leaving the hard 10% to "implementer's
  judgment." The hard 10% is exactly what the spec is for.

Template: `templates/spec.md`. Output: `docs/specs/<NN>-<slug>.md`.
