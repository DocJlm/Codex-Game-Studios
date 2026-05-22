# Contribution Guide

Codex Game Studios is both a Codex plugin package and a game project template. Contributions should preserve both roles.

## Start Here

Before changing behavior, read:

- `AGENTS.md`
- `docs/v1-readiness/freeze-checklist.md`
- `docs/upstream-parity.md`
- `docs/install/upgrade.md`

Run the validator suite:

```bash
python3 tools/run_all_validators.py
```

On Windows:

```powershell
python tools\run_all_validators.py
```

## Stable Interfaces

Keep these stable unless the change is explicitly a breaking release:

- 73 skills under `plugins/codex-game-studios/skills/cgs-*/SKILL.md`
- 49 role cards under `plugins/codex-game-studios/references/role-cards/`
- 11 path rules under `plugins/codex-game-studios/references/rules/`
- Plugin manifest path `plugins/codex-game-studios/.codex-plugin/plugin.json`
- Marketplace path `.agents/plugins/marketplace.json`
- No runtime hooks in the plugin package

## Skill Changes

For skill edits:

- Keep frontmatter to exactly `name` and `description`.
- Keep skill names prefixed with `cgs-`.
- Mention the original slash command and the Codex skill name in the description.
- Read role cards from `plugins/codex-game-studios/references/role-cards/` instead of assuming automatic subagents.
- Add or update testing framework specs when workflow behavior changes.

## Documentation Changes

Update the nearest user-facing docs when behavior changes:

- First run and quick start: `docs/getting-started/`
- Plugin install and upgrade: `docs/install/`
- Windows, macOS, and CI: `docs/platforms/`
- Release history: `docs/releases/` and `CHANGELOG.md`
- Public contract: `docs/v1-readiness/freeze-checklist.md`

If a new doc path becomes required for users, add it to `tools/validate_user_docs.py`.

## Reporting Issues

Include:

- Operating system and shell.
- Codex app channel or build if visible.
- Whether `$cgs-help` works by name or only by path.
- Output from `python3 tools/run_all_validators.py` or `python tools\run_all_validators.py`.
- The exact prompt or workflow skill that failed.
- Relevant evidence paths from `design/`, `docs/`, `production/`, `src/`, `tests/`, or `plugins/`.

## Pull Request Checklist

- [ ] Scope is clear and tied to a user workflow.
- [ ] Public docs are updated when public behavior changes.
- [ ] Validators are added or updated for new contracts.
- [ ] `python3 tools/run_all_validators.py` passes locally.
- [ ] No unrelated generated churn is included.
