---
name: cgs-start
description: "Codex Game Studios curated workflow adapted from original /start. Use when the user asks for /start, $cgs-start, or First-run onboarding for a new or unorganized game project."
---

# CGS Start

Use `$cgs-start` when the user wants to begin using Codex Game Studios in a new or lightly organized game project.

## Procedure

1. Inspect first: check `AGENTS.md`, `production/stage.txt`, `production/review-mode.txt`, `design/gdd/game-concept.md`, `docs/architecture/`, `production/epics/`, and source files under `src/`.
2. Summarize the discovered state in 5 lines or fewer.
3. Ask only the missing product choices: concept maturity, preferred engine, and review mode (`solo`, `lean`, or `full`).
4. Create or update only the minimum setup files after the user confirms the draft:
   - `production/stage.txt`
   - `production/review-mode.txt`
   - missing project folders
   - optional starter concept stub when the user asks for one
5. End with the next concrete skill, usually `$cgs-brainstorm`, `$cgs-setup-engine`, or `$cgs-project-stage-detect`.

## Output Contract

Return: detected state, decisions captured, files to create or update, and next skill.
