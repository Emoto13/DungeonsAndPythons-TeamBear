import unittest
from entities.base_entity import BaseEntity
from items.weapon import Weapon
from items.spell import Spell


class Skeleton(BaseEntity):

    def attack():
        pass

class TestBaseEntity(unittest.TestCase):

    def test_if_class_can_be_inherted_correctly(self):

        self.assertTrue(issubclass(Skeleton,BaseEntity))

    def test_if_constructor_sets_attributes_correctly(self):
        a = Skeleton(health = 20, mana = 10)

        self.assertEqual(a.health, 20)
        self.assertEqual(a.mana, 10)
        self.assertEqual(type(a.weapon), Weapon)
        self.assertEqual(type(a.spell), Spell)
        self.assertEqual(a.MAX_MANA, 10)
        self.assertEqual(a.MAX_HEALTH, 20)

    def test_if_get_health_returns_current_health(self):
        a = Skeleton(health = 20, mana = 10)

        self.assertEqual(a.get_health(), 20)

    def test_if_get_mana_returns_current_mana(self):
        a = Skeleton(health = 20, mana = 10)

        self.assertEqual(a.get_mana(), 10)

    def test_if_take_damage_removes_health_from_character_when_alive(self):
        a = Skeleton(health = 20, mana = 10)
        a.take_damage(5)

        self.assertEqual(a.health, 15)

    def test_if_take_damage_sets_health_to_zero_if_hero_is_dealt_more_damage_than_the_healt_he_has(self):
        a = Skeleton(health = 20, mana = 10)
        a.take_damage(300)

        self.assertEqual(a.health, 0)

    def test_if_is_alive_returns_true_if_health_is_above_zero(self):
        a = Skeleton(health = 20, mana = 10)

        self.assertTrue(a.is_alive())
    
    def test_if_is_alive_return_false_if_health_is_zero(self):
        a = Skeleton(health = 20, mana = 10)
        a.take_damage(20)

        self.assertFalse(a.is_alive())

    def test_if_take_healing_returns_true_if_successful(self):
        a = Skeleton(health = 20, mana = 10)

        self.assertTrue(a.take_healing(20))

    def test_take_healing_returns_false_if_character_is_dead(self):
        a = Skeleton(health = 20, mana = 10)
        a.take_damage(300)

        self.assertFalse(a.take_healing(20))

    def test_if_take_healing_restores_health_upto_max(self):
        a = Skeleton(health = 20, mana = 10)
        a.take_damage(19)
        a.take_healing(300)

        self.assertEqual(a.health,20)


if __name__ == '__main__':
    unittest.main()