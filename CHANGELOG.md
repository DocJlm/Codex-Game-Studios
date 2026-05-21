# Changelog

All notable changes to Codex Game Studios are tracked here.

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
