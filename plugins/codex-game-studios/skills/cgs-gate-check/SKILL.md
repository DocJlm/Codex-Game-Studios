---
name: cgs-gate-check
description: "Codex Game Studios core workflow adapted from original /gate-check. Use when the user asks for /gate-check, $cgs-gate-check, or Run an advisory phase gate before advancing the game project."
---

# CGS Gate Check

Use `$cgs-gate-check` before moving between major phases.

## Procedure

1. Identify current and target phase from workflow catalog and project artifacts.
2. Read `production/review-mode.txt`; default to `lean` if missing.
3. Check required artifacts, unresolved risks, tests, design coverage, architecture coverage, and production readiness.
4. In `full` mode, apply creative-director, technical-director, producer, and qa-lead role-card perspectives sequentially.
5. Never hard-block the user; provide an advisory verdict.

## Output Contract

Return verdict: `PASS`, `PASS WITH CONCERNS`, or `FAIL`.
Include required fixes, optional fixes, and user decision options.
