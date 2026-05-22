# Moonlight Dispatch Architecture

## Architecture Goal

Build a small, data-driven Godot 4.6 game that can ship in eight weeks without turning content production into code changes.

## Layers

| Layer | Responsibility |
| --- | --- |
| Core | Save data, settings, language, scene flow |
| Gameplay | Player movement, delivery jobs, hazards, tools, scoring |
| Presentation | HUD, menus, debrief, accessibility feedback |
| Content Data | Jobs, districts, NPC lines, tool definitions |
| Platform | Export presets, store build notes, local validation |

## Scene Flow

```text
Boot -> MainMenu -> NightBriefing -> TownRun -> DeliveryDebrief -> NextNight or Ending
```

## Data Flow

1. `JobDatabase` loads authored delivery jobs.
2. `NightController` selects the active job and district state.
3. `PlayerController` handles movement and interaction.
4. `HazardController` updates light exposure and route blockers.
5. `ToolController` spends tools and emits state changes.
6. `HudController` reads current job, timer, exposure, and tool state.
7. `DebriefController` scores the run and records progress.

## Content Data Contracts

Delivery jobs require:

- Stable `id`
- English and Simplified Chinese title/brief
- Pickup or start point
- Destination
- Time limit
- Package restriction
- Required district
- Optional NPC
- Unlock condition

Tools require:

- Stable `id`
- Display name
- Description
- Charge rule
- Effect type
- Cooldown or consumption rule

## Save Model

Save only durable progress:

- Completed deliveries
- Unlocked districts
- Unlocked tools
- Language and settings
- Best route scores
- Daily challenge seed history, if needed

Do not save transient scene references.

## Risk Register

| Risk | Mitigation |
| --- | --- |
| Scope creep in authored missions | Cap at 12 deliveries and use one compact map |
| Light stealth feels unfair | Keep warning feedback clear and exposure forgiving |
| Art production too slow | Use consistent low-detail 2D style and reuse districts |
| Store page lacks immediate hook | Produce key art, capsule, GIF script, and screenshot checklist in Week 1-4 |
| Mac export friction | Validate early with export notes before release week |
