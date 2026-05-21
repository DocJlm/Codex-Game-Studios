# Concept-to-Story Transcript

This transcript shows the intended v0.3 Codex Game Studios feel: concise, project-aware, and bounded by explicit write confirmations. It uses a fictional small game called Spark Sprint.

## 1. Start A New Project

User:

```text
Use $cgs-start. I want a tiny arcade game prototype about collecting sparks before a timer ends.
```

Expected Codex shape:

```text
Detected state: fresh workspace with no production stage, concept, engine preferences, or epics.
Missing decisions: engine, target platform, review mode.
Suggested setup:
- production/stage.txt = concept
- production/review-mode.txt = lean
- design/gdd/game-concept.md starter draft
Before writing: confirm engine and review mode.
Next skill: $cgs-brainstorm or $cgs-setup-engine
```

User:

```text
Use Godot 4.3, desktop, lean review. Write the starter files.
```

Expected Codex shape:

```text
Files updated:
- production/stage.txt
- production/review-mode.txt
- design/gdd/game-concept.md
Next: $cgs-setup-engine to capture technical preferences.
```

## 2. Capture Engine Preferences

User:

```text
Use $cgs-setup-engine for Godot 4.3 and GDScript.
```

Expected Codex shape:

```text
Detected engine: no project.godot yet, user selected Godot 4.3.
Decisions captured:
- Language: GDScript
- Platform: desktop
- Test command placeholder: godot --headless --run-tests
File proposed: docs/architecture/technical-preferences.md
Next skill: $cgs-map-systems
```

## 3. Map Systems

User:

```text
Use $cgs-map-systems from the current game concept.
```

Expected Codex shape:

```text
MVP systems:
- Player movement
- Collectible spawning and pickup
- Timer and round state
- Score display
Dependency order:
1. Timer and score state
2. Player movement
3. Collectible pickup
4. HUD feedback
File proposed: design/gdd/systems-index.md
Next skill: $cgs-create-architecture
```

## 4. Create Architecture

User:

```text
Use $cgs-create-architecture. Keep it small.
```

Expected Codex shape:

```text
Architecture summary:
- GameController owns round state.
- PlayerController owns movement input.
- Collectible nodes emit pickup events.
- HUD observes score and timer.
Required ADRs: none for this tiny prototype.
File proposed: docs/architecture/architecture.md
Next skill: $cgs-create-epics
```

## 5. Create Epic And Story

User:

```text
Use $cgs-create-epics, then split the first epic with $cgs-create-stories.
```

Expected Codex shape:

```text
Epic: Core Loop
Goal: Build a playable timer-based collection loop.
Stories:
1. Player Loop Skeleton
2. HUD Feedback
3. Round Reset
First story path:
production/epics/core-loop/STORY-001-player-loop.md
Next skill: $cgs-story-readiness
```

## 6. Pick Up A Story

User:

```text
Use $cgs-dev-story production/epics/core-loop/STORY-001-player-loop.md. Implement it if ready.
```

Expected Codex shape before edits:

```text
Readiness: READY
Plan:
- Inspect existing Godot project files.
- Add or update player movement, score, timer, and reset logic.
- Add score/timer tests if the project test harness exists.
Files likely touched:
- src/gameplay/player_controller.gd
- src/gameplay/game_controller.gd
- tests/test_game_controller.gd
As requested, proceeding with implementation.
```

Expected Codex shape after edits:

```text
Changed files: listed with paths.
Tests run: command and result.
Acceptance criteria:
- Player moves: pass or manual check required
- Pickup increments score: pass
- Timer ends round: pass
- Reset restores timer and score: pass
Next skill: $cgs-story-done
```

## 7. Close The Story

User:

```text
Use $cgs-story-done production/epics/core-loop/STORY-001-player-loop.md.
```

Expected Codex shape:

```text
Verdict: DONE or NEEDS FIXES
Evidence:
- Diff paths reviewed
- Automated tests and manual smoke checks
- Acceptance criteria checklist
If complete: offer to update story status.
If incomplete: list blockers and route back to $cgs-dev-story or $cgs-smoke-check.
```

## 8. Review And QA Follow-Up

User:

```text
Use $cgs-code-review on the current diff, then $cgs-qa-plan for the Core Loop epic.
```

Expected Codex shape:

```text
$cgs-code-review:
- Findings first, ordered P0-P3.
- File and line references when possible.
- Test gaps and residual risk.

$cgs-qa-plan:
- Risk matrix.
- Automated and manual checks.
- Evidence artifacts.
- Exit criteria for the epic.
```
