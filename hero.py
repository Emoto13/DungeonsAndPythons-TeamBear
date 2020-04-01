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

    def attack(self, by: str = "weapon") -> float:
        dicts = {
            "weapon": self.weapon,
            "spell": self.spell
        }

        if dicts[by] is None:
            return 0

        return dicts[by].damage


def main():
    h = Hero()
    print(h.attack('alabala'))


if __name__ == '__main__':
    main()
