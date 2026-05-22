# Core Loop System

## Player Goal

Collect 5 sparks before the 30-second timer reaches zero.

## Rules

- The round starts in `playing` state.
- Each spark pickup increments score by 1.
- The player wins when score reaches `target_score`.
- The player loses when time reaches zero before the target score.
- Reset restores score, timer, and state.

## Acceptance Criteria

- Movement accepts four-direction input.
- Spark pickup increments score.
- Timer reaching zero ends the round.
- Reset restores initial score, time, and state.
