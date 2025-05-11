# Refactored game_rpg.py as game_engine.py

from player import Player
from npc import NPC
import random

class GameEngine:
    def __init__(self, player_name):
        self.player = Player(player_name)
        self.npcs = []  # List of NPCs in the world
        self.current_enemy = None

    def spawn_enemy(self):
        # Create a new enemy and add it to the list
        enemy = random.choice([
            NPC("Goblin", 15, 6, 4, experience=20),
            NPC("Skeleton", 25, 7, 7, experience=30),
            NPC("Wolf", 20, 6, 5, experience=25)
        ])
        self.npcs.append(enemy)
        return enemy

    def check_for_encounter(self):
        # Simple random chance of encounter
        if random.random() < 0.3:  # 30% chance
            self.current_enemy = self.spawn_enemy()
            return True
        return False

    def engage_combat(self):
        if not self.current_enemy:
            return "There is no enemy to fight."

        combat_log = []
        while self.player.is_alive() and self.current_enemy.is_alive():
            dmg_to_enemy = self.player.attack_target(self.current_enemy)
            combat_log.append(f"You dealt {dmg_to_enemy} damage to {self.current_enemy.name}.")

            if self.current_enemy.is_alive():
                dmg_to_player = self.current_enemy.attack_target(self.player)
                combat_log.append(f"{self.current_enemy.name} dealt {dmg_to_player} damage to you.")

        if self.player.is_alive():
            combat_log.append(f"You defeated {self.current_enemy.name}!")
            self.player.gain_exp(self.current_enemy.experience)
        else:
            combat_log.append("You have been defeated...")

        self.current_enemy = None  # Reset enemy after combat
        return combat_log

    def get_player_stats(self):
        return {
            "name": self.player.name,
            "health": self.player.health,
            "attack": self.player.attack,
            "defense": self.player.defense,
            "experience": self.player.exp
        }

    def get_enemy_stats(self):
        if not self.current_enemy:
            return None
        return {
            "name": self.current_enemy.name,
            "health": self.current_enemy.health,
            "attack": self.current_enemy.attack,
            "defense": self.current_enemy.defense,
            "experience": self.current_enemy.experience
        }

    def is_player_alive(self):
        return self.player.is_alive()
