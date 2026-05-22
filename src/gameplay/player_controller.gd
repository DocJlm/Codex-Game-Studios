extends CharacterBody2D
class_name MoonlightPlayerController

const GAMEPAD_DEADZONE := 0.22

@export var movement_speed := 230.0
@export var play_area_min := Vector2(72, 96)
@export var play_area_max := Vector2(1208, 624)

func _physics_process(_delta: float) -> void:
    var input_vector := _read_input_vector()
    velocity = input_vector * movement_speed
    move_and_slide()
    position.x = clampf(position.x, play_area_min.x, play_area_max.x)
    position.y = clampf(position.y, play_area_min.y, play_area_max.y)

func _read_input_vector() -> Vector2:
    var input_vector := Input.get_vector("move_left", "move_right", "move_up", "move_down")

    if Input.is_key_pressed(KEY_A) or Input.is_key_pressed(KEY_LEFT):
        input_vector.x -= 1.0
    if Input.is_key_pressed(KEY_D) or Input.is_key_pressed(KEY_RIGHT):
        input_vector.x += 1.0
    if Input.is_key_pressed(KEY_W) or Input.is_key_pressed(KEY_UP):
        input_vector.y -= 1.0
    if Input.is_key_pressed(KEY_S) or Input.is_key_pressed(KEY_DOWN):
        input_vector.y += 1.0

    var connected_pads := Input.get_connected_joypads()
    if not connected_pads.is_empty():
        var device_id: int = connected_pads[0]
        var axis_vector := Vector2(
            Input.get_joy_axis(device_id, JOY_AXIS_LEFT_X),
            Input.get_joy_axis(device_id, JOY_AXIS_LEFT_Y)
        )
        if axis_vector.length() >= GAMEPAD_DEADZONE:
            input_vector += axis_vector

    return input_vector.limit_length(1.0)
