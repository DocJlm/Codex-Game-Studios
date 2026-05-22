#!/usr/bin/env python3
"""Validate the optional runnable Godot example."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples" / "spark-sprint"
SCENE = EXAMPLE / "scenes" / "main.tscn"
PROJECT = EXAMPLE / "project.godot"

REQUIRED_FILES = [
    "project.godot",
    "scenes/main.tscn",
    "src/gameplay/main_scene.gd",
    "src/gameplay/game_controller.gd",
    "src/gameplay/player_controller.gd",
    "src/gameplay/collectible.gd",
    "src/ui/hud.gd",
]

REQUIRED_TOKENS = {
    "project.godot": ["run/main_scene=\"res://scenes/main.tscn\"", "Godot 4.3"],
    "scenes/main.tscn": [
        "res://src/gameplay/main_scene.gd",
        "res://src/gameplay/game_controller.gd",
        "res://src/gameplay/player_controller.gd",
        "res://src/gameplay/collectible.gd",
        "res://src/ui/hud.gd",
        'node name="Player"',
        'node name="Spark"',
        'node name="Hud"',
    ],
    "src/gameplay/main_scene.gd": ["reset_round", "game_controller.tick_timer", "spark.reset_spark"],
    "src/gameplay/collectible.gd": ["reset_spark", "randomize_position", "body_entered.connect"],
    "src/ui/hud.gd": ["ScoreLabel", "TimerLabel", "StateLabel"],
}


def read(relative: str, errors: list[str]) -> str:
    path = EXAMPLE / relative
    if not path.exists():
        errors.append(f"missing Godot example file: {relative}")
        return ""
    return path.read_text(encoding="utf-8")


def find_godot() -> str | None:
    for candidate in ["godot4", "godot", "godot4.exe", "godot.exe"]:
        path = shutil.which(candidate)
        if path:
            return path
    return None


def validate_static_shape(errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        read(relative, errors)

    for relative, tokens in REQUIRED_TOKENS.items():
        text = read(relative, errors)
        for token in tokens:
            if token not in text:
                errors.append(f"{relative} missing token: {token}")

    project = read("project.godot", errors)
    if 'run/main_scene="res://scenes/main.tscn"' not in project:
        errors.append("project.godot must point to scenes/main.tscn")

    scene = SCENE.read_text(encoding="utf-8") if SCENE.exists() else ""
    if scene.count("[ext_resource") < 5:
        errors.append("main.tscn must declare runtime script resources")


def validate_runtime(godot: str) -> int:
    version = subprocess.run(
        [godot, "--version"],
        cwd=EXAMPLE,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=15,
    )
    version_text = version.stdout.strip()
    if version.returncode != 0:
        print("Godot example validation SKIP: Godot version check failed")
        if version_text:
            print(version_text)
        return 0
    if not version_text.startswith("4."):
        print(f"Godot example validation SKIP: Godot 4.x required, found {version_text}")
        return 0

    command = [godot, "--headless", "--path", str(EXAMPLE), "--quit-after", "2"]
    print(f"Godot detected: {godot}")
    print(f"Godot version: {version_text}")
    print("Running optional scene load check")
    try:
        result = subprocess.run(
            command,
            cwd=EXAMPLE,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=45,
        )
    except subprocess.TimeoutExpired:
        print("Godot example validation failed: scene load timed out")
        return 1

    output = result.stdout.strip()
    if output:
        print(output)
    if result.returncode != 0:
        print(f"Godot example validation failed with exit code {result.returncode}")
        return result.returncode

    print("Godot example runtime validation passed")
    return 0


def main() -> int:
    errors: list[str] = []
    validate_static_shape(errors)
    if errors:
        print("Godot example static validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    godot = find_godot()
    if not godot:
        print("Godot example validation SKIP: Godot executable not found")
        print("- static scene shape: passed")
        return 0

    return validate_runtime(godot)


if __name__ == "__main__":
    sys.exit(main())
