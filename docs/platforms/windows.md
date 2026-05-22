# Windows Usage

Codex Game Studios supports Windows as a first-class local development platform.

## Requirements

- Python 3.11 or newer on `PATH`.
- Git for cloning and status checks.
- Codex desktop or another Codex environment opened at the cloned repository root.
- Godot, Unity, or Unreal are optional. The included validators do not require a game engine.

## Validate The Repository

From PowerShell in the repository root:

```powershell
python tools\run_all_validators.py
```

For release-maintainer checks that regenerate curated docs and metadata:

```powershell
python tools\migrate_from_claude.py
python tools\prepare_v01.py
python tools\run_all_validators.py
```

## Use The Plugin

Preferred path:

```text
Use $cgs-start to set up a new game project.
Use $cgs-project-stage-detect on this existing game.
Use $cgs-dev-story to implement the next story.
```

Fallback path when repo-local plugin discovery is unavailable:

```text
Use the skill at plugins/codex-game-studios/skills/cgs-start/SKILL.md to set up this project.
Use the skill at plugins/codex-game-studios/skills/cgs-project-stage-detect/SKILL.md to audit this project.
Use the skill at plugins/codex-game-studios/skills/cgs-dev-story/SKILL.md for production/epics/core-loop/STORY-001-player-loop.md.
```

## Notes

- If PowerShell renders Chinese text incorrectly, the Markdown files are still UTF-8. View them in Codex, VS Code, GitHub, or another UTF-8-aware editor.
- Use the cloned repository root as the workspace. Do not depend on a machine-specific absolute path.
- Backslash examples are for PowerShell. Forward-slash paths in prompts also work because Codex reads repository files, not shell paths.
- If Godot 4.x is installed, `python tools\validate_godot_example.py` attempts to load `examples/spark-sprint/scenes/main.tscn`; otherwise it reports `SKIP`.
