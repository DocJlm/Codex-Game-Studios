# Story: Release Readiness

Status: Ready
Owner role: producer

## Context

Prepare the final paid release gate for Steam and itch.io.

## Acceptance Criteria

- QA plan is complete.
- Smoke checklist is complete.
- Release checklist is complete.
- Steam page asset checklist is complete.
- itch.io paid page checklist is complete.
- Payment setup notes contain no private account data.

## Test Plan

- Run `$cgs-qa-plan`.
- Run `$cgs-smoke-check`.
- Run `$cgs-release-checklist`.
- Run `$cgs-gate-check`.
