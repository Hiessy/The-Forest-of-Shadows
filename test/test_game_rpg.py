import unittest

from src.npc import Enemy
from src.player import Player


class TestRPG(unittest.TestCase):

    def test_player_initialization(self):
        """Test that a new player starts with correct default stats."""
        player = Player("Hero")
        self.assertEqual(player.name, "Hero")
        self.assertEqual(player.level, 1)
        self.assertEqual(player.hp, player.max_hp)
        self.assertEqual(player.mp, player.max_mp)

    def test_player_gain_exp_and_level_up(self):
        """Test that gaining experience levels the player up properly."""
        player = Player("Hero")
        player.exp = 90
        player.gain_exp(15)  # Should trigger level up
        self.assertEqual(player.level, 2)
        self.assertEqual(player.exp, 5)  # 105 total, 100 needed
        self.assertGreater(player.max_hp, 100)
        self.assertGreater(player.max_mp, 50)

    def test_player_multiple_level_ups(self):
        """Test that the player can level up multiple times at once."""
        player = Player("Hero")
        player.gain_exp(300)
        self.assertEqual(player.level, 3)
        self.assertEqual(player.exp, 50)

    def test_spell_heal_increases_hp(self):
        """Test that the 'heal' spell restores health and reduces MP."""
        player = Player("Hero")
        player.hp = 50
        result = player.cast_spell("heal")
        self.assertTrue(result)
        self.assertGreater(player.hp, 50)
        self.assertEqual(player.mp, 42)

    def test_spell_heal_caps_at_max_hp(self):
        """Test that healing does not exceed max HP."""
        player = Player("Hero")
        player.hp = player.max_hp - 5
        player.cast_spell("heal")
        self.assertLessEqual(player.hp, player.max_hp)

    def test_spell_fireball_damages_enemy(self):
        """Test that the 'fireball' spell decreases enemy HP."""
        player = Player("Hero")
        enemy = Enemy("Dummy", hp=30, attack=5, exp=10)
        result = player.cast_spell("fireball", enemy)
        self.assertTrue(result)
        self.assertLess(enemy.hp, 30)
        self.assertEqual(player.mp, 40)

    def test_spell_cast_insufficient_mp(self):
        """Test that a spell fails when player has insufficient MP."""
        player = Player("Hero")
        player.mp = 5  # Too low for heal (costs 8)
        result = player.cast_spell("heal")
        self.assertFalse(result)

    def test_spell_invalid_name(self):
        """Test that an invalid spell name returns False."""
        player = Player("Hero")
        result = player.cast_spell("lightning")  # Not defined
        self.assertFalse(result)

    def test_enemy_attack_damage_to_player(self):
        """Test that enemy attacks reduce player HP correctly."""
        player = Player("Hero")
        enemy = Enemy("Goblin", hp=10, attack=12, defense=2, exp=5)
        old_hp = player.hp
        enemy.attack_target(player)
        expected_damage = max(0, enemy.attack - player.defense)
        self.assertEqual(player.hp, old_hp - expected_damage)

    def test_player_attack_enemy(self):
        """Test that player's attack reduces enemy HP."""
        player = Player("Hero")
        enemy = Enemy("Goblin", hp=30, attack=5, exp=10)
        old_hp = enemy.hp
        player.attack_target(enemy)
        self.assertLess(enemy.hp, old_hp)

    def test_enemy_death_on_zero_hp(self):
        """Test that an enemy is flagged as dead at 0 HP."""
        enemy = Enemy("Goblin", hp=5, attack=5, exp=10)
        enemy.hp = 0
        self.assertTrue(enemy.is_defeated())

    def test_player_death(self):
        """Test that a player at 0 HP is dead."""
        player = Player("Hero")
        player.hp = 0
        self.assertTrue(player.is_defeated())

if __name__ == '__main__':
    unittest.main()
