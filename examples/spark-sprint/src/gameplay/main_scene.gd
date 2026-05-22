extends Node2D

@onready var game_controller = $GameController
@onready var player = $Player
@onready var spark = $Spark
@onready var hud = $CanvasLayer/Hud

var _reset_key_down := false

func _ready() -> void:
    game_controller.score_changed.connect(hud.update_score)
    game_controller.timer_changed.connect(hud.update_timer)
    game_controller.round_state_changed.connect(hud.update_state)
    spark.game_controller_path = spark.get_path_to(game_controller)
    reset_round()

func _process(delta: float) -> void:
    game_controller.tick_timer(delta)
    var reset_pressed := Input.is_key_pressed(KEY_R)
    if reset_pressed and not _reset_key_down:
        reset_round()
    _reset_key_down = reset_pressed

func reset_round() -> void:
    player.position = Vector2(320, 240)
    game_controller.reset_round()
    spark.reset_spark()
