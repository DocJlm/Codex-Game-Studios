# Spark Sprint Codex Run Transcript

This v0.8 transcript records a realistic Codex Game Studios pass through the static Spark Sprint example. It is written as a concrete usage transcript, not a runnable Godot log. The example intentionally validates without requiring Godot to be installed.

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
- examples/spark-sprint/src/gameplay/game_controller.gd
- examples/spark-sprint/tests/test_game_controller.gd

Next 3 actions:
1. $cgs-dev-story for the player loop story.
2. $cgs-smoke-check to verify static evidence and manual runtime gaps.
3. $cgs-story-done to decide whether the story can close.
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
- Read story, epic, core-loop GDD, architecture, control manifest, and source drafts.
- Compare acceptance criteria against GameController, PlayerController, Collectible, HUD, and test draft.
- Avoid writing changes unless coverage is missing.

Inspection result:
- Movement draft exists: examples/spark-sprint/src/gameplay/player_controller.gd
- Score, timer, win, timeout, and reset logic exists: examples/spark-sprint/src/gameplay/game_controller.gd
- Pickup draft exists: examples/spark-sprint/src/gameplay/collectible.gd
- HUD draft exists: examples/spark-sprint/src/ui/hud.gd
- Static tests cover score, win, timeout, and reset: examples/spark-sprint/tests/test_game_controller.gd

Files updated: none. The story is already represented by static source and test drafts.
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

Result:
- Example validation passed.

Automated coverage:
- Required project files exist.
- Walkthrough and docs mention the full workflow sequence.
- Source drafts include GameController, PlayerController, Collectible, and HUD tokens.
- Test draft includes score, win, timeout, and reset cases.

Manual checks remaining:
- Launch a future Godot scene.
- Confirm input bindings move the player.
- Confirm overlap wiring calls Collectible._on_body_entered().
- Confirm HUD labels are connected in a real scene.

Next skill: $cgs-story-done
```

## 5. Close The Story

User:

```text
Use $cgs-story-done examples/spark-sprint/production/epics/core-loop/STORY-001-player-loop.md.
```

Codex:

```text
Verdict: DONE for static example evidence.

Acceptance criteria:
- Player entity can move in four directions: covered by PlayerController draft; runtime input check remains manual.
- Collectible pickup increments score: covered by Collectible and GameController drafts.
- Timer reaches zero and ends the round: covered by GameController draft and test draft.
- Reset returns score, timer, and round state to initial values: covered by GameController draft and test draft.

Evidence:
- examples/spark-sprint/src/gameplay/player_controller.gd
- examples/spark-sprint/src/gameplay/collectible.gd
- examples/spark-sprint/src/gameplay/game_controller.gd
- examples/spark-sprint/src/ui/hud.gd
- examples/spark-sprint/tests/test_game_controller.gd
- examples/spark-sprint/tests/SMOKE-CHECKLIST.md

No story status edit was needed; the story already says Status: Review.
Next skill: $cgs-code-review
```

## 6. Review The Example Code

User:

```text
Use $cgs-code-review on the Spark Sprint source draft.
```

Codex:

```text
Findings:
- P2 examples/spark-sprint/project.godot: run/main_scene points to res://scenes/main.tscn, but the static example does not include scene files. Acceptable for repository validation; required before a runnable Godot demo.
- P2 examples/spark-sprint/src/gameplay/collectible.gd: pickup behavior depends on scene signal wiring that is not represented in static files. Add a scene or wiring note before runtime testing.

Open questions:
- Should v1 include a runnable Godot scene, or keep examples static-only?

Test gaps:
- No Godot runtime test was executed.
- No visual HUD connection check was executed.

Change summary:
- No source changes were made during review.
```

## 7. Create A QA Plan

User:

```text
Use $cgs-qa-plan for examples/spark-sprint/production/epics/core-loop/EPIC.md.
```

Codex:

```text
Scope:
- Core loop movement, pickup, score, timer, reset, HUD feedback, and story evidence.

Risk matrix:
- High: scene wiring for pickup and HUD labels once a real Godot scene exists.
- Medium: input bindings differ across keyboard layouts or controller support.
- Medium: timer edge cases around zero and repeated reset.
- Low: static source/test documentation drift.

Test matrix:
- Automated static: python tools\validate_examples.py.
- Source review: GameController, PlayerController, Collectible, and HUD drafts.
- Manual runtime: launch scene, move in four directions, collect 5 sparks, wait for timeout, reset.
- Evidence: command output, screenshots or short capture for runtime pass, updated smoke checklist.

Exit criteria:
- Static validator passes.
- Runtime playtest evidence is attached if the example becomes runnable.
- Any scene-wiring findings are either fixed or explicitly tracked.
```

## Final State

The v0.8 run demonstrates the full Spark Sprint loop:

```text
$cgs-start -> $cgs-project-stage-detect -> $cgs-dev-story -> $cgs-smoke-check -> $cgs-story-done -> $cgs-code-review -> $cgs-qa-plan
```

The transcript keeps Codex behavior read-first, evidence-based, and explicit about the boundary between static validation and future Godot runtime testing.
