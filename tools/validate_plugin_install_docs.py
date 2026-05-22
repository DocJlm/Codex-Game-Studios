#!/usr/bin/env python3
"""Validate local plugin install documentation."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "install" / "local-plugin.md"
FIELD_TEST = ROOT / "docs" / "install" / "field-test-2026-05-22.md"

REQUIRED_TOKENS = [
    ".agents/plugins/marketplace.json",
    "./plugins/codex-game-studios",
    "plugins/codex-game-studios/.codex-plugin/plugin.json",
    "plugins/codex-game-studios/skills/",
    "docs/install/field-test-2026-05-22.md",
    "$cgs-start",
    "$cgs-project-stage-detect",
    "$cgs-dev-story",
    "plugins/codex-game-studios/skills/cgs-start/SKILL.md",
    "python tools\\validate_cgs.py",
    "python tools\\validate_plugin_install_docs.py",
    "python tools\\validate_hook_policy.py",
    "python -m json.tool .agents\\plugins\\marketplace.json",
    "runtime hooks",
]

FIELD_TEST_TOKENS = [
    "# Local Plugin Field Test 2026-05-22",
    "D:\\Git\\Codex-Game-Studios",
    "Plugin version under test: `0.9.0`",
    "active built-in skill list did not automatically show `cgs-*` skills",
    "Success Path",
    "Fallback Path",
    "User-visible success signs",
    "User-visible fallback signs",
    "python tools\\validate_plugin_install_docs.py",
    "path-based skill invocation remains the compatibility path",
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

    if not FIELD_TEST.exists():
        errors.append(f"missing field test doc: {FIELD_TEST.relative_to(ROOT).as_posix()}")
        field_text = ""
    else:
        field_text = FIELD_TEST.read_text(encoding="utf-8")

    for token in FIELD_TEST_TOKENS:
        if token not in field_text:
            errors.append(f"field test doc missing token: {token}")

    for token in LEGACY_RUNTIME_TOKENS:
        if token in text:
            errors.append(f"install doc contains legacy runtime token: {token}")
        if token in field_text:
            errors.append(f"field test doc contains legacy runtime token: {token}")

    if errors:
        print("Plugin install documentation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Plugin install documentation validation passed")
    print(f"- doc: {DOC.relative_to(ROOT).as_posix()}")
    print(f"- field test: {FIELD_TEST.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
