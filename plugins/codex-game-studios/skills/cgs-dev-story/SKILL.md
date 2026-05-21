---
name: cgs-dev-story
description: "Codex Game Studios curated workflow adapted from original /dev-story. Use when the user asks for /dev-story, $cgs-dev-story, or Implement one ready story using Codex-native engineering workflow."
---

# CGS Dev Story

Use `$cgs-dev-story` to implement exactly one ready production story.

## Procedure

1. Read the story, epic, linked GDDs, ADRs, control manifest, path rules, and relevant role cards.
2. Inspect existing code before proposing changes.
3. Produce a short implementation plan with files to touch and tests to run.
4. Implement only the story scope after the user confirms the plan or has clearly asked for execution.
5. Run targeted tests and update story status or notes only when requested or when the story workflow requires it.

## Output Contract

Return changed files, tests run, acceptance criteria status, and next `$cgs-story-done` command.
