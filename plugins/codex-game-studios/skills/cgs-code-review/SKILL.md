---
name: cgs-code-review
description: "Codex Game Studios curated workflow adapted from original /code-review. Use when the user asks for /code-review, $cgs-code-review, or Review game code changes for correctness, scope, tests, and story alignment."
---

# CGS Code Review

Use `$cgs-code-review` when the user asks for a review of game code, a story diff, or a pull-request-style check.

## Procedure

1. Inspect the requested diff or changed files before summarizing.
2. Read the active story, linked GDDs, ADRs, path rules, and test notes when they exist.
3. Prioritize findings that can break gameplay, saves, builds, performance budgets, or acceptance criteria.
4. Keep role-card use sequential: technical director, lead programmer, qa lead, then producer only when scope drift is possible.
5. Do not rewrite the code during review unless the user explicitly asks for fixes.

## Output Contract

Lead with findings ordered by severity and include file paths plus line numbers when possible.
If no issues are found, say that clearly and list any test gaps or residual risks.
