#!/usr/bin/env python3
"""Validate Windows and macOS user-facing support docs and CI shape."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

README = ROOT / "README.md"
AGENTS = ROOT / "AGENTS.md"
LOCAL_PLUGIN = ROOT / "docs" / "install" / "local-plugin.md"
V1 = ROOT / "docs" / "v1-readiness" / "freeze-checklist.md"
WINDOWS = ROOT / "docs" / "platforms" / "windows.md"
MACOS = ROOT / "docs" / "platforms" / "macos.md"
GETTING_STARTED = ROOT / "docs" / "getting-started" / "first-run.md"
QUICK_START = ROOT / "docs" / "getting-started" / "quick-start.md"
CI = ROOT / "docs" / "platforms" / "ci.md"
WORKFLOW = ROOT / ".github" / "workflows" / "validate.yml"
RELEASE = ROOT / "docs" / "releases" / "v2.0.0.md"

DOCS_TO_SCAN_FOR_ABSOLUTE_WINDOWS_PATHS = [
    README,
    AGENTS,
    LOCAL_PLUGIN,
    V1,
    WINDOWS,
    MACOS,
    GETTING_STARTED,
    QUICK_START,
    CI,
]

REQUIRED_TOKENS = {
    README: [
        "Windows and macOS",
        "python tools/run_all_validators.py",
        "python tools\\run_all_validators.py",
        "docs/platforms/windows.md",
        "docs/platforms/macos.md",
        "docs/platforms/ci.md",
        "docs/getting-started/quick-start.md",
        "docs/getting-started/first-run.md",
        "plugins/codex-game-studios/skills/cgs-start/SKILL.md",
    ],
    AGENTS: [
        "python tools/run_all_validators.py",
        "python tools\\run_all_validators.py",
        "tools\\validate_cross_platform.py",
    ],
    LOCAL_PLUGIN: [
        "Windows",
        "macOS",
        "docs/platforms/ci.md",
        "python tools/run_all_validators.py",
        "python tools\\run_all_validators.py",
        "Fallback Path",
    ],
    V1: [
        "Windows and macOS",
        "python tools/run_all_validators.py",
        "python tools\\run_all_validators.py",
        "python tools\\validate_cross_platform.py",
    ],
    WINDOWS: [
        "# Windows Usage",
        "PowerShell",
        "python tools\\run_all_validators.py",
        "docs/platforms/ci.md",
        "plugins/codex-game-studios/skills/cgs-start/SKILL.md",
    ],
    MACOS: [
        "# macOS Usage",
        "zsh",
        "python3 tools/run_all_validators.py",
        "docs/platforms/ci.md",
        "plugins/codex-game-studios/skills/cgs-start/SKILL.md",
    ],
    GETTING_STARTED: [
        "# First Run Guide",
        "Windows",
        "macOS",
        "$cgs-start",
        "$cgs-project-stage-detect",
        "$cgs-dev-story",
        "docs/getting-started/quick-start.md",
    ],
    QUICK_START: [
        "# Quick Start",
        "Codex Desktop",
        "repo-local plugin",
        "path-based fallback",
        "python tools\\run_all_validators.py",
        "python3 tools/run_all_validators.py",
    ],
    CI: [
        "# CI Usage",
        "windows-latest",
        "macos-latest",
        "ubuntu-latest",
        "python tools/run_all_validators.py",
    ],
    RELEASE: [
        "# Codex Game Studios v2.0.0",
        "Windows",
        "macOS",
        "tools/run_all_validators.py",
        "tools/validate_complete_port.py",
        "Final parity gate",
    ],
}

WORKFLOW_TOKENS = [
    "windows-latest",
    "macos-latest",
    "ubuntu-latest",
    "python tools/run_all_validators.py",
]


def read(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f"missing file: {path.relative_to(ROOT).as_posix()}")
        return ""
    return path.read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []

    for path, tokens in REQUIRED_TOKENS.items():
        text = read(path, errors)
        for token in tokens:
            if token not in text:
                errors.append(f"{path.relative_to(ROOT).as_posix()} missing token: {token}")

    workflow = read(WORKFLOW, errors)
    for token in WORKFLOW_TOKENS:
        if token not in workflow:
            errors.append(f"GitHub Actions workflow missing token: {token}")

    for path in DOCS_TO_SCAN_FOR_ABSOLUTE_WINDOWS_PATHS:
        text = read(path, errors)
        if "D:\\" in text or "C:\\" in text:
            errors.append(
                f"{path.relative_to(ROOT).as_posix()} must not use a Windows absolute path as a user-facing default"
            )

    if "find plugins/codex-game-studios" in workflow or "wc -l" in workflow:
        errors.append("GitHub Actions workflow must not use POSIX-only find/wc count checks")

    if errors:
        print("Cross-platform validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Cross-platform validation passed")
    print("- platforms: Windows, macOS, Linux CI")
    return 0


if __name__ == "__main__":
    sys.exit(main())
