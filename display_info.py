class DisplayInfo:
    def __init__(self, hero):
        self.hero = hero

    def display_info(self, info_type):
        dicts = {'character_info': self.display_hero_information,
                 'help': DisplayInfo.display_help
                 }

        dicts[info_type]()

    def display_hero_information(self):
        FORMAT_SPACES = '      '
        print(
            f'{self.hero.name} the {self.hero.title}\n\n'
            f'current helth: {self.hero.health}\n'
            f'current mana: {self.hero.mana}\n'
            f'mana regeneration: {self.hero.mana_regeneration_rate}\n\n'
            f'current Weapon:\n'
            f'{FORMAT_SPACES}Name: {self.hero.weapon.name}\n'
            f'{FORMAT_SPACES}Damage: {self.hero.weapon.damage}\n\n'
            f'current Spell:\n'
            f'{FORMAT_SPACES}Name: {self.hero.spell.name}\n'
            f'{FORMAT_SPACES}Damage: {self.hero.spell.damage}\n'
            f'{FORMAT_SPACES}Mana Cost: {self.hero.spell.mana_cost}\n'
            f'{FORMAT_SPACES}Range: {self.hero.spell.cast_range}'
        )
        input('\nPress Enter to continue... ')

    def display_help(self):
        from utils import clear_screen
        clear_screen()
        with open('help.txt', 'r') as fp:
            print(fp.read())
        input('\nPress Enter to continue... ')

    # TODO ADD DISPLAY STARTING
    #  METHOD TO DISPLAY RULES AND MECHANICS
