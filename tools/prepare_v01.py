#!/usr/bin/env python3
"""Prepare curated Codex-native workflows for the current release."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "codex-game-studios"
SKILLS = PLUGIN / "skills"
FIXTURE = ROOT / "tests" / "fixtures" / "empty-game"
EXAMPLE = ROOT / "examples" / "spark-sprint"
RELEASE_VERSION = "1.2.0"


CORE_SKILLS: dict[str, tuple[str, str]] = {
    "start": (
        "First-run onboarding for a new or unorganized game project.",
        """# CGS Start

Use `$cgs-start` when the user wants to begin using Codex Game Studios in a new or lightly organized game project.

## Procedure

1. Inspect first: check `AGENTS.md`, `production/stage.txt`, `production/review-mode.txt`, `design/gdd/game-concept.md`, `docs/architecture/`, `production/epics/`, and source files under `src/`.
2. Summarize the discovered state in 5 lines or fewer.
3. Ask only the missing product choices: concept maturity, preferred engine, and review mode (`solo`, `lean`, or `full`).
4. Create or update only the minimum setup files after the user confirms the draft:
   - `production/stage.txt`
   - `production/review-mode.txt`
   - missing project folders
   - optional starter concept stub when the user asks for one
5. End with the next concrete skill, usually `$cgs-brainstorm`, `$cgs-setup-engine`, or `$cgs-project-stage-detect`.

## Output Contract

Return: detected state, decisions captured, files to create or update, and next skill.
""",
    ),
    "help": (
        "Context-aware next-step navigator for Codex Game Studios projects.",
        """# CGS Help

Use `$cgs-help` when the user asks what to do next in the Codex Game Studios pipeline.

## Procedure

1. Read `plugins/codex-game-studios/references/studio-docs/workflow-catalog.yaml`.
2. Inspect project artifacts for each phase: concept, systems design, technical setup, pre-production, production, polish, release.
3. Identify the current phase by the first missing required artifact.
4. Recommend one next required action and up to two optional actions.
5. If the state is contradictory, route to `$cgs-project-stage-detect`.

## Output Contract

Return: current phase, completed signals, blockers, recommended next skill, and why it is next.
""",
    ),
    "project-stage-detect": (
        "Audit an existing game project and classify its Codex Game Studios stage.",
        """# CGS Project Stage Detect

Use `$cgs-project-stage-detect` for brownfield projects or when project state is unclear.

## Procedure

1. Inspect folders and files without changing them.
2. Detect engine and language from source, manifests, and project files.
3. Count design docs, architecture docs, epics, stories, sprint files, tests, prototypes, and release artifacts.
4. Compare findings with `workflow-catalog.yaml`.
5. Produce a stage report and a migration path.

## Output Contract

Return verdict: `FRESH`, `CONCEPT`, `SYSTEMS DESIGN`, `TECHNICAL SETUP`, `PRE-PRODUCTION`, `PRODUCTION`, `POLISH`, `RELEASE`, or `INCONSISTENT`.
Include evidence paths and the next 3 actions.
""",
    ),
    "brainstorm": (
        "Guided ideation for turning a theme or blank slate into a game concept.",
        """# CGS Brainstorm

Use `$cgs-brainstorm` when the user needs a game idea, pitch, pillars, or concept direction.

## Procedure

1. Capture the seed: blank slate, theme, genre, mechanic, audience, platform, and constraints.
2. Generate 3 distinct concept options using MDA, player motivation, and verb-first design.
3. Ask the user to choose or combine options.
4. Expand the selected direction into pitch, core loop, pillars, fantasy, risks, and MVP scope.
5. Offer to write `design/gdd/game-concept.md` from the approved draft.

## Output Contract

Return concept options first, then a selected concept draft only after user choice.
""",
    ),
    "setup-engine": (
        "Configure engine, version, language, and technical preferences.",
        """# CGS Setup Engine

Use `$cgs-setup-engine` when engine configuration is missing or outdated.

## Procedure

1. Detect existing engine files before asking: Godot, Unity, Unreal, or custom.
2. If no engine is discoverable, ask for engine, version, language, target platforms, and input method.
3. Read matching references under `plugins/codex-game-studios/references/engine-reference/`.
4. Draft technical preferences: engine version, language, source layout, naming, test command, performance budget, and specialist role cards.
5. Write approved preferences to `docs/architecture/technical-preferences.md`.

## Output Contract

Return detected engine, decisions, files updated, and the next recommended architecture or design skill.
""",
    ),
    "map-systems": (
        "Break an approved game concept into systems and dependency order.",
        """# CGS Map Systems

Use `$cgs-map-systems` after a concept exists and before writing per-system GDDs.

## Procedure

1. Read `design/gdd/game-concept.md` and any existing GDDs.
2. Identify player-facing systems, support systems, content systems, and platform systems.
3. Classify each system as MVP, stretch, or later.
4. Map dependencies and recommended design order.
5. Offer to write `design/gdd/systems-index.md`.

## Output Contract

Return system list, dependency graph in text form, MVP boundary, and next `$cgs-design-system` targets.
""",
    ),
    "design-system": (
        "Create or revise a focused game design document for one system.",
        """# CGS Design System

Use `$cgs-design-system` to author a GDD for a single system from the systems index.

## Procedure

1. Select exactly one system.
2. Read concept, systems index, art bible, UX docs, and related GDDs.
3. Ask for missing design intent before drafting mechanics.
4. Draft sections: purpose, player verbs, rules, formulas, states, content, UX hooks, edge cases, tuning values, acceptance criteria.
5. Offer to write `design/gdd/<system-slug>.md` after approval.

## Output Contract

Return a complete system GDD draft and call out unresolved decisions explicitly.
""",
    ),
    "create-architecture": (
        "Create the master architecture plan from approved design docs.",
        """# CGS Create Architecture

Use `$cgs-create-architecture` after core GDDs exist and before implementation stories.

## Procedure

1. Read GDDs, technical preferences, engine references, and existing source.
2. Identify modules, data ownership, runtime flow, persistence, UI boundary, testing strategy, and engine-specific constraints.
3. List required ADRs for decisions that should not live only in prose.
4. Draft `docs/architecture/architecture.md`.
5. Offer to write the draft and recommend `$cgs-architecture-decision` for each required ADR.

## Output Contract

Return architecture summary, module map, required ADR list, and known risks.
""",
    ),
    "create-epics": (
        "Translate approved design and architecture into production epics.",
        """# CGS Create Epics

Use `$cgs-create-epics` when GDDs and architecture are ready for production planning.

## Procedure

1. Read GDDs, architecture, accepted ADRs, and control manifest.
2. Group work into epics by coherent deliverable, not by file type.
3. For each epic, define goal, included systems, out-of-scope items, dependencies, acceptance criteria, and test evidence.
4. Offer to create `production/epics/<epic-slug>/EPIC.md`.

## Output Contract

Return proposed epic list first; write files only after approval.
""",
    ),
    "create-stories": (
        "Break one epic into implementable production stories.",
        """# CGS Create Stories

Use `$cgs-create-stories` to split an approved epic into small implementation stories.

## Procedure

1. Read one `production/epics/<epic>/EPIC.md`.
2. Check dependencies, GDD links, ADR links, and test expectations.
3. Create stories sized for 1-3 days of focused work.
4. Each story must include context, implementation notes, acceptance criteria, test plan, owner role, and done checklist.
5. Offer to write story files under the epic folder.

## Output Contract

Return story sequence, dependency order, and first recommended `$cgs-dev-story` target.
""",
    ),
    "story-readiness": (
        "Check whether a story is ready before implementation begins.",
        """# CGS Story Readiness

Use `$cgs-story-readiness` before `$cgs-dev-story` or when a story feels ambiguous.

## Procedure

1. Read exactly one target story plus its epic, linked GDDs, ADRs, control manifest, and available test notes.
2. Check implementation scope, acceptance criteria, dependencies, required assets, data readiness, testability, and unresolved decisions.
3. Inspect relevant source only to confirm existing context; do not edit implementation files.
4. Identify the smallest unblocker: one question, one upstream doc fix, or one dependency to finish.
5. If ready, name the first `$cgs-dev-story` implementation focus and the tests that should prove it.

## Readiness Rules

- `READY`: scope is bounded, criteria are testable, dependencies are available, and the next implementation step is clear.
- `NEEDS WORK`: story can be fixed locally by clarifying criteria, narrowing scope, or adding missing test notes.
- `BLOCKED`: implementation depends on missing design, architecture, asset, engine, or product decisions.

## Output Contract

Return verdict: `READY`, `NEEDS WORK`, or `BLOCKED`.
Include evidence paths, blockers, smallest next action, and recommended next skill.
""",
    ),
    "dev-story": (
        "Implement one ready story using Codex-native engineering workflow.",
        """# CGS Dev Story

Use `$cgs-dev-story` to implement exactly one ready production story.

## Procedure

1. Read the story, epic, linked GDDs, ADRs, control manifest, path rules, and relevant role cards.
2. Inspect existing code before proposing changes.
3. Produce a short implementation plan with files to touch and tests to run.
4. Implement only the story scope after the user confirms the plan or has clearly asked for execution.
5. Run targeted tests and update story status or notes only when requested or when the story workflow requires it.

## Output Contract

Return changed files, tests run, acceptance criteria status, and next `$cgs-story-done` command.
""",
    ),
    "story-done": (
        "Verify and close a completed implementation story.",
        """# CGS Story Done

Use `$cgs-story-done` after implementation to decide whether a story can close.

## Procedure

1. Read the story, diff, tests, linked GDDs, ADRs, and acceptance criteria.
2. Verify behavior, test evidence, documentation drift, design drift, and known risks.
3. If incomplete, return blockers and do not mark done.
4. If complete, offer to update the story status and summarize follow-up work.

## Output Contract

Return verdict: `DONE`, `NEEDS FIXES`, or `BLOCKED`.
Include acceptance criteria checklist and tests.
""",
    ),
    "gate-check": (
        "Run an advisory phase gate before advancing the game project.",
        """# CGS Gate Check

Use `$cgs-gate-check` before moving between major phases.

## Procedure

1. Identify current and target phase from workflow catalog and project artifacts.
2. Read `production/review-mode.txt`; default to `lean` if missing.
3. Check required artifacts, unresolved risks, tests, design coverage, architecture coverage, and production readiness.
4. In `full` mode, apply creative-director, technical-director, producer, and qa-lead role-card perspectives sequentially.
5. Never hard-block the user; provide an advisory verdict.

## Output Contract

Return verdict: `PASS`, `PASS WITH CONCERNS`, or `FAIL`.
Include required fixes, optional fixes, and user decision options.
""",
    ),
    "code-review": (
        "Review game code changes for correctness, scope, tests, and story alignment.",
        """# CGS Code Review

Use `$cgs-code-review` when the user asks for a review of game code, a story diff, or a pull-request-style check.

## Procedure

1. Inspect the requested diff or changed files before summarizing; use `git diff`, PR files, or explicit paths.
2. Read the active story, linked GDDs, ADRs, path rules, and test notes when they exist.
3. Prioritize findings that can break gameplay, saves, builds, performance budgets, platform constraints, or acceptance criteria.
4. Keep role-card use sequential: technical director, lead programmer, qa lead, then producer only when scope drift is possible.
5. Do not rewrite code during review unless the user explicitly asks for fixes.

## Severity Rules

- `P0`: corrupts data, prevents launch, blocks shipping, or makes the game unplayable.
- `P1`: breaks story acceptance criteria, core loop behavior, tests, or important platform behavior.
- `P2`: creates maintainability, UX, performance, or coverage risk that should be fixed soon.
- `P3`: polish or follow-up note.

## Output Contract

Lead with findings ordered by severity. Include file paths and line numbers when possible.
Then list open questions, test gaps, and a short change summary.
If no issues are found, say that clearly and still report residual risk.
""",
    ),
    "qa-plan": (
        "Create a focused QA plan for a story, milestone, prototype, or release candidate.",
        """# CGS QA Plan

Use `$cgs-qa-plan` when the user needs test coverage for a gameplay story, milestone, prototype, or release candidate.

## Procedure

1. Read the story, epic, GDDs, architecture notes, known bugs, and target platforms.
2. Identify risk areas: core loop, input, save/load, UI feedback, performance, accessibility, localization, and platform differences.
3. Split checks into automated tests, manual smoke tests, exploratory passes, device or platform checks, and evidence to capture.
4. Keep the plan small enough to run for the requested scope; name what is intentionally out of scope.
5. Offer to write or update `tests/SMOKE-CHECKLIST.md`, story-local QA notes, or a release candidate checklist after approval.

## Evidence Rules

- Each acceptance criterion needs at least one verification path.
- Manual checks must name the scene, input path, expected result, and evidence artifact.
- Automated checks must name the command and the behavior they cover.

## Output Contract

Return scope, risk matrix, test matrix, evidence requirements, owner handoff, and exit criteria.
""",
    ),
    "smoke-check": (
        "Run or design a fast smoke check for core game workflows.",
        """# CGS Smoke Check

Use `$cgs-smoke-check` when the user wants a fast confidence pass after changes.

## Procedure

1. Identify the smallest playable or verifiable path for the current story or milestone.
2. Prefer existing commands in `AGENTS.md`, package manifests, engine project files, or test docs.
3. Run safe automated checks when available, then list manual checks that still require the user, editor, or game runtime.
4. Capture failures with exact commands, paths, expected result, actual result, and reproduction steps.
5. Avoid broad regression testing unless the user asks for a full QA pass.

## Smoke Scope

Cover only launch, the touched gameplay loop, one success path, one failure or timeout path, and the acceptance criteria changed by the story.
Route broader coverage to `$cgs-qa-plan`.

## Output Contract

Return commands run, pass/fail results, manual checks remaining, and the next fix or verification step.
""",
    ),
    "architecture-review": (
        "Review architecture against design goals, engine constraints, and production stories.",
        """# CGS Architecture Review

Use `$cgs-architecture-review` when architecture, module boundaries, ADRs, or technical direction need review.

## Procedure

1. Read `docs/architecture/architecture.md`, ADRs, technical preferences, control manifest, GDDs, and relevant source.
2. Check module ownership, data flow, persistence, scene or entity boundaries, UI separation, testability, and engine constraints.
3. Compare the architecture to active epics and stories; flag gaps that will block implementation.
4. Use technical director and lead programmer role-card perspectives sequentially.
5. Recommend ADRs only for decisions that need durable project memory.

## Output Contract

Return strengths, risks, required changes, optional improvements, and ADR recommendations.
""",
    ),
    "ux-design": (
        "Design or review player-facing UX flows for a game feature.",
        """# CGS UX Design

Use `$cgs-ux-design` when the user needs player-facing UX for menus, HUD, onboarding, controls, accessibility, or feedback loops.

## Procedure

1. Read the concept, relevant GDDs, art direction, accessibility notes, platform targets, and input constraints.
2. Define the player goal, screen or flow states, feedback moments, error states, and accessibility considerations.
3. Keep recommendations tied to gameplay readability and repeated use, not marketing copy.
4. If implementation is requested, map UX states to files, components, scenes, or prefabs before editing.
5. Offer to write `design/ux/<feature-slug>.md` after the draft is accepted.

## Output Contract

Return flow outline, state list, interaction notes, accessibility checks, and implementation handoff notes.
""",
    ),
    "scope-check": (
        "Detect scope creep by comparing a story, epic, sprint, or milestone against its baseline plan.",
        """# CGS Scope Check

Use `$cgs-scope-check` when the user asks whether a story, epic, sprint, milestone, or feature has drifted from the approved plan.

## Procedure

1. Identify the baseline: story, epic, sprint plan, milestone, GDD, or architecture document.
2. Inspect current implementation, open story notes, changed files, and relevant commits when available.
3. Compare planned items to current items; separate additions, removals, and substitutions.
4. Classify each change as required discovery, optional polish, accidental creep, or formal re-scope.
5. Recommend cuts or deferrals that preserve the player-facing core loop.

## Verdict Rules

- `PASS`: net change is small and acceptance criteria remain intact.
- `CONCERNS`: additions are manageable but need explicit cuts, deferrals, or owner approval.
- `FAIL`: scope no longer matches the baseline and needs re-planning before more implementation.

## Output Contract

Return baseline evidence, current evidence, additions, removals, risk, verdict, and the smallest re-scope action.
Do not edit planning or implementation files unless the user explicitly asks.
""",
    ),
    "test-evidence-review": (
        "Review whether test files and manual evidence are strong enough to support story or milestone closure.",
        """# CGS Test Evidence Review

Use `$cgs-test-evidence-review` before `$cgs-story-done`, QA handoff, milestone review, or release review when evidence quality matters.

## Procedure

1. Read the target story, epic, acceptance criteria, test plan, and referenced evidence files.
2. Locate automated tests, smoke check notes, manual evidence, screenshots, transcripts, CI logs, or playtest notes.
3. Map each acceptance criterion to at least one evidence item.
4. Review evidence quality: meaningful assertions, edge cases, manual sign-off, freshness, and reproducibility.
5. Keep the pass read-only unless the user asks to write a persistent review note.

## Verdict Rules

- `ADEQUATE`: every closure-critical criterion has credible evidence.
- `INCOMPLETE`: evidence exists but is thin, stale, missing sign-off, or missing important edge cases.
- `MISSING`: one or more closure-critical criteria have no evidence.

## Output Contract

Return scope, evidence table, criterion coverage, blocking gaps, advisory gaps, verdict, and next skill.
Route missing implementation evidence to `$cgs-dev-story`; route missing smoke evidence to `$cgs-smoke-check`.
""",
    ),
    "regression-suite": (
        "Audit or maintain a regression-suite manifest for critical paths and fixed bugs.",
        """# CGS Regression Suite

Use `$cgs-regression-suite` when preparing a release, closing a sprint, or checking whether fixed bugs and critical paths have regression coverage.

## Procedure

1. Determine mode: `report` for read-only status, `audit` for full coverage review, or `update` when the user explicitly wants manifest changes.
2. Read existing `tests/regression-suite.md` if present, then inspect tests, closed bugs, recent stories, GDD critical paths, and release notes.
3. Map critical paths and fixed bugs to existing automated or manual regression evidence.
4. Identify missing, partial, stale, flaky, and quarantined coverage.
5. Write or update the manifest only after explicit user approval.

## Coverage Rules

- Critical gameplay state machines, formulas, save/load paths, and fixed severe bugs should have regression coverage.
- Visual or feel checks can be manual, but must name evidence and owner.
- Quarantined tests remain listed; they are not silently removed.

## Output Contract

Return mode, files scanned, coverage summary, missing regression tests, stale entries, recommended manifest changes, and verdict: `OK`, `GAPS`, or `STALE`.
""",
    ),
    "release-checklist": (
        "Create a focused release readiness checklist for one version and target platform set.",
        """# CGS Release Checklist

Use `$cgs-release-checklist` only when the user explicitly asks for a release checklist, launch checklist, or go/no-go preparation.

## Procedure

1. Identify version, platform targets, release type, and milestone scope; default platform to `all` only if the user did not specify one.
2. Read milestone notes, release notes, known bugs, regression suite status, QA evidence, store/distribution notes, and CI/build evidence.
3. Separate blockers from advisory launch risks.
4. Include platform sections only for requested targets: PC, console, mobile, web, or custom.
5. Offer to write `production/releases/release-checklist-<version>.md` only after the user approves the draft.

## Gate Rules

- `READY`: no known blocker, build/test evidence exists, and sign-off owners are named.
- `READY WITH RISKS`: launch is possible but explicit risk acceptance is required.
- `NOT READY`: blocker bugs, missing build evidence, missing regression coverage, or missing required release assets.

## Output Contract

Return release scope, blocker list, checklist grouped by build/QA/content/store/ops/sign-off, go-no-go verdict, and next skill.
Recommend `$cgs-gate-check` or `$cgs-team-release` for final approval.
""",
    ),
}


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def write_core_skills() -> None:
    for name, (summary, body) in CORE_SKILLS.items():
        skill_name = f"cgs-{name}"
        description = (
            f"Codex Game Studios curated workflow adapted from original /{name}. "
            f"Use when the user asks for /{name}, ${skill_name}, or {summary}"
        )
        content = f"---\nname: {skill_name}\ndescription: \"{description}\"\n---\n\n{body.strip()}\n"
        write_text(SKILLS / skill_name / "SKILL.md", content)


def update_plugin_metadata() -> None:
    path = PLUGIN / ".codex-plugin" / "plugin.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["version"] = RELEASE_VERSION
    data["author"] = {
        "name": "DocJlm",
        "email": "1952199902@qq.com",
        "url": "https://github.com/DocJlm",
    }
    data["homepage"] = "https://github.com/DocJlm/Codex-Game-Studios"
    data["repository"] = "https://github.com/DocJlm/Codex-Game-Studios"
    data.setdefault("interface", {})["developerName"] = "DocJlm"
    write_text(path, json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def write_fixture() -> None:
    files = {
        "README.md": """# Empty Game Fixture

This fixture is a tiny Codex Game Studios project used for workflow smoke checks.

Expected smoke path:

1. `$cgs-start` detects an already bootstrapped lean project.
2. `$cgs-project-stage-detect` reports `PRODUCTION` because concept, engine preferences, architecture, epic, and ready story exist.
3. `$cgs-dev-story production/epics/core-loop/STORY-001-player-loop.md` has a small ready story to inspect.
4. `$cgs-story-done production/epics/core-loop/STORY-001-player-loop.md` can report missing implementation evidence.

See `WALKTHROUGH.md` for the expected transcript shape.
""",
        "WALKTHROUGH.md": """# Empty Game Workflow Walkthrough

This fixture is not a real game implementation. It is a stable project shape for checking that the core Codex Game Studios loop gives useful, bounded answers.

## `$cgs-start`

Expected result:
- Detects an existing Codex Game Studios workspace.
- Reports `production/stage.txt` as `production` and `production/review-mode.txt` as `lean`.
- Does not recreate existing folders or overwrite planning files.
- Recommends `$cgs-project-stage-detect` or `$cgs-dev-story` as the next step.

## `$cgs-project-stage-detect`

Expected result:
- Detects Godot 4.3 / GDScript preferences from `docs/architecture/technical-preferences.md`.
- Reports `PRODUCTION` because concept, systems index, architecture, epic, and ready story exist.
- Lists evidence paths for the concept, architecture, epic, story, and smoke checklist.
- Calls out that source implementation evidence is intentionally absent.

## `$cgs-dev-story production/epics/core-loop/STORY-001-player-loop.md`

Expected result:
- Reads exactly one ready story.
- Produces a short implementation plan instead of broad project restructuring.
- Proposes scoped gameplay files and tests for movement, score, timer, and reset.
- Asks before writing unless the user has explicitly requested implementation.

## `$cgs-story-done production/epics/core-loop/STORY-001-player-loop.md`

Expected result:
- Returns `NEEDS FIXES` or `BLOCKED`, not `DONE`, because no implementation files or test evidence exist.
- Checks all four acceptance criteria.
- Names missing evidence: source changes, automated score/timer tests, and manual smoke result.
- Recommends `$cgs-dev-story` as the next action.
""",
        "AGENTS.md": """# Fixture Agent Guide

Use this as a minimal game project for Codex Game Studios smoke tests.
Do not treat it as a real shipped game.
""",
        "production/stage.txt": "production\n",
        "production/review-mode.txt": "lean\n",
        "docs/architecture/technical-preferences.md": """# Technical Preferences

Engine: Godot 4.3
Language: GDScript
Target platform: Desktop
Test command: godot --headless --run-tests
""",
        "design/gdd/game-concept.md": """# Game Concept

Pitch: A minimal arcade prototype where the player collects sparks before time runs out.

Pillars:
- Immediate movement clarity
- One-screen readable goals
- Fast reset after failure
""",
        "design/gdd/systems-index.md": """# Systems Index

| System | Priority | Status |
| --- | --- | --- |
| Core Loop | MVP | Approved |
""",
        "docs/architecture/architecture.md": """# Architecture

The fixture uses a small scene-controller architecture with separate player, collectible, timer, and score systems.
""",
        "docs/architecture/control-manifest.md": """# Control Manifest

- Keep gameplay values in data resources or constants documented by story acceptance criteria.
- Keep UI display separate from gameplay state ownership.
""",
        "production/epics/core-loop/EPIC.md": """# Epic: Core Loop

Goal: Build a playable loop with movement, collectibles, timer, score, and reset.

Acceptance:
- Player can move.
- Collectibles increase score.
- Timer ends the round.
""",
        "production/epics/core-loop/STORY-001-player-loop.md": """# Story: Player Loop Skeleton

Status: Ready
Owner role: gameplay-programmer

## Context

Create the smallest playable loop skeleton for the empty game fixture.

## Acceptance Criteria

- Player entity can move in four directions.
- Collectible pickup increments score.
- Timer reaches zero and ends the round.
- Reset returns score and timer to initial values.

## Test Plan

- Add or update unit tests for score and timer logic.
- Manually smoke test movement, pickup, timeout, and reset.
""",
        "tests/SMOKE-CHECKLIST.md": """# Fixture Smoke Checklist

- `$cgs-start`: detects project state and does not recreate existing files unnecessarily.
- `$cgs-project-stage-detect`: reports production-ready planning artifacts.
- `$cgs-dev-story`: reads the ready story and proposes scoped files/tests.
- `$cgs-story-done`: notices implementation evidence is absent until code exists.
""",
    }
    for relative, content in files.items():
        write_text(FIXTURE / relative, content)


def write_transcripts() -> None:
    write_text(
        ROOT / "docs" / "transcripts" / "concept-to-story.md",
        """# Concept-to-Story Transcript

This transcript shows the intended v0.3 Codex Game Studios feel: concise, project-aware, and bounded by explicit write confirmations. It uses a fictional small game called Spark Sprint.

## 1. Start A New Project

User:

```text
Use $cgs-start. I want a tiny arcade game prototype about collecting sparks before a timer ends.
```

Expected Codex shape:

```text
Detected state: fresh workspace with no production stage, concept, engine preferences, or epics.
Missing decisions: engine, target platform, review mode.
Suggested setup:
- production/stage.txt = concept
- production/review-mode.txt = lean
- design/gdd/game-concept.md starter draft
Before writing: confirm engine and review mode.
Next skill: $cgs-brainstorm or $cgs-setup-engine
```

User:

```text
Use Godot 4.3, desktop, lean review. Write the starter files.
```

Expected Codex shape:

```text
Files updated:
- production/stage.txt
- production/review-mode.txt
- design/gdd/game-concept.md
Next: $cgs-setup-engine to capture technical preferences.
```

## 2. Capture Engine Preferences

User:

```text
Use $cgs-setup-engine for Godot 4.3 and GDScript.
```

Expected Codex shape:

```text
Detected engine: no project.godot yet, user selected Godot 4.3.
Decisions captured:
- Language: GDScript
- Platform: desktop
- Test command placeholder: godot --headless --run-tests
File proposed: docs/architecture/technical-preferences.md
Next skill: $cgs-map-systems
```

## 3. Map Systems

User:

```text
Use $cgs-map-systems from the current game concept.
```

Expected Codex shape:

```text
MVP systems:
- Player movement
- Collectible spawning and pickup
- Timer and round state
- Score display
Dependency order:
1. Timer and score state
2. Player movement
3. Collectible pickup
4. HUD feedback
File proposed: design/gdd/systems-index.md
Next skill: $cgs-create-architecture
```

## 4. Create Architecture

User:

```text
Use $cgs-create-architecture. Keep it small.
```

Expected Codex shape:

```text
Architecture summary:
- GameController owns round state.
- PlayerController owns movement input.
- Collectible nodes emit pickup events.
- HUD observes score and timer.
Required ADRs: none for this tiny prototype.
File proposed: docs/architecture/architecture.md
Next skill: $cgs-create-epics
```

## 5. Create Epic And Story

User:

```text
Use $cgs-create-epics, then split the first epic with $cgs-create-stories.
```

Expected Codex shape:

```text
Epic: Core Loop
Goal: Build a playable timer-based collection loop.
Stories:
1. Player Loop Skeleton
2. HUD Feedback
3. Round Reset
First story path:
production/epics/core-loop/STORY-001-player-loop.md
Next skill: $cgs-story-readiness
```

## 6. Pick Up A Story

User:

```text
Use $cgs-dev-story production/epics/core-loop/STORY-001-player-loop.md. Implement it if ready.
```

Expected Codex shape before edits:

```text
Readiness: READY
Plan:
- Inspect existing Godot project files.
- Add or update player movement, score, timer, and reset logic.
- Add score/timer tests if the project test harness exists.
Files likely touched:
- src/gameplay/player_controller.gd
- src/gameplay/game_controller.gd
- tests/test_game_controller.gd
As requested, proceeding with implementation.
```

Expected Codex shape after edits:

```text
Changed files: listed with paths.
Tests run: command and result.
Acceptance criteria:
- Player moves: pass or manual check required
- Pickup increments score: pass
- Timer ends round: pass
- Reset restores timer and score: pass
Next skill: $cgs-story-done
```

## 7. Close The Story

User:

```text
Use $cgs-story-done production/epics/core-loop/STORY-001-player-loop.md.
```

Expected Codex shape:

```text
Verdict: DONE or NEEDS FIXES
Evidence:
- Diff paths reviewed
- Automated tests and manual smoke checks
- Acceptance criteria checklist
If complete: offer to update story status.
If incomplete: list blockers and route back to $cgs-dev-story or $cgs-smoke-check.
```

## 8. Review And QA Follow-Up

User:

```text
Use $cgs-code-review on the current diff, then $cgs-qa-plan for the Core Loop epic.
```

Expected Codex shape:

```text
$cgs-code-review:
- Findings first, ordered P0-P3.
- File and line references when possible.
- Test gaps and residual risk.

$cgs-qa-plan:
- Risk matrix.
- Automated and manual checks.
- Evidence artifacts.
- Exit criteria for the epic.
```
""",
    )

    write_text(
        ROOT / "docs" / "transcripts" / "spark-sprint-codex-run.md",
        """# Spark Sprint Codex Run Transcript

This transcript records a realistic Codex Game Studios pass through the Spark Sprint example. It is written as a concrete usage transcript for an optional runnable Godot example that still validates without requiring Godot to be installed.

Project path:

```text
examples/spark-sprint/
```

Story path:

```text
examples/spark-sprint/production/epics/core-loop/STORY-001-player-loop.md
```

## 1. Onboard The Example

User:

```text
Use $cgs-start on examples/spark-sprint. Do not edit files unless something required is missing.
```

Codex:

```text
Detected state: structured Codex Game Studios example project.
Stage file: examples/spark-sprint/production/stage.txt -> production
Review mode: examples/spark-sprint/production/review-mode.txt -> lean
Engine signal: examples/spark-sprint/project.godot plus Godot 4.3 technical preferences.

Evidence paths:
- examples/spark-sprint/design/gdd/game-concept.md
- examples/spark-sprint/design/gdd/systems-index.md
- examples/spark-sprint/docs/architecture/architecture.md
- examples/spark-sprint/production/epics/core-loop/EPIC.md

Files updated: none.
Next skill: $cgs-project-stage-detect
```

## 2. Detect Production Stage

User:

```text
Use $cgs-project-stage-detect on examples/spark-sprint. Report the stage and evidence paths.
```

Codex:

```text
Verdict: PRODUCTION

Why:
- Concept, systems index, architecture, control manifest, epic, and story exist.
- Source drafts exist under examples/spark-sprint/src/.
- Test and smoke evidence drafts exist under examples/spark-sprint/tests/.
- The story is already in Review state, so this is beyond planning but not a release candidate.

Evidence paths:
- examples/spark-sprint/project.godot
- examples/spark-sprint/docs/architecture/technical-preferences.md
- examples/spark-sprint/production/epics/core-loop/STORY-001-player-loop.md
- examples/spark-sprint/scenes/main.tscn
- examples/spark-sprint/src/gameplay/game_controller.gd
- examples/spark-sprint/tests/test_game_controller.gd

Next 3 actions:
1. $cgs-dev-story for the player loop story.
2. $cgs-smoke-check to verify static evidence and optional Godot scene loading.
3. $cgs-story-done to decide whether the story can close.
```

## 3. Pick Up The Story

User:

```text
Use $cgs-dev-story examples/spark-sprint/production/epics/core-loop/STORY-001-player-loop.md. Implement only if the story is not already covered.
```

Codex:

```text
Readiness: READY

Plan:
- Read story, epic, core-loop GDD, architecture, control manifest, scene, and source drafts.
- Compare acceptance criteria against MainScene, GameController, PlayerController, Collectible, HUD, and test draft.
- Avoid writing changes unless coverage is missing.

Inspection result:
- Movement draft exists: examples/spark-sprint/src/gameplay/player_controller.gd
- Score, timer, win, timeout, and reset logic exists: examples/spark-sprint/src/gameplay/game_controller.gd
- Pickup draft exists: examples/spark-sprint/src/gameplay/collectible.gd
- HUD draft exists: examples/spark-sprint/src/ui/hud.gd
- Main scene exists: examples/spark-sprint/scenes/main.tscn
- Static tests cover score, win, timeout, and reset: examples/spark-sprint/tests/test_game_controller.gd

Files updated: none. The story is already represented by source, scene, and test drafts.
Next skill: $cgs-smoke-check
```

## 4. Run A Smoke Check

User:

```text
Use $cgs-smoke-check for examples/spark-sprint.
```

Codex:

```text
Commands run:
- python tools\\validate_examples.py
- python tools\\validate_godot_example.py

Result:
- Example validation passed.
- Godot scene validation loaded the scene when Godot was available, or reported SKIP when Godot was not installed.

Automated coverage:
- Required project files exist.
- Walkthrough and docs mention the full workflow sequence.
- Source drafts include MainScene, GameController, PlayerController, Collectible, and HUD tokens.
- Scene draft references runtime scripts.
- Test draft includes score, win, timeout, and reset cases.

Manual checks remaining:
- Launch the Godot scene when a local editor/runtime is available.
- Confirm input bindings move the player.
- Confirm collecting 5 sparks sets the state to won.
- Confirm pressing R resets score, timer, and spark visibility.

Next skill: $cgs-story-done
```

## 5. Close The Story

User:

```text
Use $cgs-story-done examples/spark-sprint/production/epics/core-loop/STORY-001-player-loop.md.
```

Codex:

```text
Verdict: DONE for static example evidence, with optional runtime evidence when Godot is available.

Acceptance criteria:
- Player entity can move in four directions: covered by PlayerController draft and scene.
- Collectible pickup increments score: covered by Collectible and GameController drafts.
- Timer reaches zero and ends the round: covered by GameController draft and test draft.
- Reset returns score, timer, and round state to initial values: covered by GameController draft and test draft.

Evidence:
- examples/spark-sprint/scenes/main.tscn
- examples/spark-sprint/src/gameplay/main_scene.gd
- examples/spark-sprint/src/gameplay/player_controller.gd
- examples/spark-sprint/src/gameplay/collectible.gd
- examples/spark-sprint/src/gameplay/game_controller.gd
- examples/spark-sprint/src/ui/hud.gd
- examples/spark-sprint/tests/test_game_controller.gd
- examples/spark-sprint/tests/SMOKE-CHECKLIST.md

No story status edit was needed; the story already says Status: Review.
Next skill: $cgs-code-review
```

## 6. Review The Example Code

User:

```text
Use $cgs-code-review on the Spark Sprint source draft.
```

Codex:

```text
Findings:
- No P0/P1 issues found in the static example review.
- P2 examples/spark-sprint/tests/test_game_controller.gd: tests are GDScript-style drafts, not an installed Godot test runner. Keep this documented until a real test plugin is added.

Open questions:
- Should a future release add a real Godot test runner, or keep this as a lightweight scene demo?

Test gaps:
- Optional Godot runtime validation may be skipped when Godot is not installed.
- Visual playtest evidence is still manual.

Change summary:
- No source changes were made during review.
```

## 7. Create A QA Plan

User:

```text
Use $cgs-qa-plan for examples/spark-sprint/production/epics/core-loop/EPIC.md.
```

Codex:

```text
Scope:
- Core loop movement, pickup, score, timer, reset, HUD feedback, and story evidence.

Risk matrix:
- Medium: scene wiring for pickup and HUD labels should be checked in a local Godot playtest.
- Medium: input bindings differ across keyboard layouts or controller support.
- Medium: timer edge cases around zero and repeated reset.
- Low: static source/test documentation drift.

Test matrix:
- Automated static: python tools\\validate_examples.py.
- Optional runtime load: python tools\\validate_godot_example.py.
- Source review: MainScene, GameController, PlayerController, Collectible, and HUD drafts.
- Manual runtime: launch scene, move in four directions, collect 5 sparks, wait for timeout, reset.
- Evidence: command output, screenshots or short capture for runtime pass, updated smoke checklist.

Exit criteria:
- Static validator passes.
- Optional Godot validator passes or reports SKIP because Godot is unavailable.
- Runtime playtest evidence is attached when a local Godot runtime is available.
```

## Final State

The current run demonstrates the full Spark Sprint loop:

```text
$cgs-start -> $cgs-project-stage-detect -> $cgs-dev-story -> $cgs-smoke-check -> $cgs-story-done -> $cgs-code-review -> $cgs-qa-plan
```

The transcript keeps Codex behavior read-first, evidence-based, and explicit about the boundary between required static validation and optional Godot runtime testing.
""",
    )

    write_text(
        ROOT / "docs" / "workflows" / "high-frequency-workflows.md",
        """# High-Frequency Workflow Notes

These notes document the v0.3 polish targets for the first workflows users are likely to repeat during production.

## `$cgs-code-review`

Use it like a code review, not a rewrite command. It should inspect the diff, read the story context when available, and lead with concrete findings. A good answer starts with severity-ordered risks and only then gives summary context.

Minimum useful output:
- Findings with severity, file path, and line when possible.
- Open questions or assumptions.
- Test gaps and residual risk.
- Short change summary.

## `$cgs-qa-plan`

Use it when the user needs a scoped test plan. It should map acceptance criteria to verification paths and separate automated checks from manual gameplay checks.

Minimum useful output:
- Scope and out-of-scope boundaries.
- Risk matrix.
- Test matrix.
- Evidence artifacts.
- Exit criteria.

## `$cgs-smoke-check`

Use it for a fast confidence pass after implementation. It should run safe commands when available and clearly mark checks that require the game editor or a human play session.

Minimum useful output:
- Commands run.
- Pass/fail result.
- Manual checks remaining.
- Reproduction details for failures.
- Next fix or verification step.
""",
    )


def write_workflow_polish_docs() -> None:
    write_text(
        ROOT / "docs" / "workflows" / "production-readiness-workflows.md",
        """# Production Readiness Workflow Notes

These notes document the v0.7 polish targets for workflows used around story readiness, scope control, evidence review, regression coverage, and release readiness.

## `$cgs-story-readiness`

Use before implementation starts. The skill should decide whether one story is implementable now, not redesign the story or edit code.

Minimum useful output:
- Verdict: `READY`, `NEEDS WORK`, or `BLOCKED`.
- Evidence paths.
- Blocking decisions or dependencies.
- Smallest next action.
- Recommended next skill.

## `$cgs-scope-check`

Use when a story, epic, sprint, milestone, or feature may have drifted from its baseline. The skill should compare planned scope to current state and recommend cuts or formal re-scope.

Minimum useful output:
- Baseline evidence.
- Current evidence.
- Additions and removals.
- Schedule, quality, and integration risk.
- Verdict: `PASS`, `CONCERNS`, or `FAIL`.

## `$cgs-test-evidence-review`

Use before story closure, QA handoff, milestone review, or release review. The skill should map acceptance criteria to actual evidence and flag closure blockers.

Minimum useful output:
- Evidence table.
- Criterion coverage.
- Blocking gaps and advisory gaps.
- Verdict: `ADEQUATE`, `INCOMPLETE`, or `MISSING`.
- Routing to `$cgs-dev-story` or `$cgs-smoke-check` when evidence is absent.

## `$cgs-regression-suite`

Use before release gates, sprint close, or after bug fixes. The skill should report or update the regression-suite manifest only with explicit approval.

Minimum useful output:
- Mode: `report`, `audit`, or `update`.
- Critical-path and bug-fix coverage summary.
- Missing, partial, stale, flaky, and quarantined coverage.
- Recommended manifest changes.
- Verdict: `OK`, `GAPS`, or `STALE`.

## `$cgs-release-checklist`

Use only when explicitly requested for release readiness or go/no-go preparation. The skill should produce a focused checklist for a version and platform set.

Minimum useful output:
- Release scope and target platforms.
- Blocker list.
- Build, QA, content, store, ops, and sign-off checklist.
- Verdict: `READY`, `READY WITH RISKS`, or `NOT READY`.
- Routing to `$cgs-gate-check` or `$cgs-team-release`.
""",
    )


def write_install_docs() -> None:
    write_text(
        ROOT / "docs" / "install" / "local-plugin.md",
        """# Local Plugin Install UX

This guide describes how to use Codex Game Studios as a repo-local Codex plugin, and what to do when the current Codex build does not expose local plugin installation in the UI.

For a dated local field test, see `docs/install/field-test-2026-05-22.md`.
For platform-specific setup, see `docs/platforms/windows.md` and `docs/platforms/macos.md`.

## Files Codex Should Discover

The repo-local marketplace entry is:

```text
.agents/plugins/marketplace.json
```

It points to the plugin root:

```text
./plugins/codex-game-studios
```

The plugin manifest is:

```text
plugins/codex-game-studios/.codex-plugin/plugin.json
```

The skill root declared by the manifest is:

```text
plugins/codex-game-studios/skills/
```

## Preferred Path

1. Open the repository root in Codex.
2. Use the Codex plugin or marketplace UI if your build exposes repo-local plugin installation.
3. Install or enable `codex-game-studios`.
4. Start with one of the default prompts:

```text
Use $cgs-start to set up a new game project.
Use $cgs-project-stage-detect on this existing game.
Use $cgs-dev-story to implement the next story.
```

## Verification Prompts

After enabling the plugin, verify discovery with small prompts:

```text
Use $cgs-help and tell me the next Codex Game Studios step for this repository.
Use $cgs-project-stage-detect and report only the detected stage plus evidence paths.
```

Good signs:
- Codex recognizes `$cgs-*` names without a path.
- The answer references `plugins/codex-game-studios/references/studio-docs/workflow-catalog.yaml` only when needed.
- The answer treats role cards as reference prompts, not automatic subagents.
- The answer does not try to install runtime hooks.

## Fallback Path

If local plugin installation is not visible or the skill name does not trigger, call the skill by path:

```text
Use the skill at plugins/codex-game-studios/skills/cgs-start/SKILL.md to set up this project.
Use the skill at plugins/codex-game-studios/skills/cgs-project-stage-detect/SKILL.md to audit this project.
Use the skill at plugins/codex-game-studios/skills/cgs-dev-story/SKILL.md for production/epics/core-loop/STORY-001-player-loop.md.
```

This is the same workflow content. It only bypasses plugin discovery.

## Local Validation

Run these checks before reporting an install or discovery problem:

Windows PowerShell:

```powershell
python tools\\run_all_validators.py
```

macOS zsh or bash:

```bash
python3 tools/run_all_validators.py
python tools/run_all_validators.py
```

The important install fields are:

```json
{
  "name": "codex-game-studios",
  "skills": "./skills/"
}
```

and:

```json
{
  "name": "codex-game-studios",
  "source": {
    "source": "local",
    "path": "./plugins/codex-game-studios"
  }
}
```

## Troubleshooting

| Symptom | Check | Fix |
| --- | --- | --- |
| Plugin does not appear | Opened folder is not repo root | Open the cloned repository root |
| Plugin appears but skills do not trigger | Manifest `skills` path is wrong | Run `python tools\\validate_cgs.py` |
| Marketplace entry fails to parse | Invalid JSON | Run `python -m json.tool .agents\\plugins\\marketplace.json` |
| Skill trigger is unreliable | Local plugin UI is unavailable or stale | Use the path-based fallback prompts |
| Hook behavior is missing | Runtime hooks are intentionally not wired | Run explicit validation scripts instead |

## Hook Boundary

Legacy hook scripts are preserved for reference under `plugins/codex-game-studios/scripts/checks/legacy-claude-hooks/`, but Codex Game Studios does not declare plugin runtime hooks. Until the hook policy changes, safety checks stay explicit through scripts and skill instructions.
""",
    )

    write_text(
        ROOT / "docs" / "install" / "field-test-2026-05-22.md",
        """# Local Plugin Field Test 2026-05-22

This note captures user-visible repo-local plugin behavior observed while preparing Codex Game Studios v0.9. It is intentionally practical: if discovery is not available in a given Codex build, the path-based fallback remains the supported route.

## Environment

- Repository root: `D:\\Git\\Codex-Game-Studios`
- Plugin root: `plugins/codex-game-studios/`
- Marketplace entry: `.agents/plugins/marketplace.json`
- Plugin manifest: `plugins/codex-game-studios/.codex-plugin/plugin.json`
- Skill root: `plugins/codex-game-studios/skills/`
- Plugin version under test: `0.9.0`

## Structural Checks

These commands passed before the field note was recorded:

```powershell
python tools\\validate_cgs.py
python tools\\validate_skills.py
python tools\\validate_plugin_install_docs.py
python -m json.tool plugins\\codex-game-studios\\.codex-plugin\\plugin.json
python -m json.tool .agents\\plugins\\marketplace.json
```

The manifest and marketplace entry both point to repo-relative paths:

```json
{
  "name": "codex-game-studios",
  "skills": "./skills/"
}
```

```json
{
  "source": {
    "source": "local",
    "path": "./plugins/codex-game-studios"
  }
}
```

## Observed Current-Session Behavior

In the Codex desktop session used for this release, the active built-in skill list did not automatically show `cgs-*` skills before an explicit plugin enable or install step. That means a user may see the repository files and still not see `$cgs-start` as an installed skill trigger.

This is not treated as a plugin package failure when all structural validators pass. It means the current build or session is not exposing repo-local plugin discovery as an active runtime capability.

## Success Path

When a Codex build exposes repo-local plugin installation, the expected path is:

1. Open the cloned repository root.
2. Install or enable `codex-game-studios` from the repo-local marketplace entry.
3. Verify with a small prompt:

```text
Use $cgs-help and tell me the next Codex Game Studios step for this repository.
```

User-visible success signs:

- `$cgs-*` names work without a file path.
- The answer uses the Codex Game Studios workflow catalog when needed.
- Role cards are treated as references, not automatic subagents.
- No runtime hooks are installed or invoked.

## Fallback Path

When the plugin does not appear or skill triggers are not active, call the skill by path:

```text
Use the skill at plugins/codex-game-studios/skills/cgs-start/SKILL.md to set up this project.
Use the skill at plugins/codex-game-studios/skills/cgs-project-stage-detect/SKILL.md to audit this project.
Use the skill at plugins/codex-game-studios/skills/cgs-dev-story/SKILL.md for production/epics/core-loop/STORY-001-player-loop.md.
```

User-visible fallback signs:

- Codex can read the target `SKILL.md` directly.
- The workflow still uses `cgs-*` names internally.
- The response cites project evidence paths before proposing writes.
- The response does not require hidden local plugin state.

## Reporting Install Problems

Before filing an install or discovery issue, include:

- Codex build or app channel if visible.
- Whether the repo root was the opened workspace.
- Output from `python tools\\validate_cgs.py`.
- Output from `python tools\\validate_plugin_install_docs.py`.
- Whether `$cgs-help` worked by name or only by path.
- Any user-visible marketplace or plugin UI message.

## Release Decision

v0.9 keeps both paths documented. Repo-local plugin installation is the preferred user experience, but path-based skill invocation remains the compatibility path until local marketplace discovery is consistently visible in normal Codex builds.
""",
    )


def write_hook_policy_docs() -> None:
    write_text(
        ROOT / "docs" / "hooks" / "runtime-hook-evaluation.md",
        """# Runtime Hook Evaluation

This document records the Codex Game Studios v0.5 decision on runtime hooks.

Checked sources on 2026-05-22:
- OpenAI Codex hooks docs: https://developers.openai.com/codex/hooks
- OpenAI Codex plugin build docs: https://developers.openai.com/codex/plugins/build
- Local Codex plugin manifest sample: `C:\\Users\\ZQC\\.codex\\skills\\.system\\plugin-creator\\references\\plugin-json-spec.md`

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
python tools\\validate_cgs.py
python tools\\validate_skills.py
python tools\\validate_smoke_fixture.py
python tools\\validate_transcripts.py
python tools\\validate_plugin_install_docs.py
python tools\\validate_hook_policy.py
python tools\\validate_godot_example.py
python tools\\scan_legacy_tokens.py
```

## Rationale

Codex Game Studios is intended to be usable in a fresh clone without hidden local configuration. Because plugin hooks are disabled by default unless `[features].plugin_hooks = true`, shipping hook files now would create two different behavior modes:

- users with plugin hooks enabled would get extra runtime behavior;
- users without plugin hooks enabled would get only skills and explicit scripts.

That split is too easy to misunderstand for this template. The safer v0.5 behavior is to make all safety checks visible, repeatable, and CI-backed.

## Legacy Hook Mapping

| Legacy hook intent | v0.5 replacement |
| --- | --- |
| Pre-commit code quality | `python tools\\validate_cgs.py` plus project-specific tests |
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
""",
    )


def write_example_project() -> None:
    files = {
        "README.md": """# Spark Sprint Example

Spark Sprint is a minimal Godot-style example project for Codex Game Studios. It demonstrates a realistic workflow loop and can optionally run in Godot 4.x, while repository validation still works without Godot installed.

Use it to exercise:

1. `$cgs-start`
2. `$cgs-project-stage-detect`
3. `$cgs-dev-story`
4. `$cgs-smoke-check`
5. `$cgs-story-done`
6. `$cgs-code-review`
7. `$cgs-qa-plan`

The source, scene, and tests are intentionally small and static-validation friendly. If Godot is available, open `project.godot` and run `scenes/main.tscn` to try the playable loop.
""",
        "AGENTS.md": """# Spark Sprint Agent Guide

Use Codex Game Studios workflows for this example.
Treat files as a minimal runnable Godot example plus static workflow fixture.
Do not require a local Godot installation for repository validation.
""",
        "project.godot": """; Engine configuration file.
; This optional runnable example targets Godot 4.3 style structure.

config_version=5

[application]
config/name="Spark Sprint"
run/main_scene="res://scenes/main.tscn"
config/features=PackedStringArray("4.3")

[input]
move_left={
"deadzone": 0.5,
"events": []
}
move_right={
"deadzone": 0.5,
"events": []
}
move_up={
"deadzone": 0.5,
"events": []
}
move_down={
"deadzone": 0.5,
"events": []
}
""",
        "production/stage.txt": "production\n",
        "production/review-mode.txt": "lean\n",
        "docs/architecture/technical-preferences.md": """# Technical Preferences

Engine: Godot 4.3
Language: GDScript
Target platform: Desktop
Review mode: lean
Test command: use `python tools\\validate_examples.py` for static validation and `python tools\\validate_godot_example.py` for optional Godot scene loading.

## Source Layout

- `src/gameplay/`: gameplay state and actors
- `src/ui/`: HUD presentation
- `scenes/`: playable Godot scene
- `tests/`: GDScript-style test drafts
""",
        "design/gdd/game-concept.md": """# Game Concept

Pitch: Spark Sprint is a one-screen arcade prototype where the player collects sparks before the timer ends.

## Pillars

- Fast readability: the next spark and timer are always obvious.
- Low friction: movement starts immediately and reset is instant.
- Tiny loop: one round can be understood in under 30 seconds.

## MVP Loop

Move, collect sparks, watch the timer, and reset after win or timeout.
""",
        "design/gdd/systems-index.md": """# Systems Index

| System | Priority | Status | Notes |
| --- | --- | --- | --- |
| Player Movement | MVP | Drafted | Four-direction input |
| Spark Pickup | MVP | Drafted | Pickup increments score |
| Round Timer | MVP | Drafted | Timeout ends round |
| HUD Feedback | MVP | Drafted | Displays score, timer, and state |
""",
        "design/gdd/core-loop.md": """# Core Loop System

## Player Goal

Collect 5 sparks before the 30-second timer reaches zero.

## Rules

- The round starts in `playing` state.
- Each spark pickup increments score by 1.
- The player wins when score reaches `target_score`.
- The player loses when time reaches zero before the target score.
- Reset restores score, timer, and state.

## Acceptance Criteria

- Movement accepts four-direction input.
- Spark pickup increments score.
- Timer reaching zero ends the round.
- Reset restores initial score, time, and state.
""",
        "docs/architecture/architecture.md": """# Architecture

Spark Sprint uses a small controller-driven architecture.

## Modules

- `GameController`: owns score, timer, round state, and reset behavior.
- `PlayerController`: owns movement input and velocity.
- `Collectible`: emits pickup behavior and delegates scoring to `GameController`.
- `Hud`: reads round state and presents score, time, and status text.

## Data Flow

Player overlaps collectible -> collectible calls `GameController.collect_spark()` -> controller updates score/state -> HUD refreshes display.
""",
        "docs/architecture/control-manifest.md": """# Control Manifest

- Gameplay constants live in `GameController`.
- UI never owns gameplay state.
- Reset must go through `GameController.reset_round()`.
- Tests should cover score, timer, win, timeout, and reset behavior.
""",
        "production/epics/core-loop/EPIC.md": """# Epic: Core Loop

Goal: Build a tiny playable loop for Spark Sprint.

## Included Systems

- Player movement
- Spark pickup and scoring
- Timer and round state
- Reset behavior
- HUD feedback

## Acceptance

- Core loop can be inspected through source and test drafts.
- Story evidence maps to design and architecture documents.
- Smoke checklist covers success, timeout, and reset paths.
""",
        "production/epics/core-loop/STORY-001-player-loop.md": """# Story: Player Loop Skeleton

Status: Review
Owner role: gameplay-programmer

## Context

Implement the smallest Spark Sprint loop: movement, spark pickup, timer, win/timeout state, and reset.

## Acceptance Criteria

- Player entity can move in four directions.
- Collectible pickup increments score.
- Timer reaches zero and ends the round.
- Reset returns score, timer, and round state to initial values.

## Implementation Notes

- Gameplay state lives in `src/gameplay/game_controller.gd`.
- Movement draft lives in `src/gameplay/player_controller.gd`.
- Pickup draft lives in `src/gameplay/collectible.gd`.
- HUD draft lives in `src/ui/hud.gd`.

## Test Plan

- Review `tests/test_game_controller.gd` for score, win, timeout, and reset coverage.
- Run static repository validation from the root with `python tools\\validate_examples.py`.
- Run optional scene validation with `python tools\\validate_godot_example.py`; it skips when Godot is not installed.
- Manual runtime smoke test is documented but not required for CI.

## Evidence

- Source draft: `src/gameplay/game_controller.gd`
- Playable scene: `scenes/main.tscn`
- Test draft: `tests/test_game_controller.gd`
- Smoke checklist: `tests/SMOKE-CHECKLIST.md`
""",
        "scenes/main.tscn": """[gd_scene load_steps=8 format=3]

[ext_resource type="Script" path="res://src/gameplay/main_scene.gd" id="1_main"]
[ext_resource type="Script" path="res://src/gameplay/game_controller.gd" id="2_game"]
[ext_resource type="Script" path="res://src/gameplay/player_controller.gd" id="3_player"]
[ext_resource type="Script" path="res://src/gameplay/collectible.gd" id="4_spark"]
[ext_resource type="Script" path="res://src/ui/hud.gd" id="5_hud"]

[sub_resource type="CircleShape2D" id="CircleShape2D_player"]
radius = 16.0

[sub_resource type="CircleShape2D" id="CircleShape2D_spark"]
radius = 12.0

[node name="Main" type="Node2D"]
script = ExtResource("1_main")

[node name="GameController" type="Node" parent="."]
script = ExtResource("2_game")

[node name="Player" type="CharacterBody2D" parent="."]
position = Vector2(320, 240)
script = ExtResource("3_player")

[node name="CollisionShape2D" type="CollisionShape2D" parent="Player"]
shape = SubResource("CircleShape2D_player")

[node name="Body" type="Polygon2D" parent="Player"]
color = Color(0.15, 0.65, 1, 1)
polygon = PackedVector2Array(-16, -16, 16, -16, 16, 16, -16, 16)

[node name="Spark" type="Area2D" parent="."]
position = Vector2(480, 220)
script = ExtResource("4_spark")

[node name="CollisionShape2D" type="CollisionShape2D" parent="Spark"]
shape = SubResource("CircleShape2D_spark")

[node name="Body" type="Polygon2D" parent="Spark"]
color = Color(1, 0.82, 0.2, 1)
polygon = PackedVector2Array(0, -18, 5, -5, 18, 0, 5, 5, 0, 18, -5, 5, -18, 0, -5, -5)

[node name="CanvasLayer" type="CanvasLayer" parent="."]

[node name="Hud" type="Control" parent="CanvasLayer"]
layout_mode = 3
anchors_preset = 15
anchor_right = 1.0
anchor_bottom = 1.0
script = ExtResource("5_hud")

[node name="ScoreLabel" type="Label" parent="CanvasLayer/Hud"]
offset_left = 16.0
offset_top = 12.0
offset_right = 220.0
offset_bottom = 38.0
text = "Score: 0"

[node name="TimerLabel" type="Label" parent="CanvasLayer/Hud"]
offset_left = 16.0
offset_top = 42.0
offset_right = 220.0
offset_bottom = 68.0
text = "Time: 30.0"

[node name="StateLabel" type="Label" parent="CanvasLayer/Hud"]
offset_left = 16.0
offset_top = 72.0
offset_right = 360.0
offset_bottom = 98.0
text = "Playing"

[node name="HelpLabel" type="Label" parent="CanvasLayer/Hud"]
offset_left = 16.0
offset_top = 410.0
offset_right = 620.0
offset_bottom = 450.0
text = "Move with WASD or arrows. Collect 5 sparks. Press R to reset."
""",
        "src/gameplay/main_scene.gd": """extends Node2D

@onready var game_controller: GameController = $GameController
@onready var player: PlayerController = $Player
@onready var spark: Collectible = $Spark
@onready var hud: Hud = $CanvasLayer/Hud

var _reset_key_down := false

func _ready() -> void:
    game_controller.score_changed.connect(hud.update_score)
    game_controller.timer_changed.connect(hud.update_timer)
    game_controller.round_state_changed.connect(hud.update_state)
    spark.game_controller_path = spark.get_path_to(game_controller)
    reset_round()

func _process(delta: float) -> void:
    game_controller.tick_timer(delta)
    var reset_pressed := Input.is_key_pressed(KEY_R)
    if reset_pressed and not _reset_key_down:
        reset_round()
    _reset_key_down = reset_pressed

func reset_round() -> void:
    player.position = Vector2(320, 240)
    game_controller.reset_round()
    spark.reset_spark()
""",
        "src/gameplay/game_controller.gd": """extends Node
class_name GameController

signal score_changed(score: int)
signal timer_changed(time_left: float)
signal round_state_changed(state: String)

const ROUND_TIME := 30.0
const TARGET_SCORE := 5

var score := 0
var time_left := ROUND_TIME
var round_state := "playing"

func reset_round() -> void:
    score = 0
    time_left = ROUND_TIME
    round_state = "playing"
    score_changed.emit(score)
    timer_changed.emit(time_left)
    round_state_changed.emit(round_state)

func collect_spark() -> void:
    if round_state != "playing":
        return
    score += 1
    score_changed.emit(score)
    if score >= TARGET_SCORE:
        round_state = "won"
        round_state_changed.emit(round_state)

func tick_timer(delta: float) -> void:
    if round_state != "playing":
        return
    time_left = max(time_left - delta, 0.0)
    timer_changed.emit(time_left)
    if time_left <= 0.0:
        round_state = "lost"
        round_state_changed.emit(round_state)
""",
        "src/gameplay/player_controller.gd": """extends CharacterBody2D
class_name PlayerController

@export var speed := 220.0
@export var play_area_min := Vector2(24, 100)
@export var play_area_max := Vector2(616, 392)

func _physics_process(_delta: float) -> void:
    var input_vector := _read_input()
    velocity = input_vector.normalized() * speed
    move_and_slide()
    position.x = clampf(position.x, play_area_min.x, play_area_max.x)
    position.y = clampf(position.y, play_area_min.y, play_area_max.y)

func _read_input() -> Vector2:
    var input_vector := Vector2.ZERO
    if Input.is_action_pressed("move_left") or Input.is_key_pressed(KEY_A) or Input.is_key_pressed(KEY_LEFT):
        input_vector.x -= 1.0
    if Input.is_action_pressed("move_right") or Input.is_key_pressed(KEY_D) or Input.is_key_pressed(KEY_RIGHT):
        input_vector.x += 1.0
    if Input.is_action_pressed("move_up") or Input.is_key_pressed(KEY_W) or Input.is_key_pressed(KEY_UP):
        input_vector.y -= 1.0
    if Input.is_action_pressed("move_down") or Input.is_key_pressed(KEY_S) or Input.is_key_pressed(KEY_DOWN):
        input_vector.y += 1.0
    return input_vector
""",
        "src/gameplay/collectible.gd": """extends Area2D
class_name Collectible

@export var game_controller_path: NodePath
@export var play_area_min := Vector2(80, 120)
@export var play_area_max := Vector2(560, 360)

func _ready() -> void:
    var callback := Callable(self, "_on_body_entered")
    if not body_entered.is_connected(callback):
        body_entered.connect(callback)

func reset_spark() -> void:
    visible = true
    monitoring = true
    randomize_position()

func _on_body_entered(_body: Node) -> void:
    var controller := get_node_or_null(game_controller_path)
    if controller and controller.has_method("collect_spark"):
        controller.collect_spark()
        if controller.round_state == "playing":
            randomize_position()
        else:
            visible = false
            monitoring = false

func randomize_position() -> void:
    position = Vector2(
        randf_range(play_area_min.x, play_area_max.x),
        randf_range(play_area_min.y, play_area_max.y)
    )
""",
        "src/ui/hud.gd": """extends Control
class_name Hud

@export var score_label_path: NodePath
@export var timer_label_path: NodePath
@export var state_label_path: NodePath

func update_score(score: int) -> void:
    var label := _get_label(score_label_path, "ScoreLabel")
    if label:
        label.text = "Score: %d" % score

func update_timer(time_left: float) -> void:
    var label := _get_label(timer_label_path, "TimerLabel")
    if label:
        label.text = "Time: %.1f" % time_left

func update_state(state: String) -> void:
    var label := _get_label(state_label_path, "StateLabel")
    if label:
        label.text = state.capitalize()

func _get_label(path: NodePath, fallback_name: String) -> Label:
    if path != NodePath(""):
        var explicit_label := get_node_or_null(path) as Label
        if explicit_label:
            return explicit_label
    return get_node_or_null(fallback_name) as Label
""",
        "tests/test_game_controller.gd": """extends RefCounted

# Static GDScript-style test draft for documentation and review.

func test_collect_spark_increments_score() -> void:
    var controller := GameController.new()
    controller.collect_spark()
    assert(controller.score == 1)

func test_target_score_wins_round() -> void:
    var controller := GameController.new()
    for index in range(controller.TARGET_SCORE):
        controller.collect_spark()
    assert(controller.round_state == "won")

func test_timer_timeout_loses_round() -> void:
    var controller := GameController.new()
    controller.tick_timer(controller.ROUND_TIME)
    assert(controller.round_state == "lost")

func test_reset_restores_initial_values() -> void:
    var controller := GameController.new()
    controller.collect_spark()
    controller.tick_timer(5.0)
    controller.reset_round()
    assert(controller.score == 0)
    assert(controller.time_left == controller.ROUND_TIME)
    assert(controller.round_state == "playing")
""",
        "tests/SMOKE-CHECKLIST.md": """# Spark Sprint Smoke Checklist

This is a manual checklist for the optional runnable Godot version. CI validates the static example shape and skips runtime loading when Godot is not installed.

- Launch: main scene opens without script errors.
- Movement: arrow/WASD bindings move the player in four directions.
- Success path: collecting 5 sparks sets state to `won`.
- Timeout path: timer reaching zero sets state to `lost`.
- Reset path: pressing R returns score to 0, timer to 30, and state to `playing`.
""",
        "WALKTHROUGH.md": """# Spark Sprint Workflow Walkthrough

Use this walkthrough to test the v1.2 example project with Codex Game Studios.

## `$cgs-start`

Expected result:
- Detects an already structured Codex Game Studios project.
- Finds `production/stage.txt` and `production/review-mode.txt`.
- Does not overwrite existing design, architecture, epic, or story files.

## `$cgs-project-stage-detect`

Expected result:
- Reports `PRODUCTION`.
- Detects Godot 4.3 / GDScript style from `project.godot` and technical preferences.
- Lists evidence paths for concept, systems index, architecture, epic, story, source, and tests.

## `$cgs-dev-story production/epics/core-loop/STORY-001-player-loop.md`

Expected result:
- Reads one story and the linked architecture/design context.
- Identifies existing source, scene, and test drafts.
- Proposes scoped edits only if the user asks to continue implementation.

## `$cgs-smoke-check`

Expected result:
- Runs static validation when operating from the repository root.
- Runs `python tools\\validate_godot_example.py`; this loads the scene when Godot is installed and reports `SKIP` otherwise.

## `$cgs-story-done production/epics/core-loop/STORY-001-player-loop.md`

Expected result:
- Returns `DONE` for static evidence if source, scene, tests, and smoke checklist satisfy the story.
- Calls out runtime playtest evidence as optional when Godot is unavailable.

## `$cgs-code-review`

Expected result:
- Reviews the source/test drafts with findings-first output.
- Checks that `scenes/main.tscn` exists and references the runtime scripts.
- Mentions whether optional Godot loading was run or skipped.

## `$cgs-qa-plan`

Expected result:
- Produces a scoped QA matrix for movement, pickup, timer, reset, HUD, and runtime playtest evidence.
""",
    }

    for relative, content in files.items():
        write_text(EXAMPLE / relative, content)

    write_text(
        ROOT / "docs" / "examples" / "spark-sprint.md",
        """# Spark Sprint Example Transcript

This document links the Spark Sprint example project to the Codex Game Studios workflow loop. It is statically validated by default and optionally runnable in Godot 4.x.

Example path:

```text
examples/spark-sprint/
```

Realistic Codex run transcript:

```text
docs/transcripts/spark-sprint-codex-run.md
```

Suggested prompt sequence:

```text
Use $cgs-start on examples/spark-sprint.
Use $cgs-project-stage-detect on examples/spark-sprint.
Use $cgs-dev-story examples/spark-sprint/production/epics/core-loop/STORY-001-player-loop.md.
Use $cgs-smoke-check for examples/spark-sprint.
Use $cgs-story-done examples/spark-sprint/production/epics/core-loop/STORY-001-player-loop.md.
Use $cgs-code-review on the Spark Sprint source draft.
Use $cgs-qa-plan for the Spark Sprint Core Loop epic.
```

Expected behavior:

- Codex should treat the project as a Godot 4.3 / GDScript optional runnable example.
- Codex should not require Godot to be installed for repository validation.
- `python tools\\validate_godot_example.py` should report `SKIP` when Godot is unavailable and try to load `scenes/main.tscn` when Godot is available.
- Codex should cite evidence paths before proposing edits.
- Runtime playtest evidence should be listed as optional manual follow-up.
""",
    )


def write_v1_readiness_docs() -> None:
    write_text(
        ROOT / "docs" / "v1-readiness" / "freeze-checklist.md",
        """# v1 Readiness Freeze Checklist

This checklist defines the Codex Game Studios v1.x compatibility boundary. It is a release gate, not a roadmap wish list, and v1.1 adds Windows and macOS usability checks.

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
- Windows and macOS platform docs: `docs/platforms/windows.md`, `docs/platforms/macos.md`

## Documentation Audit

Before a v1.x release, check these user-facing surfaces:

- `README.md`: quick start, fallback path, validation commands, examples, release list.
- `AGENTS.md`: operating contract, validation checklist, role-card policy.
- `docs/CODEX-MIGRATION-GUIDE.md`: migration direction and naming policy.
- `docs/install/local-plugin.md`: discovery files and fallback prompts.
- `docs/install/field-test-2026-05-22.md`: current local plugin discovery field note.
- `docs/hooks/runtime-hook-evaluation.md`: no-runtime-hooks decision and future adoption gate.
- `docs/transcripts/concept-to-story.md`: concept-to-story demonstration.
- `docs/transcripts/spark-sprint-codex-run.md`: realistic Spark Sprint Codex run.
- `docs/examples/spark-sprint.md`: example prompt sequence.
- `docs/getting-started/first-run.md`: Windows and macOS first-run guide.
- `docs/platforms/windows.md`: Windows setup and troubleshooting.
- `docs/platforms/macos.md`: macOS setup and troubleshooting.
- `docs/releases/`: release notes from `v0.1.0` through the current release.

## Validation Gate

Run from the repository root:

Windows PowerShell:

```powershell
python tools\\run_all_validators.py
```

macOS zsh or bash:

```bash
python3 tools/run_all_validators.py
python tools/run_all_validators.py
```

Release maintainers can also run the expanded sequence:

```text
python tools\\migrate_from_claude.py
python tools\\prepare_v01.py
python tools\\validate_cgs.py
python tools\\validate_skills.py
python tools\\validate_smoke_fixture.py
python tools\\validate_transcripts.py
python tools\\validate_plugin_install_docs.py
python tools\\validate_hook_policy.py
python tools\\validate_examples.py
python tools\\validate_godot_example.py
python tools\\validate_workflow_polish.py
python tools\\validate_v1_readiness.py
python tools\\validate_cross_platform.py
python tools\\scan_legacy_tokens.py
python -m json.tool plugins\\codex-game-studios\\.codex-plugin\\plugin.json
python -m json.tool .agents\\plugins\\marketplace.json
```

GitHub Actions must run the same structural validators on Windows, macOS, and Linux, including `tools/validate_v1_readiness.py` and `tools/validate_cross_platform.py`.

## Fresh Clone Gate

Before publishing a v1.x release:

1. Clone `https://github.com/DocJlm/Codex-Game-Studios.git` into a temporary directory.
2. Run `python tools\\run_all_validators.py` on Windows or `python3 tools/run_all_validators.py` on macOS.
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
- README, install docs, migration guide, release notes, validators, manifest, marketplace entry, and examples agree on the same public interfaces.
""",
    )


def write_platform_docs() -> None:
    write_text(
        ROOT / "docs" / "platforms" / "windows.md",
        """# Windows Usage

Codex Game Studios supports Windows as a first-class local development platform.

## Requirements

- Python 3.11 or newer on `PATH`.
- Git for cloning and status checks.
- Codex desktop or another Codex environment opened at the cloned repository root.
- Godot, Unity, or Unreal are optional. The included validators do not require a game engine.

## Validate The Repository

From PowerShell in the repository root:

```powershell
python tools\\run_all_validators.py
```

For release-maintainer checks that regenerate curated docs and metadata:

```powershell
python tools\\migrate_from_claude.py
python tools\\prepare_v01.py
python tools\\run_all_validators.py
```

## Use The Plugin

Preferred path:

```text
Use $cgs-start to set up a new game project.
Use $cgs-project-stage-detect on this existing game.
Use $cgs-dev-story to implement the next story.
```

Fallback path when repo-local plugin discovery is unavailable:

```text
Use the skill at plugins/codex-game-studios/skills/cgs-start/SKILL.md to set up this project.
Use the skill at plugins/codex-game-studios/skills/cgs-project-stage-detect/SKILL.md to audit this project.
Use the skill at plugins/codex-game-studios/skills/cgs-dev-story/SKILL.md for production/epics/core-loop/STORY-001-player-loop.md.
```

## Notes

- If PowerShell renders Chinese text incorrectly, the Markdown files are still UTF-8. View them in Codex, VS Code, GitHub, or another UTF-8-aware editor.
- Use the cloned repository root as the workspace. Do not depend on a machine-specific absolute path.
- Backslash examples are for PowerShell. Forward-slash paths in prompts also work because Codex reads repository files, not shell paths.
- If Godot 4.x is installed, `python tools\\validate_godot_example.py` attempts to load `examples/spark-sprint/scenes/main.tscn`; otherwise it reports `SKIP`.
""",
    )

    write_text(
        ROOT / "docs" / "platforms" / "macos.md",
        """# macOS Usage

Codex Game Studios supports macOS through zsh or bash plus the same repo-local plugin and path fallback model.

## Requirements

- Python 3.11 or newer, usually available as `python3`.
- Git for cloning and status checks.
- Codex desktop or another Codex environment opened at the cloned repository root.
- Godot, Unity, or Unreal are optional. The included validators do not require a game engine.

## Validate The Repository

From zsh or bash in the repository root:

```bash
python3 tools/run_all_validators.py
```

If your Python command is named `python`, this is also fine:

```bash
python tools/run_all_validators.py
```

For release-maintainer checks that regenerate curated docs and metadata:

```bash
python3 tools/migrate_from_claude.py
python3 tools/prepare_v01.py
python3 tools/run_all_validators.py
```

## Use The Plugin

Preferred path:

```text
Use $cgs-start to set up a new game project.
Use $cgs-project-stage-detect on this existing game.
Use $cgs-dev-story to implement the next story.
```

Fallback path when repo-local plugin discovery is unavailable:

```text
Use the skill at plugins/codex-game-studios/skills/cgs-start/SKILL.md to set up this project.
Use the skill at plugins/codex-game-studios/skills/cgs-project-stage-detect/SKILL.md to audit this project.
Use the skill at plugins/codex-game-studios/skills/cgs-dev-story/SKILL.md for production/epics/core-loop/STORY-001-player-loop.md.
```

## Notes

- Use forward-slash repository paths in shell commands and prompts.
- The repo-local marketplace entry is `.agents/plugins/marketplace.json`.
- If the Codex build does not expose repo-local plugin installation, use the path-based fallback prompts above.
- If Godot 4.x is installed, `python3 tools/validate_godot_example.py` attempts to load `examples/spark-sprint/scenes/main.tscn`; otherwise it reports `SKIP`.
""",
    )

    write_text(
        ROOT / "docs" / "getting-started" / "first-run.md",
        """# First Run Guide

This guide is the shortest path from a fresh clone to a useful Codex Game Studios session on Windows or macOS.

## 1. Open The Repository

Clone the repository and open the cloned root in Codex.

Windows PowerShell validation:

```powershell
python tools\\run_all_validators.py
```

macOS zsh or bash validation:

```bash
python3 tools/run_all_validators.py
```

## 2. Try The Plugin Name

If repo-local plugin discovery is available in your Codex build, start with:

```text
Use $cgs-start to set up a new game project.
Use $cgs-project-stage-detect on this existing game.
Use $cgs-dev-story to implement the next story.
```

## 3. Use The Fallback Path

If `$cgs-start` is not recognized as an installed skill, use the same workflow by path:

```text
Use the skill at plugins/codex-game-studios/skills/cgs-start/SKILL.md to set up this project.
Use the skill at plugins/codex-game-studios/skills/cgs-project-stage-detect/SKILL.md to audit this project.
Use the skill at plugins/codex-game-studios/skills/cgs-dev-story/SKILL.md for production/epics/core-loop/STORY-001-player-loop.md.
```

## 4. Pick A Starting Scenario

New game:

```text
Use $cgs-start. I want to create a small game from scratch.
```

Existing project:

```text
Use $cgs-project-stage-detect and tell me the current phase, evidence paths, and next 3 actions.
```

Story implementation:

```text
Use $cgs-dev-story production/epics/core-loop/STORY-001-player-loop.md. Inspect first, then implement only the story scope.
```

## 5. Platform References

- Windows: `docs/platforms/windows.md`
- macOS: `docs/platforms/macos.md`
- Plugin install and fallback behavior: `docs/install/local-plugin.md`

## Optional Spark Sprint Runtime Check

Spark Sprint validates without Godot, but if Godot 4.x is installed you can also try:

```text
Open examples/spark-sprint/project.godot and run scenes/main.tscn.
```

or run:

```bash
python tools/validate_godot_example.py
```
""",
    )


def main() -> None:
    write_core_skills()
    update_plugin_metadata()
    write_fixture()
    write_transcripts()
    write_workflow_polish_docs()
    write_install_docs()
    write_hook_policy_docs()
    write_example_project()
    write_v1_readiness_docs()
    write_platform_docs()
    print(f"Prepared v{RELEASE_VERSION} curated skills, plugin metadata, and empty-game fixture")


if __name__ == "__main__":
    main()
