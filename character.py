import random

class Character:
    def __init__(self, name, health, attack, defense, special_name):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.special_name = special_name
        self.turn_counter = 0

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        reduced = max(damage - self.defense, 0)
        self.health -= reduced
        return reduced