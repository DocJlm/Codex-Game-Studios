#!/usr/bin/env python3
"""Repo-local quick validator for Codex Game Studios skills.

This intentionally mirrors the small subset of Codex skill validation this repo
needs, so CI and fresh clones do not depend on a developer's local ~/.codex
installation.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "plugins" / "codex-game-studios" / "skills"
EXPECTED_SKILLS = 73

LEGACY_TOKENS = [
    ".claude/",
    "CLAUDE.md",
    "AskUserQuestion",
    "allowed-tools",
    "argument-hint",
    "user-invocable",
]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def parse_frontmatter(path: Path, errors: list[str]) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{rel(path)}: missing YAML frontmatter")
        return {}, text

    end = text.find("\n---\n", 4)
    if end == -1:
        errors.append(f"{rel(path)}: unterminated YAML frontmatter")
        return {}, text

    raw = text[4:end].splitlines()
    body = text[end + 5 :].lstrip()
    data: dict[str, str] = {}
    for line in raw:
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"{rel(path)}: invalid frontmatter line {line!r}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if key in data:
            errors.append(f"{rel(path)}: duplicate frontmatter key {key!r}")
        if len(value) >= 2 and value[0] == value[-1] == '"':
            value = value[1:-1]
        data[key] = value
    return data, body


def validate_skill(path: Path, errors: list[str]) -> None:
    data, body = parse_frontmatter(path, errors)
    folder_name = path.parent.name
    original = folder_name.removeprefix("cgs-")

    if set(data) != {"name", "description"}:
        errors.append(f"{rel(path)}: frontmatter must contain only name and description")

    if data.get("name") != folder_name:
        errors.append(f"{rel(path)}: frontmatter name must match folder {folder_name}")

    if not re.fullmatch(r"cgs-[a-z0-9-]{1,60}", folder_name):
        errors.append(f"{rel(path)}: skill folder must be cgs-* lowercase hyphen-case")

    description = data.get("description", "")
    if not description:
        errors.append(f"{rel(path)}: description is empty")
    if len(description) > 700:
        errors.append(f"{rel(path)}: description is too long ({len(description)} chars)")
    if "\n" in description or "\r" in description:
        errors.append(f"{rel(path)}: description must be a single line")
    if f"/{original}" not in description or f"$cgs-{original}" not in description:
        errors.append(f"{rel(path)}: description must mention /{original} and $cgs-{original}")

    if not body:
        errors.append(f"{rel(path)}: body is empty")
    if not body.startswith("# "):
        errors.append(f"{rel(path)}: body must start with a markdown H1")

    text = path.read_text(encoding="utf-8", errors="ignore")
    for token in LEGACY_TOKENS:
        if token in text:
            errors.append(f"{rel(path)}: contains legacy runtime token {token!r}")
            break


def main() -> int:
    errors: list[str] = []

    skill_files = sorted(SKILLS.glob("cgs-*/SKILL.md"))
    if len(skill_files) != EXPECTED_SKILLS:
        errors.append(f"expected {EXPECTED_SKILLS} skills, found {len(skill_files)}")

    folders = sorted(path for path in SKILLS.glob("cgs-*") if path.is_dir())
    missing = [folder for folder in folders if not (folder / "SKILL.md").exists()]
    for folder in missing:
        errors.append(f"{rel(folder)}: missing SKILL.md")

    for path in skill_files:
        validate_skill(path, errors)

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Skill validation passed")
    print(f"- skills: {len(skill_files)}")
    print("- frontmatter: name + description")
    print("- legacy runtime tokens: none")
    return 0


if __name__ == "__main__":
    sys.exit(main())
