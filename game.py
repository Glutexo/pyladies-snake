class Snake:
    def __init__(self, initial_coords):
        """
        Creates a new snake of length one block on the given coords.
        """
        self.coords = [initial_coords]

    def head_coords(self):
        """
        Returns coordinates of the snake’s head – the last coordinates in the
        list.
        """
        return self.coords[-1]

    def extend_to(self, coords):
        """
        Make the snake longer by moving his head to new coordinates. Its
        previous head coordinates become its body.
        """
        self.coords.append(coords)

    def trim_tail(self):
        """
        Make the snake shorter by removing the last block of its tail.
        """
        del self.coords[0]

    def slither_to(self, coords):
        """
        Slither to the given coordinates. Effectively extending the snake to
        the new coordinates from the head end and then trimming its tail.
        """
        self.extend_to(coords)
        self.trim_tail()

    def slither_north(self):
        """
        Slither northward.
        """
        # Append new head coordinates one block up from the current head.
        old_head_coords = self.head_coords()
        new_head_coords = (old_head_coords[0], old_head_coords[1] - 1)
        self.slither_to(new_head_coords)


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
        Tells the snake to slither northward.
        """
        self.snake.slither_north()
