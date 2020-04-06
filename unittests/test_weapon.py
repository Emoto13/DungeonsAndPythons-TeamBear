import unittest
import sys

sys.path.append('..')

from items.weapon import Weapon


class TestWeaponClass(unittest.TestCase):

    def test_if_constructor_sets_attributes_correctly(self):
        w = Weapon('Spear', 20)

        self.assertEqual(w.name, 'Spear')
        self.assertEqual(w.damage, 20)

    def test_if_create_weapon_class_method_creates_a_Weapon_instance(self):
        w = Weapon.create_weapon('Spear')
        range_damage = range(1, 21)

        self.assertEqual(Weapon, type(w))
        self.assertEqual(w.name, 'Spear')
        self.assertTrue(w.damage in range_damage)


if __name__ == '__main__':
    unittest.main()
