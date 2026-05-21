#!/usr/bin/env python3
"""Prepare the v0.1 Codex-native workflow layer."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "codex-game-studios"
SKILLS = PLUGIN / "skills"
FIXTURE = ROOT / "tests" / "fixtures" / "empty-game"


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
}


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def write_core_skills() -> None:
    for name, (summary, body) in CORE_SKILLS.items():
        skill_name = f"cgs-{name}"
        description = (
            f"Codex Game Studios core workflow adapted from original /{name}. "
            f"Use when the user asks for /{name}, ${skill_name}, or {summary}"
        )
        content = f"---\nname: {skill_name}\ndescription: \"{description}\"\n---\n\n{body.strip()}\n"
        write_text(SKILLS / skill_name / "SKILL.md", content)


def update_plugin_metadata() -> None:
    path = PLUGIN / ".codex-plugin" / "plugin.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["version"] = "0.1.0"
    data["author"] = {
        "name": "DocJlm",
        "email": "1952199902@qq.com",
        "url": "https://github.com/DocJlm",
    }
    data["homepage"] = "https://github.com/DocJlm/Codex-Game-Studios"
    data["repository"] = "https://github.com/DocJlm/Codex-Game-Studios"
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


def main() -> None:
    write_core_skills()
    update_plugin_metadata()
    write_fixture()
    print("Prepared v0.1 core skills, plugin metadata, and empty-game fixture")


if __name__ == "__main__":
    main()
