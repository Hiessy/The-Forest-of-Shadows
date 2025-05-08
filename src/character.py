class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.health > 0

    def attack_target(self, target):
        damage = max(0, self.attack - target.defense)
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.health = max(0, target.health - damage)
        return damage