# Quick Start

This is the copy-paste path for a fresh Codex Game Studios clone. It covers Codex Desktop, the repo-local plugin, and the path-based fallback that works when local plugin discovery is unavailable.

## 1. Verify The Clone

Run the full validator from the repository root before starting a real project session.

Windows PowerShell:

```powershell
python tools\run_all_validators.py
```

macOS zsh or bash:

```bash
python3 tools/run_all_validators.py
```

Expected result:

```text
All validators passed
```

## 2. Try Codex Desktop Plugin Discovery

1. Open the cloned repository root in Codex Desktop.
2. Enable or install `codex-game-studios` if your build shows repo-local plugins from `.agents/plugins/marketplace.json`.
3. Try a small discovery prompt:

```text
Use $cgs-help and tell me the next Codex Game Studios step for this repository.
```

Good signs:

- `$cgs-*` names work without a file path.
- Codex reads project evidence before recommending writes.
- Role cards are treated as reference prompts, not automatic subagents.
- No runtime hooks are installed or invoked.

## 3. Use The Path-Based Fallback

If `$cgs-start` is not recognized by name, call the same skill by path:

```text
Use the skill at plugins/codex-game-studios/skills/cgs-start/SKILL.md to set up this project.
Use the skill at plugins/codex-game-studios/skills/cgs-project-stage-detect/SKILL.md to audit this project.
Use the skill at plugins/codex-game-studios/skills/cgs-dev-story/SKILL.md for production/epics/core-loop/STORY-001-player-loop.md.
```

This is still Codex Game Studios. It only bypasses local plugin discovery.

## 4. Pick The First Useful Workflow

New game:

```text
Use $cgs-start. I want to create a small game from scratch.
```

Existing game:

```text
Use $cgs-project-stage-detect and report the current phase, evidence paths, blockers, and next 3 actions.
```

Implementation story:

```text
Use $cgs-dev-story production/epics/core-loop/STORY-001-player-loop.md. Inspect first, then implement only the story scope.
```

Release confidence check:

```text
Use $cgs-smoke-check after the current change and report commands run, pass/fail results, and manual checks remaining.
```

## 5. Keep These Docs Nearby

- Codex Desktop setup: `docs/install/codex-desktop.md`
- Local plugin and fallback details: `docs/install/local-plugin.md`
- Upgrade guide: `docs/install/upgrade.md`
- Windows notes: `docs/platforms/windows.md`
- macOS notes: `docs/platforms/macos.md`
- CI notes: `docs/platforms/ci.md`
- Contribution guide: `docs/community/contributing.md`
