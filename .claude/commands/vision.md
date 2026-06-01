<!-- path: .claude/commands/vision.md -->

# /vision <slug>

Set the strategic horizon — where we are going and why.

Load the skill `.claude/skills/vision-writing/SKILL.md` and the
template `templates/vision.md` before starting.

1. If `references/dq-platform/` is absent, tell the operator to run
   `make refs-sync`, then stop. Never reason about the reference from
   memory.
2. Capture the pin (`make refs-status`) — used in the `Reference pin`
   header and any citation.
3. Open `.claude/state/index.yaml` to inventory the inputs a vision
   must lean on:
   - **scouts**: entries with `type: scout`.
   - **studies**: entries with `type: study`.
   Cite scouts/studies by their stable IDs in the *Informed by*
   header; the human-readable filenames are in the `path` field of
   each entry.
4. If **no scout** and **no study** exist, the vision has nothing to
   stand on. Tell the operator:
   > No scout or study exists yet. A vision needs to lean on what
   > the reference IS (`/scout`) and what we have learned from it
   > (`/study`). Run `/scout <slug>` first; come back when at least
   > one of those exists.

   Then stop.
5. If a scout exists but no study, proceed — note in the document's
   "Informed by" header that this vision is "wide-based on the scout
   map alone; depth pass(es) still to come". Flag this in the
   self-critique too.
6. Fill `templates/vision.md` into
   `docs/strategy/<YYYY-MM-DD>-<slug>-vision.md`. The load-bearing
   sections are *Desired future state* (concrete, not slogan),
   *Anti-goals* (what we refuse), and *Open premises* (what we
   haven't proven).
7. Cite scouts/studies in *Informed by*; cite the reference with the
   pin where the vision leans on it directly.
8. **Do not number the pillars.** Themes are not a sequence — that is
   the roadmap's job. If you catch yourself ordering them, stop and
   move the order into a future `/roadmap`.
9. **Give every pillar a stable ID.** Immediately before each
   `### <theme name>` heading, add an HTML comment
   `<!-- pillar-id: <slug> -->`. The slug is lowercase, dash-separated,
   and survives heading rewordings. Briefs cite the pillar as
   `pillar:<vision-slug>:<pillar-slug>` — the integrity check blocks
   a brief whose pillar ID doesn't exist here.
10. Write the self-critique honestly — naming the section most likely
    to be a slogan in disguise, and the premise that would force a
    rewrite if it broke.
11. End with a one-line commit summary.

Produces strategic direction, not a sequence. Run again when the
underlying problem shifts or a load-bearing premise breaks — not on a
schedule.
