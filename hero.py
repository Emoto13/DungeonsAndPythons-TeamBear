from base_entity import BaseEntity


class Hero(BaseEntity):
    def __init__(self, name: str = "Hero", title: str = "No title", health: float = 1, mana: float = 0,
                 mana_regeneration_rate: float = 0):
        super().__init__(health=health, mana=mana)
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


def main():
    h = Hero()
    print(h.attack('alabala'))


if __name__ == '__main__':
    main()
