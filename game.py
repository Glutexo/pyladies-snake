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
        old_head_coords = self.coords[-1]
        new_head_coords = (
            old_head_coords[0] + offset[0],
            old_head_coords[1] + offset[1]
        )
        self.coords.append(new_head_coords)  # Move the head
        del self.coords[0]  # Trim the tail


class Game:
    def __init__(self, field_size):
        """
        Spawn a snake in the center of the field of a given size. Creates a
        list of all things on the field.
        """
        self.field_size = field_size
        self.snake = Snake(self.center_coords())
        self.things = [self.snake]

    def what_is_on_coords(self, coords):
        """
        Returns a list of all things that are on given coordinates.
        """
        return [thing for thing in self.things if coords in thing.coords]

    def center_coords(self):
        """
        Computes the (approximate for even numbers) center of the game field.
        """
        max_x = self.field_size[0] - 1
        max_y = self.field_size[1] - 1
        return (max_x // 2, max_y // 2)

    def input_north(self):
        """
        Tells the snake to slither northward: one block up
        """
        self.snake.slither((0, -1))

    def input_south(self):
        """
        Tells the snake to slither southward: one block down
        """
        self.snake.slither((0, 1))

    def input_west(self):
        """
        Tells the snake to slither westward: one block left
        """
        self.snake.slither((-1, 0))

    def input_east(self):
        """
        Tells the snake to slither eastward: one block right
        """
        self.snake.slither((1, 0))
