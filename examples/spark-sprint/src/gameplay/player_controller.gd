extends CharacterBody2D
class_name PlayerController

@export var speed := 220.0

func _physics_process(_delta: float) -> void:
    var input_vector := Vector2(
        Input.get_axis("move_left", "move_right"),
        Input.get_axis("move_up", "move_down")
    )
    velocity = input_vector.normalized() * speed
    move_and_slide()
