from utils import read_file, add_coordinates, set_coordinates_for_starting_positions_and_treasures, move_is_legal
from hero import Hero


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

def main():
    d = Dungeon('level1.txt')
    h = Hero()
    print(d.curr_column)
    print(d.dungeon_map)
    print(d.starting_positions)


if __name__ == '__main__':
    main()
