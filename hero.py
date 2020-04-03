from base_entity import BaseEntity
from spell import Spell
from verification_mixin import VerificationMixin
from weapon import Weapon


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

    def attack(self) -> float:
        spell_is_more_powerful = self.spell.damage >= self.weapon.damage

        if not spell_is_more_powerful and self.can_cast():
            self.reduce_mana()
            return self.spell.damage
        return self.weapon.damage

    def attack_by(self, by='spell'):
        dicts = {'weapon': self.weapon.damage,
                 'spell': self.spell.damage
                 }

        if by == 'spell':
            self.reduce_mana()

        return dicts[by]

    @classmethod
    def create_hero(cls):
        name = input('Hero name: ')
        title = input('Hero title: ')
        health = int(input('Hero health: '))
        mana = int(input('Hero mana: '))
        mana_regeneration_rate = int(input('Hero mana regeneration rate: '))

        has_weapon = input(f"Should {name} the {title} have a weapon? (yes/no) ").lower()
        weapon = Weapon()
        if has_weapon == 'yes':
            print('Create your weapon')
            weapon_name = input('Weapon name: ')
            weapon_damage = int(input(f'{weapon_name} damage: '))
            weapon = Weapon(name=weapon_name, damage=weapon_damage)

        has_spell = input(f"Should {name} the {title} have a spell? (yes/no) ").lower()
        spell = Spell()
        if has_spell == 'yes':
            print(f'Create your spell')
            spell_name = input('Spell name: ')
            spell_damage = int(input(f'{spell_name} damage: '))
            spell_mana_cost = int(input(f'Mana cost of the {spell_name}: '))
            spell_range = int(input(f'Cast range of the {spell_name}: '))
            spell = Spell(name=spell_name, damage=spell_damage, mana_cost=spell_mana_cost, cast_range=spell_range)

        return cls(name=name, title=title,
                   health=health,
                   mana=mana, mana_regeneration_rate=mana_regeneration_rate,
                   weapon=weapon, spell=spell)
