#!/usr/bin/env python3
"""Migrate Claude Code Game Studios assets into a Codex plugin layout."""

from __future__ import annotations

import json
import re
import shutil
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / "Claude-Code-Game-Studios"
PLUGIN = ROOT / "plugins" / "codex-game-studios"

SKILL_SOURCE = SOURCE / ".claude" / "skills"
AGENT_SOURCE = SOURCE / ".claude" / "agents"
DOC_SOURCE = SOURCE / ".claude" / "docs"
RULE_SOURCE = SOURCE / ".claude" / "rules"
HOOK_SOURCE = SOURCE / ".claude" / "hooks"
TEST_SOURCE = SOURCE / "CCGS Skill Testing Framework"

SKILL_TARGET = PLUGIN / "skills"
ROLE_TARGET = PLUGIN / "references" / "role-cards"
REFERENCE_TARGET = PLUGIN / "references"
ASSET_TARGET = PLUGIN / "assets"


CORE_SKILLS = {
    "start",
    "help",
    "project-stage-detect",
    "brainstorm",
    "setup-engine",
    "map-systems",
    "design-system",
    "create-architecture",
    "create-epics",
    "create-stories",
    "dev-story",
    "story-readiness",
    "story-done",
    "gate-check",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def reset_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def parse_frontmatter(content: str) -> tuple[dict[str, str], str]:
    if not content.startswith("---\n"):
        return {}, content
    end = content.find("\n---\n", 4)
    if end == -1:
        return {}, content
    raw = content[4:end].splitlines()
    body = content[end + 5 :]
    frontmatter: dict[str, str] = {}
    for line in raw:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] == '"':
            value = value[1:-1]
        frontmatter[key.strip()] = value
    return frontmatter, body.lstrip()


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def ascii_sanitize(text: str) -> str:
    replacements = {
        "\u2013": "-",
        "\u2014": "--",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2026": "...",
        "\u2192": "->",
        "\u00d7": "x",
        "\u2265": ">=",
        "\u2264": "<=",
        "\u00a0": " ",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = unicodedata.normalize("NFKD", text)
    return text.encode("ascii", "ignore").decode("ascii")


def sanitize_description(text: str) -> str:
    text = ascii_sanitize(text)
    text = text.replace("->", "to")
    text = text.replace("<", "(").replace(">", ")")
    return " ".join(text.split())


def known_skill_names() -> list[str]:
    return sorted((path.parent.name for path in SKILL_SOURCE.glob("*/SKILL.md")), key=len, reverse=True)


KNOWN_SKILLS = known_skill_names()


def replace_legacy_runtime_paths(text: str) -> str:
    replacements = {
        ".claude/docs/templates/": "plugins/codex-game-studios/assets/templates/",
        ".claude/docs/": "plugins/codex-game-studios/references/studio-docs/",
        ".claude/rules/": "plugins/codex-game-studios/references/rules/",
        ".claude/agents/": "plugins/codex-game-studios/references/role-cards/",
        ".claude/skills/": "plugins/codex-game-studios/skills/",
        ".claude/hooks/": "plugins/codex-game-studios/scripts/checks/",
        ".claude/agent-memory/": "production/agent-memory/",
        ".claude/": "plugins/codex-game-studios/",
        "CCGS Skill Testing Framework/": "plugins/codex-game-studios/references/testing-framework/",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = text.replace("CLAUDE.md", "AGENTS.md")
    text = text.replace("CLAUDE.local.md", "AGENTS.local.md")
    text = text.replace("Claude Code Game Studios", "Codex Game Studios")
    text = text.replace("Claude Code", "Codex")
    text = text.replace("Claude", "Codex")
    text = text.replace("AskUserQuestion", "ask the user directly or use available Codex UI question tools")
    text = text.replace("argument-hint", "usage note")
    text = text.replace("user-invocable", "Codex-discoverable")
    text = text.replace("allowed-tools", "tool expectations")

    for name in KNOWN_SKILLS:
        text = re.sub(rf"(?<![\w$])/{re.escape(name)}(?![\w/-])", f"$cgs-{name}", text)

    return text


def skill_preamble(original_name: str) -> str:
    phase = "Core workflow MVP" if original_name in CORE_SKILLS else "Full migration"
    return (
        f"> Codex adaptation: this skill is migrated from the upstream `/{original_name}` "
        f"workflow. Invoke it as `$cgs-{original_name}`. "
        "Use Codex tools and the current workspace rules; do not depend on Claude-only "
        "frontmatter, settings hooks, or slash-command runtime behavior.\n\n"
        f"> Migration phase: {phase}. Legacy role names are available as role cards under "
        "`plugins/codex-game-studios/references/role-cards/`.\n\n"
    )


def migrate_skill(source_path: Path) -> None:
    original = source_path.parent.name
    frontmatter, body = parse_frontmatter(read_text(source_path))
    description = frontmatter.get("description") or f"Codex Game Studios workflow adapted from /{original}."
    description = replace_legacy_runtime_paths(description)
    description = (
        f"Codex Game Studios skill adapted from original /{original}. "
        f"Use when the user asks for /{original}, $cgs-{original}, or this workflow. "
        f"{description}"
    )
    body = replace_legacy_runtime_paths(body)
    content = (
        "---\n"
        f"name: cgs-{original}\n"
        f"description: {yaml_quote(sanitize_description(description))}\n"
        "---\n\n"
        f"# CGS: {original}\n\n"
        + skill_preamble(original)
        + body
    )
    write_text(SKILL_TARGET / f"cgs-{original}" / "SKILL.md", ascii_sanitize(content))


def migrate_role_card(source_path: Path) -> None:
    name = source_path.stem
    frontmatter, body = parse_frontmatter(read_text(source_path))
    description = frontmatter.get("description", "").strip()
    body = replace_legacy_runtime_paths(body)
    content = (
        f"# Role Card: {name}\n\n"
        f"Original role: `{name}`\n\n"
        f"Description: {description}\n\n"
        "Codex adaptation: use this as a reference prompt or sequential review role. "
        "Do not treat it as an automatically available subagent unless the current Codex "
        "session explicitly supports and the user requests subagent delegation.\n\n"
        "---\n\n"
        + body
    )
    write_text(ROLE_TARGET / f"{name}.md", content)


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    if src.exists():
        shutil.copytree(src, dst)


def transform_text_tree(root: Path) -> None:
    suffixes = {".md", ".yaml", ".yml", ".json", ".txt", ".toml"}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in suffixes:
            continue
        try:
            text = read_text(path)
        except UnicodeDecodeError:
            continue
        write_text(path, replace_legacy_runtime_paths(text))


def write_manifest_files() -> None:
    plugin_json = {
        "name": "codex-game-studios",
        "version": "2.0.0",
        "description": "Codex plugin and project template for structured solo and small-team game development workflows.",
        "author": {
            "name": "DocJlm",
            "email": "1952199902@qq.com",
            "url": "https://github.com/DocJlm",
        },
        "homepage": "https://github.com/DocJlm/Codex-Game-Studios",
        "repository": "https://github.com/DocJlm/Codex-Game-Studios",
        "license": "MIT",
        "keywords": ["codex", "game-development", "skills", "studio-workflow", "templates"],
        "skills": "./skills/",
        "interface": {
            "displayName": "Codex Game Studios",
            "shortDescription": "Game studio workflows, role cards, gates, and templates for Codex.",
            "longDescription": (
                "A Codex-adapted version of Claude Code Game Studios. It provides cgs-* skills, "
                "studio role cards, design and production templates, rules, engine references, "
                "and validation scripts for guided game development."
            ),
            "developerName": "DocJlm",
            "category": "Productivity",
            "capabilities": ["Interactive", "Write", "Analysis"],
            "defaultPrompt": [
                "Use $cgs-start to set up a new game project.",
                "Use $cgs-project-stage-detect on this existing game.",
                "Use $cgs-dev-story to implement the next story.",
            ],
            "brandColor": "#2563EB",
        },
    }
    write_text(PLUGIN / ".codex-plugin" / "plugin.json", json.dumps(plugin_json, indent=2, ensure_ascii=False) + "\n")

    marketplace = {
        "name": "codex-game-studios-local",
        "interface": {"displayName": "Codex Game Studios Local"},
        "plugins": [
            {
                "name": "codex-game-studios",
                "source": {"source": "local", "path": "./plugins/codex-game-studios"},
                "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                "category": "Productivity",
            }
        ],
    }
    write_text(ROOT / ".agents" / "plugins" / "marketplace.json", json.dumps(marketplace, indent=2, ensure_ascii=False) + "\n")


def write_reference_indexes() -> None:
    skill_rows = []
    for path in sorted((SKILL_TARGET).glob("cgs-*/SKILL.md")):
        original = path.parent.name.removeprefix("cgs-")
        skill_rows.append(f"| `/{original}` | `$cgs-{original}` | `{path.relative_to(ROOT).as_posix()}` |")
    write_text(
        REFERENCE_TARGET / "migration" / "skill-map.md",
        "# Skill Map\n\n| Original Claude command | Codex skill | File |\n| --- | --- | --- |\n"
        + "\n".join(skill_rows)
        + "\n",
    )

    role_rows = []
    for path in sorted(ROLE_TARGET.glob("*.md")):
        role_rows.append(f"| `{path.stem}` | `{path.relative_to(ROOT).as_posix()}` |")
    write_text(
        REFERENCE_TARGET / "migration" / "role-card-map.md",
        "# Role Card Map\n\n| Original agent | Codex role card |\n| --- | --- |\n"
        + "\n".join(role_rows)
        + "\n",
    )


def write_project_template_placeholders() -> None:
    template_dirs = [
        "assets/data",
        "assets/shaders",
        "design/accessibility",
        "design/art",
        "design/assets",
        "design/gdd",
        "design/narrative",
        "docs/architecture",
        "production/bugs",
        "production/epics",
        "production/milestones",
        "production/playtests",
        "production/sprints",
        "prototypes",
        "src/ai",
        "src/core",
        "src/gameplay",
        "src/networking",
        "src/ui",
        "tests",
        "tools",
    ]
    for item in template_dirs:
        path = ROOT / item
        path.mkdir(parents=True, exist_ok=True)
        keep = path / ".gitkeep"
        if not keep.exists():
            keep.write_text("", encoding="utf-8")


def write_gitignore() -> None:
    content = """# Codex Game Studios
.DS_Store
Thumbs.db

# Runtime and local state
.env
.env.*
*.log
production/agent-memory/
production/session-log/

# Engine/build outputs
Library/
Temp/
Obj/
Build/
Builds/
.godot/
.import/
Binaries/
Intermediate/
Saved/
DerivedDataCache/

# Test/cache outputs
.pytest_cache/
node_modules/
dist/
coverage/
"""
    write_text(ROOT / ".gitignore", content)


def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"Source project not found: {SOURCE}")

    reset_dir(SKILL_TARGET)
    reset_dir(ROLE_TARGET)
    reset_dir(REFERENCE_TARGET / "rules")
    reset_dir(REFERENCE_TARGET / "studio-docs")
    reset_dir(REFERENCE_TARGET / "engine-reference")
    reset_dir(REFERENCE_TARGET / "testing-framework")
    reset_dir(ASSET_TARGET / "templates")
    reset_dir(PLUGIN / "scripts" / "checks")

    for source_path in sorted(SKILL_SOURCE.glob("*/SKILL.md")):
        migrate_skill(source_path)

    for source_path in sorted(AGENT_SOURCE.glob("*.md")):
        migrate_role_card(source_path)

    copy_tree(RULE_SOURCE, REFERENCE_TARGET / "rules")
    copy_tree(DOC_SOURCE, REFERENCE_TARGET / "studio-docs")
    copy_tree(SOURCE / "docs" / "engine-reference", REFERENCE_TARGET / "engine-reference")
    copy_tree(DOC_SOURCE / "templates", ASSET_TARGET / "templates")
    copy_tree(TEST_SOURCE, REFERENCE_TARGET / "testing-framework")
    copy_tree(HOOK_SOURCE, PLUGIN / "scripts" / "checks" / "legacy-claude-hooks")

    transform_text_tree(REFERENCE_TARGET / "studio-docs")
    transform_text_tree(REFERENCE_TARGET / "engine-reference")
    transform_text_tree(REFERENCE_TARGET / "rules")
    transform_text_tree(REFERENCE_TARGET / "testing-framework")
    transform_text_tree(ASSET_TARGET / "templates")
    testing_claude = REFERENCE_TARGET / "testing-framework" / "CLAUDE.md"
    if testing_claude.exists():
        testing_claude.rename(REFERENCE_TARGET / "testing-framework" / "AGENTS.md")

    write_manifest_files()
    write_reference_indexes()
    write_project_template_placeholders()
    write_gitignore()

    print(f"Migrated {len(list(SKILL_TARGET.glob('cgs-*/SKILL.md')))} skills")
    print(f"Migrated {len(list(ROLE_TARGET.glob('*.md')))} role cards")
    print(f"Plugin root: {PLUGIN}")


if __name__ == "__main__":
    main()
