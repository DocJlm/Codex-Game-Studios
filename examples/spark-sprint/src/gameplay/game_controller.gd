extends Node
class_name GameController

signal score_changed(score: int)
signal timer_changed(time_left: float)
signal round_state_changed(state: String)

const ROUND_TIME := 30.0
const TARGET_SCORE := 5

var score := 0
var time_left := ROUND_TIME
var round_state := "playing"

func reset_round() -> void:
    score = 0
    time_left = ROUND_TIME
    round_state = "playing"
    score_changed.emit(score)
    timer_changed.emit(time_left)
    round_state_changed.emit(round_state)

func collect_spark() -> void:
    if round_state != "playing":
        return
    score += 1
    score_changed.emit(score)
    if score >= TARGET_SCORE:
        round_state = "won"
        round_state_changed.emit(round_state)

func tick_timer(delta: float) -> void:
    if round_state != "playing":
        return
    time_left = max(time_left - delta, 0.0)
    timer_changed.emit(time_left)
    if time_left <= 0.0:
        round_state = "lost"
        round_state_changed.emit(round_state)
