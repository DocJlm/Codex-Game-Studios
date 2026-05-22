extends Area2D
class_name Collectible

@export var game_controller_path: NodePath
@export var play_area_min := Vector2(80, 120)
@export var play_area_max := Vector2(560, 360)

func _ready() -> void:
    var callback := Callable(self, "_on_body_entered")
    if not body_entered.is_connected(callback):
        body_entered.connect(callback)

func reset_spark() -> void:
    visible = true
    monitoring = true
    randomize_position()

func _on_body_entered(_body: Node) -> void:
    var controller := get_node_or_null(game_controller_path)
    if controller and controller.has_method("collect_spark"):
        controller.collect_spark()
        if controller.round_state == "playing":
            randomize_position()
        else:
            visible = false
            monitoring = false

func randomize_position() -> void:
    position = Vector2(
        randf_range(play_area_min.x, play_area_max.x),
        randf_range(play_area_min.y, play_area_max.y)
    )
