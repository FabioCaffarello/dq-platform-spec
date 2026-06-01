<!-- path: .claude/commands/system-design.md -->

# /system-design <topic>

Turn study learning into an architecture document.

Load `.claude/skills/system-design/SKILL.md` and
`templates/system-design.md` first.

1. Identify the studies in `studies/` that inform `<topic>`. If none
   exist yet, say so — a design with no study beneath it is a guess;
   confirm with the operator before proceeding.
2. Fill `templates/system-design.md` into
   `docs/system-design/<NN>-<slug>.md` (next free NN).
3. Write Problem and Non-goals first and tight. Design boundaries
   before insides. Spend real effort on Failure modes. Force one real
   Alternative.
4. Make it stand alone — restate reference ideas in our terms; the
   argument must not need the study or the reference.
5. Self-critique: name the part you'd least want to defend.
6. One-line commit summary.
