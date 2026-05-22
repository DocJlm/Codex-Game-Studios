# Control Manifest

- Gameplay constants live in `GameController`.
- UI never owns gameplay state.
- Reset must go through `GameController.reset_round()`.
- Tests should cover score, timer, win, timeout, and reset behavior.
