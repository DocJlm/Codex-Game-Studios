# Moonlight Dispatch Smoke Checklist

## Documentation Smoke

- `design/gdd/game-concept.md` communicates the paid hook in one paragraph.
- `design/gdd/core-loop.md` defines the delivery loop and fail states.
- `docs/architecture/technical-preferences.md` pins Godot 4.6 and GDScript.
- `production/milestones/8-week-roadmap.md` covers all eight weeks.
- `docs/store/steam-itch-page.md` has short description, features, tags, and price.

## Future Runtime Smoke

Every playable build must check:

- New game starts.
- Player moves with WASD or arrow keys.
- Player movement supports gamepad left stick.
- Player cannot leave the graybox route bounds.
- Player is stopped by the market blocker.
- Player accepts a delivery.
- Player reaches destination.
- Timer can fail a delivery.
- Light exposure can fail a delivery.
- At least one tool changes route outcome.
- Pause/settings open and close.
- Save/load preserves progress.

## v0.2.0 Movement Prototype Smoke

- Scene: `scenes/main.tscn`
- Command: `python3 tools/validate_moonlight_godot.py`
- Expected: Godot 4.x loads the scene without `SCRIPT ERROR:` or `ERROR:`.
- Manual follow-up: use keyboard and left stick to move the courier inside the route bounds.
