#!/usr/bin/env python3
"""Validate static example projects."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples" / "spark-sprint"
DOC = ROOT / "docs" / "examples" / "spark-sprint.md"

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "project.godot",
    "production/stage.txt",
    "production/review-mode.txt",
    "docs/architecture/technical-preferences.md",
    "design/gdd/game-concept.md",
    "design/gdd/systems-index.md",
    "design/gdd/core-loop.md",
    "docs/architecture/architecture.md",
    "docs/architecture/control-manifest.md",
    "production/epics/core-loop/EPIC.md",
    "production/epics/core-loop/STORY-001-player-loop.md",
    "src/gameplay/game_controller.gd",
    "src/gameplay/player_controller.gd",
    "src/gameplay/collectible.gd",
    "src/ui/hud.gd",
    "tests/test_game_controller.gd",
    "tests/SMOKE-CHECKLIST.md",
    "WALKTHROUGH.md",
]

REQUIRED_SKILLS = [
    "$cgs-start",
    "$cgs-project-stage-detect",
    "$cgs-dev-story",
    "$cgs-smoke-check",
    "$cgs-story-done",
    "$cgs-code-review",
    "$cgs-qa-plan",
]

SOURCE_TOKENS = {
    "src/gameplay/game_controller.gd": [
        "class_name GameController",
        "func collect_spark()",
        "func tick_timer(delta: float)",
        "func reset_round()",
    ],
    "src/gameplay/player_controller.gd": ["class_name PlayerController", "move_and_slide()"],
    "src/gameplay/collectible.gd": ["class_name Collectible", "collect_spark"],
    "src/ui/hud.gd": ["class_name Hud", "update_score", "update_timer", "update_state"],
}

TEST_TOKENS = [
    "test_collect_spark_increments_score",
    "test_target_score_wins_round",
    "test_timer_timeout_loses_round",
    "test_reset_restores_initial_values",
]

LEGACY_TOKENS = [
    ".claude/",
    "CLAUDE.md",
    "AskUserQuestion",
    "allowed-tools",
    "argument-hint",
    "user-invocable",
]


def read(relative: str, errors: list[str]) -> str:
    path = EXAMPLE / relative
    if not path.exists():
        errors.append(f"missing example file: {relative}")
        return ""
    return path.read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        read(relative, errors)

    if not DOC.exists():
        errors.append(f"missing docs example file: {DOC.relative_to(ROOT).as_posix()}")
        doc_text = ""
    else:
        doc_text = DOC.read_text(encoding="utf-8")

    technical = read("docs/architecture/technical-preferences.md", errors)
    for token in ["Godot 4.3", "GDScript", "validate_examples.py"]:
        if token not in technical:
            errors.append(f"technical preferences missing token: {token}")

    story = read("production/epics/core-loop/STORY-001-player-loop.md", errors)
    for token in ["Status: Review", "Acceptance Criteria", "Implementation Notes", "Evidence"]:
        if token not in story:
            errors.append(f"story missing token: {token}")

    walkthrough = read("WALKTHROUGH.md", errors)
    for skill in REQUIRED_SKILLS:
        if skill not in walkthrough:
            errors.append(f"walkthrough missing {skill}")
        if skill not in doc_text:
            errors.append(f"docs example missing {skill}")

    if "docs/transcripts/spark-sprint-codex-run.md" not in doc_text:
        errors.append("docs example missing Spark Sprint transcript link")

    for relative, tokens in SOURCE_TOKENS.items():
        text = read(relative, errors)
        for token in tokens:
            if token not in text:
                errors.append(f"{relative} missing token: {token}")

    tests = read("tests/test_game_controller.gd", errors)
    for token in TEST_TOKENS:
        if token not in tests:
            errors.append(f"tests/test_game_controller.gd missing token: {token}")

    smoke = read("tests/SMOKE-CHECKLIST.md", errors)
    for token in ["Launch", "Movement", "Success path", "Timeout path", "Reset path"]:
        if token not in smoke:
            errors.append(f"smoke checklist missing token: {token}")

    for path in [*EXAMPLE.rglob("*"), DOC]:
        if not path.is_file() or path.suffix.lower() not in {".md", ".gd", ".godot", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for token in LEGACY_TOKENS:
            if token in text:
                errors.append(f"{path.relative_to(ROOT).as_posix()} contains legacy token {token!r}")
                break

    if errors:
        print("Example validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Example validation passed")
    print(f"- example: {EXAMPLE.relative_to(ROOT).as_posix()}")
    print(f"- docs: {DOC.relative_to(ROOT).as_posix()}")
    print(f"- required files: {len(REQUIRED_FILES)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
