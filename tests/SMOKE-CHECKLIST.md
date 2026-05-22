# Moonlight Dispatch Smoke Checklist

## Documentation Smoke

- `design/gdd/game-concept.md` communicates the paid hook in one paragraph.
- `design/gdd/core-loop.md` defines the delivery loop and fail states.
- `docs/architecture/technical-preferences.md` pins Godot 4.6 and GDScript.
- `production/milestones/8-week-roadmap.md` covers all eight weeks.
- `docs/store/steam-itch-page.md` has short description, features, tags, and price.

## Future Runtime Smoke

Once the Godot project exists, every playable build must check:

- New game starts.
- Player accepts a delivery.
- Player reaches destination.
- Timer can fail a delivery.
- Light exposure can fail a delivery.
- At least one tool changes route outcome.
- Pause/settings open and close.
- Save/load preserves progress.
