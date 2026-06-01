<!-- path: .claude/commands/study.md -->

# /study <topic>

Produce a study of the reference on `<topic>`.

Load the skill `.claude/skills/study-from-reference/SKILL.md` and the
template `templates/study.md` before starting.

1. If `references/dq-platform/` is absent, tell the operator to run
   `make refs-sync`, then stop. Never reason about the reference from
   memory.
2. Capture the pin (`make refs-status`) — every citation uses this SHA.
3. Read the actual reference files bearing on `<topic>`. Depth over
   breadth.
4. Fill `templates/study.md` into `studies/<YYYY-MM-DD>-<slug>.md`,
   keeping "what the reference does / keep / leave behind / I'd do
   differently" cleanly separated.
5. Write the self-critique honestly — including what you did NOT read.
6. End with a one-line commit summary.

Produces learning, not a decision. Stops at the study.
