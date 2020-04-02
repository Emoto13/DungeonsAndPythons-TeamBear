def read_file(file_path):
    with open(file_path, 'r') as f:
        content = f.readlines()

    dungeon_map = [[char for char in line.strip()] for line in content]

    return dungeon_map


def add_coordinates(lst):
    def add_row_and_col(row, col):
        lst.append((row, col))

    return add_row_and_col


def set_coordinates_for_starting_positions_and_treasures(dungeon_map, dicts):
    for row in range(len(dungeon_map)):
        for col in range(len(dungeon_map[row])):
            if dungeon_map[row][col] == 'S' or dungeon_map[row][col] == 'T':
                dicts[dungeon_map[row][col]](row, col)


def move_is_legal(dungeon_map, row, col):
    if row < 0 or row >= len(dungeon_map):
        return False

    if col < 0 or col >= len(dungeon_map[row]):
        return False

    if dungeon_map[row][col] == '#':
        return False

    return True


def main():
    print(move_is_legal([[1, 2]], 0, 1))


if __name__ == '__main__':
    main()
