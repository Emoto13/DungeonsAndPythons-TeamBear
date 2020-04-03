from base_entity import BaseEntity
import random


# TODO ADD WEAPONS AND SPELLS TO ENEMY

class Enemy(BaseEntity):
    def __init__(self, health: int = 1, mana: int = 0, damage: int = 0):
        super().__init__(health, mana)
        self.damage = damage

    def attack(self):
        spell_is_most_powerful = self.damage <= self.spell.damage >= self.weapon.damage

        if spell_is_most_powerful and self.can_cast():
            self.reduce_mana()
            return self.spell.damage

        return max(self.weapon.damage, self.damage)

    @classmethod
    def spawn_enemy(cls):
        health = random.randint(1, 100)
        mana = random.randint(1, 100)
        damage = random.randint(1, 20)
        return cls(health=health, mana=mana, damage=damage)

    def __del__(self):
        print("Enemy has been slain")
