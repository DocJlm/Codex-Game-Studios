#!/usr/bin/env python3
"""Validate the v2.0 complete-port claim."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
PARITY = ROOT / "docs" / "upstream-parity.md"
RELEASE = ROOT / "docs" / "releases" / "v2.0.0.md"
PLUGIN = ROOT / "plugins" / "codex-game-studios" / ".codex-plugin" / "plugin.json"
RUN_ALL = ROOT / "tools" / "run_all_validators.py"

EXPECTED_VERSION = "2.0.0"
UPSTREAM_COMMIT = "984023ddac0d5e27624f2baacde6105e45de375f"

TOKENS = {
    README: [
        "Codex-native complete port",
        "docs/upstream-parity.md",
        "docs/releases/v2.0.0.md",
        "tools/validate_complete_port.py",
    ],
    PARITY: [
        "Final Parity Gate",
        "No unexplained parity gaps remain",
        "Codex-native complete port",
        UPSTREAM_COMMIT,
        "v2.0.0 completed the final parity gate",
        "tools/validate_complete_port.py",
    ],
    RELEASE: [
        "# Codex Game Studios v2.0.0",
        "Final parity gate",
        "Codex-native complete port",
        "No unexplained parity gaps remain",
        "tools/validate_complete_port.py",
        "python3 tools/run_all_validators.py",
    ],
    RUN_ALL: [
        "validate_complete_port.py",
    ],
}


def read(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f"missing file: {path.relative_to(ROOT).as_posix()}")
        return ""
    return path.read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []

    for path, tokens in TOKENS.items():
        text = read(path, errors)
        for token in tokens:
            if token not in text:
                errors.append(f"{path.relative_to(ROOT).as_posix()} missing token: {token}")

    try:
        plugin = json.loads(PLUGIN.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"plugin.json is not valid JSON: {exc}")
        plugin = {}

    if plugin.get("version") != EXPECTED_VERSION:
        errors.append(f"plugin.json version must be {EXPECTED_VERSION}")
    if "hooks" in plugin:
        errors.append("plugin.json must not declare runtime hooks in the complete port")

    if errors:
        print("Complete-port validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Complete-port validation passed")
    print(f"- version: {EXPECTED_VERSION}")
    print(f"- upstream commit: {UPSTREAM_COMMIT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
