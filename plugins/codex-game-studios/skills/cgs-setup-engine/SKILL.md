---
name: cgs-setup-engine
description: "Codex Game Studios curated workflow adapted from original /setup-engine. Use when the user asks for /setup-engine, $cgs-setup-engine, or Configure engine, version, language, and technical preferences."
---

# CGS Setup Engine

Use `$cgs-setup-engine` when engine configuration is missing or outdated.

## Procedure

1. Detect existing engine files before asking: Godot, Unity, Unreal, or custom.
2. If no engine is discoverable, ask for engine, version, language, target platforms, and input method.
3. Read matching references under `plugins/codex-game-studios/references/engine-reference/`.
4. Draft technical preferences: engine version, language, source layout, naming, test command, performance budget, and specialist role cards.
5. Write approved preferences to `docs/architecture/technical-preferences.md`.

## Output Contract

Return detected engine, decisions, files updated, and the next recommended architecture or design skill.
