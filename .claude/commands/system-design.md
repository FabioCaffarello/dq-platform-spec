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
     suggestions.
   - **designs** (`type: design`) — to pick the next free NN.
2. **Before omitting `Brief:`**, scan every `type: brief` entry in
   the index. If any brief's path or mission plausibly frames this
   initiative, **stop** and tell the operator:
   > Found `<brief-id>` in the index, which appears to frame this
   > design (`<one-line reason: slug match, mission overlap>`). Is
   > this the strategic brief this design answers to? If yes, cite
   > it as `> Brief: <brief-id>` in the header. If no, confirm so
   > I can proceed without a brief.

   Wait for the operator. Only proceed without `Brief:` after
   explicit confirmation, or when the index contains no briefs at
   all.
3. If proceeding without a brief, insert this admonishment in the
   generated artifact immediately after the blockquote header and
   **before** `## Problem`:
   > **No strategic brief frames this design.** Proceeding without
   > one is allowed by the chain, but this design has no `Done
   > state` to answer to. Run `/brief` first if the initiative
   > warrants strategic framing; otherwise the gap is deliberate
   > and the self-critique should justify it.

   The warning is visible, not hidden in `## Self-critique`. It
   travels with the document; a reader six months later sees the
   missing strategic framing immediately.
4. Fill `templates/system-design.md` into
   `docs/system-design/<NN>-<slug>.md` (next free NN).
5. Write Problem and Non-goals first and tight. Design boundaries
   before insides. Spend real effort on Failure modes. Force one real
   Alternative.
6. Make it stand alone — restate reference ideas in our terms; the
   argument must not need the study or the reference.
7. Self-critique: name the part you'd least want to defend.
8. One-line commit summary.
