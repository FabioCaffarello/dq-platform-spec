<!-- path: .claude/skills/vision-writing/SKILL.md -->

# Skill — Vision writing

A vision sets the **strategic horizon** — where we're going and why
the work along the way adds up to something. It is *not* part of the
execution chain; it hovers above it. Scout and study feed it (what
exists, what we've learned); system-design, spec, and roadmap answer
to it (architecture, build, sequence).

A vision is durable. You rewrite it when the underlying problem shifts
or the open premises break — not because a quarter ended.

## How to think

**Describe a state, not a slogan.** "World-class observability" is
not a vision; "operators see why a rule failed without leaving the
alert" is. If a reader can't disagree with your sentence, you didn't
say anything — you applauded yourself.

**Anchor in what we learned, not what we wish.** The vision leans on
scouts and studies: it inherits the vocabulary, the constraints, the
named patterns. If you can write the vision without opening any
study, you wrote a wish. Cite the studies/scouts the vision is
"informed by".

**Separate direction from sequence.** A vision is *where*, not *when*.
Themes/pillars are blocks of intent, not ordered work. The order is
the roadmap's job — and a different doc. If you find yourself
numbering pillars or saying "first we'll do X then Y", you've stopped
writing vision and started writing a roadmap.

**Make refusal as visible as ambition.** The anti-goals section is
the most underused part of a vision. Drawing the boundary keeps
features from sneaking in by gravity. Name two or three things a
reasonable colleague might propose, and refuse them here with one line
each.

**Surface the load-bearing premises.** A vision rests on beliefs that
aren't yet proven. Name them. "Operators will adopt a self-service
flow if friction stays under X" is a premise, not a fact. The vision
that hides its premises will keep being right until it suddenly isn't.

**Stand alone — but admit provenance.** Like a system design, a vision
is published; it must read without the studies behind it. The
"Informed by" header points at the provenance; the argument doesn't
depend on it.

**Pillars carry stable IDs.** Each `### <theme name>` heading is
preceded by `<!-- pillar-id: <slug> -->`. The slug is the handle
downstream briefs cite as `pillar:<vision-slug>:<pillar-slug>`; it
survives heading rewordings. Pick slugs that read clearly six
months from now — short, dash-separated, semantically pointed
(`rule-pack-ownership`, not `theme-2`). Renaming a slug is a
real edit that breaks brief citations; the integrity check will
catch it, but you should avoid the churn.

## What good looks like

- A new engineer reads it and can name three things this team would
  refuse to build.
- A skeptic reads it and can articulate the disagreement — there is
  enough specificity to push back on.
- The pillars are themes (one paragraph each), not a backlog.
- The open premises section is honest and short; each premise has a
  "would invalidate this if" sentence.
- The self-critique names the part most likely to be a slogan in
  disguise.

## Traps

- **The empty slogan.** "Best-in-class data quality." Reader can't
  disagree, can't act on it, can't refuse anything by reading it.
  Replace with a state someone could observe.
- **Vision as feature list.** A bulleted "we will ship A, B, C, D" is
  a backlog with a hat on. Vision is the *shape* the list serves; it
  is not the list.
- **Vision unmoored from learning.** Written from intuition or copied
  from the reference's own vision. Vision must lean on our scouts and
  studies — otherwise it is wish or mimicry.
- **Premises buried as facts.** Stating "users want X" as a given
  when the studies don't show it. The Open premises section is the
  honest landing for these — use it.
- **Roadmap creep.** Numbering pillars, picking quarters, sequencing
  themes. Vision is direction; the moment it gets sequential, it
  becomes a roadmap and stops being durable.
- **Mirroring the reference's vision.** The reference has its own
  goals; we are building our thing. Restate problems in our terms;
  refuse the temptation to inherit slogans.

Template: `templates/vision.md`.
Output: `docs/strategy/<YYYY-MM-DD>-<slug>-vision.md`.
