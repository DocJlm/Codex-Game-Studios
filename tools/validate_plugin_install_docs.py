#!/usr/bin/env python3
"""Validate local plugin install documentation."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "install" / "local-plugin.md"

REQUIRED_TOKENS = [
    ".agents/plugins/marketplace.json",
    "./plugins/codex-game-studios",
    "plugins/codex-game-studios/.codex-plugin/plugin.json",
    "plugins/codex-game-studios/skills/",
    "$cgs-start",
    "$cgs-project-stage-detect",
    "$cgs-dev-story",
    "plugins/codex-game-studios/skills/cgs-start/SKILL.md",
    "python tools\\validate_cgs.py",
    "python tools\\validate_plugin_install_docs.py",
    "python -m json.tool .agents\\plugins\\marketplace.json",
    "runtime hooks",
]

LEGACY_RUNTIME_TOKENS = [
    ".claude/",
    "CLAUDE.md",
    "AskUserQuestion",
    "allowed-tools",
    "argument-hint",
    "user-invocable",
]


def main() -> int:
    errors: list[str] = []

    if not DOC.exists():
        errors.append(f"missing doc: {DOC.relative_to(ROOT).as_posix()}")
        text = ""
    else:
        text = DOC.read_text(encoding="utf-8")

    if text and not text.startswith("# Local Plugin Install UX"):
        errors.append("install doc must start with '# Local Plugin Install UX'")

    for token in REQUIRED_TOKENS:
        if token not in text:
            errors.append(f"install doc missing token: {token}")

    for token in LEGACY_RUNTIME_TOKENS:
        if token in text:
            errors.append(f"install doc contains legacy runtime token: {token}")

    if errors:
        print("Plugin install documentation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Plugin install documentation validation passed")
    print(f"- doc: {DOC.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
