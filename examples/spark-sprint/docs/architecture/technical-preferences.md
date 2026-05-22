# Technical Preferences

Engine: Godot 4.3
Language: GDScript
Target platform: Desktop
Review mode: lean
Test command: use `python tools\validate_examples.py` for static validation and `python tools\validate_godot_example.py` for optional Godot scene loading.

## Source Layout

- `src/gameplay/`: gameplay state and actors
- `src/ui/`: HUD presentation
- `scenes/`: playable Godot scene
- `tests/`: GDScript-style test drafts
