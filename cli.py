# coding=utf-8
from had import Game, Snake


FIELD_SIZE = (11, 13)
SYMBOLS = {Snake: 'X', None: '.'}


def print_field(game):
    """
    Prints the current game field state as a text grid.
    """
    for y in range(FIELD_SIZE[1]):
        for x in range(FIELD_SIZE[0]):
            thing_type = None  # Default: nothing on the coords.

            all_things_on_coords = game.what_is_on_coords((x, y))
            if all_things_on_coords:
                # If there are more things on one coordinates, only the first
                # one is printed. Symbol is determined by the class of the
                # thing.
                thing_type = type(all_things_on_coords[0])

            # Symbols are horizontally separated by a space for better
            # legibility.
            print(SYMBOLS[thing_type], end=' ')  # . . . X . .
        print('')  # \n


if __name__ == '__main__':
    game = Game(FIELD_SIZE)
    print_field(game)
