#!/usr/bin/env python3
"""Validate demo transcript and workflow documentation."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

TRANSCRIPT = ROOT / "docs" / "transcripts" / "concept-to-story.md"
SPARK_SPRINT_TRANSCRIPT = ROOT / "docs" / "transcripts" / "spark-sprint-codex-run.md"
WORKFLOW_NOTES = ROOT / "docs" / "workflows" / "high-frequency-workflows.md"

REQUIRED_SKILLS = [
    "$cgs-start",
    "$cgs-setup-engine",
    "$cgs-map-systems",
    "$cgs-create-architecture",
    "$cgs-create-epics",
    "$cgs-create-stories",
    "$cgs-dev-story",
    "$cgs-story-done",
    "$cgs-code-review",
    "$cgs-qa-plan",
]

LEGACY_TOKENS = [
    ".claude/",
    "CLAUDE.md",
    "AskUserQuestion",
    "allowed-tools",
    "argument-hint",
    "user-invocable",
]


def check_file(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f"missing doc: {path.relative_to(ROOT).as_posix()}")
        return ""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("# "):
        errors.append(f"{path.relative_to(ROOT).as_posix()} must start with an H1")
    for token in LEGACY_TOKENS:
        if token in text:
            errors.append(f"{path.relative_to(ROOT).as_posix()} contains legacy token {token!r}")
    return text


def main() -> int:
    errors: list[str] = []
    transcript = check_file(TRANSCRIPT, errors)
    spark_sprint = check_file(SPARK_SPRINT_TRANSCRIPT, errors)
    notes = check_file(WORKFLOW_NOTES, errors)

    for skill in REQUIRED_SKILLS:
        if skill not in transcript:
            errors.append(f"transcript missing {skill}")

    for token in ["Expected Codex shape", "Files updated", "Verdict", "Evidence"]:
        if token not in transcript:
            errors.append(f"transcript missing token: {token}")

    for skill in [
        "$cgs-start",
        "$cgs-project-stage-detect",
        "$cgs-dev-story",
        "$cgs-smoke-check",
        "$cgs-story-done",
        "$cgs-code-review",
        "$cgs-qa-plan",
    ]:
        if skill not in spark_sprint:
            errors.append(f"spark sprint transcript missing {skill}")

    for token in [
        "examples/spark-sprint/",
        "Verdict: PRODUCTION",
        "Files updated: none",
        "python tools\\validate_examples.py",
        "Manual checks remaining",
        "No Godot runtime test was executed",
        "Final State",
    ]:
        if token not in spark_sprint:
            errors.append(f"spark sprint transcript missing token: {token}")

    for skill in ["$cgs-code-review", "$cgs-qa-plan", "$cgs-smoke-check"]:
        if skill not in notes:
            errors.append(f"workflow notes missing {skill}")

    if errors:
        print("Transcript validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Transcript validation passed")
    print(f"- transcript: {TRANSCRIPT.relative_to(ROOT).as_posix()}")
    print(f"- spark sprint transcript: {SPARK_SPRINT_TRANSCRIPT.relative_to(ROOT).as_posix()}")
    print(f"- workflow notes: {WORKFLOW_NOTES.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
