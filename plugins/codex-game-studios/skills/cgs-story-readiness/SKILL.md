---
name: cgs-story-readiness
description: "Codex Game Studios core workflow adapted from original /story-readiness. Use when the user asks for /story-readiness, $cgs-story-readiness, or Check whether a story is ready before implementation begins."
---

# CGS Story Readiness

Use `$cgs-story-readiness` before `$cgs-dev-story` or when a story feels ambiguous.

## Procedure

1. Read the target story, its epic, linked GDDs, ADRs, and control manifest.
2. Check scope, acceptance criteria, dependencies, assets, testability, and missing decisions.
3. Do not edit implementation files.
4. If blocked, provide the smallest question or upstream doc change needed.

## Output Contract

Return verdict: `READY`, `NEEDS WORK`, or `BLOCKED`.
Include evidence and next action.
