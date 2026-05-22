# Story: Player Movement

Status: Ready
Owner role: gameplay-programmer

## Context

Create the courier's top-down movement foundation for the graybox prototype.

## Acceptance Criteria

- Player moves in four directions with keyboard.
- Player movement supports analog gamepad input.
- Player cannot leave the test route bounds.
- Movement speed is tunable from one constant or exported property.

## Test Plan

- Manual smoke: move up, down, left, right in the prototype scene.
- Manual smoke: confirm player stops at route blockers.
- Future automated check: scene contains player controller script and movement speed configuration.
