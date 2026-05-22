# Moonlight Dispatch v0.2.0

v0.2.0 starts the playable Godot prototype by closing `STORY-001-player-movement`.

## Changes

- Added root Godot 4.6 project file.
- Added `scenes/main.tscn` graybox route scene.
- Added `src/gameplay/player_controller.gd` with keyboard and gamepad movement support.
- Added route bounds and one market blocker.
- Added `tools/validate_moonlight_godot.py` and wired it into the full validator suite.
- Added `examples/.gdignore` so the root Godot project ignores nested example projects.
- Updated smoke checklist and story evidence.

## Validation

```bash
python3 tools/validate_moonlight_godot.py
python3 tools/run_all_validators.py
```

Result: both commands passed on macOS with Godot 4.6.2. The Moonlight scene loaded headlessly without `SCRIPT ERROR:` or `ERROR:`.

## Known Limits

- This version only proves movement and route bounds.
- Delivery job flow, timer, exposure, tools, and debrief remain future stories.
- Manual Godot editor playtest evidence should be captured before closing the full MVP epic.
