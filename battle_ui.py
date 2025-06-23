import tkinter as tk

class BattleUi:
    def __init__(self):
        pass

    def update_health(self, player_health_label, enemy_health_label, player, enemy):
        player_health_label.config(text=f"HP: {player.health}/{player.max_health}")
        enemy_health_label.config(text=f"HP: {enemy.health}/{enemy.max_health}")

    def log_message(self, log_widget, message, tag=None):
        log_widget.config(state='normal')
        if tag:
            log_widget.insert('end', message + '\n', tag)
        else:
            log_widget.insert('end', message + '\n')
        log_widget.see('end')
        log_widget.config(state='disabled')

    def style_log_widget(self, widget):
        widget.tag_config("player", foreground="#ff3399", font=("Comic Sans MS", 12, "bold"))
        widget.tag_config("enemy", foreground="#6600cc", font=("Comic Sans MS", 12, "bold"))
        widget.tag_config("heal", foreground="#009966", font=("Comic Sans MS", 12, "italic"))
        widget.tag_config("system", foreground="#999999", font=("Comic Sans MS", 11))

    def show_damage_popup(self, canvas, x, y, damage, color="#ff0000"):
        bg_color = canvas["bg"] if "bg" in canvas.keys() else "#ffffff"
        popup = tk.Label(canvas, text=f"-{damage}", font=("Comic Sans MS", 16, "bold"), fg=color, bg=bg_color)
        popup.place(x=x, y=y)
        self.animate_float(popup)

    def animate_float(self, widget, distance=40, speed=20):
        def float_step(step=0):
            if step >= distance:
                widget.destroy()
            else:
                widget.place_configure(y=widget.winfo_y() - 1)
                widget.after(speed, lambda: float_step(step + 1))
        float_step()

    def shake_widget(self, widget, intensity=8, duration=200):
        place_info = widget.place_info()
        if "relx" in place_info:
            return

        orig_x = int(place_info.get("x", 0))

        def shake(count=0):
            if count >= duration:
                widget.place_configure(x=orig_x)
            else:
                offset = intensity if count % 2 == 0 else -intensity
                widget.place_configure(x=orig_x + offset)
                widget.after(10, lambda: shake(count + 10))
        shake()