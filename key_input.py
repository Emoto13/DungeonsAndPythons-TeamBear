import sys
import tty
import termios
from verification_mixin import VerificationMixin


class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch


def get_key_input():
    inkey = _Getch()
    key_combination = inkey()

    dicts = {
        '\x1b[A': 'up',
        '\x1b[B': 'down',
        '\x1b[C': 'right',
        '\x1b[D': 'left',
        'hlp': 'help',
        'chr': 'character_info'
    }

    VerificationMixin.verify_command(dicts, key_combination)
    direction = dicts[key_combination]

    return direction


def main():
        for i in range(0, 20):
                print(get_key_input())


if __name__ == '__main__':
        main()
