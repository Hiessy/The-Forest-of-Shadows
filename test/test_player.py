import unittest
from src.character import Character
from src.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("TestHero")
        self.enemy = Character("TestEnemy", health=100, attack=5, defense=2)

    def test_initial_stats(self):
        """Test that player initializes with correct stats"""
        self.assertEqual(self.player.name, "TestHero")
        self.assertEqual(self.player.health, 100)
        self.assertEqual(self.player.max_health, 100)
        self.assertEqual(self.player.attack, 10)
        self.assertEqual(self.player.defense, 5)
        self.assertEqual(self.player.level, 1)
        self.assertEqual(self.player.exp, 0)
        self.assertEqual(self.player.mp, 50)
        self.assertEqual(self.player.max_mp, 50)
        self.assertEqual(self.player.exp_to_next_level, 100)
        self.assertIn("fireball", self.player.spells)
        self.assertIn("heal", self.player.spells)

    def test_cast_spell_damage(self):
        """Test casting a damage spell on a target"""
        initial_enemy_hp = self.enemy.health
        spell_damage = self.player.spells["fireball"]["amount"]

        result = self.player.cast_spell("fireball", self.enemy)

        self.assertTrue(result)
        self.assertEqual(self.enemy.health, initial_enemy_hp - spell_damage)
        self.assertEqual(self.player.mp, 50 - self.player.spells["fireball"]["cost"])

    def test_cast_spell_heal(self):
        """Test casting a heal spell"""
        # Damage player first
        self.player.health = 50
        initial_hp = self.player.health
        heal_amount = self.player.spells["heal"]["amount"]

        result = self.player.cast_spell("heal")

        self.assertTrue(result)
        self.assertEqual(self.player.health, initial_hp + heal_amount)
        self.assertEqual(self.player.mp, 50 - self.player.spells["heal"]["cost"])

    def test_cast_spell_insufficient_mp(self):
        """Test casting with insufficient MP"""
        self.player.mp = 5  # Too low for any spell

        result = self.player.cast_spell("fireball", self.enemy)

        self.assertFalse(result)
        self.assertEqual(self.player.mp, 5)  # Should remain unchanged

    def test_cast_unknown_spell(self):
        """Test casting a non-existent spell"""
        result = self.player.cast_spell("meteor_shower")

        self.assertFalse(result)

    def test_gain_exp_level_up(self):
        """Test gaining enough EXP to level up"""
        initial_level = self.player.level
        initial_stats = {
            'max_health': self.player.max_health,
            'max_mp': self.player.max_mp,
            'attack': self.player.attack,
            'defense': self.player.defense
        }

        # Gain exactly enough EXP to level up once
        self.player.gain_exp(100)

        self.assertEqual(self.player.level, initial_level + 1)
        self.assertEqual(self.player.exp, 0)
        self.assertEqual(self.player.exp_to_next_level, 150)  # 100 + (2-1)*50
        self.assertEqual(self.player.max_health, initial_stats['max_health'] + 20)
        self.assertEqual(self.player.max_mp, initial_stats['max_mp'] + 10)
        self.assertEqual(self.player.attack, initial_stats['attack'] + 5)
        self.assertEqual(self.player.defense, initial_stats['defense'] + 2)
        self.assertEqual(self.player.health, self.player.max_health)  # Full heal
        self.assertEqual(self.player.mp, self.player.max_mp)  # Full mana restore

    def test_gain_exp_multiple_levels(self):
        """Test gaining enough EXP for multiple level ups"""
        # Gain enough EXP for 2 level ups (100 + 150 = 250)
        self.player.gain_exp(250)

        self.assertEqual(self.player.level, 3)
        self.assertEqual(self.player.exp, 0)  # 250 - (100 + 150) = 0
        self.assertEqual(self.player.exp_to_next_level, 200)  # 100 + (3-1)*50

    def test_gain_exp_partial(self):
        """Test gaining partial EXP (not enough to level up)"""
        self.player.gain_exp(50)

        self.assertEqual(self.player.level, 1)
        self.assertEqual(self.player.exp, 50)
        self.assertEqual(self.player.exp_to_next_level, 100)

    def test_heal_does_not_exceed_max_hp(self):
        """Test that healing doesn't exceed max HP"""
        self.player.health = self.player.max_health - 5  # 5 HP below max
        heal_amount = self.player.spells["heal"]["amount"]  # 20

        self.player.cast_spell("heal")

        self.assertEqual(self.player.health, self.player.max_health)  # Should only heal 5, not 20

    def test_damage_does_not_go_below_zero(self):
        """Test that damage doesn't reduce HP below zero"""
        self.enemy.health = 10
        spell_damage = self.player.spells["fireball"]["amount"]  # 25

        self.player.cast_spell("fireball", self.enemy)

        self.assertEqual(self.enemy.health, 0)  # Not -15
        self.assertEqual(spell_damage, 25)  # Not -15


if __name__ == '__main__':
    unittest.main()