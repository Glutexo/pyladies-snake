class Snake:
    """
    🐍
    """

    def __init__(self, initial_coords):
        """
        Creates a new snake of length one block on the given coords.
        """
        self.coords = [initial_coords]

    def slither_north(self):
        """
        Slithers northward: one block up. Returns the resulting coordinates.
        """
        return self._slither((0, -1))

    def slither_south(self):
        """
        Slithers southward: one block down. Returns the resulting coordinates.
        """
        return self._slither((0, 1))

    def slither_west(self):
        """
        Slithers westward: one block left. Returns the resulting coordinates.
        """
        return self._slither((-1, 0))

    def slither_east(self):
        """
        Slithers eastward: one block right. Returns the resulting coordinates.
        """
        return self._slither((1, 0))

    def slithered_to(self, coords):
        """
        Finish the slithering to the given coordinates.
        """
        self.coords.append(coords)  # Move the head
        del self.coords[0]  # Trim the tail

    def head_coords(self):
        return self.coords[-1]

    def _slither(self, offset):
        """
        Slithers by the given offset. Returns the resulting coordinates.
        """
        head_coords = self.head_coords()
        return head_coords[0] + offset[0], head_coords[1] + offset[1]


class Game:
    """
    The main game logic. Handles all the game actions including its IO. Emits
    events to the UI/launcher, provides event methods to be called by the UI.
    """
    def __init__(self, field_size):
        """
        Spawn a snake in the center of the field of a given size. Creates a
        list of all things on the field.
        """
        self.field = Field(field_size)
        self.snake = Snake(self.field.center())
        self.things = [self.snake]

        self.events = {
            'collision': None
        }

    def register_events(self, **kwargs):
        """
        Registers collision event.
        """
        self.events = {
            'collision': kwargs['on_collision']
        }

    def what_is_on_coords(self, coords):
        """
        Returns a list of all things that are on given coordinates.
        """
        return [thing for thing in self.things if coords in thing.coords]

    def input_north(self):
        """
        Tells the snake to slither northward: one block up.
        """
        self._slither(self.snake.slither_north)

    def input_south(self):
        """
        Tells the snake to slither southward: one block down.
        """
        self._slither(self.snake.slither_south)

    def input_west(self):
        """
        Tells the snake to slither westward: one block left.
        """
        self._slither(self.snake.slither_west)

    def input_east(self):
        """
        Tells the snake to slither eastward: one block right.
        """
        self._slither(self.snake.slither_east)

    def _slither(self, snake_slither_callback):
        """
        Tells the snake to slither in a given direction, checks whether the
        snake remains in the field.
        """
        new_head_coords = snake_slither_callback()
        if self.field.is_inside(new_head_coords):
            self.snake.slithered_to(new_head_coords)
        else:
            self._fire_event('collision')

    def _fire_event(self, event_name):
        """
        Fires a registered event.
        """
        if self.events[event_name]:
            self.events[event_name]()


class Field:
    """
    Game field of some size.
    """

    def __init__(self, size):
        """
        Creates a new game field of a given size
        """
        self.size = size

    def center(self):
        """
        Computes the (approximate for even numbers) center of the game field.
        """
        max_x = self.size[0] - 1
        max_y = self.size[1] - 1
        return max_x // 2, max_y // 2

    def is_inside(self, coords):
        """
        Checks where the given coords are inside the field.
        """
        return 0 <= coords[0] < self.size[0] and 0 <= coords[1] < self.size[1]
