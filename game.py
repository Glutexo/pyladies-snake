# coding=utf-8

from random import choice


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

    def slithered_to(self, coords, extend=False):
        """
        Finish the slithering to the given coordinates.
        """
        self.coords.append(coords)  # Move the head

        # Do not trim the tail (grow) if a piece of fruit has been eaten.
        if not extend:
            del self.coords[0]  # Trim the tail

    def head_coords(self):
        """
        Returns single coordinates of the snake’s head.
        """
        return self.coords[-1]

    def _slither(self, offset):
        """
        Slithers by the given offset. Returns the resulting coordinates.
        """
        head_coords = self.head_coords()
        return head_coords[0] + offset[0], head_coords[1] + offset[1]


class Fruit:
    def __init__(self, coords):
        self.coords = [coords]


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
        self.things = set()

        self._spawn_snake()
        self._spawn_fruit()

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

    def slither_north(self):
        """
        Tells the snake to slither northward: one block up.
        """
        self._slither(self.snake.slither_north)

    def slither_south(self):
        """
        Tells the snake to slither southward: one block down.
        """
        self._slither(self.snake.slither_south)

    def slither_west(self):
        """
        Tells the snake to slither westward: one block left.
        """
        self._slither(self.snake.slither_west)

    def slither_east(self):
        """
        Tells the snake to slither eastward: one block right.
        """
        self._slither(self.snake.slither_east)

    def _slither(self, snake_slither_callback):
        """
        Tells the snake to slither in a given direction. Process collision.s
        """
        new_head_coords = snake_slither_callback()
        if not self.field.is_inside(new_head_coords):
            # The snake leaves the field. Collision, game over!
            self._fire_event('collision')
            return

        fruit_eaten = False
        for thing in self.what_is_on_coords(new_head_coords):
            if type(thing) == Fruit:
                # The snake has eaten a piece of fruit: Remove it and spawn a
                # new one.
                fruit_eaten = True
                self.things.remove(thing)
                self._spawn_fruit(set([new_head_coords]))

        # If the snake has eaten a piece of fruit, it will grow.
        self.snake.slithered_to(new_head_coords, fruit_eaten)

    def _fire_event(self, event_name):
        """
        Fires a registered event.
        """
        if self.events[event_name]:
            self.events[event_name]()

    def _spawn_snake(self):
        """
        Spawns the snake in the middle of the field.
        """
        self.snake = Snake(self.field.center_coords())
        self.things.add(self.snake)

    def _spawn_fruit(self, excluded_coords=set()):
        """
        Spawns a new fruit at random empty coords, if the field is not
        completely full.
        """
        fruit_coords = self._random_free_coords(excluded_coords)
        if fruit_coords:
            fruit = Fruit(fruit_coords)
            self.things.add(fruit)

    def _all_occupied_coords(self):
        """
        Populates all occupied coords in the field.
        """
        return set(
            thing_coords
            for thing in self.things
            for thing_coords in thing.coords
        )

    def _all_free_coords(self):
        """
        Populates all free coords in the field.
        """
        return self.field.all_coords() - self._all_occupied_coords()

    def _random_free_coords(self, excluded_coords):
        """
        Finds random free coords in the field. Returns None if the fields is
        completely full.
        """
        free_coords = self._all_free_coords() - excluded_coords
        return choice(list(free_coords)) if free_coords else None


class Field:
    """
    Game field of some size.
    """

    def __init__(self, size):
        """
        Creates a new game field of a given size
        """
        self.size = size

    def center_coords(self):
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

    def all_coords(self):
        """
        Populate all coords in the field.
        """
        return {
            (x, y)
            for x in range(self.size[0])
            for y in range(self.size[1])
        }
