<!-- path: .claude/commands/system-design.md -->

# /system-design <topic>

Turn study learning into an architecture document.

Load `.claude/skills/system-design/SKILL.md` and
`templates/system-design.md` first.

1. Open `.claude/state/index.yaml` to discover inputs by type:
   - **studies** (`type: study`) — the learning beneath this design.
     If none exist yet, say so — a design with no study beneath it
     is a guess; confirm with the operator before proceeding.
   - **briefs** (`type: brief`) — if one frames this initiative,
     cite its stable ID in the header as `> Brief: brief:<slug>`.
     Its *Done state*, *In/Out of scope*, *Decisions already made*,
     and *Decision principle* are constraints on the design, not
     suggestions. If no brief exists yet, proceed (the chain allows
     it) and omit the `Brief:` line; note in the self-critique what
     strategic framing is missing.
   - **designs** (`type: design`) — to pick the next free NN.
2. Fill `templates/system-design.md` into
   `docs/system-design/<NN>-<slug>.md` (next free NN).
3. Write Problem and Non-goals first and tight. Design boundaries
   before insides. Spend real effort on Failure modes. Force one real
   Alternative.
4. Make it stand alone — restate reference ideas in our terms; the
   argument must not need the study or the reference.
5. Self-critique: name the part you'd least want to defend.
6. One-line commit summary.
