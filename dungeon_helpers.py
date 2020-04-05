import random
from names import WEAPON_NAMES, SPELL_NAMES
from treasures import TYPES_OF_TREASURES
from verification_mixin import VerificationMixin
from print_helpers import print_hero_takes_damage, print_collect_treasure, print_has_been_slain,\
    print_entity_name_and_health


__all__ = ['read_file',
           'set_coordinates_for_starting_positions',
           'move_is_legal',
           'apply_direction',
           'take_action_after_move',
           'fight_enemy',
           'reset_hero_attributes',
           'collect_treasure',
           'reached_exit'
           ]


def read_file(file_path):
    with open(file_path, 'r') as f:
        content = f.readlines()
    dungeon_map = [[char for char in line.strip()] for line in content]
    return dungeon_map


def add_coordinates(lst):
    def add_row_and_col(row, col):
        lst.append((row, col))
    return add_row_and_col


def set_coordinates_for_starting_positions(dungeon_map, starting_positions):
    for row in range(len(dungeon_map)):
        if 'S' in dungeon_map[row]:
            col = dungeon_map[row].index('S')
            add_coordinates(starting_positions)(row, col)


def move_is_legal(dungeon_map, row, col):
    if row < 0 or col < 0 or row >= len(dungeon_map) or col >= len(dungeon_map[row]):
        raise ValueError('\nYou cannot go out of the map.')

    if dungeon_map[row][col] == '#':
        raise ValueError('\nThere is a wall. You cannot go there.')

    if dungeon_map[row][col] == 'S':
        raise ValueError('\nYou cannot enter the Spawn Zone')


def apply_direction(direction, curr_row, curr_column):
    dicts = {
        'up': (curr_row - 1, curr_column),
        'down': (curr_row + 1, curr_column),
        'left': (curr_row, curr_column - 1),
        'right': (curr_row, curr_column + 1)
    }

    VerificationMixin.verify_command(dicts, direction)

    row = dicts[direction][0]
    col = dicts[direction][1]

    return row, col


def take_action_after_move(hero, position):
    if position == '.':
        return

    dict_of_actions = {
        'E': fight_enemy,
        'T': collect_treasure,
    }

    dict_of_actions[position](hero)


def fight_enemy(hero):
    from enemy import Enemy
    enemy = Enemy.spawn_enemy()
    attack_with_spell_range(hero, enemy)
    regular_fight(hero, enemy)
    input('\nPress Enter to continue... ')


def attack_with_spell_range(hero, enemy):
    spell_attack_counter = 0

    while hero.can_cast() and spell_attack_counter < hero.spell.cast_range:

        enemy.take_damage(hero.attack_by_spell())
        spell_attack_counter += 1

        print_entity_name_and_health('Enemy', enemy.health)
        if not enemy.is_alive():
            print_has_been_slain('Enemy')
            break
        print(f'Enemy moves closer!')


def regular_fight(hero, enemy):
    while True:
        enemy.take_damage(hero.attack())
        print_entity_name_and_health('Enemy', enemy.health)

        if not enemy.is_alive():
            print_has_been_slain('Enemy')
            break

        hero.take_damage(enemy.attack())
        print_hero_takes_damage(hero, enemy)
        print_entity_name_and_health(hero.name, hero.health)

        if not hero.is_alive():
            print_has_been_slain(hero.known_as())
            break


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
    print_collect_treasure(treasure)


def reset_hero_attributes(hero):
    from weapon import Weapon
    from spell import Spell
    hero.health = hero.MAX_HEALTH
    hero.mana = hero.MAX_MANA
    hero.weapon = Weapon.create_weapon(random.choice(WEAPON_NAMES))
    hero.spell = Spell.create_spell(random.choice(SPELL_NAMES))


def reached_exit(position):
    if position == 'G':
        print("You've successfully reached the exit!")
        return True
    return False
