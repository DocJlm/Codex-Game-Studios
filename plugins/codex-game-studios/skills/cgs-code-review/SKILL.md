---
name: cgs-code-review
description: "Codex Game Studios curated workflow adapted from original /code-review. Use when the user asks for /code-review, $cgs-code-review, or Review game code changes for correctness, scope, tests, and story alignment."
---

# CGS Code Review

Use `$cgs-code-review` when the user asks for a review of game code, a story diff, or a pull-request-style check.

## Procedure

1. Inspect the requested diff or changed files before summarizing; use `git diff`, PR files, or explicit paths.
2. Read the active story, linked GDDs, ADRs, path rules, and test notes when they exist.
3. Prioritize findings that can break gameplay, saves, builds, performance budgets, platform constraints, or acceptance criteria.
4. Keep role-card use sequential: technical director, lead programmer, qa lead, then producer only when scope drift is possible.
5. Do not rewrite code during review unless the user explicitly asks for fixes.

## Severity Rules

- `P0`: corrupts data, prevents launch, blocks shipping, or makes the game unplayable.
- `P1`: breaks story acceptance criteria, core loop behavior, tests, or important platform behavior.
- `P2`: creates maintainability, UX, performance, or coverage risk that should be fixed soon.
- `P3`: polish or follow-up note.

## Output Contract

Lead with findings ordered by severity. Include file paths and line numbers when possible.
Then list open questions, test gaps, and a short change summary.
If no issues are found, say that clearly and still report residual risk.
