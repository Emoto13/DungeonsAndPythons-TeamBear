from base_entity import BaseEntity


class Enemy(BaseEntity):
    def __init__(self, health: float = 1, mana: float = 0, damage: float = 0):
        super().__init__(health, mana)
        self.damage = damage

    def attack(self):
        spell_is_most_powerful = self.damage <= self.spell.damage >= self.weapon.damage

        if spell_is_most_powerful and self.can_cast():
            self.reduce_mana()
            return self.spell.damage

        return max(self.weapon.damage, self.damage)
