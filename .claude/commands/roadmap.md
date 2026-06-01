<!-- path: .claude/commands/roadmap.md -->

# /roadmap

Sequence existing specs into a roadmap. Introduces no new scope.

Load `.claude/skills/roadmapping/SKILL.md` and `templates/roadmap.md`
first.

1. Inventory the specs in `docs/specs/` and their stated dependencies.
2. Build the dependency map first; read the order off it.
3. Fill `templates/roadmap.md` into
   `docs/roadmap/<YYYY-MM-DD>-roadmap.md`.
4. For each item, name what it unblocks and why it sits where it does.
   Record deferred work with reasons. Stress-test the order.
5. Self-critique: dependency-driven or comfort-driven? Which item most
   threatens the chain?
6. One-line commit summary.
