<!-- path: .claude/skills/scouting/SKILL.md -->

# Skill — Scouting

A scout is the **wide pass** over the reference. It produces a map of
what the reference IS and DOES — its top-level shape, its capabilities,
its essential vocabulary, the structural decisions that hold it
together. A scout is *not* a study: it orients future depth passes; it
does not run them.

A scout is the **zero step** of the chain. You usually run it once per
reference, and again only when the pin moves enough to invalidate the
map. Everything downstream — `/study`, `/system-design`, `/spec`,
`/roadmap` — leans on it without saying so.

## How to think

**Breadth before depth, always.** The job is to see the whole thing
once, badly, before you see any part of it well. If you find yourself
reading a single ADR closely, you've stopped scouting. Note it as a
`/study` entry point and move on.

**Map the structure, don't redescribe it.** Open the top of the tree,
read the READMEs, scan the ADR titles, glance at the directory names.
Name what's there in one line each. The reference's own
self-description is a starting point, not a result — restate in our
words and flag where the labels mislead.

**Separate "load-bearing" from "incidental".** A decision recorded as
an ADR, a directory that several others depend on, a file the agents'
contract repeatedly cites — that's structural. A test fixture, a
generated artifact, a one-off script — that's incidental. Capture the
first, list the second only to mark you saw it.

**Name a future study; don't start it.** The "Entry points for /study"
section is the point of the scout. For each topic, lead with *why it
matters first* — the reason it earns a depth pass — not *what's in
it*. If you can't articulate the why in one line, it isn't an entry
point yet.

**Distill, don't copy.** Their five workspaces are not our five
workspaces. The capability map is what the reference *does*, in our
terms, not a clone of their directory listing.

## What good looks like

- A reader uses the scout to decide what to `/study` first, and gets
  pointed at the right thing.
- The capability table is short (under ~10 rows), each row clear at
  the verb-and-object level.
- The vocabulary lists only terms a reader *needs* to follow the
  rest of the map — not every named concept in the reference.
- The self-critique names where you slipped into depth, and which
  capability you mapped without opening any file beneath it.

## Traps

- **Scouting becomes studying.** You opened one ADR, then another,
  then read the code it cites. Stop. Capture the topic as an entry
  point, close the file, go wider.
- **Cloning their structure.** Listing the reference's top-level dirs
  in the capability map verbatim. The map describes *capabilities*
  ("rule validation", "compiled rule plans") — not folders.
- **Trusting their tagline.** Repeating the reference's own one-line
  description as your Purpose. Restate it in our words; if it
  resists restatement, that's a finding.
- **The 30-topic entry-point list.** If everything is worth studying,
  nothing is. Three to seven, ranked by why-first.
- **Reading only top-level READMEs.** Top README plus AGENTS/CLAUDE
  plus the ADR titles plus the directory layout is the minimum.
  Stopping at just the README means you mapped the marketing, not
  the system.

Template: `templates/scout.md`.
Output: `studies/scout/<YYYY-MM-DD>-<slug>.md`.
