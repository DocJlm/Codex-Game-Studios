# Core Loop GDD

## Loop Summary

Each night asks the player to deliver one or more moon-bound parcels before time runs out.

```text
Briefing -> choose delivery -> inspect map -> plan route -> travel -> avoid light/risk -> use tool -> deliver -> score/debrief -> next night
```

## Primary Verbs

- Accept
- Inspect
- Plan
- Move
- Hide
- Unlock
- Mark
- Deliver
- Debrief

## Night Structure

1. **Briefing**
   - NPC gives delivery destination, time limit, package restriction, and optional rumor.
2. **Planning**
   - Player reviews known routes, light patrols, closures, and available tools.
3. **Transit**
   - Player navigates the district, reacts to light sweeps, and spends tools.
4. **Delivery**
   - Player reaches the drop point and resolves delivery outcome.
5. **Debrief**
   - Game awards time, route, discretion, and optional objective ratings.

## Risk Families

| Risk | Player Read | Failure Pressure | Counterplay |
| --- | --- | --- | --- |
| Patrol light | Moving cone or lamp sweep | Package exposure meter rises | Wait, route around, use Shade Cloak |
| Time pressure | Moon clock and job timer | Delivery expires | Plan shorter route, use Shortcut Key |
| Route blockage | Closed gate, fog wall, one-way alley | Forces detour | Use Moonmark, learn district state |

## Tools

| Tool | Use | Limit |
| --- | --- | --- |
| Shade Cloak | Ignore one brief light exposure | Single charge per night |
| Shortcut Key | Open one locked alley gate | Consumed on use |
| Quiet Bell | Freeze one patrol for a few seconds | Cooldown, limited charges |
| Moonmark | Mark one discovered hazard on map | Persists as route knowledge |

## Progression

- New districts unlock through story deliveries.
- Tools unlock one at a time across the first four nights.
- New delivery modifiers appear after the player understands the base loop.
- Daily Challenge recombines authored destinations, timers, and hazard patterns without requiring large procedural generation.

## Fail States

- Timer expires.
- Package exposure reaches the limit.
- Player abandons route from pause menu.

Failure returns to debrief with useful feedback and lets the player retry the night quickly.

## Win State

A night is complete when all required parcels are delivered and the courier reaches the safe return point or the story explicitly ends the night at the destination.

## MVP Acceptance

- Player can complete a full delivery in under 12 minutes.
- At least one route decision is meaningfully different between two attempts.
- At least one tool use creates a memorable shortcut or save.
- Failure explains what went wrong without shaming the player.
