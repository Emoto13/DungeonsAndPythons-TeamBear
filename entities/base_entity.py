from abc import ABC, abstractmethod
from helpers_and_utilities.verification_mixin import VerificationMixin
from items.weapon import Weapon
from items.spell import Spell


class BaseEntity(ABC, VerificationMixin):
    def __init__(self, health: int = 1, mana: int = 0):
        self.verify_health(health)
        self.health = health
        self.MAX_HEALTH = health

        self.verify_number_value(mana)
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

    def take_damage(self, damage_points: int):
        self.verify_number_value(damage_points)
        self.health -= damage_points

        if not self.is_alive():
            self.health = 0

    def take_healing(self, healing_points: int) -> bool:
        if self.health == 0:
            return False
        self.verify_number_value(healing_points)
        self.health += healing_points
        self.health = self.verify_if_more_than_max(self.health, self.MAX_HEALTH)
        return True

    def take_mana(self, mana_points: int):
        if self.health == 0:
            return False
        self.verify_number_value(mana_points)
        self.mana += mana_points
        self.mana = self.verify_if_more_than_max(self.mana, self.MAX_MANA)

    def reduce_mana(self):
        self.mana -= self.spell.mana_cost

    def equip(self, weapon: Weapon = None):
        print(f'\nYour weapon [name,damage]: [{self.weapon.name}, {self.weapon.damage}]')
        print(f'New weapon [name,damage]: [{weapon.name}, {weapon.damage}]')
        choice = input('Do you want to equip this weapon? (yes/no) ')
        if choice == 'yes':
            self.weapon = weapon

    def learn(self, spell: Spell = None):
        print(
            f'\nYour spell [name,mana_cost,damage,range]:'
            f'[{self.spell.name}, {self.spell.damage}, {self.spell.mana_cost}, {self.spell.cast_range}]'
        )
        print(
            f'New spell [name,mana_cost,damage,range]:'
            f' [{spell.name}, {spell.damage}, {spell.mana_cost}, {spell.cast_range}]'
        )
        choice = input('Do you want to equip this spell? (yes/no) ')
        if choice == 'yes':
            self.spell = spell

    @abstractmethod
    def attack(self):
        pass
