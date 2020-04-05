import random
from helpers_and_utilities.verification_mixin import VerificationMixin


class Weapon(VerificationMixin):

    def __init__(self, name: str = 'Weapon', damage: int = 0):
        self.verify_attributes(name, damage)

        self.name = name
        self.damage = damage

    @classmethod
    def create_weapon(cls, name):
        damage = random.randint(1, 20)
        return cls(name=name, damage=damage)
