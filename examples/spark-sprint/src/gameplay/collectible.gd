extends Area2D
class_name Collectible

@export var game_controller_path: NodePath

func _on_body_entered(_body: Node) -> void:
    var controller := get_node_or_null(game_controller_path)
    if controller and controller.has_method("collect_spark"):
        controller.collect_spark()
        queue_free()
