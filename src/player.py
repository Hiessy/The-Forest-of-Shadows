from src.character import Character


class Player(Character):
    def __init__(self, name):
        super().__init__(name, hp=100, attack=10, defense=5)
        self.level = 1
        self.exp = 0
        self.mp = 50
        self.max_mp = 50
        self.exp_to_next_level = 100
        self.spells = {
            "fireball": {"cost": 10, "type": "damage", "amount": 25},
            "heal": {"cost": 8, "type": "heal", "amount": 20}
        }

    def cast_spell(self, spell_name, target=None):
        spell = self.spells.get(spell_name.lower())
        if not spell:
            print("❌ Unknown spell.")
            return False

        if self.mp < spell["cost"]:
            print("❌ Not enough mana!")
            return False

        self.mp -= spell["cost"]
        if spell["type"] == "damage":
            if target:
                target.hp = max(0, target.hp - spell["amount"])
                print(f"🔥 {self.name} casts {spell_name} and hits {target.name} for {spell['amount']} damage!")
        elif spell["type"] == "heal":
            healed = min(spell["amount"], self.max_hp - self.hp)
            self.hp += healed
            print(f"💖 {self.name} casts {spell_name} and heals for {healed} HP!")

        return True

    def gain_exp(self, amount):
        print(f"{self.name} gains {amount} EXP.")
        self.exp += amount
        while self.exp >= self.exp_to_next_level:
            self.exp -= self.exp_to_next_level
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp_to_next_level = 100 + (self.level - 1) * 50
        self.max_hp += 20
        self.max_mp += 10
        self.attack += 5
        self.defense += 2
        self.hp = self.max_hp
        self.mp = self.max_mp
        print(f"\n🎉 {self.name} leveled up to level {self.level}!")
        print(f"Stats: HP: {self.max_hp}, MP: {self.max_mp}, ATK: {self.attack}, DEF: {self.defense}\n")
