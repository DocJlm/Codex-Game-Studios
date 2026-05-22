# Story: Debrief And Retry

Status: Ready
Owner role: ui-ux-designer

## Context

Give the player clear feedback after success or failure and a fast path back into play.

## Acceptance Criteria

- Success debrief shows delivery result and time remaining.
- Failure debrief states whether timer or exposure caused failure.
- Retry restarts the current delivery quickly.
- Return to menu is available.

## Test Plan

- Manual smoke: complete delivery and retry.
- Manual smoke: fail delivery by timer and exposure.
- Manual smoke: return to menu from debrief.
