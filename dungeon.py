from utils import read_file, add_coordinates, set_coordinates_for_starting_positions, move_is_legal \
    , reached_exit, take_action_after_move, apply_direction
from hero import Hero
from weapon import Weapon


# TODO WRITE SOME TEST SO MARTO DOESN'T COMPLAIN ABOUT IT
# TODO ADD USER CHOICE TO EQUIP AND LEARN

class Dungeon:

    def __init__(self, file_path: str = None):
        self.starting_positions = []

        self.dungeon_map = read_file(file_path)
        self.__set_starting_positions()

        self.curr_row = 0
        self.curr_column = 0
        self.hero = None

    def spawn(self, hero_instance: Hero = None):
        self.hero = hero_instance
        self.__set_hero_coordinates()

    def print_map(self):
        for rows in self.dungeon_map:
            print(*rows)

    def move_hero(self, direction):
        row, col = apply_direction(direction, self.curr_row, self.curr_column)

        if not move_is_legal(self.dungeon_map, row, col):
            return False

        position = self.dungeon_map[row][col]

        if reached_exit(position):
            return True

        take_action_after_move(self.hero, position)

        if not self.hero.is_alive():
            self.__respawn_hero()
            return False

        self.hero.take_mana(self.hero.mana_regeneration_rate)
        self.__update_position(row, col)
        return True

    def __set_starting_positions(self):
        dicts = {
            'S': add_coordinates(self.starting_positions),
        }

        set_coordinates_for_starting_positions(self.dungeon_map, dicts)

    def __respawn_hero(self):
        if not self.starting_positions:
            print('Game over')
            return
        hero = Hero(name=self.hero.name, title=self.hero.title,
                    health=self.hero.MAX_HEALTH,
                    mana=self.hero.MAX_MANA,
                    mana_regeneration_rate=self.hero.mana_regeneration_rate)
        self.spawn(hero)

    def __update_position(self, row, col):
        self.dungeon_map[self.curr_row][self.curr_column] = '.'
        self.dungeon_map[row][col] = 'H'
        self.curr_row = row
        self.curr_column = col

    def __set_hero_coordinates(self):
        self.curr_row = self.starting_positions[0][0]
        self.curr_column = self.starting_positions[0][1]
        del self.starting_positions[0]
        self.dungeon_map[self.curr_row][self.curr_column] = 'H'


def main():
    d = Dungeon('level1.txt')
    hero = Hero(name='Luster', title='Dracoslayer', health=100, )
    d.spawn(hero)
    hero.equip(Weapon(damage=200))
    d.move_hero('right')
    d.move_hero('down')
    print(hero.weapon.damage, hero.spell.damage)
    d.move_hero('down')
    d.move_hero('down')
    d.move_hero('right')
    d.print_map()

    print(d.curr_row, d.curr_column)
    print(hero.spell.damage, hero.weapon.damage)


if __name__ == '__main__':
    main()
