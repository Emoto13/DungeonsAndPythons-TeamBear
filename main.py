from hero import Hero
from dungeon import Dungeon
from key_input import get_key_input
from utils import clear_screen, end_game, check_choice
from print_helpers import print_ask_direction


def main():
    hero = Hero.create_hero()
    dungeon = Dungeon('level1.txt')
    dungeon.spawn(hero)
    # TODO add metohd for starting info
    clear_screen()

    while not end_game(dungeon) and dungeon.hero.is_alive():
        dungeon.print_map()
        print_ask_direction(hero)

        try:
            choice = get_key_input()
            check_choice(choice, dungeon)
        except Exception as e:
            print(e)
            input('\nPress Enter to continue...')

        clear_screen()
    clear_screen()


if __name__ == '__main__':
    main()
