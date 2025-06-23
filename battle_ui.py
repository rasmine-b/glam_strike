import tkinter as tk

class BattleUi:
    def update_health(player_health_label, enemy_health_label, player, enemy):
        player_health_label.config(text=f"HP: {player.health}/{player.max_health}")
        enemy_health_label.config(text=f"HP: {enemy.health}/{enemy.max_health}")
        