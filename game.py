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