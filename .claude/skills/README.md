<!-- path: .claude/skills/README.md -->

# Skills index

One skill per craft. Each carries *how to think* while filling the
matching template — the patterns of a good artifact of that kind, the
traps, and what good looks like. Read the index to know what exists;
open the SKILL file when you're about to do that craft.

The skills follow the chain. Pick the one that matches the artifact
you're producing.

| Skill | Craft | Used by | Output |
|-------|-------|---------|--------|
| [`scouting/`](./scouting/SKILL.md) | Wide pass: map the reference's capabilities and vocabulary, no depth. | `/scout` | `studies/scout/` |
| [`study-from-reference/`](./study-from-reference/SKILL.md) | Deep pass on one topic: what the reference does, what to keep, what to leave. | `/study` | `studies/` |
| [`system-design/`](./system-design/SKILL.md) | Turn study learning into architecture that stands alone. | `/system-design` | `docs/system-design/` |
| [`spec-authoring/`](./spec-authoring/SKILL.md) | Turn a design slice into a buildable, checkable spec. | `/spec` | `docs/specs/` |
| [`roadmapping/`](./roadmapping/SKILL.md) | Sequence existing specs into an order defended by their dependencies. | `/roadmap` | `docs/roadmap/` |

## Adding a skill

Add a directory `<name>/SKILL.md` here, a matching command in
`.claude/commands/<name>.md`, and a template in `templates/<name>.md`.
Then add one row to the table above. Same shape as the five that
already exist. See `CLAUDE.md` §"Growth" for the rule of thumb.
