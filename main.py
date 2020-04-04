from hero import Hero
from dungeon import Dungeon
from utils import end_game, clear_screen, display_help, check_choice
from key_input import get_key_input


def main():
    hero = Hero.create_hero()
    dungeon = Dungeon('level1.txt')
    dungeon.spawn(hero)
    display_help()
    clear_screen()

    while not end_game(dungeon) and dungeon.hero.is_alive():
        dungeon.print_map()
        print(f"In what direction should {hero.known_as()} move?")
        try:
            choice = get_key_input()
            check_choice(choice, dungeon, hero)
            clear_screen()
        except Exception as e:
            print(e)
            input('\nPress Enter to continue...')
            clear_screen()
    clear_screen()


if __name__ == '__main__':
    main()
