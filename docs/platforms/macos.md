# macOS Usage

Codex Game Studios supports macOS through zsh or bash plus the same repo-local plugin and path fallback model.

## Requirements

- Python 3.11 or newer, usually available as `python3`.
- Git for cloning and status checks.
- Codex desktop or another Codex environment opened at the cloned repository root.
- Godot, Unity, or Unreal are optional. The included validators do not require a game engine.

## Validate The Repository

From zsh or bash in the repository root:

```bash
python3 tools/run_all_validators.py
```

If your Python command is named `python`, this is also fine:

```bash
python tools/run_all_validators.py
```

For release-maintainer checks that regenerate curated docs and metadata:

```bash
python3 tools/migrate_from_claude.py
python3 tools/prepare_v01.py
python3 tools/run_all_validators.py
```

The same validator entrypoint is used by GitHub Actions through `docs/platforms/ci.md`.

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

- Use forward-slash repository paths in shell commands and prompts.
- The repo-local marketplace entry is `.agents/plugins/marketplace.json`.
- If the Codex build does not expose repo-local plugin installation, use the path-based fallback prompts above.
- If Godot 4.x is installed, `python3 tools/validate_godot_example.py` attempts to load `examples/spark-sprint/scenes/main.tscn`; otherwise it reports `SKIP`.
- For Codex Desktop setup and fallback prompts, see `docs/install/codex-desktop.md`.
