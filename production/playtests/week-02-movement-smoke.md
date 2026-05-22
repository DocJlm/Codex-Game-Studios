# Week 02 Movement Smoke Notes

## Scope

Validate the first Godot movement prototype for Moonlight Dispatch.

## Evidence Targets

- `project.godot`
- `scenes/main.tscn`
- `src/gameplay/player_controller.gd`
- `tools/validate_moonlight_godot.py`

## Result Template

```text
Verdict: PASS / PASS WITH CONCERNS / FAIL
Keyboard movement:
Gamepad movement:
Route bounds:
Market blocker:
Runtime errors:
Notes:
```

## Current Automated Result

```text
Verdict: PASS
Keyboard movement: Static and runtime script path validated; manual input check remains a follow-up.
Gamepad movement: Left stick axis handling is present in `src/gameplay/player_controller.gd`; manual hardware check remains a follow-up.
Route bounds: Route boundary bodies and clamp limits are present in `scenes/main.tscn`.
Market blocker: `RouteBounds/MarketBlocker` collision body is present.
Runtime errors: None from Godot 4.6.2 headless scene load.
Notes: `python3 tools/validate_moonlight_godot.py` passed.
```

```bash
python3 tools/validate_moonlight_godot.py
```

## Computer Use Observation

Godot 4.6.2 launched to the local project manager. The reliable v0.2.0 runtime evidence is the headless scene load, because the editor UI did not expose a usable imported-project window during this smoke pass.
