#!/usr/bin/env python3
"""Scan runtime-facing files for legacy Claude-only tokens."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SCAN_ROOTS = [
    ROOT / "plugins/codex-game-studios/skills",
    ROOT / "plugins/codex-game-studios/references/role-cards",
    ROOT / "plugins/codex-game-studios/assets/templates",
    ROOT / "plugins/codex-game-studios/references/studio-docs",
    ROOT / "docs/transcripts",
    ROOT / "docs/workflows",
    ROOT / "docs/install",
    ROOT / "docs/hooks",
]

TOKENS = [
    ".claude/",
    "CLAUDE.md",
    "AskUserQuestion",
    "allowed-tools",
    "argument-hint",
    "user-invocable",
]

TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".txt"}


def main() -> int:
    findings: list[str] = []
    for root in SCAN_ROOTS:
        for path in root.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for token in TOKENS:
                if token in text:
                    findings.append(f"{path.relative_to(ROOT)} contains {token!r}")
                    break

    if findings:
        print("Legacy token scan failed:")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("Legacy token scan passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
