import random
from verification_mixin import VerificationMixin

class Spell(VerificationMixin):

    def __init__(self, name: str = 'Spell', damage: int = 0, mana_cost: int = 0, cast_range: int = 0):
        self.verify_attributes(name, damage, mana_cost, cast_range)

        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    @classmethod
    def create_spell(cls, name):
        damage = random.randint(1, 20)
        mana_cost = random.randint(1, 10)
        cast_range = random.randint(1, 3)
        return cls(name=name, damage=damage, mana_cost=mana_cost, cast_range=cast_range)
