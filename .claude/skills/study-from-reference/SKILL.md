<!-- path: .claude/skills/study-from-reference/SKILL.md -->

# Skill — Studying a reference

A study extracts *learning* from the pinned reference. It is not a
decision and not a design — it is the honest reading that everything
downstream rests on.

## How to think

**Read the actual files.** The first move is always `make refs-sync`
then opening the real files under `references/dq-platform/`. The
reference is dense and well-reasoned; skimming it and reconstructing
from memory produces confident, wrong studies. If you cite it, you
read it.

**Describe in our terms.** When you explain what the reference does,
translate it into the vocabulary of *our* problem. "They use a
manifest with a generation-conditional pointer write" becomes useful
only when you say what that buys and whether we have the same need.

**Separate three things cleanly:**
- what the reference *does* (fact, cited),
- what's *worth keeping* for us (judgment, justified by fit),
- what *you'd do differently* (your idea, marked as yours).

Blurring these is the most common failure. A study that smuggles your
opinion in as "the reference says" poisons every design built on it.

**Judge on fit, not provenance.** "The reference does X" is never
itself a reason to do X. The reason is "X solves a problem we have."
If we don't have the problem, X goes in "leave behind."

## What good looks like

- Every reference claim is cited with the pin.
- "Keep" and "leave behind" each have real entries — a study that
  keeps everything didn't think.
- The self-critique names what you *didn't* read.

## Traps

- **Cargo-culting:** keeping a pattern because it's impressive, not
  because it fits.
- **Reverence:** treating the reference as correct by default. It
  solved *its* problem; ours may differ.
- **Breadth over depth:** touching twenty files shallowly instead of
  the five that matter, deeply.

Template: `templates/study.md`. Output: `studies/<date>-<slug>.md`.
