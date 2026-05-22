# Codex Game Studios Agent Guide

This repository is both a Codex plugin package and a game project template.

## Operating Contract

- Use Codex-native skills from `plugins/codex-game-studios/skills/`.
- Treat upstream slash commands as aliases only: `/dev-story` means `$cgs-dev-story`, `/gate-check` means `$cgs-gate-check`, and so on.
- Read role cards from `plugins/codex-game-studios/references/role-cards/` when a workflow asks for a studio role.
- Do not assume role cards are automatically available subagents. Run role reviews sequentially unless the user explicitly requests parallel agent work.
- Do not wire legacy Claude hooks into Codex runtime behavior. Use the validators under `tools/` for repository and skill checks.

## Project Layout

- `plugins/codex-game-studios/`: Codex plugin package.
- `.agents/plugins/marketplace.json`: repo-local plugin marketplace entry.
- `design/`: game design, UX, art, narrative, accessibility docs.
- `docs/architecture/`: architecture documents, ADRs, control manifest.
- `production/`: epics, stories, sprints, bugs, playtests, release artifacts.
- `src/`: game source, organized by domain.
- `assets/`: game data, art, audio, shaders, generated asset manifests.
- `tests/`: unit, integration, regression, performance, and manual evidence.
- `prototypes/`: disposable prototypes and vertical slices.

## Validation Checklist

Before declaring a migration or structural change complete:

```powershell
python tools\validate_cgs.py
python tools\validate_skills.py
python tools\validate_smoke_fixture.py
python tools\validate_transcripts.py
python tools\validate_plugin_install_docs.py
python tools\validate_hook_policy.py
python tools\scan_legacy_tokens.py
```

For plugin and skill edits, verify:

- `plugin.json` is valid JSON.
- Every skill has only `name` and `description` frontmatter.
- Every skill name starts with `cgs-`.
- Skill descriptions mention both the original slash command and the Codex skill name.
- Counts remain at 73 skills, 49 role cards, and 11 path rules unless the change explicitly updates those numbers.
- Curated workflows remain concise and Codex-native: `cgs-start`, `cgs-help`, `cgs-project-stage-detect`, `cgs-brainstorm`, `cgs-setup-engine`, `cgs-map-systems`, `cgs-design-system`, `cgs-create-architecture`, `cgs-create-epics`, `cgs-create-stories`, `cgs-story-readiness`, `cgs-dev-story`, `cgs-story-done`, `cgs-gate-check`, `cgs-code-review`, `cgs-qa-plan`, `cgs-smoke-check`, `cgs-architecture-review`, and `cgs-ux-design`.
- `tests/fixtures/empty-game/` stays usable for smoke checks of onboarding, stage detection, story pickup, and story closure review.

## Collaboration Defaults

- Preserve the user's control over design and architecture decisions.
- Ask concise questions only when the decision cannot be discovered from the project and guessing would materially affect the result.
- Keep game-source edits scoped to the active story, GDD, ADR, or user request.
- Run project-specific tests when a change touches code, data schemas, or workflow validation.
