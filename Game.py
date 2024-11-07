"""
Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""
from Cell import Cell
from GameField import GameField
from State import State

# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
def apply_rule_underpopulation(col: Cell, living_neighbours):
    if col.state != State.ALIVE: return
    if living_neighbours < 2: col.flag = State.DEAD

#Any live cell with two or three live neighbours lives on to the next generation.
def apply_rule_sweetspot(col, living_neighbours):
    if col.state != State.ALIVE: return
    if living_neighbours in [2,3]: return
    col.flag = State.DEAD

# Any live cell with more than three live neighbours dies, as if by overpopulation.
def apply_rule_overpopulation(col, living_neighbours):
    if col.state != State.ALIVE: return
    if living_neighbours >3: col.flag = State.DEAD

# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
def apply_rule_generation(col, living_neighbours):
    if col.state != State.DEAD: return
    if living_neighbours ==3: col.flag = State.ALIVE


class Game:
    def __init__(self, field: GameField):
        self._field = field

    @property
    def field(self): return self._field

    def tick(self):
        _map = self._field.map
        for row_idx, row in enumerate(_map):
            for col_idx, col in enumerate(row):
                living_neighbours = self.field.get_living_neighbours_of(row_idx, col_idx)
                apply_rule_underpopulation(col, living_neighbours)
                apply_rule_sweetspot(col, living_neighbours)
                apply_rule_overpopulation(col, living_neighbours)
                apply_rule_generation(col, living_neighbours)
        for row in _map:
            for col in row:
                col.resolve_flag()
