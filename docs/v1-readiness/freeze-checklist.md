# v1 Readiness Freeze Checklist

This checklist defines the Codex Game Studios v1.x compatibility boundary. It is a release gate, not a roadmap wish list, and v1.6 adds user-facing install, upgrade, CI, and community documentation checks.

## Frozen Public Interfaces

- Skill names stay stable: 73 skills under `plugins/codex-game-studios/skills/cgs-*/SKILL.md`.
- Canonical skill prefix stays `cgs-`.
- Plugin manifest stays at `plugins/codex-game-studios/.codex-plugin/plugin.json`.
- Plugin manifest keeps `name: codex-game-studios` and `skills: ./skills/`.
- Repo-local marketplace entry stays `.agents/plugins/marketplace.json`.
- Marketplace entry continues to point at `./plugins/codex-game-studios`.
- Role cards stay reference prompts under `plugins/codex-game-studios/references/role-cards/`.
- Role cards are not automatic subagents unless the user explicitly asks for parallel agent work.
- Runtime hooks remain disabled by default and are not declared in the plugin package.
- Safety behavior remains explicit through scripts under `tools/`.

## Required Counts

- Skills: 73
- Role cards: 49
- Path rules: 11
- Static example project: `examples/spark-sprint/`
- Smoke fixture: `tests/fixtures/empty-game/`
- Windows, macOS, and CI platform docs: `docs/platforms/windows.md`, `docs/platforms/macos.md`, `docs/platforms/ci.md`
- Codex Desktop, fallback, and upgrade docs: `docs/install/codex-desktop.md`, `docs/install/local-plugin.md`, `docs/install/upgrade.md`
- Community contribution guide: `docs/community/contributing.md`

## Documentation Audit

Before a v1.x release, check these user-facing surfaces:

- `README.md`: quick start, fallback path, validation commands, examples, release list.
- `AGENTS.md`: operating contract, validation checklist, role-card policy.
- `docs/CODEX-MIGRATION-GUIDE.md`: migration direction and naming policy.
- `docs/install/local-plugin.md`: discovery files and fallback prompts.
- `docs/install/codex-desktop.md`: Codex Desktop setup, discovery, and fallback behavior.
- `docs/install/upgrade.md`: update, tag checkout, and release maintainer steps.
- `docs/install/field-test-2026-05-22.md`: current local plugin discovery field note.
- `docs/hooks/runtime-hook-evaluation.md`: no-runtime-hooks decision and future adoption gate.
- `docs/transcripts/concept-to-story.md`: concept-to-story demonstration.
- `docs/transcripts/spark-sprint-codex-run.md`: realistic Spark Sprint Codex run.
- `docs/transcripts/empty-game-smoke-run.md`: no-write smoke fixture run through `$cgs-gate-check`.
- `docs/examples/spark-sprint.md`: example prompt sequence.
- `docs/getting-started/first-run.md`: Windows and macOS first-run guide.
- `docs/getting-started/quick-start.md`: copy-paste Codex Desktop and fallback start path.
- `docs/platforms/windows.md`: Windows setup and troubleshooting.
- `docs/platforms/macos.md`: macOS setup and troubleshooting.
- `docs/platforms/ci.md`: GitHub Actions matrix and local CI reproduction.
- `docs/community/contributing.md`: contribution and issue-reporting expectations.
- `docs/releases/`: release notes from `v0.1.0` through the current release.
- `tests/fixtures/empty-game/production/gates/production-readiness.md`: stable gate-check fixture with expected `BLOCKED` verdict.

## Validation Gate

Run from the repository root:

Windows PowerShell:

```powershell
python tools\run_all_validators.py
```

macOS zsh or bash:

```bash
python3 tools/run_all_validators.py
python tools/run_all_validators.py
```

Release maintainers can also run the expanded sequence:

```text
python tools\migrate_from_claude.py
python tools\prepare_v01.py
python tools\validate_cgs.py
python tools\validate_skills.py
python tools\validate_smoke_fixture.py
python tools\validate_transcripts.py
python tools\validate_plugin_install_docs.py
python tools\validate_hook_policy.py
python tools\validate_examples.py
python tools\validate_godot_example.py
python tools\validate_upstream_parity.py
python tools\validate_codex_native_skills.py
python tools\validate_testing_framework_paths.py
python tools\validate_user_docs.py
python tools\validate_workflow_polish.py
python tools\validate_v1_readiness.py
python tools\validate_cross_platform.py
python tools\scan_legacy_tokens.py
python -m json.tool plugins\codex-game-studios\.codex-plugin\plugin.json
python -m json.tool .agents\plugins\marketplace.json
```

GitHub Actions must run the same structural validators on Windows, macOS, and Linux, including `tools/validate_v1_readiness.py`, `tools/validate_cross_platform.py`, and `tools/validate_user_docs.py`.

## Fresh Clone Gate

Before publishing a v1.x release:

1. Clone `https://github.com/DocJlm/Codex-Game-Studios.git` into a temporary directory.
2. Run `python tools\run_all_validators.py` on Windows or `python3 tools/run_all_validators.py` on macOS.
3. Confirm `git status --short --branch` is clean and tracking `origin/main`.
4. Confirm the latest tag and GitHub Release point to the same commit.

## Compatibility Policy

- Patch and minor releases may add docs, examples, validators, role cards, templates, or new skills.
- Patch and minor releases must not rename or remove existing `cgs-*` skills.
- Breaking changes to skill names, manifest shape, marketplace path, or runtime hook policy require a new major version.
- Runtime hooks can only be introduced after `docs/hooks/runtime-hook-evaluation.md` is updated and a hook validator is added.
- If plugin discovery behavior changes, update `docs/install/local-plugin.md` and add a new dated field note instead of overwriting the old observation.

## v1.x Release Decision

Any v1.x release is ready when:

- The validation gate passes locally.
- The validation gate passes in GitHub Actions.
- The fresh clone gate passes.
- Open GitHub issues for `v1-readiness` are closed or explicitly deferred.
- README, install docs, platform docs, community docs, migration guide, release notes, validators, manifest, marketplace entry, and examples agree on the same public interfaces.
