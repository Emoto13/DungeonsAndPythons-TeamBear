import random

from base_entity import BaseEntity
from verification_mixin import VerificationMixin
from weapon import Weapon
from spell import Spell
from print_helpers import print_attack
from names import WEAPON_NAMES, SPELL_NAMES


class Hero(BaseEntity, VerificationMixin):
    def __init__(self, name: str = "Hero", title: str = "No title", health: int = 1, mana: int = 0,
                 mana_regeneration_rate: int = 0, weapon: Weapon = Weapon(), spell: Spell = Spell()):
        super().__init__(health=health, mana=mana)
        self.verify_attributes(name, title, mana_regeneration_rate)

        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate
        self.weapon = weapon
        self.spell = spell

    def known_as(self):
        return f'{self.name} the {self.title}'

    def attack(self):
        spell_is_more_powerful = self.spell.damage >= self.weapon.damage

        if spell_is_more_powerful and self.can_cast():
            self.reduce_mana()
            print_attack('spell', self)
            return self.spell.damage

        print_attack('weapon', self)
        return self.weapon.damage

    def attack_by_spell(self):
        self.reduce_mana()
        print_attack('spell', self)
        return self.spell.damage

    @classmethod
    def create_hero(cls):
        # add except
        name = input('Hero name: ')
        title = input('Hero title: ')
        health = int(input('Hero health: '))
        mana = int(input('Hero mana: '))
        mana_regeneration_rate = int(input('Hero mana regeneration rate: '))

        weapon = Weapon.create_weapon(random.choice(WEAPON_NAMES))
        spell = Spell.create_spell(random.choice(SPELL_NAMES))

        return cls(name=name, title=title,
                   health=health,
                   mana=mana, mana_regeneration_rate=mana_regeneration_rate,
                   weapon=weapon, spell=spell)
