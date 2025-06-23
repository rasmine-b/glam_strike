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