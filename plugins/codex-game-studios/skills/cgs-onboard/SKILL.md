---
name: cgs-onboard
description: "Codex Game Studios skill adapted from original /onboard. Use when the user asks for /onboard, $cgs-onboard, or this workflow. Generates a contextual onboarding document for a new contributor or agent joining the project. Summarizes project state, architecture, conventions, and current priorities relevant to the specified role or area."
---

# CGS: onboard

> Codex adaptation: this skill is migrated from the upstream `/onboard` workflow. Invoke it as `$cgs-onboard`. Use Codex tools and the current workspace rules; do not depend on Claude-only frontmatter, settings hooks, or slash-command runtime behavior.

> Migration phase: Full migration. Legacy role names are available as role cards under `plugins/codex-game-studios/references/role-cards/`.

## Phase 1: Load Project Context

Read AGENTS.md for project overview and standards.

Read the relevant agent definition from `plugins/codex-game-studios/references/role-cards/` if a specific role is specified.

---

## Phase 2: Scan Relevant Area

- For programmers: scan `src/` for architecture, patterns, key files
- For designers: scan `design/` for existing design documents
- For narrative: scan `design/narrative/` for world-building and story docs
- For QA: scan `tests/` for existing test coverage
- For production: scan `production/` for current sprint and milestone

Read recent changes (git log if available) to understand current momentum.

---

## Phase 3: Generate Onboarding Document

```markdown
# Onboarding: [Role/Area]

## Project Summary
[2-3 sentence summary of what this game is and its current state]

## Your Role
[What this role does on this project, key responsibilities, who you report to]

## Project Architecture
[Relevant architectural overview for this role]

### Key Directories
| Directory | Contents | Your Interaction |
|-----------|----------|-----------------|

### Key Files
| File | Purpose | Read Priority |
|------|---------|--------------|

## Current Standards and Conventions
[Summary of conventions relevant to this role from AGENTS.md and agent definition]

## Current State of Your Area
[What has been built, what is in progress, what is planned next]

## Current Sprint Context
[What the team is working on now and what is expected of this role]

## Key Dependencies
[What other roles/systems this role interacts with most]

## Common Pitfalls
[Things that trip up new contributors in this area]

## First Tasks
[Suggested first tasks to get oriented and productive]

1. [Read these documents first]
2. [Review this code/content]
3. [Start with this small task]

## Questions to Ask
[Questions the new contributor should ask to get fully oriented]
```

---

## Phase 4: Save Document

Present the onboarding document to the user.

Ask: "May I write this to `production/onboarding/onboard-[role]-[date].md`?"

If yes, write the file, creating the directory if needed.

---

## Phase 5: Next Steps

Verdict: **COMPLETE** -- onboarding document generated.

- Share the onboarding doc with the new contributor before their first session.
- Run `$cgs-sprint-status` to show the new contributor current progress.
- Run `$cgs-help` if the contributor needs guidance on what to work on next.
