# Technical Preferences

Engine: Godot 4.6
Language: GDScript
Target platforms: Windows, macOS
Primary input: Keyboard and gamepad
Review mode: lean, with full review for phase gates

## Project Shape

- `project.godot`: root Godot project file.
- `scenes/`: Godot scene files.
- `src/core/`: app state, save data, settings, localization helpers.
- `src/gameplay/`: movement, jobs, hazards, tools, scoring.
- `src/ui/`: HUD, menu, settings, debrief.
- `assets/data/`: JSON or `.tres` data for jobs, districts, tools, localization keys.
- `assets/art/`: concept, production, and store art.
- `tests/`: static validators, smoke checklists, and future Godot test drafts.

## Godot Guidelines

- Prefer small scene scripts with explicit exported references.
- Keep job definitions data-driven.
- Avoid hardcoding delivery data inside scene scripts.
- Use constants or config resources for balance values.
- Keep UI display separate from gameplay state ownership.
- Validate data files with Python validators where possible.

## Test Commands

```bash
python3 tools/run_all_validators.py
python3 tools/validate_moonlight_dispatch.py
python3 tools/validate_moonlight_godot.py
```

Godot runtime checks load `scenes/main.tscn` when Godot 4.x is available.

## Performance Budget

- Target: 60 FPS on typical indie PC hardware.
- Render style: 2D, low overdraw, limited dynamic lighting.
- Scene size: one compact town map split into districts or loaded subscenes.
- Memory: keep launch build lightweight; no large uncompressed concept assets in runtime exports.
