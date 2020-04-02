def read_file(file_path):
	with open(file_path,'r') as f:
		content = f.readlines()

	dungeon_map =[[char for char in line.strip()] for line in content]

	return dungeon_map


def add_coordinates(lst):
	def add_row_and_col(row,col):
		lst.append((row,col))

	return add_row_and_col
