---
name: cgs-qa-plan
description: "Codex Game Studios curated workflow adapted from original /qa-plan. Use when the user asks for /qa-plan, $cgs-qa-plan, or Create a focused QA plan for a story, milestone, prototype, or release candidate."
---

# CGS QA Plan

Use `$cgs-qa-plan` when the user needs test coverage for a gameplay story, milestone, prototype, or release candidate.

## Procedure

1. Read the story, epic, GDDs, architecture notes, known bugs, and target platforms.
2. Identify risk areas: core loop, input, save/load, UI feedback, performance, accessibility, localization, and platform differences.
3. Split checks into automated tests, manual smoke tests, exploratory passes, device or platform checks, and evidence to capture.
4. Keep the plan small enough to run for the requested scope; name what is intentionally out of scope.
5. Offer to write or update `tests/SMOKE-CHECKLIST.md`, story-local QA notes, or a release candidate checklist after approval.

## Evidence Rules

- Each acceptance criterion needs at least one verification path.
- Manual checks must name the scene, input path, expected result, and evidence artifact.
- Automated checks must name the command and the behavior they cover.

## Output Contract

Return scope, risk matrix, test matrix, evidence requirements, owner handoff, and exit criteria.
