---
name: cgs-qa-plan
description: "Codex Game Studios curated workflow adapted from original /qa-plan. Use when the user asks for /qa-plan, $cgs-qa-plan, or Create a focused QA plan for a story, milestone, prototype, or release candidate."
---

# CGS QA Plan

Use `$cgs-qa-plan` when the user needs test coverage for a gameplay story, milestone, prototype, or release candidate.

## Procedure

1. Read the story, epic, GDDs, architecture notes, known bugs, and target platforms.
2. Identify risk areas: core loop, input, save/load, UI feedback, performance, accessibility, localization, and platform differences.
3. Split checks into automated tests, manual smoke tests, exploratory passes, and evidence to capture.
4. Keep the plan small enough to run for the requested scope.
5. Offer to write or update `tests/SMOKE-CHECKLIST.md` or story-local QA notes after approval.

## Output Contract

Return scope, risk matrix, test list, evidence requirements, and exit criteria.
