def print_attack(equipment, hero):
    dicts = {'weapon': f'{hero.name} attacks with {hero.weapon.name} dealing {hero.weapon.damage} damage',
             'spell': f'{hero.name} casts {hero.spell.name} dealing {hero.spell.damage} damage'}

    print(dicts[equipment])


def print_hero_takes_damage(hero, enemy):
    print(f'Enemy attacks dealing {enemy.damage} damage to {hero.name}')


def print_entity_name_and_health(entity_name, health):
    print(f'{entity_name} health: {health}')


def print_collect_treasure(treasure):
    print(f'\nYou collected {treasure}')
    input('\nPress Enter to continue... ')


def print_has_been_slain(entity_message):
    print(f'{entity_message} has been slain')


def print_ask_direction(hero):
    print(f"In what direction should {hero.known_as()} move?")
