"""
Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""
from src.Cell import Cell
from src.GameField import GameField
from src.GameRenderer import GameRenderer
from src.NoopRenderer import NoopRenderer
from src.State import State

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


class GameOfLife:
    def __init__(self, seed: list[str], renderer: GameRenderer = NoopRenderer()):
        self._field = GameField.from_seed(seed, 'X')
        self.renderer = renderer
        self.renderer.render(self._field)

    @property
    def field(self): return self._field

    def tick(self):
        self.__prepare_cells()
        self.__apply_cells()
        self.renderer.render(self._field)

    def __prepare_cells(self):
        _map = self.field.map
        for (row, col) in _map:
            cell = _map[(row, col)]
            living_neighbours = self.field.get_living_neighbours_of(row, col)
            apply_rule_underpopulation(cell, living_neighbours)
            apply_rule_sweetspot(cell, living_neighbours)
            apply_rule_overpopulation(cell, living_neighbours)
            apply_rule_generation(cell, living_neighbours)

    def __apply_cells(self):
        _map = self.field.map
        self.field.resolve_flags()
        self.field.cleanup()

