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
3. Open `.claude/state/index.yaml` to inventory inputs:
   - **visions**: entries with `type: vision`. Each carries a
     `pillars:` list with stable IDs (`pillar:<vision-slug>:<pillar-slug>`).
   - **scouts**: entries with `type: scout`.
   - **studies**: entries with `type: study`.
4. If **no vision** exists in the index, the brief has no pillar to
   operationalize. Tell the operator:
   > No vision document exists in `docs/strategy/`. A brief takes
   > ONE pillar of an existing vision and turns it into operating
   > context — there is no pillar to point at yet. Run `/vision
   > <slug>` first; come back when at least one vision file exists.

   Then stop.
5. If a vision exists but **no study**, proceed with a soft warning —
   the brief can stand on the vision and any scout, but the
   self-critique must flag that no depth pass grounds it yet.
6. Ask the operator (or infer from the slug) which **pillar** of which
   vision this brief serves. Cite the pillar in the header by its
   stable ID: `> Vision pillar: pillar:<vision-slug>:<pillar-slug>`.
   The integrity check blocks the commit if the ID doesn't exist in
   the index — so picking the wrong slug fails fast.
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
10. **Next handoff.** Print at the end of the artifact:
    > Next: `/system-design <slug>` matching this brief — turn the
    > pillar into architecture. One-line reason naming the most
    > architecturally load-bearing piece of the brief.
11. End with a one-line commit summary.

Produces operating context, not a plan. Run once per initiative; it
lives until the underlying pillar shifts or the work is retired.
