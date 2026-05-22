# Spark Sprint Workflow Walkthrough

Use this walkthrough to test the v1.2 example project with Codex Game Studios.

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
- Identifies existing source, scene, and test drafts.
- Proposes scoped edits only if the user asks to continue implementation.

## `$cgs-smoke-check`

Expected result:
- Runs static validation when operating from the repository root.
- Runs `python tools\validate_godot_example.py`; this loads the scene when Godot is installed and reports `SKIP` otherwise.

## `$cgs-story-done production/epics/core-loop/STORY-001-player-loop.md`

Expected result:
- Returns `DONE` for static evidence if source, scene, tests, and smoke checklist satisfy the story.
- Calls out runtime playtest evidence as optional when Godot is unavailable.

## `$cgs-code-review`

Expected result:
- Reviews the source/test drafts with findings-first output.
- Checks that `scenes/main.tscn` exists and references the runtime scripts.
- Mentions whether optional Godot loading was run or skipped.

## `$cgs-qa-plan`

Expected result:
- Produces a scoped QA matrix for movement, pickup, timer, reset, HUD, and runtime playtest evidence.
