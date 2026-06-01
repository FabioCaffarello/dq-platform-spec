<!-- path: .claude/skills/system-design/SKILL.md -->

# Skill — System design

A system design turns accumulated study learning into architecture:
the components, boundaries, flows, and failure modes of the thing we're
building. It is the first *published* artifact — it must stand on its
own, without the studies or the reference behind it.

## How to think

**Start from the problem, not the solution.** Write the Problem and
Non-goals sections first and make them tight. Half of bad architecture
is solving a problem nobody stated, or solving three at once.

**Design the boundaries before the insides.** The valuable decisions
are where components meet — the contracts and invariants. Get those
right and the insides can be rewritten freely. Get them wrong and no
amount of clean code saves you.

**Spend your effort on failure modes.** A design that only describes
the happy path isn't a design, it's a wish. The Failure modes section
is where you find out if you actually understand the system. Name what
you chose *not* to protect against — that's a real decision.

**Make it stand alone.** Restate reference-derived ideas in our own
terms and defend them on our merits. If a reader needs the study to
follow your design, the design isn't finished. (Provenance can stay as
a one-line "informed by" note; the argument can't depend on it.)

**Force one real alternative.** If you can't articulate an architecture
you rejected and why, you haven't designed — you've taken the first
idea. The Alternatives section keeps you honest.

**Answer to the brief if one frames the initiative.** When a brief
exists, cite it in the header as `> Brief: brief:<slug>` — its
*Done state*, *Out of scope*, *Decisions already made* and
*Decision principle* are constraints on the design, not
suggestions. If no brief frames this design, an explicit warning
block goes at the top of the artifact; the missing strategic frame
is the first thing a reader sees, not something hidden in the
self-critique.

## What good looks like

- A new engineer could implement from this without reading anything
  else.
- Boundaries are explicit; each component has one responsibility.
- Failure modes are concrete and include deliberate non-protections.
- The self-critique names the part you'd least want to defend.

## Traps

- **Big-ball-of-mud diagram:** everything connects to everything. If
  the diagram has no clean cut lines, the design has no boundaries.
- **Premature precision:** specifying field-level detail that belongs
  in a spec. A system design is the shape, not the schema.
- **Happy-path-only:** see above. The failure section is load-bearing.

Template: `templates/system-design.md`.
Output: `docs/system-design/<NN>-<slug>.md`.
