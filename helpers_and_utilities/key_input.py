import sys
import tty
import termios
from helpers_and_utilities.verification_mixin import VerificationMixin


class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def check_arrow_key(key, get_key):
    if key == '\x1b':
        new_key = f'{key}{get_key()}{get_key()}'
        return new_key
    return key


def get_key_input():
    get_key = _Getch()
    key_combination = get_key()

    key_combination = check_arrow_key(key_combination, get_key)
    dicts = {
        '\x1b[A': 'up',
        '\x1b[B': 'down',
        '\x1b[C': 'right',
        '\x1b[D': 'left',
        'w': 'up',
        's': 'down',
        'a': 'left',
        'd': 'right',
        'h': 'help',
        'c': 'character_info',
        'l': 'lore',
        'k': 'map_keys',
        'p': 'credits'
    }

    VerificationMixin.verify_command(dicts, key_combination)
    direction = dicts[key_combination]

    return direction


def main():
    for i in range(0, 20):
        print(get_key_input())


if __name__ == '__main__':
        main()
