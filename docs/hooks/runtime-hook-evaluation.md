# Runtime Hook Evaluation

This document records the Codex Game Studios v0.5 decision on runtime hooks.

Checked sources on 2026-05-22:
- OpenAI Codex hooks docs: https://developers.openai.com/codex/hooks
- OpenAI Codex plugin build docs: https://developers.openai.com/codex/plugins/build
- Local Codex plugin manifest sample: `C:\Users\ZQC\.codex\skills\.system\plugin-creator\references\plugin-json-spec.md`

## Current Codex Hook Facts

- Codex supports hook config through `hooks.json` or inline `[hooks]` config.
- Installed plugins can bundle hook config through `.codex-plugin/plugin.json` or a default `hooks/hooks.json` file.
- Plugin hooks are off by default in the documented release.
- Users must set `[features].plugin_hooks = true` before enabled plugins can run bundled hooks.
- Hook paths must start with `./`, resolve relative to the plugin root, and stay inside the plugin root.
- Plugin hook commands receive `PLUGIN_ROOT` and `PLUGIN_DATA`.
- Supported hook events include `PreToolUse`, `PermissionRequest`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `SessionStart`, `SessionEnd`, and compaction/session events.
- Multiple matching command hooks for the same event can run concurrently.
- Non-managed command hooks require review and trust before they run.

## Decision

Codex Game Studios does not bundle runtime hooks in v0.5.

The plugin manifest must not declare `hooks`, and the plugin root must not contain `hooks/hooks.json`. Legacy upstream hook scripts remain preserved only as reference material under:

```text
plugins/codex-game-studios/scripts/checks/legacy-claude-hooks/
```

Safety behavior stays explicit through:

```powershell
python tools\validate_cgs.py
python tools\validate_skills.py
python tools\validate_smoke_fixture.py
python tools\validate_transcripts.py
python tools\validate_plugin_install_docs.py
python tools\validate_hook_policy.py
python tools\scan_legacy_tokens.py
```

## Rationale

Codex Game Studios is intended to be usable in a fresh clone without hidden local configuration. Because plugin hooks are disabled by default unless `[features].plugin_hooks = true`, shipping hook files now would create two different behavior modes:

- users with plugin hooks enabled would get extra runtime behavior;
- users without plugin hooks enabled would get only skills and explicit scripts.

That split is too easy to misunderstand for this template. The safer v0.5 behavior is to make all safety checks visible, repeatable, and CI-backed.

## Legacy Hook Mapping

| Legacy hook intent | v0.5 replacement |
| --- | --- |
| Pre-commit code quality | `python tools\validate_cgs.py` plus project-specific tests |
| Pre-push test gate | GitHub Actions `Validate` workflow plus manual project tests |
| Asset validation | Skill instructions and explicit project scripts when a real engine project exists |
| Session start or context loading | `AGENTS.md`, skills, and explicit references |
| Session cleanup | Release notes, changelog, and story done checks |

## Future Adoption Gate

Runtime hooks can be reconsidered when all of these are true:

1. Codex plugin hook support is stable enough to document without caveats for normal users.
2. A fresh clone can verify hook behavior without requiring hidden local user config.
3. Hook behavior is tested on Windows, macOS, and Linux.
4. Hook commands use `PLUGIN_ROOT` and `PLUGIN_DATA` only, not absolute developer-machine paths.
5. Hook failures produce clear user-facing messages and do not block unrelated workflows.
6. CI validates hook schema, hook command paths, and explicit non-hook fallback scripts.

Until then, `tools/validate_hook_policy.py` enforces the no-runtime-hooks policy.
