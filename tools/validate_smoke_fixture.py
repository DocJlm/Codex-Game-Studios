#!/usr/bin/env python3
"""Validate the empty-game smoke fixture for workflow smoke checks."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "empty-game"

REQUIRED_FILES = [
    "README.md",
    "WALKTHROUGH.md",
    "AGENTS.md",
    "production/stage.txt",
    "production/review-mode.txt",
    "docs/architecture/technical-preferences.md",
    "design/gdd/game-concept.md",
    "design/gdd/systems-index.md",
    "docs/architecture/architecture.md",
    "docs/architecture/control-manifest.md",
    "production/epics/core-loop/EPIC.md",
    "production/epics/core-loop/STORY-001-player-loop.md",
    "tests/SMOKE-CHECKLIST.md",
]

EXPECTED_SKILLS = ["$cgs-start", "$cgs-project-stage-detect", "$cgs-dev-story", "$cgs-story-done"]


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        path = FIXTURE / relative
        if not path.exists():
            errors.append(f"missing fixture file: {relative}")

    story = FIXTURE / "production/epics/core-loop/STORY-001-player-loop.md"
    if story.exists():
        text = story.read_text(encoding="utf-8")
        for token in ["Status: Ready", "Acceptance Criteria", "Test Plan"]:
            if token not in text:
                errors.append(f"story missing token: {token}")

    checklist = FIXTURE / "tests/SMOKE-CHECKLIST.md"
    if checklist.exists():
        text = checklist.read_text(encoding="utf-8")
        for skill in EXPECTED_SKILLS:
            if skill not in text:
                errors.append(f"smoke checklist missing {skill}")

    walkthrough = FIXTURE / "WALKTHROUGH.md"
    if walkthrough.exists():
        text = walkthrough.read_text(encoding="utf-8")
        for skill in EXPECTED_SKILLS:
            if skill not in text:
                errors.append(f"walkthrough missing {skill}")
        for token in ["Expected result", "PRODUCTION", "NEEDS FIXES"]:
            if token not in text:
                errors.append(f"walkthrough missing token: {token}")

    if errors:
        print("Smoke fixture validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Smoke fixture validation passed")
    print(f"- fixture: {FIXTURE}")
    print(f"- required files: {len(REQUIRED_FILES)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
