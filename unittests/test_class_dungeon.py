import unittest
import sys

sys.path.append('..')
from dungeon_module.dungeon import Dungeon
from entities.hero import Hero


class MyTestCase(unittest.TestCase):
    def test_if_set_starting_positions_raises_exception_when_there_are_no_starting_points(self):
        res = None
        exp = "Invalid map. No place to spawn."
        try:
            dungeon = Dungeon('test_invalid_map.txt')
        except Exception as e:
            res = str(e)

        self.assertEqual(res, exp)

    def test_if_update_position_works_correctly(self):
        dungeon = Dungeon('test_valid_map.txt')
        dungeon._Dungeon__update_position(1, 1)
        self.assertEqual(dungeon.curr_row, 1)
        self.assertEqual(dungeon.curr_column, 1)

    def test_if_move_hero_on_the_map_works_correctly(self):
        dungeon = Dungeon('test_valid_map.txt')
        dungeon._Dungeon__move_hero_on_the_map(1, 1)
        res = [['.', '.', '.', '.', '.', '.', '.', '.', 'S'],
               ['#', 'H', '#', '#', '.', '.', 'T', '.', 'E'],
               ['.', '.', '.', 'G', '.', '.', 'S', '.', 'T']]
        exp = dungeon.dungeon_map
        self.assertEqual(res, exp)

    def test_if_set_hero_coordinates_works_correctly(self):
        dungeon = Dungeon('test_valid_map.txt')
        dungeon._Dungeon__set_hero_coordinates()
        exp = [['.', '.', '.', '.', '.', '.', '.', '.', 'H'],
               ['#', '#', '#', '#', '.', '.', 'T', '.', 'E'],
               ['.', '.', '.', 'G', '.', '.', 'S', '.', 'T']]
        res = dungeon.dungeon_map
        self.assertEqual(res, exp)

    def test_if_respawn_hero_raises_exception(self):
        dungeon = Dungeon('test_valid_map.txt')
        dungeon.starting_positions = []
        res = None
        exp = "Game over. No place to respawn."
        try:
            dungeon._Dungeon__respawn_hero()
        except Exception as e:
            res = str(e)
        self.assertEqual(res, exp)

    def test_if_spawn_hero_works_correctly(self):
        hero = Hero()
        dungeon = Dungeon('test_valid_map.txt')
        exp = [['.', '.', '.', '.', '.', '.', '.', '.', 'H'],
               ['#', '#', '#', '#', '.', '.', 'T', '.', 'E'],
               ['.', '.', '.', 'G', '.', '.', 'S', '.', 'T']]

        dungeon.spawn(hero)
        self.assertEqual(exp, dungeon.dungeon_map)
        self.assertIs(hero, dungeon.hero)


if __name__ == '__main__':
    unittest.main()
