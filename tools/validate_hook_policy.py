#!/usr/bin/env python3
"""Validate the Codex Game Studios runtime hook policy."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "codex-game-studios"
PLUGIN_JSON = PLUGIN / ".codex-plugin" / "plugin.json"
HOOK_POLICY_DOC = ROOT / "docs" / "hooks" / "runtime-hook-evaluation.md"
LEGACY_HOOKS = PLUGIN / "scripts" / "checks" / "legacy-claude-hooks"

REQUIRED_DOC_TOKENS = [
    "Plugin hooks are off by default",
    "[features].plugin_hooks = true",
    "hooks/hooks.json",
    "PLUGIN_ROOT",
    "PLUGIN_DATA",
    "PreToolUse",
    "PermissionRequest",
    "PostToolUse",
    "UserPromptSubmit",
    "Stop",
    "Codex Game Studios does not bundle runtime hooks in v0.5",
    "tools\\validate_hook_policy.py",
    "plugins/codex-game-studios/scripts/checks/legacy-claude-hooks/",
]


def main() -> int:
    errors: list[str] = []

    try:
        plugin_json = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        plugin_json = {}
        errors.append(f"plugin.json is not valid JSON: {exc}")

    if "hooks" in plugin_json:
        errors.append("plugin.json must not declare hooks for the v0.5 policy")

    plugin_hooks_dir = PLUGIN / "hooks"
    if plugin_hooks_dir.exists():
        errors.append("plugin root must not contain hooks/ while runtime hooks are disabled")

    if (PLUGIN / "hooks.json").exists():
        errors.append("plugin root must not contain hooks.json while runtime hooks are disabled")

    if not LEGACY_HOOKS.exists():
        errors.append("legacy hook reference directory is missing")

    if not HOOK_POLICY_DOC.exists():
        errors.append(f"missing hook policy doc: {HOOK_POLICY_DOC.relative_to(ROOT).as_posix()}")
        doc = ""
    else:
        doc = HOOK_POLICY_DOC.read_text(encoding="utf-8")

    if doc and not doc.startswith("# Runtime Hook Evaluation"):
        errors.append("hook policy doc must start with '# Runtime Hook Evaluation'")

    for index, char in enumerate(doc):
        if ord(char) < 32 and char not in "\n\r\t":
            errors.append(f"hook policy doc contains control character U+{ord(char):04X} at offset {index}")
            break

    for token in REQUIRED_DOC_TOKENS:
        if token not in doc:
            errors.append(f"hook policy doc missing token: {token}")

    if errors:
        print("Hook policy validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Hook policy validation passed")
    print(f"- doc: {HOOK_POLICY_DOC.relative_to(ROOT).as_posix()}")
    print("- plugin runtime hooks: not declared")
    print("- legacy hook scripts: reference-only")
    return 0


if __name__ == "__main__":
    sys.exit(main())
