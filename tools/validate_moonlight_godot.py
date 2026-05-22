#!/usr/bin/env python3
"""Validate Moonlight Dispatch Godot prototype files and optional scene load."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "project.godot"
SCENE = ROOT / "scenes" / "main.tscn"

REQUIRED_FILES = [
    "project.godot",
    "scenes/main.tscn",
    "src/gameplay/main_scene.gd",
    "src/gameplay/player_controller.gd",
    "tests/godot/movement-smoke.md",
]

REQUIRED_TOKENS = {
    "project.godot": [
        'config/name="Moonlight Dispatch"',
        'run/main_scene="res://scenes/main.tscn"',
        'config/version="0.2.0"',
        "move_left",
        "move_right",
        "move_up",
        "move_down",
    ],
    "scenes/main.tscn": [
        'path="res://src/gameplay/main_scene.gd"',
        'path="res://src/gameplay/player_controller.gd"',
        'node name="Player" type="CharacterBody2D"',
        'node name="RouteBounds"',
        'node name="MarketBlocker"',
        "Moonlight Dispatch prototype v0.2.0",
    ],
    "src/gameplay/player_controller.gd": [
        "class_name MoonlightPlayerController",
        "@export var movement_speed",
        "@export var play_area_min",
        "@export var play_area_max",
        "Input.get_vector",
        "Input.get_connected_joypads",
        "Input.get_joy_axis",
        "move_and_slide()",
        "clampf",
    ],
    "src/gameplay/main_scene.gd": [
        "@onready var player = $Player",
        "status_label.text",
        "Vector2(160, 560)",
    ],
    "tests/godot/movement-smoke.md": [
        "WASD",
        "arrow keys",
        "left stick",
        "route edge",
        "market blocker",
    ],
}


def read(relative: str, errors: list[str]) -> str:
    path = ROOT / relative
    if not path.exists():
        errors.append(f"missing Moonlight Godot file: {relative}")
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

    scene = SCENE.read_text(encoding="utf-8") if SCENE.exists() else ""
    if scene.count("[ext_resource") < 2:
        errors.append("scenes/main.tscn must declare gameplay script resources")
    if scene.count("StaticBody2D") < 5:
        errors.append("scenes/main.tscn must include route boundary bodies and a blocker")


def validate_runtime(godot: str) -> int:
    version = subprocess.run(
        [godot, "--version"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=15,
    )
    version_text = version.stdout.strip()
    if version.returncode != 0:
        print("Moonlight Godot validation SKIP: Godot version check failed")
        if version_text:
            print(version_text)
        return 0
    if not version_text.startswith("4."):
        print(f"Moonlight Godot validation SKIP: Godot 4.x required, found {version_text}")
        return 0

    print(f"Godot detected: {godot}")
    print(f"Godot version: {version_text}")
    print("Running Moonlight Dispatch scene load check")
    try:
        result = subprocess.run(
            [godot, "--headless", "--path", str(ROOT), "--quit-after", "2"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=45,
        )
    except subprocess.TimeoutExpired:
        print("Moonlight Godot validation failed: scene load timed out")
        return 1

    output = result.stdout.strip()
    if output:
        print(output)
    if result.returncode != 0:
        print(f"Moonlight Godot validation failed with exit code {result.returncode}")
        return result.returncode
    if any(token in output for token in ["SCRIPT ERROR:", "ERROR:"]):
        print("Moonlight Godot validation failed: runtime output contains Godot errors")
        return 1

    print("Moonlight Godot runtime validation passed")
    return 0


def main() -> int:
    errors: list[str] = []
    validate_static_shape(errors)
    if errors:
        print("Moonlight Godot static validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    godot = find_godot()
    if not godot:
        print("Moonlight Godot validation SKIP: Godot executable not found")
        print("- static scene shape: passed")
        return 0

    return validate_runtime(godot)


if __name__ == "__main__":
    sys.exit(main())
