<!-- path: templates/scout.md -->
<!-- Template: SCOUT. Copy to studies/scout/<YYYY-MM-DD>-<slug>.md and fill. -->
<!-- A scout is the WIDE pass over the reference. Breadth, not depth.
     It produces a map that orients future /study runs — it does NOT decide
     anything and does NOT mergulhar in any one area. -->

<!-- path: studies/scout/<YYYY-MM-DD>-<slug>.md -->

# Scout — <reference name or slice>

> Reference pin: dq-platform@<short-sha> (`make refs-status`)
> Output of `/scout`. Breadth pass; depth belongs to `/study`.

## Purpose
<!-- One sentence: what the reference IS and FOR, in our words. If you
     can't say it in one line, you went too deep. Cite once:
     (ref: dq-platform@<sha> README.md). -->

## Reference shape
<!-- The top-level layout, one line per node. ASCII tree or short bullets.
     Don't describe contents — just name and locate. -->

```text
<name>/
├── <dir>/      — one-line role
├── <dir>/      — one-line role
└── <file>.md   — one-line role
```

## Capability map
<!-- The big areas of what the reference DOES. One row per capability.
     "What it does" stays at the verb-and-object level — leave the how
     for /study. -->

| Capability | What it does | Where it lives | Worth a /study? |
|------------|--------------|----------------|-----------------|
|            |              |                |  yes / later / no |

## Vocabulary
<!-- The terms a reader needs to make sense of anything else. Each term:
     one line, in our words, with a citation. If a term is overloaded in
     the reference, say so — that itself is a finding. -->

- **<term>** — short gloss (ref: dq-platform@<sha> path §"Section").

## Structural decisions
<!-- The architectural choices that SHAPE the reference. NAME and LOCATE
     them; do not evaluate. The point is "this is a load-bearing
     decision, study it later" — not "this is right or wrong". -->

- <decision name> — (ref: dq-platform@<sha> docs/adr/<NN>.md).

## Entry points for `/study`
<!-- The topics that justify a future depth pass, with WHY before WHAT.
     Three to seven is healthy; twenty means you stopped scouting and
     started cataloging. -->

1. **<topic>** — why it matters first: <one line>.
2. **<topic>** — why: <one line>.

## What I did NOT open
<!-- Honest list of dirs/files skipped, with a one-line reason
     ("generated", "deploy detail", "out of scope for this scout").
     A scout that claims to have read everything is lying. -->

- `<path>` — <reason>.

## Self-critique
<!-- Required, honest last section.
     - Where did I drift into depth instead of staying wide?
     - Which capability did I name without actually opening any file under it?
     - What in the reference resists a one-line summary, and why?
     - Did I take the reference's own self-description at face value? -->
