import unittest 
from items.spell import Spell


class TestSpellClass(unittest.TestCase):

    def test_if_constructor_sets_attributes_correctly(self):
        s = Spell(name = 'Fireball',damage =  20, mana_cost = 5, cast_range = 3)

        self.assertEqual(s.name,'Fireball')
        self.assertEqual(s.damage, 20)
        self.assertEqual(s.mana_cost, 5)
        self.assertEqual(s.cast_range, 3)

    def test_if_create_spell_class_method_creates_a_Spell_instance(self):
        s = Spell.create_spell('Fireball')

        self.assertEqual(s.name, 'Fireball')
        self.assertEqual(Spell,type(s))


if __name__ == '__main__':
    unittest.main()