# Changelog

All notable changes to Codex Game Studios are tracked here.

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
