# Spark Sprint Workflow Walkthrough

Use this walkthrough to test the v0.6 example project with Codex Game Studios.

## `$cgs-start`

Expected result:
- Detects an already structured Codex Game Studios project.
- Finds `production/stage.txt` and `production/review-mode.txt`.
- Does not overwrite existing design, architecture, epic, or story files.

## `$cgs-project-stage-detect`

Expected result:
- Reports `PRODUCTION`.
- Detects Godot 4.3 / GDScript style from `project.godot` and technical preferences.
- Lists evidence paths for concept, systems index, architecture, epic, story, source, and tests.

## `$cgs-dev-story production/epics/core-loop/STORY-001-player-loop.md`

Expected result:
- Reads one story and the linked architecture/design context.
- Identifies existing source and test drafts.
- Proposes scoped edits only if the user asks to continue implementation.

## `$cgs-smoke-check`

Expected result:
- Runs static validation when operating from the repository root.
- Lists manual Godot runtime checks as remaining because this example does not require Godot in CI.

## `$cgs-story-done production/epics/core-loop/STORY-001-player-loop.md`

Expected result:
- Returns `DONE` only as a static example review if source, tests, and smoke checklist satisfy the story evidence.
- Calls out that runtime playtest evidence is not present.

## `$cgs-code-review`

Expected result:
- Reviews the source/test drafts with findings-first output.
- Mentions no runtime execution was performed unless Godot is available.

## `$cgs-qa-plan`

Expected result:
- Produces a scoped QA matrix for movement, pickup, timer, reset, HUD, and runtime playtest evidence.
