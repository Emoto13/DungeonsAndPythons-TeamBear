from base_entity import BaseEntity
from verification_mixin import VerificationMixin


class Hero(BaseEntity, VerificationMixin):
    def __init__(self, name: str = "Hero", title: str = "No title", health: int = 1, mana: int = 0,
                 mana_regeneration_rate: int = 0):

        super().__init__(health=health, mana=mana)
        self.verify_attributes(name, title, mana_regeneration_rate)

        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate

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

        return cls(name=name, title=title, health=health, mana=mana, mana_regeneration_rate=mana_regeneration_rate)
