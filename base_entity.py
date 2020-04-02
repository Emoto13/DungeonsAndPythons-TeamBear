from abc import ABC, abstractmethod
from verfication_mixin import VerificationMixin
from weapon import Weapon
from spell import Spell


class BaseEntity(ABC, VerificationMixin):
    def __init__(self, health: float = 1, mana: float = 0):
        self.verify_health(health)
        self.health = health
        self.MAX_HEALTH = health

        self.verify_value(mana)
        self.mana = mana
        self.MAX_MANA = mana

        self.weapon = Weapon()
        self.spell = Spell()

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.health > 0

    def can_cast(self):
        if self.spell is None:
            return False

        return self.mana >= self.spell.mana_cost

    def take_damage(self, damage_points: float):
        self.verify_value(damage_points)
        self.health -= damage_points

        if self.health < 0:
            self.health = 0

    def take_healing(self, healing_points: float) -> bool:
        if self.health == 0:
            return False
        self.verify_value(healing_points)
        self.health += healing_points
        self.health = self.verify_if_more_than_max(self.health, self.MAX_HEALTH)
        return True

    def take_mana(self, mana_points: float):
        self.verify_value(mana_points)
        self.mana += mana_points
        self.mana = self.verify_if_more_than_max(self.mana, self.MAX_MANA)

    def reduce_mana(self):
        self.mana -= self.spell.mana_cost

    def equip(self, weapon: Weapon = None):
        self.weapon = weapon

    def learn(self, spell: Spell = None):
        self.spell = spell

    @abstractmethod
    def attack(self):
        pass
