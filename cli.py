# coding=utf-8
from game import Game, Snake


FIELD_SIZE = (11, 13)
SYMBOLS = {Snake: 'X', None: '.'}
PROMPT = '🐍: '
ERROR_UNKNOWN_COMMAND = """
Unknown command “{cmd}”.
Available commands:
x  Exit the game
n  Slither northward ↑
s  Slither southward ↓
w  Slither westward ←
e  Slither eastward →
"""


class App:

    def __init__(self, game):
        self.game = game

        self.COMMANDS = {
            'x': self.cmd_exit,
            'n': self.cmd_north,
            's': self.cmd_south,
            'w': self.cmd_west,
            'e': self.cmd_east,
        }

    def loop(self):
        """
        Runs the app loop, endlessly promting user for input.
        """
        while True:
            self.print_field()
            try:
                cmd = input(PROMPT)
                self.run_cmd(cmd)
            except EOFError:
                break

    def print_field(self):
        """
        Prints the current game field state as a text grid.
        """
        for y in range(self.game.field_size[1]):
            for x in range(self.game.field_size[0]):
                thing_type = None  # Default: nothing on the coords.

                all_things_on_coords = game.what_is_on_coords((x, y))
                if all_things_on_coords:
                    # If there are more things on one coordinates, only the
                    # first one is printed. Symbol is determined by the class
                    # of the thing.
                    thing_type = type(all_things_on_coords[0])

                # Symbols are horizontally separated by a space for better
                # legibility.
                print(SYMBOLS[thing_type], end=' ')  # . . . X . .
            print('')  # \n
        print('')  # \n

    def run_cmd(self, cmd):
        if cmd in self.COMMANDS:
            self.COMMANDS[cmd]()
        else:
            print(ERROR_UNKNOWN_COMMAND.format(cmd=cmd))

    def cmd_exit(self):
        raise EOFError()

    def cmd_north(self):
        self.game.input_north()

    def cmd_south(self):
        self.game.input_south()

    def cmd_west(self):
        self.game.input_west()

    def cmd_east(self):
        self.game.input_east()


if __name__ == '__main__':
    """
    Initialize the game and its CLI interace.
    """
    game = Game(FIELD_SIZE)
    app = App(game)
    app.loop()
