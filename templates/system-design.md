<!-- path: templates/system-design.md -->
<!-- Template: SYSTEM-DESIGN. Copy to docs/system-design/<NN>-<slug>.md. -->
<!-- Turns accumulated STUDY learning into architecture. Stands alone:
     a reader needs neither the studies nor the reference to follow it. -->

<!-- path: docs/system-design/<NN>-<slug>.md -->

# System Design — <name>

> Status: draft | reviewed | stable
> Informed by: <studies/… filenames> (provenance only; this doc stands alone)

## Problem
<!-- What are we building and why does it need to exist? 3-5 sentences.
     No reference needed to understand this. -->

## Goals and non-goals
<!-- Goals: what success looks like, bulleted.
     Non-goals: what we are explicitly NOT doing, so scope stays honest. -->

## Constraints
<!-- The forces the design must respect: technical, operational, cost,
     organizational. Each one line. -->

## Architecture
<!-- The shape of the solution. Components and their responsibilities,
     boundaries between them, how data and control flow. Use a diagram
     in fenced ASCII or a linked image if it earns its place. -->

### Components
<!-- Per component: name, single responsibility, what it owns, what it
     depends on. -->

### Data and control flow
<!-- The main path(s) through the system, step by step. -->

### Boundaries and contracts
<!-- Where components meet: the interface, the invariant each side holds. -->

## Failure modes
<!-- What goes wrong, how the system behaves when it does, and what we
     chose NOT to protect against (and why). This section is where most
     bad designs reveal themselves. -->

## Alternatives considered
<!-- At least one real alternative architecture and why we didn't pick it.
     "We considered nothing" is a design smell. -->

## Open questions
<!-- Unresolved design points. Each: the question + what would resolve it. -->

## Self-critique
<!-- Required, honest last section.
     - Where is this design most likely wrong?
     - Which constraint did I assume rather than verify?
     - What's the part I'd least want to defend in review?
     - Does it actually stand alone, or does it secretly need the study? -->
