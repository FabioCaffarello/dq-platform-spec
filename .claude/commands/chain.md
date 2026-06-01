<!-- path: .claude/commands/chain.md -->

# /chain <from> <to>

Run a contiguous segment of the distillation chain in one session.
Multi-elo runs need operator confirmation; every individual guard
still applies; the chain halts at any non-cosmetic self-critique.

This command is orchestration, not craft. The actual work is done by
the underlying `/scout`, `/study`, `/vision`, `/brief`,
`/system-design`, `/spec`, `/roadmap` commands — `/chain` only walks
them in order under harder safety constraints.

## Canonical chain (the only path)

```text
scout → study → vision → brief → system-design → spec → roadmap
```

`<from>` and `<to>` must both be on this path, with `<to>` downstream
of `<from>`. `/chain study brief` walks `study → vision → brief`.

## Before starting

1. **Compute the walk.** Enumerate the elos from `<from>` to `<to>`
   inclusive, following the canonical chain.
   - If `<to>` is not downstream of `<from>` (e.g., `/chain brief
     scout`), refuse.
   - If `<from>` and `<to>` are not on the same path, refuse.
   - **If the walk exceeds 3 elos, refuse.** A chain does not
     generate ten documents on its own.

   Refusal message:
   > Chain refused: `<reason>`. Run the elos separately, or pick
   > endpoints within 3 hops on the canonical chain.

   Then stop.

2. **Operator confirmation** (mandatory when walk > 1 elo). Print:
   > About to run: `<elo-1>` → `<elo-2>` → `<elo-3>`. This will
   > produce N artifacts. Reply `go` to proceed; anything else
   > stops the chain.

   Wait for explicit `go`. Anything else — silence, "wait", a
   question — stops. Do not assume consent.

3. **Load once at the top.** Read these files now and do NOT re-read
   them between elos:
   - `.claude/state/index.yaml`
   - For each elo in the walk:
     - `.claude/commands/<elo>.md`
     - `.claude/skills/<elo>/SKILL.md`
     - `templates/<elo>.md`

   CLAUDE.md is already in the session's system context — never
   re-load. The economy of `/chain` is *one chained session* instead
   of *three separate sessions*, each of which would re-read all of
   the above. Within a single Claude Code session the LLM already
   carries forward conversation context for free; what `/chain`
   removes is the per-elo file-loading overhead, not in-session
   token cost.

## Execution

For each elo in the walk, in order:

1. **Run the elo as if invoked directly.** Honor every step of
   its standalone command — including all guards (existence checks,
   coverage checks, missing-brief admonishment block). The chain
   adds safety constraints; it never relaxes one.

2. **Write the artifact to disk.** Do NOT commit. Do NOT regenerate
   the index manually (pre-commit will, on the eventual commit).

3. **Hand the new artifact's stable ID forward in conversation.**
   The next elo uses that ID directly; it does not re-discover from
   the on-disk index, which is now stale (see §"After a halt" below).

4. **Checkpoint at the self-critique** — the gate of the chain.

   Read the self-critique you just wrote. Apply the asymmetric
   materiality test:
   > **Halt unless the weakness is clearly cosmetic.** The same agent
   > writes and judges the self-critique, so the burden of proof is
   > on continuing. Material *or uncertain* → halt and call the
   > operator. Only proceed if cosmetic with no doubt.

   - **Material** (the next elo would build on this being right):
     - "I didn't read the reference file that grounds this claim."
     - "The done state has a line that isn't observable."
     - "Two pillars overlap; a brief would have to pick one
       arbitrarily."
     - "I assumed a constraint instead of verifying."
     - "The cited brief's done state does not name this slice."
   - **Cosmetic** (the next elo would not depend on this):
     - "Could be tighter prose."
     - "Wording of pillar 2 could be sharper."
     - "One more example would help."
     - "The title could be more specific."
   - **Uncertain** → treat as material. Halt.

   Halt message:
   > Chain halted at `<elo-id>`. The self-critique surfaces a
   > weakness the next elo would build on: `<one-line summary>`.
   > Resolve before continuing manually. Artifacts produced so far:
   > `<list of ids + paths>`.

5. **If a guard from the elo's own command fires**, honor it and
   stop the chain. Surface the guard's own message; do not paper
   over it.

6. **Decisions already made are not relitigated.** If the elo is a
   brief or downstream, treat `Decisions already made` entries as
   constraints. If a decision seems wrong, halt the chain and call
   the operator — do not silently work around it.

## After the chain (natural finish or halt)

Print a summary:

```text
Chain run: <from> → <to>
  Artifacts produced:
    - <id-1> (path-1)  status=<status>
    - <id-2> (path-2)  status=<status>
  Elos NOT run (and why, if halted): <list>
  Suggested manual next: /<command> <arg>  — <one-line reason>
```

**Do NOT commit.** The operator reviews and commits. This is
deliberate: one chain may produce up to 3 artifacts, which is a
larger surface than a single artifact session; the operator needs
the review window.

## After a halt — the index is stale

When the chain halts mid-walk, artifacts already written to disk
exist as files but **are not yet in `.claude/state/index.yaml`** —
pre-commit only regenerates the index on `git commit`, and the
chain does not commit.

Two consequences for the operator:

- The on-disk index reflects pre-chain state, not what the chain
  wrote. The chain's summary block (above) is the authoritative
  list of what was produced.
- If the operator inspects the working tree before committing,
  `git status` shows the artifact files as untracked or modified.
  That is expected — committing them is what brings the index back
  into sync.

If the operator wants to abandon a halted chain, deleting the
artifact files (and not committing) returns the tree to a coherent
state.
