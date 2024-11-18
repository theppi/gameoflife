import string
from src.GameField import GameField
from src.GameRenderer import GameRenderer
from src.State import State


class Area:
    def __init__(self, width: int, height:int = None, x: int = 0, y: int = 0):
        self.width = abs(width)
        if height is None:
            self.height = width
        else:
            self.height = abs(height)
        self.x = x
        self.y = y

    def horizontal_range(self):
        return range(self.x, self.x + self.width)

    def vertical_range(self):
        return range(self.y, self.y + self.height)


class ConsoleRenderer(GameRenderer):

    character_map = {State.DEAD: "▯", State.ALIVE: "▮", None: "▯"}

    def __init__(self, area: Area, state_alive: string = None, state_dead: string = None, state_none: string = None):
        if state_alive is not None and len(state_alive) == 1:
            self.character_map.update({State.ALIVE: state_alive})
        if state_dead is not None and len(state_dead) == 1:
            self.character_map.update({State.DEAD: state_dead})
        if state_none is not None and len(state_dead) == 1:
            self.character_map.update({None: state_none})
        self.range = range
        self.area = area

    def render(self, field: GameField):
        self.print_sep()
        self.print_field(field)

    def print_field(self, field: GameField):
        for row in self.area.vertical_range():
            for col in self.area.horizontal_range():
                print(self.character_map.get(field.get_cell_state(row, col)), end="")
            print()

    def print_sep(self):
            for _ in self.area.vertical_range():
                print("#", end="")
            print()
