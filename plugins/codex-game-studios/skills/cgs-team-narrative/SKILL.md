---
name: cgs-team-narrative
description: "Codex Game Studios skill adapted from original /team-narrative. Use when the user asks for /team-narrative, $cgs-team-narrative, or this workflow. Orchestrate the narrative team: coordinates narrative-director, writer, world-builder, and level-designer to create cohesive story content, world lore, and narrative-driven level design."
---

# CGS: team-narrative

## Codex Operating Notes

- This is the Codex-native version of the upstream `/team-narrative` workflow; invoke it as `$cgs-team-narrative`.
- Inspect repository state before asking questions; use `AGENTS.md` and project validators as the execution boundary.
- When a role perspective is needed, read the matching role card from `plugins/codex-game-studios/references/role-cards/` and apply it in the current session.
- Run role-card reviews sequentially by default. Use parallel agent work only when the user explicitly requests it and suitable tools are available.
- Treat legacy hook behavior as explicit checks: run relevant validators or project tests instead of relying on hidden runtime hooks.

If no argument is provided, output usage guidance and exit without running any role-card reviews:
> Usage: `$cgs-team-narrative [narrative content description]` -- describe the story content, scene, or narrative area to work on (e.g., `boss encounter cutscene`, `faction intro dialogue`, `tutorial narrative`). Do not use `ask one concise question` here; output the guidance directly.

When this skill is invoked with an argument, orchestrate the narrative team through a structured pipeline.

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
- **narrative-director** -- Story arcs, character design, dialogue strategy, narrative vision
- **writer** -- Dialogue writing, lore entries, item descriptions, in-game text
- **world-builder** -- World rules, faction design, history, geography, environmental storytelling
- **art-director** -- Character visual design, environmental visual storytelling, cutscene/cinematic tone
- **level-designer** -- Level layouts that serve the narrative, pacing, environmental storytelling beats
- **localization-lead** -- Localization readiness -- flags non-localizable strings, cultural assumptions, and i18n gaps

## How to Delegate

Run these role-card reviews from `plugins/codex-game-studios/references/role-cards/`:
- Role card `narrative-director` -- Story arcs, character design, narrative vision
- Role card `writer` -- Dialogue writing, lore entries, in-game text
- Role card `world-builder` -- World rules, faction design, history, geography
- Role card `art-director` -- Character visual profiles, environmental visual storytelling, cinematic tone
- Role card `level-designer` -- Level layouts that serve the narrative, pacing
- Role card `localization-lead` -- Localization readiness -- flags non-localizable strings, cultural assumptions, and i18n gaps

Always provide full context in each role review brief (narrative brief, lore dependencies, character profiles). Run independent role-card reviews sequentially by default; use parallel agent work only when the user explicitly requests it and tools are available (e.g., Phase 2 role-card reviews can be grouped when the user explicitly asks for parallel agent work).

## Pipeline

### Phase 1: Narrative Direction
Delegate to **narrative-director**:
- Define the narrative purpose of this content: what story beat does it serve?
- Identify characters involved, their motivations, and how this fits the overall arc
- Set the emotional tone and pacing targets
- Specify any lore dependencies or new lore this introduces
- Output: narrative brief with story requirements

### Phase 2: World Foundation (parallel)
Delegate in parallel -- issue all three role-card review passes simultaneously before waiting for any result:
- **world-builder**: Create or update lore entries for factions, locations, and history relevant to this content. Cross-reference against existing lore for contradictions. Set canon level for new entries.
- **writer**: Draft character dialogue using voice profiles. Ensure all lines are under 120 characters, use named placeholders for variables, and are localization-ready.
- **art-director**: Define character visual design direction for key characters appearing in this content (silhouette, visual archetype, distinguishing features). Specify environmental visual storytelling elements for each key space (prop composition, lighting notes, spatial arrangement). Define tone palette and cinematic direction for any cutscenes or scripted sequences.

### Phase 3: Level Narrative Integration
Delegate to **level-designer**:
- Review the narrative brief and lore foundation
- Design environmental storytelling elements in the level
- Place narrative triggers, dialogue zones, and discovery points
- Ensure pacing serves both gameplay and story

### Phase 4: Review and Consistency
Delegate to **narrative-director**:
- Review all dialogue against character voice profiles
- Verify lore consistency across new and existing entries
- Confirm narrative pacing aligns with level design
- Check that all mysteries have documented "true answers"

### Phase 5: Polish (parallel)
Delegate in parallel:
- **writer**: Final self-review -- verify no line exceeds dialogue box constraints, all text uses string keys (not raw strings), placeholder variable names are consistent
- **localization-lead**: Validate i18n compliance -- check string key naming conventions, flag any strings with hardcoded formatting that won't survive translation, verify character limit headroom for languages that expand (German/Finnish typically +30%), confirm no cultural assumptions in text that would need locale-specific variants
- **world-builder**: Finalize canon levels for all new lore entries

## Error Recovery Protocol

If any role-card review (through role-card review) returns BLOCKED, errors, or cannot complete:

1. **Surface immediately**: Report "[AgentName]: BLOCKED -- [reason]" to the user before continuing to dependent phases
2. **Assess dependencies**: Check whether the blocked role-card review's output is required by subsequent phases. If yes, do not proceed past that dependency point without user input.
3. **Offer options** via ask one concise question with choices:
   - Skip this role-card review and note the gap in the final report
   - Retry with narrower scope
   - Stop here and resolve the blocker first
4. **Always produce a partial report** -- output whatever was completed. Never discard work because one role-card review blocked.

Common blockers:
- Input file missing (story not found, GDD absent) -> redirect to the skill that creates it
- ADR status is Proposed -> do not implement; run `$cgs-architecture-decision` first
- Scope too large -> split into two stories via `$cgs-create-stories`
- Conflicting instructions between ADR and story -> surface the conflict, do not guess

## File Write Protocol

All file writes (narrative docs, dialogue files, lore entries) are delegated to
role-card reviews run as role-card reviews. Each role-card review enforces the "May I write to [path]?"
protocol. This orchestrator does not write files directly.

## Output

A summary report covering: narrative brief status, lore entries created/updated, dialogue lines written, level narrative integration points, consistency review results, and any unresolved contradictions.

Verdict: **COMPLETE** -- narrative content delivered.

If the pipeline stops because a dependency is unresolved (e.g., lore contradiction or missing prerequisite not resolved by the user):

Verdict: **BLOCKED** -- [reason]

## Next Steps

- Run `$cgs-design-review` on the narrative documents for consistency validation.
- Run `$cgs-localize extract` to extract new strings for translation after dialogue is finalized.
- Run `$cgs-dev-story` to implement dialogue triggers and narrative events in-engine.
