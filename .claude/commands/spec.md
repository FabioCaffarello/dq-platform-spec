<!-- path: .claude/commands/spec.md -->

# /spec <topic>

Turn one slice of a system design into a buildable spec.

Load `.claude/skills/spec-authoring/SKILL.md` and `templates/spec.md`
first.

1. Open `.claude/state/index.yaml`. Find the `type: design` entry
   this slice comes from; cite its ID in the spec header as
   `> Design: design:<slug>`. If no design exists, the architecture
   isn't framed yet — confirm with the operator before proceeding.
   The integrity check blocks the commit if the cited ID doesn't
   exist. Also use the index to pick the next free NN.
2. Confirm the scope is ONE buildable slice. If it needs "and" three
   times, split it and pick one (one artifact per session).
3. Fill `templates/spec.md` into `docs/specs/<NN>-<slug>.md`.
4. Specify behavior and interface; leave implementation to the builder.
   Make acceptance observably checkable. State dependencies explicitly.
5. Self-critique: could someone build exactly this and still ship the
   wrong thing?
6. One-line commit summary.
