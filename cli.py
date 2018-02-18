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
    """
    The game UI: Draws the game field, calls events on input.
    """

    def __init__(self, game):
        self.game = game

        self.COMMANDS = {
            'x': self._cmd_exit,
            'n': self.game.input_north,
            's': self.game.input_south,
            'w': self.game.input_west,
            'e': self.game.input_east,
        }

    def loop(self):
        """
        Runs the app loop, endlessly promting user for input.
        """
        while True:
            self._print_field()
            try:
                cmd = input(PROMPT)
                self._invoke_cmd(cmd)
            except EOFError:  # Allows to exit by pressing ⌃D without error
                break

    def event_game_over(self):
        """
        Makes the game over, exits after printing a message
        """
        print('Game over!')
        self._cmd_exit()

    def _print_field(self):
        """
        Prints the current game field state as a text grid.
        """
        for y in range(self.game.field.size[1]):
            for x in range(self.game.field.size[0]):
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
            nl()
        nl()

    def _invoke_cmd(self, cmd):
        """
        Invoke a command by name, print command list if unknown name given.
        """
        if cmd in self.COMMANDS:
            self.COMMANDS[cmd]()
        else:
            print(ERROR_UNKNOWN_COMMAND.format(cmd=cmd))

    def _cmd_exit(self):
        """
        Break from the game loop.
        """
        raise EOFError()


def nl():
    """
    Prints a new-line
    """
    print('')  # \n


if __name__ == '__main__':
    # Game launcher. Initializes the game and its CLI interace.
    game = Game(FIELD_SIZE)
    app = App(game)

    game.register_events(on_collision=app.event_game_over)
    app.loop()
