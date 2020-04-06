import unittest
import sys

sys.path.append('..')

from entities.hero import Hero
from items.spell import Spell
from items.weapon import Weapon


class TestHeroClass(unittest.TestCase):

    def test_if_know_as_works_as_expected(self):
        h = Hero()
        exp = 'Hero the No title'
        self.assertEqual(h.known_as(), exp)

    def test_if_attack_returns_spell_damage_if_it_is_stronger(self):
        h = Hero()
        h.spell = Spell('Fireball', 10, 5, 1)
        h.weapon = Weapon('Bat', 5)

        self.assertEqual(h.attack(), 10)

    def test_if_attack_returns_weapon_damagae_if_it_is_stronger(self):
        h = Hero()
        h.spell = Spell('Fireball', 10, 5, 1)
        h.weapon = Weapon('Bat', 20)

        self.assertEqual(h.attack(), 20)

    def test_if_attack_by_spell_returns_spell_damage(self):
        h = Hero()
        h.spell = Spell('Fireball', 10, 5, 1)

        self.assertEqual(h.attack(), 10)


if __name__ == '__main__':
    unittest.main()
