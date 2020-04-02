from utils import read_file, add_coordinates, set_coordinates_for_starting_positions_and_treasures, move_is_legal, \
    fight_enemy, collect_treasure, end_game, nothing_happens
from hero import Hero


# TODO CREATE FILES WITH CONSTANTS
# TODO SPLIT FIGHT_ENEMY AND COLLECT_TREASURE TO SMALLER FUNCTIONS
# TODO REFACTOR MOVE_HERO TO SMALLER FUNCTIONS
# TODO WRITE SOME TEST SO MARTO DOESN'T COMPLAIN ABOUT IT
# TODO UPDATE HERO POSITION ON THE MAP

class Dungeon:

    def __init__(self, file_path: str = None):
        self.starting_positions = []
        self.treasures = []

        self.dungeon_map = read_file(file_path)
        self.set_starting_positions_and_treasures()

        self.curr_row = 0
        self.curr_column = 0
        self.hero = None

    def set_starting_positions_and_treasures(self):
        dicts = {
            'S': add_coordinates(self.starting_positions),
            'T': add_coordinates(self.treasures),
        }

        set_coordinates_for_starting_positions_and_treasures(self.dungeon_map, dicts)

    def spawn(self, hero_instance: Hero = None):
        self.hero = hero_instance
        self.__set_hero_coordinates()

    def __set_hero_coordinates(self):
        self.curr_row = self.starting_positions[0][0]
        self.curr_column = self.starting_positions[0][1]
        del self.starting_positions[0]
        self.dungeon_map[self.curr_row][self.curr_column] = 'H'

    def move_hero(self, direction):
        dicts = {
            'up': (self.curr_row - 1, self.curr_column),
            'down': (self.curr_row + 1, self.curr_column),
            'left': (self.curr_row, self.curr_column - 1),
            'right': (self.curr_row, self.curr_column + 1)
        }

        row = dicts[direction][0]
        col = dicts[direction][1]

        if not move_is_legal(self.dungeon_map, row, col):
            return False

        position = self.dungeon_map[row][col]
        dict_of_actions = {
            'E': fight_enemy,
            'T': collect_treasure,
            'G': end_game,
            '.': nothing_happens
        }

        dict_of_actions[position](self.hero)
        self.__update_current_row_and_column(row, col)
        return True

    def __update_current_row_and_column(self, row, col):
        self.curr_row = row
        self.curr_column = col


def main():
    d = Dungeon('level1.txt')
    hero = Hero(name='Luster', title='Dracoslayer')
    d.spawn(hero)
    d.move_hero('right')
    d.move_hero('down')

    print(d.curr_row, d.curr_column)
    print(hero.spell.damage, hero.weapon.damage)


if __name__ == '__main__':
    main()
