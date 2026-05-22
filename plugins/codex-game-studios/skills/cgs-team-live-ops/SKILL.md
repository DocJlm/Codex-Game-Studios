---
name: cgs-team-live-ops
description: "Codex Game Studios skill adapted from original /team-live-ops. Use when the user asks for /team-live-ops, $cgs-team-live-ops, or this workflow. Orchestrate the live-ops team for post-launch content planning: coordinates live-ops-designer, economy-designer, analytics-engineer, community-manager, writer, and narrative-director to design and plan a season, event, or live content update."
---

# CGS: team-live-ops

## Codex Operating Notes

- This is the Codex-native version of the upstream `/team-live-ops` workflow; invoke it as `$cgs-team-live-ops`.
- Inspect repository state before asking questions; use `AGENTS.md` and project validators as the execution boundary.
- When a role perspective is needed, read the matching role card from `plugins/codex-game-studios/references/role-cards/` and apply it in the current session.
- Run role-card reviews sequentially by default. Use parallel agent work only when the user explicitly requests it and suitable tools are available.
- Treat legacy hook behavior as explicit checks: run relevant validators or project tests instead of relying on hidden runtime hooks.

**Argument check:** If no season name or event description is provided, output:
> "Usage: `$cgs-team-live-ops [season name or event description]` -- Provide the name or description of the season or live event to plan."
Then stop immediately without running any role-card reviews or reading any files.

When this skill is invoked with a valid argument, orchestrate the live-ops team through a structured planning pipeline.

**Decision Points:** At each phase transition, use `ask one concise question` to present
the user with the role review's proposals as selectable options. Write the role review's
full analysis in conversation, then capture the decision with concise labels.
The user must approve before moving to the next phase.

## Phase 0: Resolve Review Mode

1. If `--review [mode]` was passed as an argument, use that mode.
2. Else read `production/review-mode.txt` -- use whatever is written there.
3. Else default to `lean`.

Modes:
- `full` -- run all director and lead gates as described
- `lean` -- skip director gates unless they are PHASE-GATE type (CD-PHASE-GATE, TD-PHASE-GATE, PR-PHASE-GATE, AD-PHASE-GATE)
- `solo` -- skip all director gate role reviews entirely; run the skill without any role-card gates

Store the resolved mode for use in all subsequent phases.

## Team Composition
- **live-ops-designer** -- Season structure, event cadence, retention mechanics, battle pass
- **economy-designer** -- Live economy balance, store rotation, currency pricing, pity timers
- **analytics-engineer** -- Success metrics, A/B test design, event tracking, dashboard specs
- **community-manager** -- Player-facing announcements, event descriptions, seasonal messaging
- **narrative-director** -- Seasonal narrative theme, story arc, world event framing
- **writer** -- Event descriptions, reward item names, seasonal flavor text, announcement copy

## How to Delegate

Run these role-card reviews from `plugins/codex-game-studios/references/role-cards/`:
- Role card `live-ops-designer` -- Season/event structure and retention mechanics
- Role card `economy-designer` -- Live economy balance and reward pricing
- Role card `analytics-engineer` -- Success metrics, A/B tests, event instrumentation
- Role card `community-manager` -- Player-facing communication and messaging
- Role card `narrative-director` -- Seasonal theme and narrative framing
- Role card `writer` -- All player-facing text: event descriptions, item names, copy

Always provide full context in each role review brief (game concept path, existing season docs, ethics policy path, current economy state). Run independent role-card reviews sequentially by default; use parallel agent work only when the user explicitly requests it and tools are available (Phases 3 and 4 can run simultaneously).

## Pipeline

### Phase 1: Season/Event Scoping
Delegate to **live-ops-designer**:
- Define the season or event: type (seasonal, limited-time event, challenge), duration, theme direction
- Outline the content list: what's new (modes, items, challenges, story beats)
- Define the retention hook: what brings players back daily/weekly during this season
- Identify resource budget: how much new content needs to be created vs. reused
- Output: season brief with scope, content list, and retention mechanic overview

### Phase 2: Narrative Theme
Delegate to **narrative-director**:
- Read the season brief from Phase 1
- Design the seasonal narrative theme: how does this event connect to the game world?
- Define the central story hook players will discover during the event
- Identify which existing lore threads this season can advance
- Output: narrative framing document (theme, story hook, lore connections)

### Phase 3: Economy Design (parallel with Phase 2 if theme is clear)
Delegate to **economy-designer**:
- Read the season brief and existing economy rules from `design/live-ops/economy-rules.md`
- Design the reward track: free tier progression, premium tier value proposition
- Plan the in-season economy: seasonal currency, store rotation, pricing
- Define pity timer mechanics and bad-luck protection for any random elements
- Verify no pay-to-win items in premium track
- Output: economy design doc with reward tables, pricing, and currency flow

### Phase 4: Analytics and Success Metrics (parallel with Phase 3)
Delegate to **analytics-engineer**:
- Read the season brief
- Define success metrics: participation rate target, retention lift target, battle pass completion rate
- Design any A/B tests to run during the season (e.g., different reward cadences)
- Specify new telemetry events needed for this season's content
- Output: analytics plan with success criteria and instrumentation requirements

### Phase 5: Content Writing (parallel)
Delegate in parallel:
- **narrative-director** (if needed): Write any in-game narrative text (cutscene scripts, NPC dialogue, world event descriptions) for the season
- **writer**: Write all player-facing text -- event names, reward item descriptions, challenge objective text, seasonal flavor text
- Both should read the narrative framing doc from Phase 2

### Phase 6: Player Communication Plan
Delegate to **community-manager**:
- Read the season brief, economy design, and narrative framing
- Draft the season launch announcement (tone, key highlights, platform-specific versions)
- Plan the communication cadence: pre-launch teaser, launch day post, mid-season reminder, final week FOMO push
- Draft known-issues section placeholder for day-1 patch notes
- Output: communication calendar with draft copy for each touchpoint

### Phase 7: Review and Sign-off
Collect outputs from all phases and present a consolidated season plan:
- Season brief (Phase 1)
- Narrative framing (Phase 2)
- Economy design and reward tables (Phase 3)
- Analytics plan and success metrics (Phase 4)
- Written content inventory (Phase 5)
- Communication calendar (Phase 6)

Present a summary to the user with:
- **Content scope**: what is being created
- **Economy health check**: does the reward track feel fair and non-predatory?
- **Analytics readiness**: are success criteria defined and instrumented?
- **Ethics review**: check the Phase 3 economy design against `design/live-ops/ethics-policy.md`
  - If the file does not exist: flag "ETHICS REVIEW SKIPPED: `design/live-ops/ethics-policy.md` not found. Economy design was not reviewed against an ethics policy. Recommend creating one before production begins." Include this flag in the season design output document. Add to next steps: create `design/live-ops/ethics-policy.md`.
  - If the file exists and a violation is found: flag "ETHICS FLAG: [element] in Phase 3 economy design violates [policy rule]. Approval is blocked until this is resolved." Do NOT issue a COMPLETE verdict or write output documents. Use `ask one concise question` with options: revise economy design / override with documented rationale / cancel. If user chooses to revise: re-run economy-designer to produce a corrected design, then return to Phase 7 review. If user selects Cancel: end with Verdict: BLOCKED -- "Live ops design cancelled due to unresolved ethics violation. Resolve the flagged issues and re-run $cgs-team-live-ops."
- **Open questions**: decisions still needed before production begins

Ask the user to approve the season plan before delegating to production teams. Issue the COMPLETE verdict only after the user approves and no unresolved ethics violations remain. If an ethics violation is unresolved, end with Verdict: **BLOCKED**.

## Output Documents

All documents save to `design/live-ops/`:
- `seasons/S[N]_[name].md` -- Season design document (from Phase 1-3)
- `seasons/S[N]_[name]_analytics.md` -- Analytics plan (from Phase 4)
- `seasons/S[N]_[name]_comms.md` -- Communication calendar (from Phase 6)

## Error Recovery Protocol

If any role-card review (through role-card review) returns BLOCKED, errors, or cannot complete:

1. **Surface immediately**: Report "[AgentName]: BLOCKED -- [reason]" to the user before continuing to dependent phases
2. **Assess dependencies**: Check whether the blocked role-card review's output is required by subsequent phases. If yes, do not proceed past that dependency point without user input.
3. **Offer options** via ask one concise question with choices:
   - Skip this role-card review and note the gap in the final report
   - Retry with narrower scope
   - Stop here and resolve the blocker first
4. **Always produce a partial report** -- output whatever was completed. Never discard work because one role-card review blocked.

If a BLOCKED state is unresolvable, end with Verdict: **BLOCKED** instead of COMPLETE.

## File Write Protocol

All file writes (season design docs, analytics plans, communication calendars) are
delegated to role-card reviews run as role-card reviews. Each role-card review enforces the
"May I write to [path]?" protocol. This orchestrator does not write files directly.

## Output

A summary covering: season theme and scope, economy design highlights, success metrics, content list, communication plan, and any open decisions needing user input before production.

Verdict: **COMPLETE** -- season plan produced and handed off for production.

## Next Steps

- Run `$cgs-design-review` on the season design document for consistency validation.
- Run `$cgs-sprint-plan` to schedule content creation work for the season.
- Run `$cgs-team-release` when the season content is ready to deploy.
