# Story: Player Movement

Status: Review
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

## Implementation Notes

- Added root Godot 4.6 project file at `project.godot`.
- Added main graybox scene at `scenes/main.tscn`.
- Added player movement controller at `src/gameplay/player_controller.gd`.
- Added scene bootstrap script at `src/gameplay/main_scene.gd`.

## Evidence

- `python3 tools/validate_moonlight_godot.py` passed with Godot 4.6.2 headless scene load.
- `python3 tools/run_all_validators.py` passed before tagging v0.2.0.
