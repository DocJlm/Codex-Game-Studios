extends Control
class_name Hud

@export var score_label_path: NodePath
@export var timer_label_path: NodePath
@export var state_label_path: NodePath

func update_score(score: int) -> void:
    var label := _get_label(score_label_path, "ScoreLabel")
    if label:
        label.text = "Score: %d" % score

func update_timer(time_left: float) -> void:
    var label := _get_label(timer_label_path, "TimerLabel")
    if label:
        label.text = "Time: %.1f" % time_left

func update_state(state: String) -> void:
    var label := _get_label(state_label_path, "StateLabel")
    if label:
        label.text = state.capitalize()

func _get_label(path: NodePath, fallback_name: String) -> Label:
    if path != NodePath(""):
        var explicit_label := get_node_or_null(path) as Label
        if explicit_label:
            return explicit_label
    return get_node_or_null(fallback_name) as Label
