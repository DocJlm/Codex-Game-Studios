extends RefCounted

# Static GDScript-style test draft for documentation and review.

func test_collect_spark_increments_score() -> void:
    var controller := GameController.new()
    controller.collect_spark()
    assert(controller.score == 1)

func test_target_score_wins_round() -> void:
    var controller := GameController.new()
    for index in range(controller.TARGET_SCORE):
        controller.collect_spark()
    assert(controller.round_state == "won")

func test_timer_timeout_loses_round() -> void:
    var controller := GameController.new()
    controller.tick_timer(controller.ROUND_TIME)
    assert(controller.round_state == "lost")

func test_reset_restores_initial_values() -> void:
    var controller := GameController.new()
    controller.collect_spark()
    controller.tick_timer(5.0)
    controller.reset_round()
    assert(controller.score == 0)
    assert(controller.time_left == controller.ROUND_TIME)
    assert(controller.round_state == "playing")
