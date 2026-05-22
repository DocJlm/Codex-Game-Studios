---
name: cgs-scope-check
description: "Codex Game Studios curated workflow adapted from original /scope-check. Use when the user asks for /scope-check, $cgs-scope-check, or Detect scope creep by comparing a story, epic, sprint, or milestone against its baseline plan."
---

# CGS Scope Check

Use `$cgs-scope-check` when the user asks whether a story, epic, sprint, milestone, or feature has drifted from the approved plan.

## Procedure

1. Identify the baseline: story, epic, sprint plan, milestone, GDD, or architecture document.
2. Inspect current implementation, open story notes, changed files, and relevant commits when available.
3. Compare planned items to current items; separate additions, removals, and substitutions.
4. Classify each change as required discovery, optional polish, accidental creep, or formal re-scope.
5. Recommend cuts or deferrals that preserve the player-facing core loop.

## Verdict Rules

- `PASS`: net change is small and acceptance criteria remain intact.
- `CONCERNS`: additions are manageable but need explicit cuts, deferrals, or owner approval.
- `FAIL`: scope no longer matches the baseline and needs re-planning before more implementation.

## Output Contract

Return baseline evidence, current evidence, additions, removals, risk, verdict, and the smallest re-scope action.
Do not edit planning or implementation files unless the user explicitly asks.
