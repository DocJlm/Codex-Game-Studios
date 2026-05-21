# Available Skills (Slash Commands)

73 slash commands organized by phase. Type `/` in Codex to access any of them.

## Onboarding & Navigation

| Command | Purpose |
|---------|---------|
| `$cgs-start` | First-time onboarding — asks where you are, then guides you to the right workflow |
| `$cgs-help` | Context-aware "what do I do next?" — reads current stage and surfaces the required next step |
| `$cgs-project-stage-detect` | Full project audit — detect phase, identify existence gaps, recommend next steps |
| `$cgs-setup-engine` | Configure engine + version, detect knowledge gaps, populate version-aware reference docs |
| `$cgs-adopt` | Brownfield format audit — checks internal structure of existing GDDs/ADRs/stories, produces migration plan |

## Game Design

| Command | Purpose |
|---------|---------|
| `$cgs-brainstorm` | Guided ideation using professional studio methods (MDA, SDT, Bartle, verb-first) |
| `$cgs-map-systems` | Decompose game concept into systems, map dependencies, prioritize design order |
| `$cgs-design-system` | Guided, section-by-section GDD authoring for a single game system |
| `$cgs-quick-design` | Lightweight design spec for small changes — tuning, tweaks, minor additions |
| `$cgs-review-all-gdds` | Cross-GDD consistency and game design holism review across all design docs |
| `$cgs-propagate-design-change` | When a GDD is revised, find affected ADRs and produce an impact report |

## Art & Assets

| Command | Purpose |
|---------|---------|
| `$cgs-art-bible` | Guided, section-by-section Art Bible authoring — creates visual identity spec before asset production begins |
| `$cgs-asset-spec` | Generate per-asset visual specifications and AI generation prompts from GDDs, level docs, or character profiles |
| `$cgs-asset-audit` | Audit assets for naming conventions, file size budgets, and pipeline compliance |

## UX & Interface Design

| Command | Purpose |
|---------|---------|
| `$cgs-ux-design` | Guided section-by-section UX spec authoring (screen/flow, HUD, or pattern library) |
| `$cgs-ux-review` | Validate UX specs for GDD alignment, accessibility, and pattern compliance |

## Architecture

| Command | Purpose |
|---------|---------|
| `$cgs-create-architecture` | Guided authoring of the master architecture document |
| `$cgs-architecture-decision` | Create an Architecture Decision Record (ADR) |
| `$cgs-architecture-review` | Validate all ADRs for completeness, dependency ordering, and GDD coverage |
| `$cgs-create-control-manifest` | Generate flat programmer rules sheet from accepted ADRs |

## Stories & Sprints

| Command | Purpose |
|---------|---------|
| `$cgs-create-epics` | Translate GDDs + ADRs into epics — one per architectural module |
| `$cgs-create-stories` | Break a single epic into implementable story files |
| `$cgs-dev-story` | Read a story and implement it — routes to the correct programmer agent |
| `$cgs-sprint-plan` | Generate or update a sprint plan; initializes sprint-status.yaml |
| `$cgs-sprint-status` | Fast 30-line sprint snapshot (reads sprint-status.yaml) |
| `$cgs-story-readiness` | Validate a story is implementation-ready before pickup (READY/NEEDS WORK/BLOCKED) |
| `$cgs-story-done` | 8-phase completion review after implementation; updates story file, surfaces next story |
| `$cgs-estimate` | Structured effort estimate with complexity, dependencies, and risk breakdown |

## Reviews & Analysis

| Command | Purpose |
|---------|---------|
| `$cgs-design-review` | Review a game design document for completeness and consistency |
| `$cgs-code-review` | Architectural code review for a file or changeset |
| `$cgs-balance-check` | Analyze game balance data, formulas, and config — flag outliers |
| `$cgs-content-audit` | Audit GDD-specified content counts against implemented content |
| `$cgs-scope-check` | Analyze feature or sprint scope against original plan, flag scope creep |
| `$cgs-perf-profile` | Structured performance profiling with bottleneck identification |
| `$cgs-tech-debt` | Scan, track, prioritize, and report on technical debt |
| `$cgs-gate-check` | Validate readiness to advance between development phases (PASS/CONCERNS/FAIL) |
| `$cgs-consistency-check` | Scan all GDDs against the entity registry to detect cross-document inconsistencies (stats, names, rules that contradict each other) |
| `$cgs-security-audit` | Audit the game for security vulnerabilities: save tampering, cheat vectors, network exploits, data exposure, and input validation gaps |

## QA & Testing

| Command | Purpose |
|---------|---------|
| `$cgs-qa-plan` | Generate a QA test plan for a sprint or feature |
| `$cgs-smoke-check` | Run critical path smoke test gate before QA hand-off |
| `$cgs-soak-test` | Generate a soak test protocol for extended play sessions |
| `$cgs-regression-suite` | Map test coverage to GDD critical paths, identify fixed bugs without regression tests |
| `$cgs-test-setup` | Scaffold the test framework and CI/CD pipeline for the project's engine |
| `$cgs-test-helpers` | Generate engine-specific test helper libraries for the test suite |
| `$cgs-test-evidence-review` | Quality review of test files and manual evidence documents |
| `$cgs-test-flakiness` | Detect non-deterministic (flaky) tests from CI run logs |
| `$cgs-skill-test` | Validate skill files for structural compliance and behavioral correctness |
| `$cgs-skill-improve` | Improve a skill using a test-fix-retest loop — diagnose, propose fix, rewrite, verify |

## Production

| Command | Purpose |
|---------|---------|
| `$cgs-milestone-review` | Review milestone progress and generate status report |
| `$cgs-retrospective` | Run a structured sprint or milestone retrospective |
| `$cgs-bug-report` | Create a structured bug report |
| `$cgs-bug-triage` | Read all open bugs, re-evaluate priority vs. severity, assign owner and label |
| `$cgs-reverse-document` | Generate design or architecture docs from existing implementation |
| `$cgs-playtest-report` | Generate a structured playtest report or analyze existing playtest notes |

## Release

| Command | Purpose |
|---------|---------|
| `$cgs-release-checklist` | Generate and validate a pre-release checklist for the current build |
| `$cgs-launch-checklist` | Complete launch readiness validation across all departments |
| `$cgs-changelog` | Auto-generate changelog from git commits and sprint data |
| `$cgs-patch-notes` | Generate player-facing patch notes from git history and internal data |
| `$cgs-hotfix` | Emergency fix workflow with audit trail, bypassing normal sprint process |
| `$cgs-day-one-patch` | Prepare a focused day-one patch for known issues discovered after gold master but before or at public launch |

## Creative & Content

| Command | Purpose |
|---------|---------|
| `$cgs-prototype` | Concept prototype — throwaway build right after brainstorm to validate core idea (Phase 1) |
| `$cgs-vertical-slice` | Pre-Production validation — production-quality end-to-end build before committing to Production (Phase 4) |
| `$cgs-onboard` | Generate contextual onboarding document for a new contributor or agent |
| `$cgs-localize` | Localization workflow: string extraction, validation, translation readiness |

## Team Orchestration

Coordinate multiple agents on a single feature area:

| Command | Coordinates |
|---------|-------------|
| `$cgs-team-combat` | game-designer + gameplay-programmer + ai-programmer + technical-artist + sound-designer + qa-tester |
| `$cgs-team-narrative` | narrative-director + writer + world-builder + level-designer |
| `$cgs-team-ui` | ux-designer + ui-programmer + art-director + accessibility-specialist |
| `$cgs-team-release` | release-manager + qa-lead + devops-engineer + producer |
| `$cgs-team-polish` | performance-analyst + technical-artist + sound-designer + qa-tester |
| `$cgs-team-audio` | audio-director + sound-designer + technical-artist + gameplay-programmer |
| `$cgs-team-level` | level-designer + narrative-director + world-builder + art-director + systems-designer + qa-tester |
| `$cgs-team-live-ops` | live-ops-designer + economy-designer + community-manager + analytics-engineer |
| `$cgs-team-qa` | qa-lead + qa-tester + gameplay-programmer + producer |
