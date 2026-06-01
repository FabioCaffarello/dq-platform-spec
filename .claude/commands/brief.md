<!-- path: .claude/commands/brief.md -->

# /brief <slug>

Turn one pillar of the vision into operating context an agent can act
on autonomously. The elo between strategic horizon and architectural
shape.

Load the skill `.claude/skills/brief-writing/SKILL.md` and the
template `templates/brief.md` before starting.

1. If `references/dq-platform/` is absent, tell the operator to run
   `make refs-sync`, then stop. Never reason about the reference from
   memory.
2. Capture the pin (`make refs-status`) — used in the header and
   any citation.
3. Inventory inputs:
   - **vision**: every `docs/strategy/*-vision.md`.
   - **scouts**: every `studies/scout/*.md` (excluding `.gitkeep`).
   - **studies**: every `studies/*.md` (excluding the `scout/`
     subdirectory and `.gitkeep`).
4. If **no vision** exists, the brief has no pillar to operationalize.
   Tell the operator:
   > No vision document exists in `docs/strategy/`. A brief takes
   > ONE pillar of an existing vision and turns it into operating
   > context — there is no pillar to point at yet. Run `/vision
   > <slug>` first; come back when at least one vision file exists.

   Then stop.
5. If a vision exists but **no study**, proceed with a soft warning —
   the brief can stand on the vision and any scout, but the
   self-critique must flag that no depth pass grounds it yet.
6. Ask the operator (or infer from the slug) which **pillar** of which
   vision this brief serves. If multiple visions exist, name the file
   explicitly in the header — a brief without a pillar reference is
   not a brief.
7. Fill `templates/brief.md` into
   `docs/strategy/<YYYY-MM-DD>-<slug>-brief.md`. The load-bearing
   sections are *Done state* (observable, no fluff), *Out of scope*
   (refuse adjacent work explicitly), *Decisions already made*
   (every line cited), and the **Decision principle** at the top of
   *Open decisions* (specific X-over-Y for THIS initiative, with the
   load-bearing why).
8. **Do not sequence the handoffs.** List them; do not order them.
   Sequencing belongs to `/roadmap`.
9. Write the self-critique honestly — name the choice an agent would
   still have to invent from thin air given only this brief.
10. End with a one-line commit summary.

Produces operating context, not a plan. Run once per initiative; it
lives until the underlying pillar shifts or the work is retired.
