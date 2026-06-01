<!-- path: templates/vision.md -->
<!-- Template: VISION. Copy to docs/strategy/<YYYY-MM-DD>-<slug>-vision.md. -->
<!-- The STRATEGIC plane: where we are going, and why.
     Fed by scouts/studies (what exists and what we've learned).
     Hovers over the execution chain (system-design, spec, roadmap)
     — it does not replace any of them. -->

<!-- path: docs/strategy/<YYYY-MM-DD>-<slug>-vision.md -->

# Vision — <name>

> Status: draft | reviewed | stable
> Horizon: <year+ / "the next big thing" / etc.>
> Informed by: `studies/scout/<file>.md`, `studies/<file>.md`, …
> Reference pin (when leaning on it): dq-platform@<short-sha> (`make refs-status`)

## Background problem
<!-- The deeper problem this vision answers. Not "we want X" — the
     condition in the world that makes X worth wanting. 3–6 sentences.
     If you cannot state the problem without naming the solution, the
     vision isn't ready. -->

## Why now
<!-- What changed — in the reference, in the domain, in our learning —
     that makes this the right horizon to set now and not last year or
     next year. One paragraph. If "we just felt like it", say so and
     stop. -->

## Desired future state
<!-- A concrete picture of what is true when this vision is realized.
     Describe a day, a workflow, an observable behavior — NOT a slogan.
     "Operators see X without asking" beats "world-class observability".
     Be specific enough that a reader could disagree. -->

## Guiding principles
<!-- The 3–6 trade-off rules that decide hard calls along the way.
     Each: a SHORT principle + one line on WHEN it bites.
     "Boring substrate over novelty — when adding a dependency, prefer
      the one we already run in prod." -->

1. **<principle>** — when it bites: <one line>.
2. **<principle>** — when it bites: <one line>.

## Anti-goals
<!-- What this vision explicitly is NOT. Drawing the boundary is half
     the work — without anti-goals the vision collects features by
     gravity. State a few that you can imagine someone reasonably
     proposing, and refuse them here with one line each. -->

- NOT <thing> — because <one line>.
- NOT <thing> — because <one line>.

## Themes / pillars
<!-- The big blocks of work the vision implies, as THEMES — not a
     sequence, not a roadmap. Add one `### <Theme name>` subsection
     per pillar (the actual theme name as the heading). Three to five
     pillars is healthy; more, and the vision is diffuse.

     For each pillar, write a one-paragraph description of what it
     covers, what's inside and outside it, and one sentence on why
     it earns a pillar. Cite the reference where leaning on it:
     (ref: dq-platform@<sha> path §"Section").

     IMPORTANT — pillar-id convention. Add a stable ID per pillar via
     an HTML comment immediately before the heading:
       <!-- pillar-id: <slug> -->
     The slug is lowercase, dash-separated, and stable across edits.
     Briefs cite the pillar by `pillar:<vision-slug>:<pillar-slug>` —
     renaming the heading must not break the link. -->

<!-- pillar-id: rename-me-1 -->
### First theme name (rename or remove me)

<!-- pillar-id: rename-me-2 -->
### Second theme name (rename or remove me)

## Signals we're on the right path
<!-- Observable signs that the vision is being realized — qualitative
     where useful ("operators stop asking about X"), quantitative where
     honest ("Y% of rule packs ship with owner metadata"). Two to five.
     These are not KPIs to optimize; they are sanity checks on
     direction. -->

## Open premises
<!-- Beliefs the vision rests on that we have NOT validated. Name each
     premise + what would invalidate it. A vision without open premises
     is either a liturgy or a lie. -->

- <premise> — invalidated if: <one line>.

## Self-critique
<!-- Required, honest last section.
     - Where is this vision most likely a slogan in disguise?
     - Which premise would, if false, force a rewrite?
     - Did I describe a future state or just list features?
     - Is the "why now" really now, or is it post-hoc?
     - Could a thoughtful skeptic read this and not see what we'd refuse? -->
