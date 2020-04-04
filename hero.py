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

    def attack(self):
        spell_is_more_powerful = self.spell.damage >= self.weapon.damage

        if spell_is_more_powerful and self.can_cast():
            self.reduce_mana()
            print(f'{self.name} casts {self.spell.name} dealing {self.spell.damage} damage')
            return self.spell.damage
        print(f'{self.name} attacks with {self.weapon.name} dealing {self.weapon.damage} damage')
        return self.weapon.damage

    def attack_by(self, by='spell'):
        dicts = {'weapon': self.weapon.damage,
                 'spell': self.spell.damage
                 }

        if by == 'spell':
            self.reduce_mana()

        print(f'{self.name} casts {self.spell.name} dealing {self.spell.damage} damage')

        return dicts[by]

    def display_hero_information(self):
        # add spaces constant for fprints
        print(
            f'{self.name} the {self.title}\n\n'
            f'current helth: {self.health}\n'
            f'current mana: {self.mana}\n'
            f'mana regeneration: {self.mana_regeneration_rate}\n\n'
            f'current Weapon:\n'
            f'      Name: {self.weapon.name}\n'
            f'      Damage: {self.weapon.damage}\n\n'
            f'current Spell:\n'
            f'      Name: {self.spell.name}\n'
            f'      Damage: {self.spell.damage}\n'
            f'      Mana Cost: {self.spell.mana_cost}\n'
            f'      Range: {self.spell.cast_range}'
        )
        input('\nPress Enter to continue... ')

    @classmethod
    def create_hero(cls):
        # add except
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
