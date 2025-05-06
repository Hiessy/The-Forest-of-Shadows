from src.character import Character


class Enemy(Character):
    def __init__(self, name, hp, attack, defense=0, exp=0):
        super().__init__(name, hp, attack, defense)
        self.exp = exp

