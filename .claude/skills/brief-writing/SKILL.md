<!-- path: .claude/skills/brief-writing/SKILL.md -->

# Skill — Brief writing

A brief takes **one pillar** of the vision and turns it into operating
context an agent can act on **autonomously, over months**. It is the
elo between the strategic horizon (vision) and the architectural shape
(system-design): broader than a single capability, narrower than the
whole vision. One initiative per brief; the brief is *what the agent
carries with it* while producing the system-designs and specs that
deliver the initiative.

A brief is published. It stands alone — a reader needs neither the
study nor the reference behind it to follow the argument.

## How to think

**Write for the agent that picks it up six months in.** The audience
is not the colleague who lived the strategy meeting; it is the agent
who reads the brief cold and has to act. If the brief assumes context
that lives in your head, the autonomy promise breaks the first time
reality deviates from the explicit list.

**Make the decision principle load-bearing.** A list of open decisions
ages out — reality always raises questions you didn't list. The
*decision principle* — "when hitting an unlisted choice, optimize for
X over Y" — is what keeps an agent coherent when it walks off the map.
If you can't name X and Y for this initiative, you haven't scoped it
enough to delegate. Distinct from the vision's guiding principles
(repo-wide) — this one is initiative-specific and sharper.

**Done state is observable, not aspirational.** "Improved data
quality" is not a stop condition; "every rule pack ships with owner
metadata that the linter enforces" is. Each line of Done state should
be checkable by a third party with no interpretation — it is the
agent's stop signal, not a wish.

**Out of scope is half the document.** The boundary an initiative
refuses to cross is what keeps it focused. Pre-name two or three
adjacent things a reasonable colleague might pull in, and refuse them
with a one-line reason. A brief without out-of-scope is an open
invitation to drift.

**Decisions already made must be cited.** Anything in that section
must point at an ADR, a vision principle, or a prior brief. If a
decision has no provenance, it isn't decided — move it to Open
decisions. The cost of a forged "already made" is months of work in
the wrong direction.

**Don't sequence inside the brief.** The brief lists handoffs; it
does not order them. Sequencing belongs to the roadmap, and roadmaps
change faster than briefs should. A brief that orders its handoffs
becomes stale on the first slip.

## What good looks like

- An agent could be handed the brief, no other context, and (a) name
  three things the initiative refuses, (b) state when it can stop,
  and (c) make a coherent call on a choice not listed by using the
  decision principle.
- The Done state lines are checkable by a third party without asking
  the author what they meant.
- Decisions already made are all backed by a citation.
- The decision principle is specific to this initiative — not "do
  the right thing".
- The self-critique names a plausible choice the agent would still
  have to invent from thin air.

## Traps

- **The vision in miniature.** Restating the whole vision pillar in
  smaller words. A brief operationalizes one slice; if you can't say
  what's NEW in the brief versus the pillar, you didn't write a brief.
- **Decision principle as platitude.** "Optimize for quality over
  speed." Tells the agent nothing. The principle bites only when the
  X/Y trade is concrete and the *why* is load-bearing.
- **Outcomes that are not stop conditions.** Fluffy lines in Done
  state. If you cannot check it from outside, it does not count.
- **Soft out-of-scope.** "We will probably not do X." Either you
  refuse it or you don't. Soft refusal becomes silent inclusion.
- **Already-made laundering.** Listing decisions as "made" that were
  in fact assumed. The agent will trust it; the work will be wrong.
- **Sequencing creep.** Numbering handoffs, picking quarters,
  ordering system-designs. That's the roadmap's job. Briefs go
  stale slower than roadmaps by design — don't couple them.
- **Mirroring the reference's roadmap.** The reference has its own
  initiatives. Refuse to inherit their slicing; our brief carves the
  vision in our terms.

Template: `templates/brief.md`.
Output: `docs/strategy/<YYYY-MM-DD>-<slug>-brief.md`.
