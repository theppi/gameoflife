import string

from GameField import GameField
from State import State


class FieldPrinter:
    character_map = {State.DEAD: "▯", State.ALIVE: "▮"}

    def __init__(self, field: GameField, state_alive: string = None, state_dead: string = None):
        self.field = field
        if state_alive is not None and len(state_alive) == 1:
            self.character_map.update({State.ALIVE: state_alive})
        if state_dead is not None and len(state_dead) == 1:
            self.character_map.update({State.DEAD: state_dead})

    def print_field(self):
        for row in self.field.map:
            for col in row:
                print(self.character_map.get(col.state), end="")
            print()

    def print_sep(self):
            for _ in self.field.map[0]:
                print("#", end="")
            print()
