# Story: Player Loop Skeleton

Status: Review
Owner role: gameplay-programmer

## Context

Implement the smallest Spark Sprint loop: movement, spark pickup, timer, win/timeout state, and reset.

## Acceptance Criteria

- Player entity can move in four directions.
- Collectible pickup increments score.
- Timer reaches zero and ends the round.
- Reset returns score, timer, and round state to initial values.

## Implementation Notes

- Gameplay state lives in `src/gameplay/game_controller.gd`.
- Movement draft lives in `src/gameplay/player_controller.gd`.
- Pickup draft lives in `src/gameplay/collectible.gd`.
- HUD draft lives in `src/ui/hud.gd`.

## Test Plan

- Review `tests/test_game_controller.gd` for score, win, timeout, and reset coverage.
- Run static repository validation from the root with `python tools\validate_examples.py`.
- Manual runtime smoke test is intentionally documented but not required for CI.

## Evidence

- Source draft: `src/gameplay/game_controller.gd`
- Test draft: `tests/test_game_controller.gd`
- Smoke checklist: `tests/SMOKE-CHECKLIST.md`
