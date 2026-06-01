<!-- path: .claude/commands/study.md -->

# /study <topic>

Produce a study of the reference on `<topic>`.

Load the skill `.claude/skills/study-from-reference/SKILL.md` and the
template `templates/study.md` before starting.

1. If `references/dq-platform/` is absent, tell the operator to run
   `make refs-sync`, then stop. Never reason about the reference from
   memory.
2. Capture the pin (`make refs-status`) — every citation uses this SHA.
3. Open `.claude/state/index.yaml` to see what scouts and studies
   already exist. Your study may build on an adjacent thread or hit
   a topic an existing study already covers — discover, then decide.
4. If the topic's location in the reference isn't obvious, skim
   [`.claude/reference-map.md`](../reference-map.md) for file-level
   pointers (glossary, ADR series, decision log, governance). Scouts
   under `studies/scout/` cover capabilities — the map covers file
   locations they don't centralize.
5. Read the actual reference files bearing on `<topic>`. Depth over
   breadth.
6. Fill `templates/study.md` into `studies/<YYYY-MM-DD>-<slug>.md`,
   keeping "what the reference does / keep / leave behind / I'd do
   differently" cleanly separated.
7. Write the self-critique honestly — including what you did NOT read.
8. End with a one-line commit summary.

Produces learning, not a decision. Stops at the study.
