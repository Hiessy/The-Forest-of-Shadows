from src.character import Character

class NPC(Character):
    def __init__(self, name, health=5, attack=1, defense=0, experience=0):
        super().__init__(name, health, attack, defense)
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.experience = experience


    def is_alive(self):
        return self.health > 0


