# Story: Timer And Light Exposure

Status: Ready
Owner role: gameplay-programmer

## Context

Add the two core pressures: delivery timer and package exposure to light.

## Acceptance Criteria

- Timer counts down during active delivery.
- Timer expiry fails the delivery.
- Light hazard increases exposure.
- Exposure limit fails the delivery.
- HUD shows both timer and exposure warning.

## Test Plan

- Manual smoke: wait for timer expiry and confirm failure.
- Manual smoke: stand in light hazard and confirm exposure failure.
- Future automated check: timer and exposure thresholds are configurable.
