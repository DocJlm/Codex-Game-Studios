#!/usr/bin/env python3
"""Run all non-mutating repository validators with one cross-platform command."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

VALIDATORS = [
    "validate_cgs.py",
    "validate_skills.py",
    "validate_smoke_fixture.py",
    "validate_transcripts.py",
    "validate_plugin_install_docs.py",
    "validate_hook_policy.py",
    "validate_examples.py",
    "validate_godot_example.py",
    "validate_upstream_parity.py",
    "validate_workflow_polish.py",
    "validate_v1_readiness.py",
    "validate_cross_platform.py",
    "scan_legacy_tokens.py",
]

JSON_MANIFESTS = [
    ROOT / "plugins" / "codex-game-studios" / ".codex-plugin" / "plugin.json",
    ROOT / ".agents" / "plugins" / "marketplace.json",
]


def run_validator(script: str) -> int:
    print(f"==> python tools/{script}", flush=True)
    result = subprocess.run([sys.executable, str(ROOT / "tools" / script)], cwd=ROOT)
    return result.returncode


def validate_json(path: Path) -> int:
    print(f"==> json {path.relative_to(ROOT).as_posix()}", flush=True)
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - report exact manifest parse error.
        print(f"JSON validation failed for {path.relative_to(ROOT).as_posix()}: {exc}")
        return 1
    return 0


def main() -> int:
    failures: list[str] = []

    for script in VALIDATORS:
        if run_validator(script) != 0:
            failures.append(f"tools/{script}")

    for path in JSON_MANIFESTS:
        if validate_json(path) != 0:
            failures.append(path.relative_to(ROOT).as_posix())

    if failures:
        print("Cross-platform validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("All validators passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
