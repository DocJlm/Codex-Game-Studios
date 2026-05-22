# Story: Delivery Job Flow

Status: Ready
Owner role: gameplay-programmer

## Context

Implement one data-driven delivery job from briefing to destination completion.

## Acceptance Criteria

- A delivery job can be loaded from data.
- HUD shows destination and active objective.
- Destination trigger completes the job.
- Completion routes to a debrief state.

## Test Plan

- Manual smoke: start job, reach destination, see success debrief.
- Static validation: job data has stable id, title, destination, time limit, and restriction.
