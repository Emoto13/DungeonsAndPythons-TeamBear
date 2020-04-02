from utils import read_file, add_coordinates
from hero import Hero


class Dungeon():

	def __init__(self,file_path : str = None):
		self.starting_positions = []
		self.treasures = []

		self.dungeon_map = read_file(file_path)
		self.set_starting_positions_and_tresures()

		self.curr_row = 0
		self.curr_column = 0
		self.hero = None


	def set_starting_positions_and_tresures(self):
		dicts = {
			'S' : add_coordinates(self.starting_positions),
			'T' : add_coordinates(self.treasures),
 		}

 		#TODO refactor to another func
		for row in range(len(self.dungeon_map)):
			for col in range(len(self.dungeon_map[row])):

				if self.dungeon_map[row][col] == 'S' or self.dungeon_map[row][col] == 'T' :
					dicts[self.dungeon_map[row][col]](row,col)


	def spawn(self,hero_instance : Hero = None):
		self.hero = hero_instance

		self.set_hero_coordinates_and_character_on_map()


	def set_hero_coordinates_and_character_on_map(self):
		self.curr_row = self.starting_positions[0][0]
		self.curr_column = self.starting_positions[0][1]
		del self.starting_positions[0]

		self.dungeon_map[self.curr_row][self.curr_column] = 'H'


def main():
	d = Dungeon('level1.txt')
	h = Hero()
	d.spawn(h)
	print(d.curr_column)
	print(d.dungeon_map)


if __name__ == '__main__':
	main()