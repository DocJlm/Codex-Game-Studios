---
name: cgs-create-stories
description: "Codex Game Studios curated workflow adapted from original /create-stories. Use when the user asks for /create-stories, $cgs-create-stories, or Break one epic into implementable production stories."
---

# CGS Create Stories

Use `$cgs-create-stories` to split an approved epic into small implementation stories.

## Procedure

1. Read one `production/epics/<epic>/EPIC.md`.
2. Check dependencies, GDD links, ADR links, and test expectations.
3. Create stories sized for 1-3 days of focused work.
4. Each story must include context, implementation notes, acceptance criteria, test plan, owner role, and done checklist.
5. Offer to write story files under the epic folder.

## Output Contract

Return story sequence, dependency order, and first recommended `$cgs-dev-story` target.
