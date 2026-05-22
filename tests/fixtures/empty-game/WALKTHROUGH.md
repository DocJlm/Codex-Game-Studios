# Empty Game Workflow Walkthrough

This fixture is not a real game implementation. It is a stable project shape for checking that the core Codex Game Studios loop gives useful, bounded answers.

## `$cgs-start`

Expected result:
- Detects an existing Codex Game Studios workspace.
- Reports `production/stage.txt` as `production` and `production/review-mode.txt` as `lean`.
- Does not recreate existing folders or overwrite planning files.
- Recommends `$cgs-project-stage-detect` or `$cgs-dev-story` as the next step.

## `$cgs-project-stage-detect`

Expected result:
- Detects Godot 4.3 / GDScript preferences from `docs/architecture/technical-preferences.md`.
- Reports `PRODUCTION` because concept, systems index, architecture, epic, and ready story exist.
- Lists evidence paths for the concept, architecture, epic, story, and smoke checklist.
- Calls out that source implementation evidence is intentionally absent.

## `$cgs-dev-story production/epics/core-loop/STORY-001-player-loop.md`

Expected result:
- Reads exactly one ready story.
- Produces a short implementation plan instead of broad project restructuring.
- Proposes scoped gameplay files and tests for movement, score, timer, and reset.
- Asks before writing unless the user has explicitly requested implementation.

## `$cgs-story-done production/epics/core-loop/STORY-001-player-loop.md`

Expected result:
- Returns `NEEDS FIXES` or `BLOCKED`, not `DONE`, because no implementation files or test evidence exist.
- Checks all four acceptance criteria.
- Names missing evidence: source changes, automated score/timer tests, and manual smoke result.
- Recommends `$cgs-dev-story` as the next action.

## `$cgs-gate-check`

Expected result:
- Reads `production/gates/production-readiness.md`, the story, architecture, and smoke checklist.
- Returns `BLOCKED`, not `PROCEED`, because implementation and test evidence are intentionally absent.
- Names missing evidence: source files, automated tests, manual smoke result, and story closure.
- Recommends `$cgs-dev-story` before another gate review.
