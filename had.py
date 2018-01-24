INITIAL_SNAKE_COORDS = [(5, 5)]


class Thing:
    def __init__(self, coords):
        self.coords = coords


class Snake(Thing):
    def __init__(self):
        super().__init__(INITIAL_SNAKE_COORDS)


class Game:
    def __init__(self, field_size):
        self.field_size = field_size
        self.things = [Snake()]

    def what_is_on_coords(self, coords):
        """
        Returns a list of all things that are on given coordinates.
        """
        return [thing for thing in self.things if coords in thing.coords]
