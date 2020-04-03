from hero import Hero
from dungeon import Dungeon
from utils import end_game


def main():
    hero = Hero.create_hero()
    dungeon = Dungeon('level1.txt')
    dungeon.spawn(hero)

    while not end_game(dungeon) and dungeon.hero.is_alive():
        dungeon.print_map()
        direction = input(f"In what direction should {hero.known_as()} move? ").lower()
        try:
            dungeon.move_hero(direction)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
