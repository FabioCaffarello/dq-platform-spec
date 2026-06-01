<!-- path: .claude/commands/spec.md -->

# /spec <topic>

Turn one slice of a system design into a buildable spec.

Load `.claude/skills/spec-authoring/SKILL.md` and `templates/spec.md`
first.

1. Open `.claude/state/index.yaml`. Find the `type: design` entry
   this slice comes from; cite its ID in the spec header as
   `> Design: design:<slug>`. The integrity check blocks the commit
   if the cited ID doesn't exist. Also use the index to pick the
   next free NN.
2. If the index has **no `type: design` entry** the operator could
   plausibly mean, stop and tell them:
   > No system design exists yet for this slice. A spec turns ONE
   > slice of an architecture into something buildable — there is
   > no architecture to slice. Run `/system-design` first; come back
   > when the design exists.

   Then stop.
3. **Coverage check.** Open the design file at the entry's `path`
   and read its `## Architecture` block — specifically the
   `### Components` and `### Boundaries and contracts` subsections.
   The slice you are about to spec must be named there (by component
   name, boundary, or clearly-bounded responsibility). If it is
   **not** covered, stop and tell the operator:
   > The design `<design-id>` does not name this slice in its
   > `### Components` or `### Boundaries and contracts`. What it
   > does name: `<list the actual component/boundary names>`.
   > Either this spec belongs to a different design, or the design
   > needs updating first. Confirm before proceeding.

   This is judgment, not regex — synonyms and clear paraphrases
   count. A spec smuggled in past an architecture that does not
   frame it is exactly the silent failure this guard exists for.
4. Confirm the scope is ONE buildable slice. If it needs "and" three
   times, split it and pick one (one artifact per session).
5. Fill `templates/spec.md` into `docs/specs/<NN>-<slug>.md`.
6. Specify behavior and interface; leave implementation to the builder.
   Make acceptance observably checkable. State dependencies explicitly.
7. Self-critique: could someone build exactly this and still ship the
   wrong thing?
8. **Next handoff.** Print at the end of the artifact:
   > Next: `/spec <other-slice>` for the next adjacent component, or
   > `/roadmap` if the specs together cover the brief. One-line
   > reason for the choice.
9. One-line commit summary.
