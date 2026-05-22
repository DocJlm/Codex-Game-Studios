# Spark Sprint Codex Run Transcript

This transcript records a realistic Codex Game Studios pass through the Spark Sprint example. It is written as a concrete usage transcript for an optional runnable Godot example that still validates without requiring Godot to be installed.

Project path:

```text
examples/spark-sprint/
```

Story path:

```text
examples/spark-sprint/production/epics/core-loop/STORY-001-player-loop.md
```

## 1. Onboard The Example

User:

```text
Use $cgs-start on examples/spark-sprint. Do not edit files unless something required is missing.
```

Codex:

```text
Detected state: structured Codex Game Studios example project.
Stage file: examples/spark-sprint/production/stage.txt -> production
Review mode: examples/spark-sprint/production/review-mode.txt -> lean
Engine signal: examples/spark-sprint/project.godot plus Godot 4.3 technical preferences.

Evidence paths:
- examples/spark-sprint/design/gdd/game-concept.md
- examples/spark-sprint/design/gdd/systems-index.md
- examples/spark-sprint/docs/architecture/architecture.md
- examples/spark-sprint/production/epics/core-loop/EPIC.md

Files updated: none.
Next skill: $cgs-project-stage-detect
```

## 2. Detect Production Stage

User:

```text
Use $cgs-project-stage-detect on examples/spark-sprint. Report the stage and evidence paths.
```

Codex:

```text
Verdict: PRODUCTION

Why:
- Concept, systems index, architecture, control manifest, epic, and story exist.
- Source drafts exist under examples/spark-sprint/src/.
- Test and smoke evidence drafts exist under examples/spark-sprint/tests/.
- The story is already in Review state, so this is beyond planning but not a release candidate.

Evidence paths:
- examples/spark-sprint/project.godot
- examples/spark-sprint/docs/architecture/technical-preferences.md
- examples/spark-sprint/production/epics/core-loop/STORY-001-player-loop.md
- examples/spark-sprint/scenes/main.tscn
- examples/spark-sprint/src/gameplay/game_controller.gd
- examples/spark-sprint/tests/test_game_controller.gd

Next 3 actions:
1. $cgs-dev-story for the player loop story.
2. $cgs-smoke-check to verify static evidence and optional Godot scene loading.
3. $cgs-story-done and $cgs-gate-check to decide whether the story and production gate can close.
```

## 3. Pick Up The Story

User:

```text
Use $cgs-dev-story examples/spark-sprint/production/epics/core-loop/STORY-001-player-loop.md. Implement only if the story is not already covered.
```

Codex:

```text
Readiness: READY

Plan:
- Read story, epic, core-loop GDD, architecture, control manifest, scene, and source drafts.
- Compare acceptance criteria against MainScene, GameController, PlayerController, Collectible, HUD, and test draft.
- Avoid writing changes unless coverage is missing.

Inspection result:
- Movement draft exists: examples/spark-sprint/src/gameplay/player_controller.gd
- Score, timer, win, timeout, and reset logic exists: examples/spark-sprint/src/gameplay/game_controller.gd
- Pickup draft exists: examples/spark-sprint/src/gameplay/collectible.gd
- HUD draft exists: examples/spark-sprint/src/ui/hud.gd
- Main scene exists: examples/spark-sprint/scenes/main.tscn
- Static tests cover score, win, timeout, and reset: examples/spark-sprint/tests/test_game_controller.gd

Files updated: none. The story is already represented by source, scene, and test drafts.
Next skill: $cgs-smoke-check
```

## 4. Run A Smoke Check

User:

```text
Use $cgs-smoke-check for examples/spark-sprint.
```

Codex:

```text
Commands run:
- python tools\validate_examples.py
- python tools\validate_godot_example.py

Result:
- Example validation passed.
- Godot scene validation loaded the scene when Godot was available, or reported SKIP when Godot was not installed.

Automated coverage:
- Required project files exist.
- Walkthrough and docs mention the full workflow sequence.
- Source drafts include MainScene, GameController, PlayerController, Collectible, and HUD tokens.
- Scene draft references runtime scripts.
- Test draft includes score, win, timeout, and reset cases.

Manual checks remaining:
- Launch the Godot scene when a local editor/runtime is available.
- Confirm input bindings move the player.
- Confirm collecting 5 sparks sets the state to won.
- Confirm pressing R resets score, timer, and spark visibility.

Next skill: $cgs-story-done
```

## 5. Close The Story

User:

```text
Use $cgs-story-done examples/spark-sprint/production/epics/core-loop/STORY-001-player-loop.md.
```

Codex:

```text
Verdict: DONE for static example evidence, with optional runtime evidence when Godot is available.

Acceptance criteria:
- Player entity can move in four directions: covered by PlayerController draft and scene.
- Collectible pickup increments score: covered by Collectible and GameController drafts.
- Timer reaches zero and ends the round: covered by GameController draft and test draft.
- Reset returns score, timer, and round state to initial values: covered by GameController draft and test draft.

Evidence:
- examples/spark-sprint/scenes/main.tscn
- examples/spark-sprint/src/gameplay/main_scene.gd
- examples/spark-sprint/src/gameplay/player_controller.gd
- examples/spark-sprint/src/gameplay/collectible.gd
- examples/spark-sprint/src/gameplay/game_controller.gd
- examples/spark-sprint/src/ui/hud.gd
- examples/spark-sprint/tests/test_game_controller.gd
- examples/spark-sprint/tests/SMOKE-CHECKLIST.md

No story status edit was needed; the story already says Status: Review.
Next skill: $cgs-gate-check
```

## 6. Run A Gate Check

User:

```text
Use $cgs-gate-check for examples/spark-sprint.
```

Codex:

```text
Verdict: PROCEED WITH RISKS

Gate evidence reviewed:
- examples/spark-sprint/production/epics/core-loop/EPIC.md
- examples/spark-sprint/production/epics/core-loop/STORY-001-player-loop.md
- examples/spark-sprint/docs/architecture/architecture.md
- examples/spark-sprint/scenes/main.tscn
- examples/spark-sprint/tests/SMOKE-CHECKLIST.md
- python tools\validate_examples.py
- python tools\validate_godot_example.py

Why:
- Static example validation passes.
- Story acceptance criteria are represented by scene, source, and test drafts.
- Optional Godot runtime validation either loaded the scene or reported SKIP because Godot was unavailable.

Advisory risk:
- Manual runtime playtest evidence is still recommended before treating this as production gameplay.

Files updated: none.
Next skill: $cgs-code-review
```

## 7. Review The Example Code

User:

```text
Use $cgs-code-review on the Spark Sprint source draft.
```

Codex:

```text
Findings:
- No P0/P1 issues found in the static example review.
- P2 examples/spark-sprint/tests/test_game_controller.gd: tests are GDScript-style drafts, not an installed Godot test runner. Keep this documented until a real test plugin is added.

Open questions:
- Should a future release add a real Godot test runner, or keep this as a lightweight scene demo?

Test gaps:
- Optional Godot runtime validation may be skipped when Godot is not installed.
- Visual playtest evidence is still manual.

Change summary:
- No source changes were made during review.
```

## 8. Create A QA Plan

User:

```text
Use $cgs-qa-plan for examples/spark-sprint/production/epics/core-loop/EPIC.md.
```

Codex:

```text
Scope:
- Core loop movement, pickup, score, timer, reset, HUD feedback, and story evidence.

Risk matrix:
- Medium: scene wiring for pickup and HUD labels should be checked in a local Godot playtest.
- Medium: input bindings differ across keyboard layouts or controller support.
- Medium: timer edge cases around zero and repeated reset.
- Low: static source/test documentation drift.

Test matrix:
- Automated static: python tools\validate_examples.py.
- Optional runtime load: python tools\validate_godot_example.py.
- Source review: MainScene, GameController, PlayerController, Collectible, and HUD drafts.
- Manual runtime: launch scene, move in four directions, collect 5 sparks, wait for timeout, reset.
- Evidence: command output, screenshots or short capture for runtime pass, updated smoke checklist.

Exit criteria:
- Static validator passes.
- Optional Godot validator passes or reports SKIP because Godot is unavailable.
- Runtime playtest evidence is attached when a local Godot runtime is available.
```

## Final State

The current run demonstrates the full Spark Sprint loop:

```text
$cgs-start -> $cgs-project-stage-detect -> $cgs-dev-story -> $cgs-smoke-check -> $cgs-story-done -> $cgs-gate-check -> $cgs-code-review -> $cgs-qa-plan
```

The transcript keeps Codex behavior read-first, evidence-based, and explicit about the boundary between required static validation and optional Godot runtime testing.
