# Local Plugin Field Test 2026-05-22

This note captures user-visible repo-local plugin behavior observed while preparing Codex Game Studios v0.9. It is intentionally practical: if discovery is not available in a given Codex build, the path-based fallback remains the supported route.

## Environment

- Repository root: `D:\Git\Codex-Game-Studios`
- Plugin root: `plugins/codex-game-studios/`
- Marketplace entry: `.agents/plugins/marketplace.json`
- Plugin manifest: `plugins/codex-game-studios/.codex-plugin/plugin.json`
- Skill root: `plugins/codex-game-studios/skills/`
- Plugin version under test: `0.9.0`

## Structural Checks

These commands passed before the field note was recorded:

```powershell
python tools\validate_cgs.py
python tools\validate_skills.py
python tools\validate_plugin_install_docs.py
python -m json.tool plugins\codex-game-studios\.codex-plugin\plugin.json
python -m json.tool .agents\plugins\marketplace.json
```

The manifest and marketplace entry both point to repo-relative paths:

```json
{
  "name": "codex-game-studios",
  "skills": "./skills/"
}
```

```json
{
  "source": {
    "source": "local",
    "path": "./plugins/codex-game-studios"
  }
}
```

## Observed Current-Session Behavior

In the Codex desktop session used for this release, the active built-in skill list did not automatically show `cgs-*` skills before an explicit plugin enable or install step. That means a user may see the repository files and still not see `$cgs-start` as an installed skill trigger.

This is not treated as a plugin package failure when all structural validators pass. It means the current build or session is not exposing repo-local plugin discovery as an active runtime capability.

## Success Path

When a Codex build exposes repo-local plugin installation, the expected path is:

1. Open the cloned repository root.
2. Install or enable `codex-game-studios` from the repo-local marketplace entry.
3. Verify with a small prompt:

```text
Use $cgs-help and tell me the next Codex Game Studios step for this repository.
```

User-visible success signs:

- `$cgs-*` names work without a file path.
- The answer uses the Codex Game Studios workflow catalog when needed.
- Role cards are treated as references, not automatic subagents.
- No runtime hooks are installed or invoked.

## Fallback Path

When the plugin does not appear or skill triggers are not active, call the skill by path:

```text
Use the skill at plugins/codex-game-studios/skills/cgs-start/SKILL.md to set up this project.
Use the skill at plugins/codex-game-studios/skills/cgs-project-stage-detect/SKILL.md to audit this project.
Use the skill at plugins/codex-game-studios/skills/cgs-dev-story/SKILL.md for production/epics/core-loop/STORY-001-player-loop.md.
```

User-visible fallback signs:

- Codex can read the target `SKILL.md` directly.
- The workflow still uses `cgs-*` names internally.
- The response cites project evidence paths before proposing writes.
- The response does not require hidden local plugin state.

## Reporting Install Problems

Before filing an install or discovery issue, include:

- Codex build or app channel if visible.
- Whether the repo root was the opened workspace.
- Output from `python tools\validate_cgs.py`.
- Output from `python tools\validate_plugin_install_docs.py`.
- Whether `$cgs-help` worked by name or only by path.
- Any user-visible marketplace or plugin UI message.

## Release Decision

v0.9 keeps both paths documented. Repo-local plugin installation is the preferred user experience, but path-based skill invocation remains the compatibility path until local marketplace discovery is consistently visible in normal Codex builds.
