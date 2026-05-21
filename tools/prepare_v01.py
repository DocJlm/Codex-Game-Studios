#!/usr/bin/env python3
"""Prepare curated Codex-native workflows for the current release."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "codex-game-studios"
SKILLS = PLUGIN / "skills"
FIXTURE = ROOT / "tests" / "fixtures" / "empty-game"
RELEASE_VERSION = "0.3.0"


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

1. Read the target story, its epic, linked GDDs, ADRs, and control manifest.
2. Check scope, acceptance criteria, dependencies, assets, testability, and missing decisions.
3. Do not edit implementation files.
4. If blocked, provide the smallest question or upstream doc change needed.

## Output Contract

Return verdict: `READY`, `NEEDS WORK`, or `BLOCKED`.
Include evidence and next action.
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


def main() -> None:
    write_core_skills()
    update_plugin_metadata()
    write_fixture()
    write_transcripts()
    print(f"Prepared v{RELEASE_VERSION} curated skills, plugin metadata, and empty-game fixture")


if __name__ == "__main__":
    main()
