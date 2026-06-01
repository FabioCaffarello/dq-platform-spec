<!-- path: CONTRIBUTING.md -->

# Contributing

This repo produces **documents**, not code. The method — the
distillation chain, the seven principles, the commands — lives in
[`CLAUDE.md`](./CLAUDE.md). Read that first; this file only says how a
piece of work travels from idea to merge.

## The path

1. **Open an issue** using the form that matches your artifact:
   *study*, *system-design*, *spec*, or *roadmap*. The forms collect
   the fields the template will ask for anyway, so the issue is a
   draft of the work.
2. **Branch** off `main` as `<type>/<slug>` (e.g. `study/manifest-schema`,
   `spec/manifest-writer`). One artifact per branch.
3. **Produce the artifact** by running the matching command in Claude
   Code or Codex (`/study`, `/system-design`, `/spec`, `/roadmap`).
   The skill behind it knows how to think; the template knows the
   shape. End the document with an honest self-critique — that is the
   only quality gate inside the artifact.
4. **Open a PR** against `main`. The
   [PR template](./.github/pull_request_template.md) is the checklist.
   CI (`.github/workflows/ci.yml`) mirrors the local pre-commit hooks
   exactly, so if `pre-commit run --all-files` is green locally, CI is
   green too.
5. **Review and merge.** A document is in good shape when it stands
   alone, cites the reference where it draws on it, and is honest in
   its self-critique. Merge when those three hold.

## Labels

Labels are declared in [`.github/labels.yml`](./.github/labels.yml) and
reconciled by the `Sync labels` workflow. Add or rename there, not in
the GitHub UI. Three axes:

- `type:` — what the work produces (study / system-design / spec / roadmap / adr / devops)
- `stage:` — where it is (draft → review → ready)
- `area:` — what slice it touches; extend as the project grows

## Branch protection

`main` is protected. The settings to apply on the GitHub side are
documented in [`docs/dev/branch-protection.md`](./docs/dev/branch-protection.md).

## Growing the harness

The harness is minimal on purpose. Grow by addition, never by
rewriting from scratch:

- A new reference → new `references/<name>.lock`, add `<name>/` to
  `.gitignore`, `make refs-sync`. The script already loops over locks.
- A repeated craft → a new skill under `.claude/skills/`.
- A new artifact type → a template + a skill + a command, same shape
  as the seven that exist (scout, study, vision, brief, system-design,
  spec, roadmap).

## What not to do

- Don't reason about the reference from memory. Hydrate it
  (`make refs-sync`) and open the actual files.
- Don't touch `references/` — it is read-only vendored content.
- Don't bump the pin as a side effect. A pin move is its own commit
  with a one-line reason.
- Don't add ceremony. If a step here feels like paperwork, change it
  here.
