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

    def style_log_widget(widget):
        widget.tag_config("player", foreground="#ff3399", font=("Comic Sans MS", 12, "bold"))
        widget.tag_config("enemy", foreground="#6600cc", font=("Comic Sans MS", 12, "bold"))
        widget.tag_config("heal", foreground="#009966", font=("Comic Sans MS", 12, "italic"))
        widget.tag_config("system", foreground="#999999", font=("Comic Sans MS", 11))

    def show_damage_popup(canvas, x, y, damage, color="#ff0000"):
        popup = tk.Label(canvas, text=f"-{damage}", font=("Comic Sans MS", 16, "bold"))
        popup.place(x=x, y=y)
        animate_float(popup, distance = 50, speed = 20)

    def animate_float(widget, distance = 50, speed = 20):
        def float_step(step = 0):
            if step >= distance:
                widget.destroy()
            else:
                widget.place_config(y=widget.winfo_y() - 1)
                widget.after(speed, lambda: float_step(step + 1))
        float_step()
    
    def shake_widget(widget, intensity=3, duration=200):
        orig_x = widget.winfo_x()
        def shake(count=0):
            if count >= duration:
                widget.place_configure(x=orig_x)
            else:
                offset = intensity if count % 2 == 0 else -intensity
                widget.place_configure(x=orig_x + offset)
                widget.after(10, lambda: shake(count + 10))
        shake()