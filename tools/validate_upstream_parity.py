#!/usr/bin/env python3
"""Validate the checked upstream parity report and local parity surfaces."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "upstream-parity.md"
PLUGIN_JSON = ROOT / "plugins" / "codex-game-studios" / ".codex-plugin" / "plugin.json"
SKILLS = ROOT / "plugins" / "codex-game-studios" / "skills"
ROLE_CARDS = ROOT / "plugins" / "codex-game-studios" / "references" / "role-cards"
RULES = ROOT / "plugins" / "codex-game-studios" / "references" / "rules"
TEMPLATES = ROOT / "plugins" / "codex-game-studios" / "assets" / "templates"
LEGACY_HOOKS = ROOT / "plugins" / "codex-game-studios" / "scripts" / "checks" / "legacy-claude-hooks"

EXPECTED_COUNTS = {
    "skills": 73,
    "role cards": 49,
    "rules": 11,
    "templates": 40,
    "legacy hooks": 12,
}

EXPECTED_HOOKS = [
    "detect-gaps.sh",
    "log-agent-stop.sh",
    "log-agent.sh",
    "notify.sh",
    "post-compact.sh",
    "pre-compact.sh",
    "session-start.sh",
    "session-stop.sh",
    "validate-assets.sh",
    "validate-commit.sh",
    "validate-push.sh",
    "validate-skill-change.sh",
]

REQUIRED_DOC_TOKENS = [
    "# Upstream Parity Report",
    "984023ddac0d5e27624f2baacde6105e45de375f",
    "Surface Matrix",
    "Template Count Evidence",
    "Hook Intent Mapping",
    "Remaining Parity Work",
    "73",
    "49",
    "11",
    "40",
    "12",
    "no-runtime-hooks",
    "tools/validate_upstream_parity.py",
    "v1.4.0",
    "v1.5.0",
]


def count_files(path: Path, pattern: str) -> int:
    return len(list(path.rglob(pattern)))


def main() -> int:
    errors: list[str] = []

    if not DOC.exists():
        errors.append("missing docs/upstream-parity.md")
        doc = ""
    else:
        doc = DOC.read_text(encoding="utf-8")

    for token in REQUIRED_DOC_TOKENS:
        if token not in doc:
            errors.append(f"upstream parity report missing token: {token}")

    counts = {
        "skills": len(list(SKILLS.glob("cgs-*/SKILL.md"))),
        "role cards": count_files(ROLE_CARDS, "*.md"),
        "rules": count_files(RULES, "*.md"),
        "templates": count_files(TEMPLATES, "*.md"),
        "legacy hooks": count_files(LEGACY_HOOKS, "*.sh"),
    }
    for name, expected in EXPECTED_COUNTS.items():
        actual = counts[name]
        if actual != expected:
            errors.append(f"expected {expected} {name}, found {actual}")

    hook_names = sorted(path.name for path in LEGACY_HOOKS.glob("*.sh"))
    if hook_names != EXPECTED_HOOKS:
        errors.append("legacy hook reference set does not match upstream hook names")
    for hook in EXPECTED_HOOKS:
        if hook not in doc:
            errors.append(f"upstream parity report missing hook mapping: {hook}")

    try:
        plugin = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"plugin.json is not valid JSON: {exc}")
        plugin = {}
    if "hooks" in plugin:
        errors.append("plugin.json must not declare runtime hooks for parity v1")

    if errors:
        print("Upstream parity validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Upstream parity validation passed")
    print(f"- skills: {counts['skills']}")
    print(f"- role cards: {counts['role cards']}")
    print(f"- rules: {counts['rules']}")
    print(f"- templates: {counts['templates']}")
    print(f"- legacy hook references: {counts['legacy hooks']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
