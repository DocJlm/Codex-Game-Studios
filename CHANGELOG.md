# Changelog

All notable changes to Codex Game Studios are tracked here.

## v1.4.0 - 2026-05-22

- Converted the remaining 50 full-migration skills to Codex-native operating notes.
- Replaced Claude-specific subagent and Task-tool assumptions with role-card review language that matches `AGENTS.md`.
- Added `tools/validate_codex_native_skills.py` and wired it into `tools/run_all_validators.py`.
- Bumped plugin metadata to `1.4.0`.

## v1.3.0 - 2026-05-22

- Added `docs/upstream-parity.md` with a checked upstream commit, surface-count matrix, template-count evidence, and hook-intent mapping.
- Added `tools/validate_upstream_parity.py` and wired it into `tools/run_all_validators.py`.
- Clarified README template count as the 40 Markdown templates present in both the upstream tree and the Codex-native template assets.
- Bumped plugin metadata to `1.3.0`.

## v1.2.1 - 2026-05-22

- Fixed the runnable Spark Sprint Godot scene load by avoiding typed node references that are unavailable without `class_name` registration.
- Hardened `tools/validate_godot_example.py` so Godot runtime `SCRIPT ERROR:` or `ERROR:` output fails validation even when Godot exits with code 0.
- Bumped plugin metadata to `1.2.1`.

## v1.2.0 - 2026-05-22

- Upgraded `examples/spark-sprint/` from a static fixture to an optional runnable Godot 4.x example.
- Added `scenes/main.tscn` and `src/gameplay/main_scene.gd` to demonstrate movement, spark pickup, HUD updates, timer, win, timeout, and reset.
- Added `tools/validate_godot_example.py`, which statically checks the scene and optionally loads it when Godot is installed.
- Added Godot example validation to `tools/run_all_validators.py`.
- Bumped regenerated plugin metadata to `1.2.0`.

## v1.1.0 - 2026-05-22

- Added `tools/run_all_validators.py` as the single cross-platform validation entrypoint.
- Added `tools/validate_cross_platform.py` for Windows and macOS documentation and CI checks.
- Updated GitHub Actions to validate on Windows, macOS, and Linux.
- Added platform docs and a first-run guide for Windows and macOS users.
- Bumped regenerated plugin metadata to `1.1.0`.

## v1.0.0 - 2026-05-22

- Added `docs/v1-readiness/freeze-checklist.md` to define frozen public interfaces, validation gates, fresh clone requirements, and compatibility policy.
- Added `tools/validate_v1_readiness.py` and wired it into GitHub Actions.
- Updated README and AGENTS validation checklists for the v1 readiness gate.
- Bumped regenerated plugin metadata to `1.0.0`.

## v0.9.0 - 2026-05-22

- Added `docs/install/field-test-2026-05-22.md` with current local plugin discovery behavior, success signs, fallback signs, and reporting guidance.
- Linked the field note from README and `docs/install/local-plugin.md`.
- Extended plugin install documentation validation to cover the field note.
- Bumped regenerated plugin metadata to `0.9.0`.

## v0.8.0 - 2026-05-22

- Added `docs/transcripts/spark-sprint-codex-run.md`, a realistic Codex pass through the Spark Sprint example.
- Linked the transcript from `docs/examples/spark-sprint.md` and the README.
- Extended transcript and example validation so the v0.8 transcript is CI-covered.
- Bumped regenerated plugin metadata to `0.8.0`.

## v0.7.0 - 2026-05-22

- Polished second-batch production workflows: `$cgs-story-readiness`, `$cgs-scope-check`, `$cgs-test-evidence-review`, `$cgs-regression-suite`, and `$cgs-release-checklist`.
- Added `docs/workflows/production-readiness-workflows.md` with expected output contracts.
- Added `tools/validate_workflow_polish.py` and wired it into CI.
- Bumped regenerated plugin metadata to `0.7.0`.

## v0.6.0 - 2026-05-22

- Added the static `examples/spark-sprint/` Godot 4.3 / GDScript-style example project.
- Added `docs/examples/spark-sprint.md` with the example workflow prompt sequence.
- Added `tools/validate_examples.py` and wired it into CI.
- Extended legacy-token scanning to examples and example docs.
- Bumped regenerated plugin metadata to `0.6.0`.

## v0.5.0 - 2026-05-22

- Added runtime hook evaluation documentation in `docs/hooks/runtime-hook-evaluation.md`.
- Documented the v0.5 decision not to bundle plugin runtime hooks.
- Added `tools/validate_hook_policy.py` and wired it into CI.
- Extended legacy-token scanning to hook policy documentation.
- Bumped regenerated plugin metadata to `0.5.0`.

## v0.4.0 - 2026-05-22

- Added local plugin install UX documentation in `docs/install/local-plugin.md`.
- Documented preferred local plugin discovery, verification prompts, and path-based fallback prompts.
- Added `tools/validate_plugin_install_docs.py` and wired it into CI.
- Extended legacy-token scanning to install documentation.
- Bumped regenerated plugin metadata to `0.4.0`.

## v0.3.0 - 2026-05-22

- Added a concept-to-story transcript showing the intended Codex Game Studios demo flow from `$cgs-start` through `$cgs-story-done`.
- Added high-frequency workflow notes for `$cgs-code-review`, `$cgs-qa-plan`, and `$cgs-smoke-check`.
- Tightened `$cgs-code-review` severity rules and review output expectations.
- Tightened `$cgs-qa-plan` evidence rules and scoped test-matrix expectations.
- Tightened `$cgs-smoke-check` smoke scope and failure reporting.
- Added transcript validation to local checks and CI.

## v0.2.0 - 2026-05-22

- Fixed repeatable migration drift by writing the real `DocJlm/Codex-Game-Studios` metadata from `tools/migrate_from_claude.py`.
- Added repo-local skill validation in `tools/validate_skills.py` and wired it into GitHub Actions.
- Expanded the empty-game smoke fixture with a walkthrough for `$cgs-start`, `$cgs-project-stage-detect`, `$cgs-dev-story`, and `$cgs-story-done`.
- Refined five high-priority workflows into shorter Codex-native skills: `$cgs-code-review`, `$cgs-qa-plan`, `$cgs-smoke-check`, `$cgs-architecture-review`, and `$cgs-ux-design`.
- Added v0.2 release notes and updated validation instructions.

## v0.1.0 - 2026-05-21

- Published the initial Codex adaptation with 73 skills, 49 role cards, 11 rules, templates, engine references, and validation scripts.
- Added the repo-local plugin manifest and marketplace entry.
- Added the first smoke fixture and starter release notes.
