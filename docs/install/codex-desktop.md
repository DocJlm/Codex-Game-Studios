# Codex Desktop Setup

Use this guide when you want Codex Game Studios to behave like an installed Codex plugin inside Codex Desktop.

## Open The Right Workspace

Open the repository root, not a subfolder. Codex should be able to see these files:

```text
.agents/plugins/marketplace.json
plugins/codex-game-studios/.codex-plugin/plugin.json
plugins/codex-game-studios/skills/
AGENTS.md
```

Run a structural check if anything looks off:

```bash
python3 tools/run_all_validators.py
```

On Windows:

```powershell
python tools\run_all_validators.py
```

## Preferred Plugin Path

If your Codex Desktop build exposes repo-local plugin installation:

1. Open the plugin or marketplace UI.
2. Install or enable `codex-game-studios`.
3. Verify with:

```text
Use $cgs-help and tell me the next Codex Game Studios step for this repository.
```

Expected behavior:

- Codex recognizes `$cgs-help`, `$cgs-start`, and `$cgs-project-stage-detect`.
- The answer uses repository evidence before proposing changes.
- The answer does not try to wire runtime hooks.
- Role cards stay reference material unless the user explicitly requests parallel agent work.

## Path-Based Fallback

Some Codex Desktop builds or sessions do not expose repo-local plugin discovery. In that case, use the direct skill path:

```text
Use the skill at plugins/codex-game-studios/skills/cgs-start/SKILL.md to set up this project.
```

Useful fallback prompts:

```text
Use the skill at plugins/codex-game-studios/skills/cgs-project-stage-detect/SKILL.md to audit this project.
Use the skill at plugins/codex-game-studios/skills/cgs-dev-story/SKILL.md for production/epics/core-loop/STORY-001-player-loop.md.
Use the skill at plugins/codex-game-studios/skills/cgs-gate-check/SKILL.md to review phase readiness.
```

## When Discovery Seems Stale

Try these in order:

1. Confirm the repository root is the active Codex workspace.
2. Run `python3 tools/run_all_validators.py` or `python tools\run_all_validators.py`.
3. Check that `.agents/plugins/marketplace.json` points to `./plugins/codex-game-studios`.
4. Check that `plugins/codex-game-studios/.codex-plugin/plugin.json` has `"skills": "./skills/"`.
5. Restart the Codex Desktop session if the plugin UI appears stale.
6. Use the path-based fallback until repo-local discovery is visible.

## Boundary

Codex Game Studios does not depend on hidden local state. A fresh clone plus the validator suite is enough to verify the package. Runtime hooks are intentionally not installed; safety behavior stays visible through `tools/run_all_validators.py`, skill instructions, and GitHub Actions.
