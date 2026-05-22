# Spark Sprint Smoke Checklist

This is a manual checklist for a future runnable Godot version. CI only validates the static example shape.

- Launch: main scene opens without script errors.
- Movement: arrow/WASD bindings move the player in four directions.
- Success path: collecting 5 sparks sets state to `won`.
- Timeout path: timer reaching zero sets state to `lost`.
- Reset path: reset returns score to 0, timer to 30, and state to `playing`.
