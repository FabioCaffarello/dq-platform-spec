<!-- path: templates/brief.md -->
<!-- Template: BRIEF. Copy to docs/strategy/<YYYY-MM-DD>-<slug>-brief.md. -->
<!-- The STRATEGIC plane, downstream of vision. A brief takes ONE pillar
     of the vision and turns it into operating context an agent can
     act on autonomously: the mission, what's in and out, what's
     decided, the principle for deciding the rest, and what "done"
     looks like. -->

<!-- path: docs/strategy/<YYYY-MM-DD>-<slug>-brief.md -->

# Brief — <name>

> Status: draft | reviewed | active | retired
> Horizon: <e.g. Q3 2026 | "until the manifest writer ships">
> Vision pillar: pillar:<vision-slug>:<pillar-slug>
> Reference pin (when leaning on it): dq-platform@<short-sha> (`make refs-status`)

<!-- "Vision pillar" is the STABLE ID of the pillar this brief
     operationalizes. Find the ID in .claude/state/index.yaml under
     the vision's `pillars:` list — it derives from the vision's
     filename slug and the `<!-- pillar-id: ... -->` comment in the
     vision body. Citing the ID (not the heading text) keeps the
     link from breaking if the heading is reworded. The integrity
     check in pre-commit blocks the commit if the cited ID does not
     exist in the index. -->

## Mission
<!-- One paragraph. The slice of the vision this initiative advances,
     stated concretely. Not the whole vision — one theme — and what
     this initiative does inside it. If the mission can't be read
     without the vision, link it; the argument should still stand on
     its own once linked. -->

## Done state
<!-- The observable state of the world when this brief is delivered.
     Each line is BOTH the outcome ("this is true") and the stop
     condition ("the agent can stop"). Two to six lines is healthy.
     Write them so a third party could check each one without
     interpreting. -->

- <observable fact that is true when this is shipped>.
- <observable fact …>.

## Scope
<!-- Concrete and bulleted. Out of scope is where most briefs leak;
     spend effort there. -->

### In scope

- <thing the agent owns within this initiative>.

### Out of scope

- <adjacent thing the agent must NOT pull in, and the one-line reason>.

## Decisions already made
<!-- The named decisions an agent should NOT relitigate. Each: a
     short statement and a citation (ADR, prior brief, vision
     principle, study). If a decision has no provenance, it is not
     "made" yet — move it to Open decisions or write the ADR. -->

- <decision> — (ref: docs/adr/<NN>.md | docs/strategy/<…>-vision.md §"<principle>").

## Open decisions
<!-- The choices the agent must make as work proceeds. Lead with the
     DECISION PRINCIPLE — this is the meta-rule that holds when the
     specific list goes stale or hits a choice nobody anticipated.
     Without it, autonomous delegation degrades the moment reality
     deviates from the list. -->

**Decision principle**: when hitting an unlisted choice, optimize for
**<X>** over **<Y>** — because <one line, the load-bearing reason>.

<!-- Then the explicit open decisions, each with a one-line
     OPTIMIZATION CRITERION so they get resolved consistently. -->

- <open decision> — optimize for: <criterion>.
- <open decision> — optimize for: <criterion>.

## Operating constraints
<!-- Hard limits the agent must respect: technical, operational,
     organizational, regulatory. One line each. Anything that, if
     ignored, would invalidate the work. -->

- <constraint>.

## Handoffs
<!-- What comes after this brief. The system-designs to author, the
     specs likely to follow, the roadmap slot this will populate.
     Names + brief reason, not full plans. -->

- system-design: `docs/system-design/<NN>-<slug>.md` — <one-line role>.
- spec: `docs/specs/<NN>-<slug>.md` — <one-line role>.

## Risks the agent should watch for
<!-- What could go sideways during execution. Not generic risks —
     ones specific to this brief. Each: the signal + the
     corrective. -->

- <risk> — signal: <…> — corrective: <…>.

## Self-critique
<!-- Required, honest last section.
     - Where is the Done state wishful instead of observable?
     - Is the decision principle actually load-bearing, or generic
       advice that won't bite when reality deviates?
     - Did Out-of-scope refuse anything a reasonable colleague would
       have proposed? If not, the boundary is too soft.
     - Could an agent pick this up, work for two weeks, and discover
       a choice it had no way to make from this document? Name it. -->
