#!/usr/bin/env python3
"""Validate Moonlight Dispatch project foundation artifacts."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = {
    "production/stage.txt": ["pre-production"],
    "production/review-mode.txt": ["lean"],
    "design/gdd/game-concept.md": ["Moonlight Dispatch", "USD 7.99", "Steam", "itch.io", "Wise", "Out Of Scope"],
    "design/gdd/core-loop.md": ["Briefing -> choose delivery", "Patrol light", "Shade Cloak", "Win State"],
    "design/gdd/systems-index.md": ["Player Movement", "Delivery Jobs", "Light Hazards", "Daily Challenge"],
    "docs/architecture/technical-preferences.md": ["Godot 4.6", "GDScript", "Windows, macOS", "validate_moonlight_dispatch.py"],
    "docs/architecture/architecture.md": ["NightBriefing -> TownRun", "JobDatabase", "Save Model", "Risk Register"],
    "docs/architecture/control-manifest.md": ["no ads", "no in-app purchases", "Do not add multiplayer", "Wise"],
    "design/art/art-bible.md": ["Generated Concept Assets", "moonlight-dispatch-key-art.png", "Steam capsule"],
    "design/art/visual-direction-prompts.md": ["Key Art", "Steam Capsule Concept", "Character And Tool Sheet"],
    "design/assets/asset-manifest.md": ["Generated v0.1.0", "Runtime MVP Assets"],
    "design/narrative/narrative-brief.md": ["Lumenwick", "Mira Bellweather", "Old Venn", "Sister Lio"],
    "design/accessibility/accessibility-requirements.md": ["Accessibility tier: Standard", "Simplified Chinese"],
    "docs/store/steam-itch-page.md": ["USD 7.99", "Steam", "itch.io", "Feature Bullets"],
    "docs/store/payments-wise-checklist.md": ["Do not commit tax identifiers", "Steam", "itch.io", "Wise"],
    "production/milestones/8-week-roadmap.md": ["Week 1", "Week 8", "Release Candidate"],
    "production/sprints/week-01-plan.md": ["Week 01", "Definition Of Done"],
    "production/gates/week-01-concept-gate.md": ["PASS WITH CONCERNS", "Proceed to core prototype"],
    "tests/SMOKE-CHECKLIST.md": ["Moonlight Dispatch", "Future Runtime Smoke"],
}

EPIC_DIRS = [
    "production/epics/mvp",
    "production/epics/vertical-slice",
    "production/epics/steam-demo",
    "production/epics/release-candidate",
]

CONCEPT_IMAGES = [
    "assets/art/concept/moonlight-dispatch-key-art.png",
    "assets/art/concept/moonlight-dispatch-steam-capsule-concept.png",
    "assets/art/concept/moonlight-dispatch-character-sheet.png",
]

FORBIDDEN_PAYMENT_TOKENS = [
    "routing number:",
    "account number:",
    "iban:",
    "tax id:",
    "passport",
]


def check_text_file(relative: str, tokens: list[str], errors: list[str]) -> None:
    path = ROOT / relative
    if not path.exists():
        errors.append(f"missing file: {relative}")
        return
    text = path.read_text(encoding="utf-8")
    for token in tokens:
        if token not in text:
            errors.append(f"{relative} missing token: {token}")


def check_png(relative: str, errors: list[str]) -> None:
    path = ROOT / relative
    if not path.exists():
        errors.append(f"missing concept image: {relative}")
        return
    data = path.read_bytes()
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        errors.append(f"{relative} is not a PNG file")
    if len(data) < 100_000:
        errors.append(f"{relative} looks too small for a generated concept asset")


def main() -> int:
    errors: list[str] = []

    for relative, tokens in REQUIRED_FILES.items():
        check_text_file(relative, tokens, errors)

    for epic_dir in EPIC_DIRS:
        epic = ROOT / epic_dir / "EPIC.md"
        if not epic.exists():
            errors.append(f"missing epic: {epic_dir}/EPIC.md")
        stories = sorted((ROOT / epic_dir).glob("STORY-*.md"))
        if not stories:
            errors.append(f"missing stories under {epic_dir}")
        for story in stories:
            text = story.read_text(encoding="utf-8")
            for token in ["Status: Ready", "Acceptance Criteria", "Test Plan"]:
                if token not in text:
                    errors.append(f"{story.relative_to(ROOT).as_posix()} missing token: {token}")

    for image in CONCEPT_IMAGES:
        check_png(image, errors)

    payment_text = (ROOT / "docs/store/payments-wise-checklist.md").read_text(encoding="utf-8")
    lower_payment = payment_text.lower()
    for token in FORBIDDEN_PAYMENT_TOKENS:
        if token in lower_payment:
            errors.append(f"payment checklist may contain private data token: {token}")

    if errors:
        print("Moonlight Dispatch validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Moonlight Dispatch validation passed")
    print("- docs: project foundation")
    print("- epics: 4 tracks")
    print("- concept art: 3 generated PNG assets")
    return 0


if __name__ == "__main__":
    sys.exit(main())
