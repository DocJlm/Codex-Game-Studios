# Architecture

Spark Sprint uses a small controller-driven architecture.

## Modules

- `GameController`: owns score, timer, round state, and reset behavior.
- `PlayerController`: owns movement input and velocity.
- `Collectible`: emits pickup behavior and delegates scoring to `GameController`.
- `Hud`: reads round state and presents score, time, and status text.

## Data Flow

Player overlaps collectible -> collectible calls `GameController.collect_spark()` -> controller updates score/state -> HUD refreshes display.
