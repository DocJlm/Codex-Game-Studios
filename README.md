# Codex Game Studios

[![Validate](https://github.com/DocJlm/Codex-Game-Studios/actions/workflows/validate.yml/badge.svg)](https://github.com/DocJlm/Codex-Game-Studios/actions/workflows/validate.yml)

把一个 Codex 工作区变成结构化的游戏开发工作室：73 个 `cgs-*` skills、49 个工作室角色卡、阶段门、规则、设计模板、引擎参考和校验脚本。Windows and macOS are both supported for clone, validation, documentation, and fallback skill usage.

This is a Codex-adapted version of [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios). It keeps the studio workflow idea, but packages it as a repo-local Codex plugin plus a game project template.

## What's Included

| Area | Count | Codex location |
| --- | ---: | --- |
| Skills | 73 | `plugins/codex-game-studios/skills/cgs-*/SKILL.md` |
| Role cards | 49 | `plugins/codex-game-studios/references/role-cards/` |
| Path rules | 11 | `plugins/codex-game-studios/references/rules/` |
| Templates | 40 | `plugins/codex-game-studios/assets/templates/` |
| Engine references | Godot / Unity / Unreal | `plugins/codex-game-studios/references/engine-reference/` |
| Validation scripts | 19 | `tools/run_all_validators.py`, `tools/validate_cross_platform.py`, `tools/validate_user_docs.py`, `tools/validate_godot_example.py`, plus the structural validators under `tools/` |

## Quick Start

For the copy-paste first session path, see `docs/getting-started/quick-start.md`.

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

## Windows And macOS

Use the same validator entrypoint on both platforms.

Windows PowerShell:

```powershell
python tools\run_all_validators.py
```

macOS zsh or bash:

```bash
python3 tools/run_all_validators.py
# If your Python command is named python:
python tools/run_all_validators.py
```

Platform notes:
- Windows: `docs/platforms/windows.md`
- macOS: `docs/platforms/macos.md`
- CI: `docs/platforms/ci.md`
- Quick start: `docs/getting-started/quick-start.md`
- First run guide: `docs/getting-started/first-run.md`

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
python tools\run_all_validators.py
```

macOS:

```bash
python3 tools/run_all_validators.py
```

从本地上游副本重新同步：

```powershell
python tools\migrate_from_claude.py
python tools\prepare_v01.py
python tools\run_all_validators.py
```

macOS release-maintainer equivalent:

```bash
python3 tools/migrate_from_claude.py
python3 tools/prepare_v01.py
python3 tools/run_all_validators.py
```

The migration script uses the upstream checkout configured in `tools/migrate_from_claude.py`; keep that path local to your machine.

## Smoke Fixture

`tests/fixtures/empty-game/` is a tiny project used to exercise the v0.3 workflow loop:

- `$cgs-start`
- `$cgs-project-stage-detect`
- `$cgs-dev-story`
- `$cgs-story-done`

It is intentionally small and does not contain a real game implementation. See `tests/fixtures/empty-game/WALKTHROUGH.md` for expected output shape.

For a fuller concept-to-story demonstration, see `docs/transcripts/concept-to-story.md`.
For a realistic Spark Sprint Codex pass, see `docs/transcripts/spark-sprint-codex-run.md`.

## Examples

`examples/spark-sprint/` is an optional runnable Godot 4.3 / GDScript-style example project for the full workflow loop. It includes design docs, architecture, an epic, a story, source drafts, a playable scene, test drafts, and a walkthrough. It is validated without requiring Godot to be installed; if Godot is available, `python tools/validate_godot_example.py` attempts to load `scenes/main.tscn`.

See `docs/examples/spark-sprint.md` for the prompt sequence.

## Plugin Install UX

Local plugin installation depends on the Codex build you are using. The supported Codex Desktop path is documented in `docs/install/codex-desktop.md`; discovery files and fallback prompts are documented in `docs/install/local-plugin.md`; upgrade steps are documented in `docs/install/upgrade.md`. The current dated field note is `docs/install/field-test-2026-05-22.md`.

## Community

Contribution and issue-reporting expectations are documented in `docs/community/contributing.md`.

## v1 Readiness

The frozen public interfaces and release gates are documented in `docs/v1-readiness/freeze-checklist.md`. CI runs `tools\validate_v1_readiness.py` to keep the checklist aligned with README, AGENTS, plugin metadata, and marketplace config.

## Hook Policy

Claude hooks are not installed as Codex runtime hooks. Legacy hook scripts are preserved under `plugins/codex-game-studios/scripts/checks/legacy-claude-hooks/` for reference only. Safety behavior is handled by explicit validation scripts and skill instructions. See `docs/hooks/runtime-hook-evaluation.md` for the current decision and future adoption gate.

## Upstream Parity

The current upstream parity snapshot is documented in `docs/upstream-parity.md`. It records the checked upstream commit, surface counts, template-count evidence, and the Codex-native replacement for each upstream hook intent.

## License

MIT. See `LICENSE` and `NOTICE`.

## Releases

- `v1.6.0`: Codex Desktop, upgrade, CI, quick-start, and contribution docs with user-doc validation. See `docs/releases/v1.6.0.md`.
- `v1.5.0`: repo-local testing framework path cleanup and validator. See `docs/releases/v1.5.0.md`.
- `v1.4.0`: Codex-native migration pass for the remaining full-migration skills. See `docs/releases/v1.4.0.md`.
- `v1.3.0`: upstream parity report and validator. See `docs/releases/v1.3.0.md`.
- `v1.2.1`: Godot runtime validation hardening for Spark Sprint. See `docs/releases/v1.2.1.md`.
- `v1.2.0`: optional runnable Spark Sprint Godot example. See `docs/releases/v1.2.0.md`.
- `v1.1.0`: Windows and macOS cross-platform validation and usage docs. See `docs/releases/v1.1.0.md`.
- `v1.0.0`: v1 readiness freeze checklist and compatibility gate. See `docs/releases/v1.0.0.md`.
- `v0.9.0`: local plugin discovery field test notes. See `docs/releases/v0.9.0.md`.
- `v0.8.0`: realistic Spark Sprint Codex run transcript. See `docs/releases/v0.8.0.md`.
- `v0.7.0`: second-batch production workflow polish. See `docs/releases/v0.7.0.md`.
- `v0.6.0`: static Spark Sprint example project and example validation. See `docs/releases/v0.6.0.md`.
- `v0.5.0`: runtime hook evaluation and no-hook policy validation. See `docs/releases/v0.5.0.md`.
- `v0.4.0`: local plugin install UX and fallback documentation. See `docs/releases/v0.4.0.md`.
- `v0.3.0`: demo transcript and high-frequency workflow polish. See `docs/releases/v0.3.0.md`.
- `v0.2.0`: self-contained validation, repeatable regeneration, and workflow polish. See `docs/releases/v0.2.0.md`.
- `v0.1.0`: initial public release. See `docs/releases/v0.1.0.md`.
