# Local Plugin Install UX

This guide describes how to use Codex Game Studios as a repo-local Codex plugin, and what to do when the current Codex build does not expose local plugin installation in the UI.

## Files Codex Should Discover

The repo-local marketplace entry is:

```text
.agents/plugins/marketplace.json
```

It points to the plugin root:

```text
./plugins/codex-game-studios
```

The plugin manifest is:

```text
plugins/codex-game-studios/.codex-plugin/plugin.json
```

The skill root declared by the manifest is:

```text
plugins/codex-game-studios/skills/
```

## Preferred Path

1. Open the repository root in Codex.
2. Use the Codex plugin or marketplace UI if your build exposes repo-local plugin installation.
3. Install or enable `codex-game-studios`.
4. Start with one of the default prompts:

```text
Use $cgs-start to set up a new game project.
Use $cgs-project-stage-detect on this existing game.
Use $cgs-dev-story to implement the next story.
```

## Verification Prompts

After enabling the plugin, verify discovery with small prompts:

```text
Use $cgs-help and tell me the next Codex Game Studios step for this repository.
Use $cgs-project-stage-detect and report only the detected stage plus evidence paths.
```

Good signs:
- Codex recognizes `$cgs-*` names without a path.
- The answer references `plugins/codex-game-studios/references/studio-docs/workflow-catalog.yaml` only when needed.
- The answer treats role cards as reference prompts, not automatic subagents.
- The answer does not try to install runtime hooks.

## Fallback Path

If local plugin installation is not visible or the skill name does not trigger, call the skill by path:

```text
Use the skill at plugins/codex-game-studios/skills/cgs-start/SKILL.md to set up this project.
Use the skill at plugins/codex-game-studios/skills/cgs-project-stage-detect/SKILL.md to audit this project.
Use the skill at plugins/codex-game-studios/skills/cgs-dev-story/SKILL.md for production/epics/core-loop/STORY-001-player-loop.md.
```

This is the same workflow content. It only bypasses plugin discovery.

## Local Validation

Run these checks before reporting an install or discovery problem:

```powershell
python tools\validate_cgs.py
python tools\validate_skills.py
python tools\validate_smoke_fixture.py
python tools\validate_transcripts.py
python tools\validate_plugin_install_docs.py
python tools\scan_legacy_tokens.py
python -m json.tool plugins\codex-game-studios\.codex-plugin\plugin.json
python -m json.tool .agents\plugins\marketplace.json
```

The important install fields are:

```json
{
  "name": "codex-game-studios",
  "skills": "./skills/"
}
```

and:

```json
{
  "name": "codex-game-studios",
  "source": {
    "source": "local",
    "path": "./plugins/codex-game-studios"
  }
}
```

## Troubleshooting

| Symptom | Check | Fix |
| --- | --- | --- |
| Plugin does not appear | Opened folder is not repo root | Open `D:\Git\Codex-Game-Studios` or the cloned repo root |
| Plugin appears but skills do not trigger | Manifest `skills` path is wrong | Run `python tools\validate_cgs.py` |
| Marketplace entry fails to parse | Invalid JSON | Run `python -m json.tool .agents\plugins\marketplace.json` |
| Skill trigger is unreliable | Local plugin UI is unavailable or stale | Use the path-based fallback prompts |
| Hook behavior is missing | Runtime hooks are intentionally not wired | Run explicit validation scripts instead |

## Hook Boundary

Legacy hook scripts are preserved for reference under `plugins/codex-game-studios/scripts/checks/legacy-claude-hooks/`, but Codex Game Studios does not declare plugin runtime hooks yet. Until the Codex hook schema is stable, safety checks stay explicit through scripts and skill instructions.
