<!-- path: .claude/commands/system-design.md -->

# /system-design <topic>

Turn study learning into an architecture document.

Load `.claude/skills/system-design/SKILL.md` and
`templates/system-design.md` first.

1. Identify the studies in `studies/` that inform `<topic>`. If none
   exist yet, say so — a design with no study beneath it is a guess;
   confirm with the operator before proceeding.
2. Check `docs/strategy/` for a brief that frames this initiative
   (`*-brief.md`). If one exists, the design answers to it — its
   *Done state*, *In/Out of scope*, *Decisions already made*, and
   *Decision principle* are constraints on the design, not
   suggestions. If no brief exists yet, proceed (the chain allows it);
   note in the self-critique what strategic framing is missing.
3. Fill `templates/system-design.md` into
   `docs/system-design/<NN>-<slug>.md` (next free NN).
4. Write Problem and Non-goals first and tight. Design boundaries
   before insides. Spend real effort on Failure modes. Force one real
   Alternative.
5. Make it stand alone — restate reference ideas in our terms; the
   argument must not need the study or the reference.
6. Self-critique: name the part you'd least want to defend.
7. One-line commit summary.
