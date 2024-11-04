from GameField import GameField
from State import State


class FieldPrinter:
    character_map = {State.DEAD: "▯", State.ALIVE: "▮"}

    def __init__(self, field: GameField):
        self.field = field

    def print_field(self):
        for row in self.field.map:
            for col in row:
                print(self.character_map.get(col.state), end="")
            print()

    def print_sep(self):
            for _ in self.field.map[0]:
                print("#", end="")
            print()
