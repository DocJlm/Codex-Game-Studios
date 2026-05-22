# Codex Game Studios

[![Validate](https://github.com/DocJlm/Codex-Game-Studios/actions/workflows/validate.yml/badge.svg)](https://github.com/DocJlm/Codex-Game-Studios/actions/workflows/validate.yml)

把一个 Codex 工作区变成结构化的游戏开发工作室：73 个 `cgs-*` skills、49 个工作室角色卡、阶段门、规则、设计模板、引擎参考和校验脚本。

This is a Codex-adapted version of [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios). It keeps the studio workflow idea, but packages it as a repo-local Codex plugin plus a game project template.

## What's Included

| Area | Count | Codex location |
| --- | ---: | --- |
| Skills | 73 | `plugins/codex-game-studios/skills/cgs-*/SKILL.md` |
| Role cards | 49 | `plugins/codex-game-studios/references/role-cards/` |
| Path rules | 11 | `plugins/codex-game-studios/references/rules/` |
| Templates | 40+ | `plugins/codex-game-studios/assets/templates/` |
| Engine references | Godot / Unity / Unreal | `plugins/codex-game-studios/references/engine-reference/` |
| Validation scripts | 11 | `tools/migrate_from_claude.py`, `tools/prepare_v01.py`, `tools/validate_cgs.py`, `tools/validate_skills.py`, `tools/validate_smoke_fixture.py`, `tools/validate_transcripts.py`, `tools/validate_plugin_install_docs.py`, `tools/validate_hook_policy.py`, `tools/validate_examples.py`, `tools/validate_workflow_polish.py`, `tools/scan_legacy_tokens.py` |

## Quick Start

1. Open this repository in Codex.
2. Install or enable the repo-local plugin from `.agents/plugins/marketplace.json` if your Codex build exposes local plugin installation.
3. Ask Codex to use one of the starter workflows:

```text
Use $cgs-start to set up a new game project.
Use $cgs-project-stage-detect on this existing game.
Use $cgs-dev-story to implement the next story.
```

中文提示也可以直接写：

```text
使用 $cgs-start 帮我从零开始建立游戏项目流程。
使用 $cgs-project-stage-detect 检查这个已有游戏项目现在处于哪个阶段。
使用 $cgs-dev-story 按下一个 story 实现功能。
```

### Fallback When Local Plugin Install Is Unavailable

Some Codex desktop builds do not expose repo-local plugin installation in the UI yet. In that case, keep this repository open and explicitly reference the skill path in your request:

```text
Use the skill at plugins/codex-game-studios/skills/cgs-start/SKILL.md to set up this project.
Use the skill at plugins/codex-game-studios/skills/cgs-project-stage-detect/SKILL.md to audit this project.
```

这不是另一套流程，只是本地插件无法直接安装时的调用方式；skill 内容和验证脚本仍然相同。

## Command Mapping

原 Claude slash command 统一迁移为 Codex skill，并加上 `cgs-` 前缀：

| Claude command | Codex skill |
| --- | --- |
| `/start` | `$cgs-start` |
| `/help` | `$cgs-help` |
| `/project-stage-detect` | `$cgs-project-stage-detect` |
| `/setup-engine` | `$cgs-setup-engine` |
| `/design-system` | `$cgs-design-system` |
| `/create-architecture` | `$cgs-create-architecture` |
| `/create-epics` | `$cgs-create-epics` |
| `/create-stories` | `$cgs-create-stories` |
| `/dev-story` | `$cgs-dev-story` |
| `/story-readiness` | `$cgs-story-readiness` |
| `/story-done` | `$cgs-story-done` |
| `/gate-check` | `$cgs-gate-check` |

完整映射见 `plugins/codex-game-studios/references/migration/skill-map.md`。

## Project Template

仓库根目录同时是一个游戏项目模板，保留这些稳定工作区：

```text
assets/       design/       docs/        production/
prototypes/   src/          tests/       tools/
```

`AGENTS.md` 是 Codex 的根级工作契约；插件内的 role cards 只作为参考角色，不会自动变成可调用 subagent。团队类技能默认按角色顺序做串行评审；只有用户明确要求并行代理工作时，Codex 才应尝试 subagent delegation。

## Validation

运行结构校验：

```powershell
python tools\validate_cgs.py
python tools\validate_skills.py
python tools\validate_smoke_fixture.py
python tools\validate_transcripts.py
python tools\validate_plugin_install_docs.py
python tools\validate_hook_policy.py
python tools\validate_examples.py
python tools\validate_workflow_polish.py
python tools\scan_legacy_tokens.py
```

从本地上游副本重新同步：

```powershell
python tools\migrate_from_claude.py
python tools\prepare_v01.py
python tools\validate_cgs.py
python tools\validate_skills.py
python tools\validate_smoke_fixture.py
python tools\validate_transcripts.py
python tools\validate_plugin_install_docs.py
python tools\validate_hook_policy.py
python tools\validate_examples.py
python tools\validate_workflow_polish.py
python tools\scan_legacy_tokens.py
```

The migration script expects the upstream checkout at `D:\Git\Claude-Code-Game-Studios`.

## Smoke Fixture

`tests/fixtures/empty-game/` is a tiny project used to exercise the v0.3 workflow loop:

- `$cgs-start`
- `$cgs-project-stage-detect`
- `$cgs-dev-story`
- `$cgs-story-done`

It is intentionally small and does not contain a real game implementation. See `tests/fixtures/empty-game/WALKTHROUGH.md` for expected output shape.

For a fuller concept-to-story demonstration, see `docs/transcripts/concept-to-story.md`.

## Examples

`examples/spark-sprint/` is a static Godot 4.3 / GDScript-style example project for the full workflow loop. It includes design docs, architecture, an epic, a story, source drafts, test drafts, and a walkthrough. It is validated without requiring Godot to be installed.

See `docs/examples/spark-sprint.md` for the prompt sequence.

## Plugin Install UX

Local plugin installation depends on the Codex build you are using. The supported discovery files and fallback prompts are documented in `docs/install/local-plugin.md`.

## Hook Policy

Claude hooks are not installed as Codex runtime hooks. Legacy hook scripts are preserved under `plugins/codex-game-studios/scripts/checks/legacy-claude-hooks/` for reference only. Safety behavior is handled by explicit validation scripts and skill instructions. See `docs/hooks/runtime-hook-evaluation.md` for the current decision and future adoption gate.

## License

MIT. See `LICENSE` and `NOTICE`.

## Releases

- `v0.7.0`: second-batch production workflow polish. See `docs/releases/v0.7.0.md`.
- `v0.6.0`: static Spark Sprint example project and example validation. See `docs/releases/v0.6.0.md`.
- `v0.5.0`: runtime hook evaluation and no-hook policy validation. See `docs/releases/v0.5.0.md`.
- `v0.4.0`: local plugin install UX and fallback documentation. See `docs/releases/v0.4.0.md`.
- `v0.3.0`: demo transcript and high-frequency workflow polish. See `docs/releases/v0.3.0.md`.
- `v0.2.0`: self-contained validation, repeatable regeneration, and workflow polish. See `docs/releases/v0.2.0.md`.
- `v0.1.0`: initial public release. See `docs/releases/v0.1.0.md`.
