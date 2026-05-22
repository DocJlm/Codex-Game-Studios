#!/usr/bin/env python3
"""Validate testing-framework paths are repo-local and resolvable."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FRAMEWORK = ROOT / "plugins" / "codex-game-studios" / "references" / "testing-framework"
CATALOG = FRAMEWORK / "catalog.yaml"
SKILL_TEST = ROOT / "plugins" / "codex-game-studios" / "skills" / "cgs-skill-test" / "SKILL.md"
SKILL_IMPROVE = ROOT / "plugins" / "codex-game-studios" / "skills" / "cgs-skill-improve" / "SKILL.md"

EXPECTED_PREFIX = "plugins/codex-game-studios/references/testing-framework/"
EXPECTED_SKILL_SPECS = 73
EXPECTED_AGENT_SPECS = 49

STALE_TOKENS = [
    "CCGS Skill Testing Framework/",
    "CCGS Skill Testing Framework\\",
    "references/testing-framework/CLAUDE.md",
]

TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".txt"}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f"missing file: {rel(path)}")
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def catalog_specs(text: str) -> list[str]:
    return re.findall(r"^\s*spec:\s*(\S.*)$", text, flags=re.MULTILINE)


def main() -> int:
    errors: list[str] = []

    if not (FRAMEWORK / "AGENTS.md").exists():
        errors.append("testing framework must use AGENTS.md")
    if (FRAMEWORK / "CLAUDE.md").exists():
        errors.append("testing framework must not keep CLAUDE.md")

    scan_roots = [
        FRAMEWORK,
        ROOT / "plugins" / "codex-game-studios" / "skills",
        ROOT / "docs",
    ]
    for root in scan_roots:
        for path in root.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for token in STALE_TOKENS:
                if token in text:
                    errors.append(f"{rel(path)} contains stale testing-framework path token: {token}")

    catalog = read(CATALOG, errors)
    specs = catalog_specs(catalog)
    skill_specs = [spec for spec in specs if f"{EXPECTED_PREFIX}skills/" in spec]
    agent_specs = [spec for spec in specs if f"{EXPECTED_PREFIX}agents/" in spec]

    if len(skill_specs) != EXPECTED_SKILL_SPECS:
        errors.append(f"expected {EXPECTED_SKILL_SPECS} skill spec paths, found {len(skill_specs)}")
    if len(agent_specs) != EXPECTED_AGENT_SPECS:
        errors.append(f"expected {EXPECTED_AGENT_SPECS} agent spec paths, found {len(agent_specs)}")

    for spec in specs:
        if not spec.startswith(EXPECTED_PREFIX):
            errors.append(f"catalog spec path must be repo-local: {spec}")
            continue
        target = ROOT / spec
        if not target.exists():
            errors.append(f"catalog spec path does not exist: {spec}")

    for path in [SKILL_TEST, SKILL_IMPROVE, FRAMEWORK / "AGENTS.md", FRAMEWORK / "README.md"]:
        text = read(path, errors)
        if EXPECTED_PREFIX not in text:
            errors.append(f"{rel(path)} must document repo-local testing-framework paths")

    skill_test_text = read(SKILL_TEST, errors)
    if "plugins/codex-game-studios/skills/cgs-[name]/SKILL.md" not in skill_test_text:
        errors.append("cgs-skill-test must document cgs-[name] skill paths")
    skill_improve_text = read(SKILL_IMPROVE, errors)
    if "plugins/codex-game-studios/skills/cgs-[name]/SKILL.md" not in skill_improve_text:
        errors.append("cgs-skill-improve must document cgs-[name] skill paths")

    if errors:
        print("Testing framework path validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Testing framework path validation passed")
    print(f"- skill spec paths: {len(skill_specs)}")
    print(f"- agent spec paths: {len(agent_specs)}")
    print("- instruction file: AGENTS.md")
    print("- stale upstream root paths: none")
    return 0


if __name__ == "__main__":
    sys.exit(main())
