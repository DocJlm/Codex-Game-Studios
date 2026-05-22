extends Control
class_name Hud

@export var score_label_path: NodePath
@export var timer_label_path: NodePath
@export var state_label_path: NodePath

func update_score(score: int) -> void:
    var label := get_node_or_null(score_label_path)
    if label:
        label.text = "Score: %d" % score

func update_timer(time_left: float) -> void:
    var label := get_node_or_null(timer_label_path)
    if label:
        label.text = "Time: %.1f" % time_left

func update_state(state: String) -> void:
    var label := get_node_or_null(state_label_path)
    if label:
        label.text = state.capitalize()
