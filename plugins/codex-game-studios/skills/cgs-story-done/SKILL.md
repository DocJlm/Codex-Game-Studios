---
name: cgs-story-done
description: "Codex Game Studios curated workflow adapted from original /story-done. Use when the user asks for /story-done, $cgs-story-done, or Verify and close a completed implementation story."
---

# CGS Story Done

Use `$cgs-story-done` after implementation to decide whether a story can close.

## Procedure

1. Read the story, diff, tests, linked GDDs, ADRs, and acceptance criteria.
2. Verify behavior, test evidence, documentation drift, design drift, and known risks.
3. If incomplete, return blockers and do not mark done.
4. If complete, offer to update the story status and summarize follow-up work.

## Output Contract

Return verdict: `DONE`, `NEEDS FIXES`, or `BLOCKED`.
Include acceptance criteria checklist and tests.
