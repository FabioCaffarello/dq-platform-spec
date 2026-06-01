<!-- path: .claude/skills/roadmapping/SKILL.md -->

# Skill — Roadmapping

A roadmap sequences existing specs. It introduces no new scope — it
decides *order* and defends *why*. Its value is entirely in the
reasoning behind the sequence.

## How to think

**Order follows dependencies, not appetite.** The sequence is driven by
what unblocks what. Build the dependency map first, then read the order
off it. If you're sequencing by what's fun or easy, you'll discover the
load-bearing work too late.

**Name what each item unblocks.** An item with nothing downstream and
nothing upstream doesn't belong in a sequence — it belongs in a backlog.
The roadmap is the critical path plus its tributaries.

**Deferral is a decision, so record it.** What you leave out of the
horizon matters as much as what you keep. State the deferred work and
why, so "we forgot" never masquerades as "we decided."

**Stress-test the order.** For each item ask: if this slips, what
breaks? The riskiest item on the critical path is the one to
de-risk first or sequence earliest.

**The topology is already in the index.** Each `type: spec` entry
carries the `parent` design ID and its stated dependencies — the
graph is precomputed, you do not have to rediscover it by reading
every spec from scratch. Use the index as the dependency map's
skeleton; open individual specs only to read the dependency lines
the index does not capture (cross-spec ordering inside the
*Dependencies* section).

## What good looks like

- The order is justified by the dependency map, item by item.
- Each item names what it unblocks.
- Deferred work is listed with reasons.
- The self-critique asks whether the order is dependency-driven or
  comfort-driven, and which item most threatens the chain.

## Traps

- **Wishlist, not roadmap:** an unordered pile of nice things. A
  roadmap without a dependency map is a wishlist.
- **Easy-wins-first:** front-loading quick wins while load-bearing work
  waits. Feels productive, ships nothing that matters.
- **New scope sneaking in:** if you're inventing work here instead of
  sequencing specs, stop and write a spec first.

Template: `templates/roadmap.md`.
Output: `docs/roadmap/<date>-roadmap.md`.
