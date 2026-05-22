---
name: cgs-regression-suite
description: "Codex Game Studios curated workflow adapted from original /regression-suite. Use when the user asks for /regression-suite, $cgs-regression-suite, or Audit or maintain a regression-suite manifest for critical paths and fixed bugs."
---

# CGS Regression Suite

Use `$cgs-regression-suite` when preparing a release, closing a sprint, or checking whether fixed bugs and critical paths have regression coverage.

## Procedure

1. Determine mode: `report` for read-only status, `audit` for full coverage review, or `update` when the user explicitly wants manifest changes.
2. Read existing `tests/regression-suite.md` if present, then inspect tests, closed bugs, recent stories, GDD critical paths, and release notes.
3. Map critical paths and fixed bugs to existing automated or manual regression evidence.
4. Identify missing, partial, stale, flaky, and quarantined coverage.
5. Write or update the manifest only after explicit user approval.

## Coverage Rules

- Critical gameplay state machines, formulas, save/load paths, and fixed severe bugs should have regression coverage.
- Visual or feel checks can be manual, but must name evidence and owner.
- Quarantined tests remain listed; they are not silently removed.

## Output Contract

Return mode, files scanned, coverage summary, missing regression tests, stale entries, recommended manifest changes, and verdict: `OK`, `GAPS`, or `STALE`.
