import tkinter as tk
from tkinter import messagebox
import random

from chloe import Chloe
from lili import Lili
from asuka import Asuka
from xiaoyu import Xiaoyu
from jin import Jin
from hwoarang import Hwoarang
from kazuya import Kazuya
from lee import Lee

from battle_ui import BattleUi

class GlamStrike:
    def __init__(self, root):
        self.root = root
        self.root.title("Glam Strike: Fierce & Flawless")
        self.root.attributes('-fullscreen', True)

        self.ui = BattleUi()

        self.bg_canvas = tk.Canvas(root, bg = "#ffe6f0", highlightthickness=0)
        self.bg_canvas.pack(fill = "both", expand = True)

        self.characters = {
            "Chloe": Chloe,
            "Lili": Lili,
            "Asuka": Asuka,
            "Xiaoyu": Xiaoyu,
            "Jin": Jin,
            "Hwoarang": Hwoarang,
            "Kazuya": Kazuya,
            "Lee": Lee
        }

        self.show_character_selection()
    
    def clear_window(self):
        for widget in self.bg_canvas.winfo_children():
            widget.destroy()
    
    def show_character_selection(self):
        self.clear_window()
        self.selected_player = None

        tk.Label(self.bg_canvas, text = "✨ Choose Your Fighter ✨", font = ('Comic Sans MS', 28, 'bold'),
                 fg = "#cc00cc", bg = "#ffe6f0"). place(relx = 0.5, rely = 0.08, anchor = "center")
        
        girl_names = ["Chloe", "Lili", "Asuka", "Xiaoyu"]
        boy_names = ["Jin", "Hwoarang", "Kazuya", "Lee"]
    
        for i, name in enumerate(girl_names):
            tk.Button(self.bg_canvas, text = name, width = 20, height = 2,
                      font=('Comic Sans MS', 14, 'bold'), bg = "#ffcce6", fg = "#b30059",
                      activebackground = "#ffb3d9",
                      command = lambda name = name: self.select_player(name)).place(relx = 0.3, rely = 0.25 + i * 0.1, anchor = "center")

        for i, name in enumerate(boy_names):
            tk.Button(self.bg_canvas, text = name, width = 20, height = 2,
                      font = ('Comic Sans MS', 14, 'bold'), bg = "#cceeff", fg = "#004466",
                      activebackground = "#b3e0ff",
                      command = lambda name = name: self.select_player(name)).place(relx = 0.7, rely = 0.25 + i * 0.1, anchor = "center")
        
    def select_player(self, name):
        self.selected_player = self.characters[name]()
        self.choose_opponent_screen()

    def choose_opponent_screen(self):
        self.clear_window()

        tk.Label(self.bg_canvas, text="🤜 Choose Your Opponent or Randomize 🤛",
                 font = ('Comic Sans MS', 24, 'bold'), fg = "#3366cc", bg = "#ffe6f0").place(relx = 0.5, rely = 0.1, anchor = "center")
        
        other_names = [name for name in self.characters if type(self.characters[name]()) != type(self.selected_player)]

        for i, name in enumerate(other_names):
            tk.Button(self.bg_canvas, text = name, width = 20, height = 2,
                      font=('Comic Sans MS', 14, 'bold'),
                      bg="#e6f2ff" if name in ["Jin", "Hwoarang", "Kazuya", "Lee"] else "#ffe6f2",
                      fg="#003366" if name in ["Jin", "Hwoarang", "Kazuya", "Lee"] else "#99004d",
                      command = lambda name = name: self.start_battle(name)).place(relx = 0.5, rely = 0.25 + i * 0.1, anchor = "center")
            
        tk.Button(self.bg_canvas, text="🎲 Random Opponent", width = 22, height = 2,
                font=('Comic Sans MS', 14, 'bold'),
                bg = "#e0ccff", fg = "#330066",
                command = self.random_opponent).place(relx = 0.5, rely = 0.8, anchor = "center")
        
    def start_battle(self, opponent_name):
        self.clear_window()
        self.player = self.selected_player
        self.enemy = self.characters[opponent_name]()
        self.create_battle_ui()
        self.ui.update_health(self.player_health, self.enemy_health, self.player, self.enemy)
    
    def random_opponent(self):
        opponent_choices = [name for name in self.characters if type(self.characters[name]()) != type(self.selected_player)]
        self.start_battle(random.choice(opponent_choices))
    
    def create_battle_ui(self):
        tk.Label(self.bg_canvas, text="💥 Battle Begins! 💥", font=("Comic Sans MS", 28, 'bold'), fg = "#cc0099", bg = "#ffe6f0").place(relx = 0.5, rely = 0.05, anchor="center")
        self.player_label = tk.Label(self.bg_canvas, text = self.player.name, font=('Comic Sans MS', 18, 'bold'),
                                     fg = "#ff3399", bg = "#ffe6f0")
        self.player_label.place(relx = 0.2, rely = 0.15)
        self.enemy_label = tk.Label(self.bg_canvas, text=self.enemy.name, font=('Comic Sans MS', 18, 'bold'),
                                    fg = "#9900cc", bg = "#ffe6f0")
        self.enemy_label.place(relx = 0.7, rely = 0.15)
        self.player_health = tk.Label(self.bg_canvas, text="", font=('Comic Sans MS', 14),
                                      fg = "#ff0066", bg = "#ffe6f0")
        self.player_health.place(relx = 0.2, rely = 0.2)
        self.enemy_health = tk.Label(self.bg_canvas, text="", font=('Comic Sans MS', 14),
                                     fg = "#8000ff", bg = "#ffe6f0")
        self.enemy_health.place(relx = 0.7, rely = 0.2)
        self.attack_btn = tk.Button(self.bg_canvas, text="💥 Attack", command = self.attack,
                                    font=('Comic Sans MS', 14, 'bold'),
                                    bg = "#ffb3d9", activebackground = "#ff80bf", width = 15)
        self.attack_btn.place(relx = 0.2, rely = 0.35)
        self.heal_btn = tk.Button(self.bg_canvas, text="💗 Heal", command = self.heal,
                                  font=('Comic Sans MS', 14, 'bold'),
                                  bg = "#ffccff", activebackground = "#ffb3ff", width = 15)
        self.heal_btn.place(relx = 0.4, rely = 0.35)
        self.special_btn = tk.Button(self.bg_canvas, text="✨ Special", command = self.special_move,
                                     font = ('Comic Sans MS', 14, 'bold'),
                                     bg = "#e0b3ff", activebackground = "#cc99ff", width = 15)
        self.special_btn.place(relx = 0.6, rely = 0.35)

        self.exit_btn = tk.Button(self.bg_canvas, text = "Exit", command = self.root.destroy,
                                  font=('Comic Sans MS', 12), bg = "#ffd6e8")
        self.exit_btn.place(relx = 0.9, rely = 0.05)

        self.log = tk.Text(self.bg_canvas, height = 12, width = 80, state = 'disabled',
                           font=('Comic Sans MS', 12), bg = "#fff0f5")
        self.log.place(relx = 0.5, rely = 0.65, anchor = "center")

        self.ui.style_log_widget(self.log)
        self.enable_buttons()

    def disable_buttons(self):
        self.attack_btn.config(state = 'disabled')
        self.heal_btn.config(state = 'disabled')
        self.special_btn.config(state = 'disabled')
    
    def enable_buttons(self):
        self.attack_btn.config(state = 'normal')
        self.heal_btn.config(state = 'normal')
        self.special_btn.config(state = 'normal')

    def player_turn_wrapper(self, func):
        self.disable_buttons()
        func()
        self.ui.update_health(self.player_health, self.enemy_health, self.player, self.enemy)
        if not self.enemy.is_alive():
            self.ui.log_message(self.log, "You slayed the runway! 💖", "system")
            self.end_game("Victory 👑")
        else:
            self.root.after(1000, self.enemy_turn)
        
    def attack(self):
        def _attack():
            damage = self.player.deal_damage()
            actual = self.enemy.take_damage(damage)
            self.ui.log_message(self.log, f"{self.player.name} attacks for {actual} 💥", "player")
            self.ui.show_damage_popup(self.bg_canvas, 700, 200, actual, color="#ff0033")
            self.ui.shake_widget(self.enemy_label)
        
        self.player_turn_wrapper(_attack)
    
    def heal(self):
        def _heal():
            heal_amount = random.randint(10, 20)
            self.player.health = min(self.player.health + heal_amount, self.player.max_health) 
            self.ui.log_message(self.log, f"{self.player.name} heals {heal_amount} 💅", "heal")
        self.player_turn_wrapper(_heal)   

    def special_move(self):
        def _special():
            if self.player.turn_counter % 3 == 0:
                damage = self.player.special_attack()
                actual = self.enemy.take_damage(damage)
                self.ui.log_message(self.log, f"{self.player.name} used {self.player.special_name} for {actual} ✨", "player")
                self.ui.show_damage_popup(self.bg_canvas, 700, 200, actual, color="#9900cc")
                self.ui.shake_widget(self.enemy_label)
            else:
                self.ui.log_message(self.log, "✨ Special not ready yet! (Every 3 turns)", "system")
            self.player.turn_counter += 1
        self.player_turn_wrapper(_special)
    
    def enemy_turn(self):
        if not self.enemy.is_alive():
            return
        move = random.choice(["attack", "attack", "heal"])
        if move == "attack":
            damage = self.enemy.deal_damage()
            actual = self.player.take_damage(damage)
            self.ui.log_message(self.log, f"{self.enemy.name} strikes back for {actual} ⚔️", "enemy")
            self.ui.show_damage_popup(self.bg_canvas, 250, 200, actual, color="#6600cc")
            self.ui.shake_widget(self.player_label)
        else:
            heal = random.randint(8, 15)
            self.enemy.health = min(self.enemy.health + heal, self.enemy.max_health)
            self.ui.log_message(self.log, f"{self.enemy.name} restored {heal} 🧘‍♂️", "heal")
        self.ui.update_health(self.player_health, self.enemy_health, self.player, self.enemy)
        if not self.player.is_alive():
            self.ui.log_message(self.log, "You lost your sparkle... 💔", "system")
            self.end_game("Defeat 😭")
        else:
            self.root.after(5000, self.enable_buttons)

    def end_game(self, result):
        self.disable_buttons()
        self.ui.log_message(self.log, "\n🎮 What would you like to do next?", "system")
        tk.Button(self.bg_canvas, text="🔁 Choose Another Opponent", font=('Comic Sans MS', 12, 'bold'),
              bg="#ffd6e8", command=self.show_character_selection).place(relx = 0.65, rely = 0.9, anchor = "center")
        messagebox.showinfo("🎀 Battle Result", result)


    