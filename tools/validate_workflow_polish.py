#!/usr/bin/env python3
"""Validate v0.7 second-batch workflow polish."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "plugins" / "codex-game-studios" / "skills"
DOC = ROOT / "docs" / "workflows" / "production-readiness-workflows.md"

WORKFLOWS = {
    "cgs-story-readiness": ["READY", "NEEDS WORK", "BLOCKED", "Readiness Rules", "recommended next skill"],
    "cgs-scope-check": ["PASS", "CONCERNS", "FAIL", "Verdict Rules", "baseline evidence"],
    "cgs-test-evidence-review": ["ADEQUATE", "INCOMPLETE", "MISSING", "criterion coverage", "$cgs-smoke-check"],
    "cgs-regression-suite": ["report", "audit", "update", "OK", "GAPS", "STALE"],
    "cgs-release-checklist": ["READY WITH RISKS", "NOT READY", "go-no-go", "$cgs-gate-check"],
}

LEGACY_MARKERS = [
    "# CGS:",
    "Migration phase: Full migration",
    "$ARGUMENTS",
    "ask the user directly or use available Codex UI question tools",
]


def main() -> int:
    errors: list[str] = []

    if not DOC.exists():
        errors.append(f"missing workflow doc: {DOC.relative_to(ROOT).as_posix()}")
        doc_text = ""
    else:
        doc_text = DOC.read_text(encoding="utf-8")

    for skill_name, required_tokens in WORKFLOWS.items():
        path = SKILLS / skill_name / "SKILL.md"
        if not path.exists():
            errors.append(f"missing skill: {skill_name}")
            continue
        text = path.read_text(encoding="utf-8")
        original = skill_name.removeprefix("cgs-")
        if f"name: {skill_name}" not in text:
            errors.append(f"{skill_name} missing matching frontmatter name")
        if f"/{original}" not in text or f"${skill_name}" not in text:
            errors.append(f"{skill_name} description must mention /{original} and ${skill_name}")
        for marker in LEGACY_MARKERS:
            if marker in text:
                errors.append(f"{skill_name} still contains legacy migration marker: {marker}")
        for token in required_tokens:
            if token not in text:
                errors.append(f"{skill_name} missing token: {token}")
        if skill_name not in doc_text:
            errors.append(f"workflow doc missing {skill_name}")

    for token in ["story readiness", "scope control", "evidence review", "regression coverage", "release readiness"]:
        if token not in doc_text.lower():
            errors.append(f"workflow doc missing theme: {token}")

    if errors:
        print("Workflow polish validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Workflow polish validation passed")
    print(f"- workflows: {len(WORKFLOWS)}")
    print(f"- doc: {DOC.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
