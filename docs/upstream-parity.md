# Upstream Parity Report

Checked on 2026-05-22 against `https://github.com/Donchitos/Claude-Code-Game-Studios` at commit `984023ddac0d5e27624f2baacde6105e45de375f`. The final v2.0.0 parity pass rechecked upstream HEAD on 2026-05-22 and found the same commit.

This report tracks capability parity, not byte-for-byte runtime parity. Codex Game Studios keeps the studio workflow, roles, templates, rules, examples, and checks, but adapts invocation and safety behavior to Codex-native skills and explicit validators. The runtime policy remains `no-runtime-hooks`.

Codex Game Studios is a Codex-native complete port for the checked upstream commit. No unexplained parity gaps remain.

## Surface Matrix

| Upstream surface | Upstream count | Codex-native surface | Local count | Status |
| --- | ---: | --- | ---: | --- |
| `.claude/skills/<name>/SKILL.md` | 73 | `plugins/codex-game-studios/skills/cgs-<name>/SKILL.md` | 73 | Complete, exact name set with `cgs-` prefix |
| `.claude/agents/*.md` | 49 | `plugins/codex-game-studios/references/role-cards/*.md` | 49 | Complete, exact role-card name set |
| `.claude/rules/*.md` | 11 | `plugins/codex-game-studios/references/rules/*.md` | 11 | Complete, exact filename set |
| `.claude/docs/templates/*.md` | 40 | `plugins/codex-game-studios/assets/templates/*.md` | 40 | Complete, exact relative path set |
| `.claude/hooks/*.sh` | 12 | Reference scripts plus explicit validators and skill instructions | 12 reference scripts | Complete as non-runtime parity |
| `.claude/docs/*.md` and `workflow-catalog.yaml` | 22 docs plus templates | `plugins/codex-game-studios/references/studio-docs/` | Mirrored reference set | Complete as reference material |
| Upstream skill testing framework | 126 Markdown specs/docs | `plugins/codex-game-studios/references/testing-framework/` | Mirrored reference set | Complete with repo-local paths |

## Template Count Evidence

The upstream README currently advertises 41 templates, but the checked upstream tree contains 40 Markdown files under `.claude/docs/templates/`. The Codex-native tree has the same 40 relative template paths under `plugins/codex-game-studios/assets/templates/`.

Codex Game Studios therefore documents the public template count as 40 for now. If upstream later adds a real 41st template file, the next parity pass should copy or adapt it and update the count.

## Hook Intent Mapping

Codex Game Studios intentionally does not install Claude runtime hooks. The 12 upstream hook scripts are preserved under `plugins/codex-game-studios/scripts/checks/legacy-claude-hooks/` for review, while safety behavior is handled through visible commands, CI, and skill instructions.

| Upstream hook | Codex-native replacement |
| --- | --- |
| `validate-commit.sh` | `python3 tools/run_all_validators.py`, `$cgs-code-review`, and project-specific tests before committing |
| `validate-push.sh` | GitHub Actions `Validate` workflow, release protocol checks, and explicit `git ls-remote` verification after push |
| `validate-assets.sh` | Path rules, asset-focused skills such as `$cgs-asset-spec` and `$cgs-asset-audit`, plus project-specific asset validators |
| `validate-skill-change.sh` | `tools/validate_skills.py`, `tools/validate_upstream_parity.py`, and `$cgs-skill-test` guidance |
| `detect-gaps.sh` | `$cgs-start`, `$cgs-project-stage-detect`, and smoke fixture validation |
| `session-start.sh` | `AGENTS.md`, `$cgs-help`, and explicit repo inspection at workflow start |
| `session-stop.sh` | `$cgs-story-done`, release notes, changelog, and visible git status checks |
| `pre-compact.sh` | `plugins/codex-game-studios/references/studio-docs/context-management.md` and explicit handoff notes |
| `post-compact.sh` | `AGENTS.md`, current git state, and workflow-specific skill entrypoints |
| `notify.sh` | Codex UI notifications or user-controlled desktop notifications outside the plugin package |
| `log-agent.sh` | Role-card review notes in the assistant response or project docs when a workflow asks for role reviews |
| `log-agent-stop.sh` | Same as `log-agent.sh`; no automatic subagent audit trail is assumed |

## Final Parity Gate

No unexplained parity gaps remain.

| Capability area | Codex-native parity surface | Validator |
| --- | --- | --- |
| Skills, role cards, rules, templates, and manifest | Repo-local plugin package under `plugins/codex-game-studios/` | `tools/validate_cgs.py`, `tools/validate_skills.py` |
| Upstream surface counts and hook names | This report plus preserved reference scripts | `tools/validate_upstream_parity.py` |
| Full-migration skill behavior | Codex Operating Notes and role-card review language | `tools/validate_codex_native_skills.py` |
| Testing framework paths | Repo-local testing framework specs and `AGENTS.md` instruction file | `tools/validate_testing_framework_paths.py` |
| User setup and platform paths | Codex Desktop, fallback, upgrade, CI, and community docs | `tools/validate_user_docs.py`, `tools/validate_cross_platform.py` |
| Examples and smoke evidence | Spark Sprint and empty-game gate-check transcripts | `tools/validate_examples.py`, `tools/validate_smoke_fixture.py`, `tools/validate_transcripts.py` |
| Complete-port claim | README, this parity report, v2 release notes, and plugin metadata | `tools/validate_complete_port.py` |

## Parity Roadmap

- v1.4.0 completed the first Codex-native operating pass for the remaining 50 full-migration skills.
- v1.5.0 completed testing framework path cleanup and added regression validation for repo-local spec paths.
- v1.6.0 completed user-facing Codex Desktop setup, upgrade, CI, quick-start, and contribution documentation with regression validation.
- v1.7.0 expanded examples and smoke fixtures across `$cgs-start`, `$cgs-dev-story`, `$cgs-story-done`, and `$cgs-gate-check`.
- v2.0.0 completed the final parity gate and verified the Codex-native complete-port claim.
