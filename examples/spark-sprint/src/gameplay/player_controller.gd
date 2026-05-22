extends CharacterBody2D
class_name PlayerController

@export var speed := 220.0
@export var play_area_min := Vector2(24, 100)
@export var play_area_max := Vector2(616, 392)

func _physics_process(_delta: float) -> void:
    var input_vector := _read_input()
    velocity = input_vector.normalized() * speed
    move_and_slide()
    position.x = clampf(position.x, play_area_min.x, play_area_max.x)
    position.y = clampf(position.y, play_area_min.y, play_area_max.y)

func _read_input() -> Vector2:
    var input_vector := Vector2.ZERO
    if Input.is_action_pressed("move_left") or Input.is_key_pressed(KEY_A) or Input.is_key_pressed(KEY_LEFT):
        input_vector.x -= 1.0
    if Input.is_action_pressed("move_right") or Input.is_key_pressed(KEY_D) or Input.is_key_pressed(KEY_RIGHT):
        input_vector.x += 1.0
    if Input.is_action_pressed("move_up") or Input.is_key_pressed(KEY_W) or Input.is_key_pressed(KEY_UP):
        input_vector.y -= 1.0
    if Input.is_action_pressed("move_down") or Input.is_key_pressed(KEY_S) or Input.is_key_pressed(KEY_DOWN):
        input_vector.y += 1.0
    return input_vector
