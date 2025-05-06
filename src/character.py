class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def is_defeated(self):
        return self.hp <= 0

    def attack_target(self, target):
        damage = max(0, self.attack - target.defense)
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.hp = max(0, target.hp - damage)
