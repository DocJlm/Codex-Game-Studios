---
name: cgs-test-evidence-review
description: "Codex Game Studios curated workflow adapted from original /test-evidence-review. Use when the user asks for /test-evidence-review, $cgs-test-evidence-review, or Review whether test files and manual evidence are strong enough to support story or milestone closure."
---

# CGS Test Evidence Review

Use `$cgs-test-evidence-review` before `$cgs-story-done`, QA handoff, milestone review, or release review when evidence quality matters.

## Procedure

1. Read the target story, epic, acceptance criteria, test plan, and referenced evidence files.
2. Locate automated tests, smoke check notes, manual evidence, screenshots, transcripts, CI logs, or playtest notes.
3. Map each acceptance criterion to at least one evidence item.
4. Review evidence quality: meaningful assertions, edge cases, manual sign-off, freshness, and reproducibility.
5. Keep the pass read-only unless the user asks to write a persistent review note.

## Verdict Rules

- `ADEQUATE`: every closure-critical criterion has credible evidence.
- `INCOMPLETE`: evidence exists but is thin, stale, missing sign-off, or missing important edge cases.
- `MISSING`: one or more closure-critical criteria have no evidence.

## Output Contract

Return scope, evidence table, criterion coverage, blocking gaps, advisory gaps, verdict, and next skill.
Route missing implementation evidence to `$cgs-dev-story`; route missing smoke evidence to `$cgs-smoke-check`.
