<!-- path: docs/dev/branch-protection.md -->

# Branch protection — `main`

These settings live in GitHub, not in the repo. Apply them at
**Settings → Branches → Branch protection rules → Add rule** with
`main` as the branch name pattern.

## Required

- **Require a pull request before merging**
  - Require approvals: **1**
  - Dismiss stale pull request approvals when new commits are pushed: **on**
  - Require review from Code Owners: **on**
    (uses [`.github/CODEOWNERS`](../../.github/CODEOWNERS))

- **Require status checks to pass before merging**
  - Require branches to be up to date before merging: **on**
  - Required status check: **`Quality gates`**
    (from [`.github/workflows/ci.yml`](../../.github/workflows/ci.yml))

- **Require linear history**: **on**
  Keeps `git log --oneline` honest; merges are squash or rebase.

- **Restrict who can push to matching branches**: enable, leave empty.
  No direct pushes to `main` — everything goes through a PR.

- **Do not allow bypassing the above settings**: **on**, including
  for administrators.

## Optional, recommended once collaborators exist

- **Require signed commits**: **on**.
- **Require conversation resolution before merging**: **on**.

## How to verify

After applying, the GitHub PR UI for any new PR should show the
`Quality gates` check as required, and the merge button should be
disabled until it is green and one approval is recorded.

Re-run this check whenever the workflow name changes — GitHub matches
required checks by the **job name** (the `name:` of the job in the
workflow), so renaming the job silently breaks the protection rule.
