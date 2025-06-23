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

from battle_ui import BatteleUi

class GlamStrike:
    def __init__(self, root):
        self.root.title("Glam Strike: Fierce & Flawless")
        self.root.attributes('-fullscreen', True)

        self.ui = BattleUi()

        self.bg_canvas = tk.Canvas(root, bg="#ffe6f0", highlightthickness=0)
        self.bg_canvas.pack(fill="both", expand=True)

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

        tk.Label(self.bg_canvas, text="✨ Choose Your Fighter ✨", font=('Comic Sans MS', 28, 'bold'),
                 fg="#cc00cc", bg="#ffe6f0"). place(relx=0.5, rely=0.08, anchor="center")
        
        girl_names = ["Chloe", "Lili", "Asuka", "Xiaoyu"]
        boy_names = ["Jin", "Hwoarang", "Kazuya", "Lee"]
    
        for i, name in enumerate(girl_names):
            tk.Button(self.bg_canvas, text=name, width=20, height=2,
                      font=('Comic Sans MS', 14, 'bold'), bg="#ffcce6", fg="#b30059",
                      activebackground="#ffb3d9",
                      command=lambda n=name: self.select_player(n)).place(relx=0.3, rely=0.25 + i * 0.1, anchor="center")

        for i, name in enumerate(boy_names):
            tk.Button(self.bg_canvas, text=name, width=20, height=2,
                      font=('Comic Sans MS', 14, 'bold'), bg="#cceeff", fg="#004466",
                      activebackground="#b3e0ff",
                      command=lambda name=name: self.select_player(name)).place(relx=0.7, rely=0.25 + i * 0.1, anchor="center")
        
    def select_player(self, name):
        self.selected_player = self.characters[name]()
        self.choose_opponent_screen()

    def choose_opponent_screen(self):
        self.clear_window()

        tk.Label(self.bg_canvas, text="🤜 Choose Your Opponent or Randomize 🤛",
                 font=('Comic Sans MS', 24, 'bold'), fg="#3366cc", bg="#ffe6f0").place(relx=0.5, rely=0.1, anchor="center")
        
        other_names = [name for name in self.characters if self.character[n] != type(self.selecter_player)]

        for i, name in enumerate(other_names):
            tk.Button(self.bg_canvas, text=name, width=20, height=2,
                      font=('Comic Sans MS', 14, 'bold'),
                      bg="#e6f2ff" if name in ["Jin", "Hwoarang", "Kazuya", "Lee"] else "#ffe6f2",
                      fg="#003366" if name in ["Jin", "Hwoarang", "Kazuya", "Lee"] else "#99004d",
                      command=lambda name=name: self.start_battle(name)).place(relx=0.5, rely=0.25 + i * 0.1, anchor="center")
            
        tk.Button(self.bg_canvas, text="🎲 Random Opponent", width=22, height=2,
                font=('Comic Sans MS', 14, 'bold'),
                bg="#e0ccff", fg="#330066",
                command=self.random_opponent).place(relx=0.5, rely=0.8, anchor="center")
