import unittest
import sys

sys.path.append('..')

from items.spell import Spell


class TestSpellClass(unittest.TestCase):

    def test_if_constructor_sets_attributes_correctly(self):
        s = Spell(name='Fireball', damage=20, mana_cost=5, cast_range=3)

        self.assertEqual(s.name, 'Fireball')
        self.assertEqual(s.damage, 20)
        self.assertEqual(s.mana_cost, 5)
        self.assertEqual(s.cast_range, 3)

    def test_if_create_spell_class_method_creates_a_Spell_instance(self):
        s = Spell.create_spell('Fireball')
        range_damage = range(1, 21)
        range_mana_cost = range(1, 11)
        range_cast_range = range(1, 4)

        self.assertEqual(Spell, type(s))
        self.assertEqual(s.name, 'Fireball')
        self.assertTrue(s.damage in range_damage)
        self.assertTrue(s.mana_cost in range_mana_cost)
        self.assertTrue(s.cast_range in range_cast_range)


if __name__ == '__main__':
    unittest.main()
