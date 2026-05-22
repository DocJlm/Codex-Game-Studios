#!/usr/bin/env python3
"""Validate the v1 readiness freeze checklist."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "v1-readiness" / "freeze-checklist.md"
README = ROOT / "README.md"
AGENTS = ROOT / "AGENTS.md"
WORKFLOW = ROOT / ".github" / "workflows" / "validate.yml"
PLUGIN = ROOT / "plugins" / "codex-game-studios" / ".codex-plugin" / "plugin.json"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"

REQUIRED_DOC_TOKENS = [
    "# v1 Readiness Freeze Checklist",
    "Frozen Public Interfaces",
    "Skill names stay stable: 73 skills",
    "Canonical skill prefix stays `cgs-`",
    "Plugin manifest keeps `name: codex-game-studios` and `skills: ./skills/`",
    "Marketplace entry continues to point at `./plugins/codex-game-studios`",
    "Role cards are not automatic subagents",
    "Runtime hooks remain disabled by default",
    "Validation Gate",
    "Fresh Clone Gate",
    "Compatibility Policy",
    "v1.0.0 Release Decision",
    "python tools\\validate_v1_readiness.py",
]

REQUIRED_REPO_TOKENS = [
    "docs/v1-readiness/freeze-checklist.md",
    "tools\\validate_v1_readiness.py",
]

LEGACY_RUNTIME_TOKENS = [
    ".claude/",
    "CLAUDE.md",
    "AskUserQuestion",
    "allowed-tools",
    "argument-hint",
    "user-invocable",
]


def read(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f"missing file: {path.relative_to(ROOT).as_posix()}")
        return ""
    return path.read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []

    doc = read(DOC, errors)
    readme = read(README, errors)
    agents = read(AGENTS, errors)
    workflow = read(WORKFLOW, errors)

    for token in REQUIRED_DOC_TOKENS:
        if token not in doc:
            errors.append(f"v1 checklist missing token: {token}")

    for token in REQUIRED_REPO_TOKENS:
        if token not in readme:
            errors.append(f"README missing v1 token: {token}")
        if token not in agents:
            errors.append(f"AGENTS.md missing v1 token: {token}")

    if "python tools/validate_v1_readiness.py" not in workflow:
        errors.append("GitHub Actions workflow missing v1 readiness validator")

    for token in LEGACY_RUNTIME_TOKENS:
        if token in doc:
            errors.append(f"v1 checklist contains legacy runtime token: {token}")

    try:
        plugin = json.loads(PLUGIN.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - error path reports exact issue
        errors.append(f"plugin.json is not valid JSON: {exc}")
        plugin = {}

    if plugin.get("version") != "1.0.0":
        errors.append("plugin.json version must be 1.0.0 for v1 readiness")
    if plugin.get("name") != "codex-game-studios":
        errors.append("plugin.json name must remain codex-game-studios")
    if plugin.get("skills") != "./skills/":
        errors.append("plugin.json skills path must remain ./skills/")
    if "hooks" in plugin:
        errors.append("plugin.json must not declare runtime hooks for v1")

    try:
        marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover
        errors.append(f"marketplace.json is not valid JSON: {exc}")
        marketplace = []

    marketplace_text = json.dumps(marketplace)
    if "./plugins/codex-game-studios" not in marketplace_text:
        errors.append("marketplace entry must keep ./plugins/codex-game-studios")

    if errors:
        print("v1 readiness validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("v1 readiness validation passed")
    print(f"- checklist: {DOC.relative_to(ROOT).as_posix()}")
    print("- frozen version: 1.0.0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
