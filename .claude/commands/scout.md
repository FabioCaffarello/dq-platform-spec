<!-- path: .claude/commands/scout.md -->

# /scout <slug>

Produce a wide-pass map of the reference. The zero step of the chain.

Load the skill `.claude/skills/scouting/SKILL.md` and the template
`templates/scout.md` before starting.

1. If `references/dq-platform/` is absent, tell the operator to run
   `make refs-sync`, then stop. Never reason about the reference from
   memory.
2. Capture the pin (`make refs-status`) — every citation uses this SHA.
3. Open `.claude/state/index.yaml` to confirm no current scout already
   maps this reference at this pin. A scout is run once per
   reference, or again after a pin move that invalidates the map. If
   one already exists and the pin has not moved meaningfully, stop
   and tell the operator.
4. Scan **breadth-first**. Open, in order: the root listing, root
   `README.md`, `AGENTS.md` / `CLAUDE.md` (the operating contract),
   the `docs/` index and the titles of every ADR under
   `docs/adr/`, the top of `studies/`, and the names of the
   top-level workspaces. Do NOT descend into implementation files.
5. Fill `templates/scout.md` into
   `studies/scout/<YYYY-MM-DD>-<slug>.md`, keeping each section at
   the verb-and-object level. The capability map and entry-points
   list are the load-bearing sections.
6. For every Entry-point row, lead with *why it matters first* — not
   what is in it. Three to seven entries is healthy.
7. Write the self-critique honestly — including what you did NOT
   open and where you drifted into depth.
8. End with a one-line commit summary.

Produces orientation, not learning. **Does not mergulhar** — a single
`/study` is the next move, not a deeper scout. Run again only when the
pin moves enough that the existing map no longer fits.
