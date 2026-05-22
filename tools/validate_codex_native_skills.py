#!/usr/bin/env python3
"""Validate Codex-native skill migration markers and role-card review language."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "plugins" / "codex-game-studios" / "skills"

EXPECTED_CODEX_OPERATING_NOTES = 50

BANNED_TOKENS = [
    "Migration phase: Full migration",
    "$ARGUMENTS",
    "Task tool",
    "subagent_type",
    "subagent",
    "sub-agent",
    "SUBAGENT",
    "parallel Task",
    "Task agents",
    "role-card review_type",
    "ask the user directly or use available Codex UI question tools",
]

REQUIRED_NOTE_TOKENS = [
    "## Codex Operating Notes",
    "Codex-native version",
    "Inspect repository state before asking questions",
    "role card",
    "Run role-card reviews sequentially by default",
    "parallel agent work only when the user explicitly requests it",
    "hidden runtime hooks",
]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def main() -> int:
    errors: list[str] = []
    note_count = 0

    for path in sorted(SKILLS.glob("cgs-*/SKILL.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for token in BANNED_TOKENS:
            if token in text:
                errors.append(f"{rel(path)} contains non-Codex-native token: {token}")
        if "## Codex Operating Notes" in text:
            note_count += 1
            for token in REQUIRED_NOTE_TOKENS:
                if token not in text:
                    errors.append(f"{rel(path)} Codex Operating Notes missing token: {token}")

    if note_count != EXPECTED_CODEX_OPERATING_NOTES:
        errors.append(
            f"expected {EXPECTED_CODEX_OPERATING_NOTES} Codex Operating Notes sections, found {note_count}"
        )

    if errors:
        print("Codex-native skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Codex-native skill validation passed")
    print(f"- Codex Operating Notes sections: {note_count}")
    print("- legacy full-migration markers: none")
    print("- Claude subagent runtime tokens: none")
    return 0


if __name__ == "__main__":
    sys.exit(main())
