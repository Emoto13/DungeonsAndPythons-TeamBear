import random


class Weapon:

    def __init__(self, name: str = 'Weapon', damage: int = 0):
        self.name = name
        self.damage = damage

    @classmethod
    def create_weapon(cls, name):
        damage = random.randint(1, 20)
        return cls(name=name, damage=damage)
