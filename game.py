class Snake:
    def __init__(self, initial_coords):
        """
        Creates a new snake of length one block on the given coords.
        """
        self.coords = [initial_coords]

    def slither(self, offset):
        """
        Slither relatively from the snake’s head. The head end is extended to
        the computed coordinates and then the snake’s tail is trimmed.
        """
        old_head_coords = self.head_coords()
        new_head_coords = (
            old_head_coords[0] + offset[0],
            old_head_coords[1] + offset[1]
        )
        self.coords.append(new_head_coords)  # Move the head
        del self.coords[0]  # Trim the tail

    def head_coords(self):
        return self.coords[-1]


class Game:
    def __init__(self, field_size):
        """
        Spawn a snake in the center of the field of a given size. Creates a
        list of all things on the field.
        """
        self.field = Field(field_size)
        self.snake = Snake(self.field.center())
        self.things = [self.snake]

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
        self._slither((0, -1))

    def input_south(self):
        """
        Tells the snake to slither southward: one block down.
        """
        self._slither((0, 1))

    def input_west(self):
        """
        Tells the snake to slither westward: one block left.
        """
        self._slither((-1, 0))

    def input_east(self):
        """
        Tells the snake to slither eastward: one block right.
        """
        self._slither((1, 0))

    def _slither(self, offset):
        """
        Tells the snake to slither with a given offset, checks whether tha snake
        is still in the field.
        """
        self.snake.slither(offset)
        if not self._check_snake_in_field():
            self.events['collision']()

    def _check_snake_in_field(self):
        """
        Checks whether the snake’s head is in the field.
        """
        snake_coords = self.snake.head_coords()
        return self.field.is_inside(snake_coords)


class Field:
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