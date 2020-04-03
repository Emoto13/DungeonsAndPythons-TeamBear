import random
from names import WEAPON_NAMES, SPELL_NAMES
from treasures import TYPES_OF_TREASURES

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


def fight_enemy(hero):
    # TODO REFACTOR FOR SPELLS AND SPELL RANGE
    from enemy import Enemy
    enemy = Enemy.spawn_enemy()
    while hero.is_alive():
        enemy.take_damage(hero.attack())
        if not enemy.is_alive():
            break
        hero.take_damage(enemy.attack())


def generate_random_value_of_treasure(treasure):
    from weapon import Weapon
    from spell import Spell

    dict_treasure_values = {
        'health': random.randint(1, 20),
        'mana': random.randint(1, 20),
        'weapon': Weapon.create_weapon(random.choice(WEAPON_NAMES)),
        'spell': Spell.create_spell(random.choice(SPELL_NAMES))
    }

    treasure_value = dict_treasure_values[treasure]

    return treasure_value

def collect_treasure(hero):
    dict_add_treasure = {
        'health': hero.take_healing,
        'mana': hero.take_mana,
        'weapon': hero.equip,
        'spell': hero.learn
    }

    treasure = random.choice(TYPES_OF_TREASURES)

    treasure_value = generate_random_value_of_treasure(treasure)
    dict_add_treasure[treasure](treasure_value)

    print(f'You collected {treasure}')


def nothing_happens(hero):
    print(f'Nothing happened with hero {hero.name} the {hero.title}')


def end_game(hero):
    pass


def main():
    print(move_is_legal([[1, 2]], 0, 1))


if __name__ == '__main__':
    main()
