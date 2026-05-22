# First Run Guide

This guide is the shortest path from a fresh clone to a useful Codex Game Studios session on Windows or macOS.

## 1. Open The Repository

Clone the repository and open the cloned root in Codex.

Windows PowerShell validation:

```powershell
python tools\run_all_validators.py
```

macOS zsh or bash validation:

```bash
python3 tools/run_all_validators.py
```

## 2. Try The Plugin Name

If repo-local plugin discovery is available in your Codex build, start with:

```text
Use $cgs-start to set up a new game project.
Use $cgs-project-stage-detect on this existing game.
Use $cgs-dev-story to implement the next story.
```

## 3. Use The Fallback Path

If `$cgs-start` is not recognized as an installed skill, use the same workflow by path:

```text
Use the skill at plugins/codex-game-studios/skills/cgs-start/SKILL.md to set up this project.
Use the skill at plugins/codex-game-studios/skills/cgs-project-stage-detect/SKILL.md to audit this project.
Use the skill at plugins/codex-game-studios/skills/cgs-dev-story/SKILL.md for production/epics/core-loop/STORY-001-player-loop.md.
```

## 4. Pick A Starting Scenario

New game:

```text
Use $cgs-start. I want to create a small game from scratch.
```

Existing project:

```text
Use $cgs-project-stage-detect and tell me the current phase, evidence paths, and next 3 actions.
```

Story implementation:

```text
Use $cgs-dev-story production/epics/core-loop/STORY-001-player-loop.md. Inspect first, then implement only the story scope.
```

## 5. Platform References

- Windows: `docs/platforms/windows.md`
- macOS: `docs/platforms/macos.md`
- Plugin install and fallback behavior: `docs/install/local-plugin.md`
