// path: commitlint.config.mjs
//
// Conventional Commits, enforced via the commit-msg hook in
// .pre-commit-config.yaml. The rules are inlined (rather than
// `extends: ["@commitlint/config-conventional"]`) so commitlint does
// not need to resolve a peer package from the project directory —
// pre-commit installs its dependencies in a private cache that Node's
// resolver does not see from here.
//
// Subject case is unconstrained; header capped at 100 chars; bodies
// and footers are free so co-author trailers and longer rationales fit
// without ceremony.

const RULE_ERROR = 2;

export default {
  parserPreset: {
    parserOpts: {
      headerPattern: /^(\w+)(?:\(([^)]+)\))?!?: (.+)$/,
      headerCorrespondence: ["type", "scope", "subject"],
      noteKeywords: ["BREAKING CHANGE", "BREAKING-CHANGE"],
      revertPattern: /^(?:Revert|revert:)\s"?([\s\S]+?)"?\s*This reverts commit (\w+)\./i,
      revertCorrespondence: ["header", "hash"],
    },
  },
  rules: {
    "type-enum": [
      RULE_ERROR,
      "always",
      [
        "build",
        "chore",
        "ci",
        "docs",
        "feat",
        "fix",
        "perf",
        "refactor",
        "revert",
        "style",
        "test",
      ],
    ],
    "type-case": [RULE_ERROR, "always", "lower-case"],
    "type-empty": [RULE_ERROR, "never"],
    "subject-empty": [RULE_ERROR, "never"],
    "subject-full-stop": [RULE_ERROR, "never", "."],
    "header-max-length": [RULE_ERROR, "always", 100],
    "header-min-length": [RULE_ERROR, "always", 5],
  },
};
