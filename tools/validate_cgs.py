#!/usr/bin/env python3
"""Validate the Codex Game Studios plugin and template layout."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "codex-game-studios"
SKILLS = PLUGIN / "skills"
ROLE_CARDS = PLUGIN / "references" / "role-cards"
RULES = PLUGIN / "references" / "rules"
TEMPLATES = PLUGIN / "assets" / "templates"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"

EXPECTED_SKILLS = 73
EXPECTED_ROLE_CARDS = 49
EXPECTED_RULES = 11
EXPECTED_VERSION = "1.7.0"
EXPECTED_REPOSITORY = "https://github.com/DocJlm/Codex-Game-Studios"


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - validator should report all shape errors.
        fail(errors, f"{path.relative_to(ROOT)} is not valid JSON: {exc}")
        return {}


def parse_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(errors, f"{path.relative_to(ROOT)} missing YAML frontmatter")
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        fail(errors, f"{path.relative_to(ROOT)} has unterminated YAML frontmatter")
        return {}
    lines = text[4:end].splitlines()
    data: dict[str, str] = {}
    for line in lines:
        if ":" not in line:
            fail(errors, f"{path.relative_to(ROOT)} has invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def validate_plugin_json(errors: list[str]) -> None:
    path = PLUGIN / ".codex-plugin" / "plugin.json"
    data = load_json(path, errors)
    if not data:
        return
    if data.get("name") != "codex-game-studios":
        fail(errors, "plugin.json name must be codex-game-studios")
    if data.get("version") != EXPECTED_VERSION:
        fail(errors, f"plugin.json version must be {EXPECTED_VERSION}")
    if data.get("homepage") != EXPECTED_REPOSITORY:
        fail(errors, f"plugin.json homepage must be {EXPECTED_REPOSITORY}")
    if data.get("repository") != EXPECTED_REPOSITORY:
        fail(errors, f"plugin.json repository must be {EXPECTED_REPOSITORY}")
    author = data.get("author", {})
    if author.get("name") != "DocJlm" or author.get("email") == "maintainers@example.com":
        fail(errors, "plugin.json author metadata must use DocJlm release metadata")
    if data.get("skills") != "./skills/":
        fail(errors, "plugin.json skills path must be ./skills/")
    if "hooks" in data:
        fail(errors, "plugin.json must not declare hooks under the current hook policy")
    developer_name = data.get("interface", {}).get("developerName")
    if developer_name != "DocJlm":
        fail(errors, "plugin.json interface.developerName must be DocJlm")
    prompts = data.get("interface", {}).get("defaultPrompt", [])
    if len(prompts) != 3:
        fail(errors, "plugin.json interface.defaultPrompt must contain exactly 3 starter prompts")


def validate_marketplace(errors: list[str]) -> None:
    data = load_json(MARKETPLACE, errors)
    if not data:
        return
    entries = [item for item in data.get("plugins", []) if item.get("name") == "codex-game-studios"]
    if len(entries) != 1:
        fail(errors, "marketplace must contain exactly one codex-game-studios entry")
        return
    entry = entries[0]
    if entry.get("source", {}).get("path") != "./plugins/codex-game-studios":
        fail(errors, "marketplace source.path must be ./plugins/codex-game-studios")
    if entry.get("policy", {}).get("installation") != "AVAILABLE":
        fail(errors, "marketplace policy.installation must be AVAILABLE")
    if entry.get("policy", {}).get("authentication") != "ON_INSTALL":
        fail(errors, "marketplace policy.authentication must be ON_INSTALL")


def validate_skills(errors: list[str]) -> None:
    skill_files = sorted(SKILLS.glob("cgs-*/SKILL.md"))
    if len(skill_files) != EXPECTED_SKILLS:
        fail(errors, f"expected {EXPECTED_SKILLS} skills, found {len(skill_files)}")
    for path in skill_files:
        frontmatter = parse_frontmatter(path, errors)
        expected_name = path.parent.name
        keys = set(frontmatter)
        if keys != {"name", "description"}:
            fail(errors, f"{path.relative_to(ROOT)} frontmatter must contain only name and description")
        if frontmatter.get("name") != expected_name:
            fail(errors, f"{path.relative_to(ROOT)} name must be {expected_name}")
        if not re.fullmatch(r"cgs-[a-z0-9-]+", expected_name):
            fail(errors, f"{path.relative_to(ROOT)} has invalid cgs-* name")
        description = frontmatter.get("description", "")
        original = expected_name.removeprefix("cgs-")
        if f"/{original}" not in description or f"$cgs-{original}" not in description:
            fail(errors, f"{path.relative_to(ROOT)} description must mention /{original} and $cgs-{original}")


def validate_reference_counts(errors: list[str]) -> None:
    role_cards = list(ROLE_CARDS.glob("*.md"))
    rules = list(RULES.glob("*.md"))
    templates = list(TEMPLATES.rglob("*.md"))
    if len(role_cards) != EXPECTED_ROLE_CARDS:
        fail(errors, f"expected {EXPECTED_ROLE_CARDS} role cards, found {len(role_cards)}")
    if len(rules) != EXPECTED_RULES:
        fail(errors, f"expected {EXPECTED_RULES} rules, found {len(rules)}")
    if len(templates) < 40:
        fail(errors, f"expected at least 40 templates, found {len(templates)}")


def validate_no_runtime_legacy_paths(errors: list[str]) -> None:
    checked_roots = [
        SKILLS,
        ROLE_CARDS,
        PLUGIN / "references" / "studio-docs",
        TEMPLATES,
    ]
    patterns = [".claude/", "CLAUDE.md", "AskUserQuestion", "allowed-tools", "argument-hint", "user-invocable"]
    for root in checked_roots:
        for path in root.rglob("*"):
            if path.suffix.lower() not in {".md", ".yaml", ".yml", ".json", ".txt"}:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for pattern in patterns:
                if pattern in text:
                    fail(errors, f"{path.relative_to(ROOT)} contains legacy runtime token {pattern!r}")
                    break


def main() -> int:
    errors: list[str] = []
    validate_plugin_json(errors)
    validate_marketplace(errors)
    validate_skills(errors)
    validate_reference_counts(errors)
    validate_no_runtime_legacy_paths(errors)

    if errors:
        print("Codex Game Studios validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Codex Game Studios validation passed")
    print(f"- skills: {EXPECTED_SKILLS}")
    print(f"- role cards: {EXPECTED_ROLE_CARDS}")
    print(f"- rules: {EXPECTED_RULES}")
    print("- plugin manifest: ok")
    print("- marketplace: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
