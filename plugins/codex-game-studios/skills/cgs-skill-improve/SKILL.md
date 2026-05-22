---
name: cgs-skill-improve
description: "Codex Game Studios skill adapted from original /skill-improve. Use when the user asks for /skill-improve, $cgs-skill-improve, or this workflow. Improve a skill using a test-fix-retest loop. Runs static checks, proposes targeted fixes, rewrites the skill, re-tests, and keeps or reverts based on score change."
---

# CGS: skill-improve

## Codex Operating Notes

- This is the Codex-native version of the upstream `/skill-improve` workflow; invoke it as `$cgs-skill-improve`.
- Inspect repository state before asking questions; use `AGENTS.md` and project validators as the execution boundary.
- When a role perspective is needed, read the matching role card from `plugins/codex-game-studios/references/role-cards/` and apply it in the current session.
- Run role-card reviews sequentially by default. Use parallel agent work only when the user explicitly requests it and suitable tools are available.
- Treat legacy hook behavior as explicit checks: run relevant validators or project tests instead of relying on hidden runtime hooks.

# Skill Improve

Runs an improvement loop on a single skill:
test -> fix -> retest -> keep or revert.

---

## Phase 1: Parse Argument

Read the skill name from the first argument. If missing, output usage and stop:

```
Usage: $cgs-skill-improve [skill-name]
Example: $cgs-skill-improve tech-debt
```

Verify `plugins/codex-game-studios/skills/cgs-[name]/SKILL.md` exists. If not, stop with:
"Skill '[name]' not found."

---

## Phase 2: Baseline Test

Run `$cgs-skill-test static [name]` and record the baseline score:
- Count of FAILs
- Count of WARNs
- Which specific checks failed (Check 1-7)

Display to the user:
```
Static baseline:   [N] failures, [M] warnings
Failing: Check 4 (no ask-before-write), Check 5 (no handoff)
```

If baseline is 0 FAILs and 0 WARNs, note it and proceed to Phase 2b.

### Phase 2b: Category Baseline

Look up the skill's `category:` field in `plugins/codex-game-studios/references/testing-framework/catalog.yaml`.

If no `category:` field is found, display:
"Category: not yet assigned -- skipping category checks."
and skip to Phase 3.

If category is found, run `$cgs-skill-test category [name]` and record the category baseline:
- Count of FAILs
- Count of WARNs
- Which specific category rubric metrics failed

Display to the user:
```
Category baseline: [N] failures, [M] warnings  ([category] rubric)
```

If BOTH static and category baselines are 0 FAILs and 0 WARNs, stop:
"This skill already passes all static and category checks. No improvements needed."

---

## Phase 3: Diagnose

Read the full skill file at `plugins/codex-game-studios/skills/cgs-[name]/SKILL.md`.

For each failing or warning **static** check, identify the exact gap:

- **Check 1 fail** -> which frontmatter field is missing
- **Check 2 fail** -> how many phases found vs. minimum required
- **Check 3 fail** -> no verdict keywords anywhere in the skill body
- **Check 4 fail** -> Write or Edit in tool expectations but no ask-before-write language
- **Check 5 warn** -> no follow-up or next-step section at the end
- **Check 6 warn** -> `context: fork` set but fewer than 5 phases found
- **Check 7 warn** -> usage note is empty or doesn't match documented modes

For each failing or warning **category** check (if category was assigned in Phase 2b),
identify the exact gap in the skill's text. For example:
- If G2 fails (gate mode, full directors not reviewed): skill body never references all 4
  PHASE-GATE director prompts
- If A2 fails (authoring, no per-section May-I-write): skill asks once at the end, not
  before each section write
- If T3 fails (team, BLOCKED not surfaced): skill doesn't halt dependent work on blocked role-card review

Show the full combined diagnosis to the user before proposing any changes.

---

## Phase 4: Propose Fix

Write a targeted fix for each failure and warning. Show the proposed changes
as clearly marked before/after blocks. Only change what is failing -- do not
rewrite sections that are passing.

Ask: "May I write this improved version to `plugins/codex-game-studios/skills/cgs-[name]/SKILL.md`?"

If the user says no, stop here.

---

## Phase 5: Write and Retest

Record the current content of the skill file (for revert if needed).

Write the improved skill to `plugins/codex-game-studios/skills/cgs-[name]/SKILL.md`.

Re-run `$cgs-skill-test static [name]` and record the new static score.
If a category was assigned, also re-run `$cgs-skill-test category [name]` and record the new category score.

Display the comparison:
```
Static:   Before [N] failures, [M] warnings  ->  After [N'] failures, [M'] warnings
Category: Before [N] failures, [M] warnings  ->  After [N'] failures, [M'] warnings  (if applicable)
Combined change: improved / no change / worse
```

---

## Phase 6: Verdict

Count the combined failure total: static FAILs + category FAILs + static WARNs + category WARNs.

**If combined score improved (combined failure count is lower than baseline):**
Report: "Score improved. Changes kept."
Show a summary of what was fixed in each dimension.

**If combined score is the same or worse:**
Report: "Combined score did not improve."
Show what changed and why it may not have helped.
Ask: "May I restore `plugins/codex-game-studios/skills/cgs-[name]/SKILL.md` from the recorded baseline content?"
If yes: write back the recorded baseline content and re-run the relevant validators.

---

## Phase 7: Next Steps

- Run `$cgs-skill-test static all` to find the next skill with failures.
- Run `$cgs-skill-improve [next-name]` to continue the loop on another skill.
- Run `$cgs-skill-test audit` to see overall coverage progress.
