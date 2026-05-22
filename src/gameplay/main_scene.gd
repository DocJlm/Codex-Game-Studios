extends Node2D

@onready var player = $Player
@onready var status_label: Label = $CanvasLayer/Hud/StatusLabel

func _ready() -> void:
    player.position = Vector2(160, 560)
    status_label.text = "Moonlight Dispatch prototype v0.2.0 - movement and route bounds"
