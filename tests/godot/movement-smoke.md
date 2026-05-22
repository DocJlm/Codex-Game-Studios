# Movement Prototype Smoke

Version: moonlight-dispatch-v0.2.0
Story: `production/epics/mvp/STORY-001-player-movement.md`
Scene: `scenes/main.tscn`

## Automated Check

```bash
python3 tools/validate_moonlight_godot.py
```

Expected:

- `project.godot` points to `res://scenes/main.tscn`.
- `src/gameplay/player_controller.gd` exposes movement speed and route bounds.
- Godot 4.x loads the scene without runtime script errors.

## Manual Check

- Launch the scene in Godot.
- Move with WASD.
- Move with arrow keys.
- Move with gamepad left stick if available.
- Push against the outside route edge; courier stays inside the route.
- Push against the market blocker; courier is stopped or redirected by collision.

## Current Status

Automated validation passed on Godot 4.6.2 with headless scene load. Manual editor playtest should be captured before expanding the prototype into the delivery job flow.
