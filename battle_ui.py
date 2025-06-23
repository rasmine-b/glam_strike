import tkinter as tk

class BattleUi:
    def update_health(player_health_label, enemy_health_label, player, enemy):
        player_health_label.config(text=f"HP: {player.health}/{player.max_health}")
        enemy_health_label.config(text=f"HP: {enemy.health}/{enemy.max_health}")

    def log_message(log_widget, message, tag=None):
        log_widget.config(state='normal')
        log_widget.insert('end', message + '\n', tag)
        log_widget.see('end')
        log_widget.config(state='disabled')
        