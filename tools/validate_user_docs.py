#!/usr/bin/env python3
"""Validate user-facing setup, upgrade, CI, and community docs."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

README = ROOT / "README.md"
QUICK_START = ROOT / "docs" / "getting-started" / "quick-start.md"
FIRST_RUN = ROOT / "docs" / "getting-started" / "first-run.md"
CODEX_DESKTOP = ROOT / "docs" / "install" / "codex-desktop.md"
LOCAL_PLUGIN = ROOT / "docs" / "install" / "local-plugin.md"
UPGRADE = ROOT / "docs" / "install" / "upgrade.md"
WINDOWS = ROOT / "docs" / "platforms" / "windows.md"
MACOS = ROOT / "docs" / "platforms" / "macos.md"
CI = ROOT / "docs" / "platforms" / "ci.md"
CONTRIBUTING = ROOT / "docs" / "community" / "contributing.md"
V1 = ROOT / "docs" / "v1-readiness" / "freeze-checklist.md"
RELEASE = ROOT / "docs" / "releases" / "v1.6.0.md"

DOC_TOKENS = {
    README: [
        "docs/getting-started/quick-start.md",
        "docs/install/codex-desktop.md",
        "docs/install/upgrade.md",
        "docs/platforms/ci.md",
        "docs/community/contributing.md",
        "tools/validate_user_docs.py",
        "docs/releases/v1.6.0.md",
    ],
    QUICK_START: [
        "# Quick Start",
        "Codex Desktop",
        "repo-local plugin",
        "path-based fallback",
        "python tools\\run_all_validators.py",
        "python3 tools/run_all_validators.py",
        "$cgs-start",
        "plugins/codex-game-studios/skills/cgs-start/SKILL.md",
        "docs/install/codex-desktop.md",
    ],
    FIRST_RUN: [
        "docs/getting-started/quick-start.md",
        "docs/install/codex-desktop.md",
        "docs/install/upgrade.md",
        "docs/platforms/ci.md",
    ],
    CODEX_DESKTOP: [
        "# Codex Desktop Setup",
        ".agents/plugins/marketplace.json",
        "plugins/codex-game-studios/.codex-plugin/plugin.json",
        "plugins/codex-game-studios/skills/",
        "$cgs-help",
        "Path-Based Fallback",
        "runtime hooks",
    ],
    LOCAL_PLUGIN: [
        "docs/install/codex-desktop.md",
        "docs/install/upgrade.md",
        "Upgrade Path",
    ],
    UPGRADE: [
        "# Upgrade Guide",
        "git status --short",
        "git pull --ff-only origin main",
        "git fetch --tags origin",
        "python tools\\run_all_validators.py",
        "python3 tools/run_all_validators.py",
        "Do not copy legacy runtime hooks",
    ],
    WINDOWS: [
        "# Windows Usage",
        "docs/platforms/ci.md",
        "docs/install/codex-desktop.md",
        "python tools\\run_all_validators.py",
    ],
    MACOS: [
        "# macOS Usage",
        "docs/platforms/ci.md",
        "docs/install/codex-desktop.md",
        "python3 tools/run_all_validators.py",
    ],
    CI: [
        "# CI Usage",
        ".github/workflows/validate.yml",
        "windows-latest",
        "macos-latest",
        "ubuntu-latest",
        "Python 3.12",
        "python tools/run_all_validators.py",
        "Avoid POSIX-only",
    ],
    CONTRIBUTING: [
        "# Contribution Guide",
        "AGENTS.md",
        "73 skills",
        "49 role cards",
        "11 path rules",
        "No runtime hooks",
        "tools/validate_user_docs.py",
        "python3 tools/run_all_validators.py",
    ],
    V1: [
        "docs/getting-started/quick-start.md",
        "docs/install/codex-desktop.md",
        "docs/install/upgrade.md",
        "docs/platforms/ci.md",
        "docs/community/contributing.md",
        "python tools\\validate_user_docs.py",
    ],
    RELEASE: [
        "# Codex Game Studios v1.6.0",
        "docs/install/codex-desktop.md",
        "docs/install/upgrade.md",
        "docs/platforms/ci.md",
        "docs/community/contributing.md",
        "tools/validate_user_docs.py",
    ],
}

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

    for path, tokens in DOC_TOKENS.items():
        text = read(path, errors)
        for token in tokens:
            if token not in text:
                errors.append(f"{path.relative_to(ROOT).as_posix()} missing token: {token}")
        for token in LEGACY_RUNTIME_TOKENS:
            if token in text:
                errors.append(f"{path.relative_to(ROOT).as_posix()} contains legacy runtime token: {token}")

    if errors:
        print("User documentation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("User documentation validation passed")
    print("- quick start: docs/getting-started/quick-start.md")
    print("- install docs: docs/install/codex-desktop.md, docs/install/upgrade.md")
    print("- platform docs: docs/platforms/ci.md")
    print("- community docs: docs/community/contributing.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
