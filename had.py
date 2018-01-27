class Snake:
    def __init__(self, initial_coords):
        self.coords = [initial_coords]


class Game:
    def __init__(self, field_size):
        self.field_size = field_size
        self.things = [Snake(self.center_coords())]

    def what_is_on_coords(self, coords):
        """
        Returns a list of all things that are on given coordinates.
        """
        return [thing for thing in self.things if coords in thing.coords]

    def center_coords(self):
        max_x = self.field_size[0] - 1
        max_y = self.field_size[1] - 1
        return (max_x // 2, max_y // 2)
