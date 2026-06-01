<!-- path: templates/spec.md -->
<!-- Template: SPEC. Copy to docs/specs/<NN>-<slug>.md. -->
<!-- Turns one slice of a system design into something BUILDABLE.
     A spec is what you hand to Claude Code / Codex / a human to implement. -->

<!-- path: docs/specs/<NN>-<slug>.md -->

# Spec — <name>

> Status: draft | ready | building | done
> Design: docs/system-design/<NN>-<slug>.md (the architecture this implements)

## Summary
<!-- One paragraph: what this spec delivers when built. -->

## Scope
<!-- In scope: bulleted, concrete.
     Out of scope: equally concrete, so the implementer doesn't drift. -->

## Behavior
<!-- What the thing does, observably. Written so an implementer knows
     when they've built the right thing. Use scenarios where useful:
     "given … when … then …". -->

## Interface
<!-- The contract: API shape, CLI, schema, function signatures — whatever
     this slice exposes. Concrete enough to code against. -->

## Acceptance
<!-- How we'll know it's correct. Observable checks, not process steps.
     "X returns Y for input Z", not "code reviewed". -->

## Dependencies
<!-- What must exist first (other specs, infra, decisions). This feeds
     the roadmap's sequencing. -->

## Implementation notes
<!-- Optional: hints, gotchas, suggested approach. NOT prescriptive —
     the implementer owns the how. -->

## Self-critique
<!-- Required, honest last section.
     - Is the scope a single buildable slice, or secretly three?
     - Is the acceptance actually checkable, or hand-wavy?
     - What did I underspecify that the implementer will have to guess?
     - Could someone build exactly this and still have the wrong thing? -->
