from utils import read_file, add_coordinates, set_coordinates_for_starting_positions, move_is_legal, \
    reached_exit, take_action_after_move, apply_direction
from hero import Hero
from weapon import Weapon


# TODO ADD USER CHOICE TO EQUIP AND LEARN OPTIONAL

class Dungeon:

    def __init__(self, file_path: str = None):
        self.starting_positions = []

        self.dungeon_map = read_file(file_path)
        self.__set_starting_positions()

        self.curr_row = 0
        self.curr_column = 0

    def spawn(self, hero_instance: Hero = None):
        self.hero = hero_instance
        self.__set_hero_coordinates()

    def print_map(self):
        for rows in self.dungeon_map:
            print(*rows)

    def move_hero(self, direction):
        row, col = apply_direction(direction, self.curr_row, self.curr_column)

        move_is_legal(self.dungeon_map, row, col)

        position = self.dungeon_map[row][col]
        if reached_exit(position):
            self.__update_position(row, col)
            return

        take_action_after_move(self.hero, position)

        if not self.hero.is_alive():
            self.__respawn_hero()
            return

        self.hero.take_mana(self.hero.mana_regeneration_rate)
        self.__move_hero_on_the_map(row, col)
        self.__update_position(row, col)

    def __set_starting_positions(self):
        set_coordinates_for_starting_positions(self.dungeon_map, self.starting_positions)

    def __respawn_hero(self):
        if not self.starting_positions:
            raise Exception('Game over. No place to respawn.')

        hero = Hero(name=self.hero.name, title=self.hero.title,
                    health=self.hero.MAX_HEALTH,
                    mana=self.hero.MAX_MANA,
                    mana_regeneration_rate=self.hero.mana_regeneration_rate)

        row = self.starting_positions[0][0]
        col = self.starting_positions[0][1]

        self.__move_hero_on_the_map(row, col)
        self.__set_hero_coordinates()
        self.__update_position(row, col)
        self.hero = hero

        print(f'{self.hero.known_as()} has respawn at {self.curr_row} {self.curr_column}')

    def __update_position(self, row, col):
        self.curr_row = row
        self.curr_column = col

    def __move_hero_on_the_map(self, row, col):
        self.dungeon_map[self.curr_row][self.curr_column] = '.'
        self.dungeon_map[row][col] = 'H'

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
