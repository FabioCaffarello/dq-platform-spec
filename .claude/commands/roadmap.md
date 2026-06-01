<!-- path: .claude/commands/roadmap.md -->

# /roadmap

Sequence existing specs into a roadmap. Introduces no new scope.

Load `.claude/skills/roadmapping/SKILL.md` and `templates/roadmap.md`
first.

1. Open `.claude/state/index.yaml`. Inventory entries with
   `type: spec` and their `parent` IDs (each spec's design); open
   each spec only to read its *Dependencies* section.
2. If **no `type: spec` entries exist** in the index, the roadmap
   has nothing to sequence. Tell the operator:
   > No specs exist in `docs/specs/`. A roadmap orders existing
   > specs — there is nothing to sequence yet. Run `/spec` for the
   > slices you want to ship; come back when at least one spec exists.

   Then stop.
3. Build the dependency map first; read the order off it.
4. Fill `templates/roadmap.md` into
   `docs/roadmap/<YYYY-MM-DD>-roadmap.md`.
5. For each item, name what it unblocks and why it sits where it does.
   Record deferred work with reasons. Stress-test the order.
6. Self-critique: dependency-driven or comfort-driven? Which item most
   threatens the chain?
7. One-line commit summary.
