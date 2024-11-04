from Cell import Cell
from State import State

class GameField:
    def __init__(self, width: int, height: int):
        if abs(width) < 3 or abs(height) < 3:
            raise Exception("Out of bounds")
        self._map = [[Cell(State.DEAD) for _ in range(abs(width))] for _ in range(abs(height))]

    def set_cell_state(self, row: int, col: int, state: State):
        self._map[row][col].state = state

    @property
    def height(self): return len(self._map)

    @property
    def width(self): return len(self._map[0])

    @property
    def map(self): return self._map

    def get_cell(self, row, col):
        return self._map[row % self.height][col % self.width]

    def get_cell_state(self, row, col):
        return self.get_cell(row, col).state

    def get_subset_at(self, row: int, col: int):
        subset = [
            [self.get_cell(row - 1, col - 1), self.get_cell(row - 1, col), self.get_cell(row - 1, col + 1)],
            [self.get_cell(row, col - 1), self.get_cell(row, col), self.get_cell(row, col + 1)],
            [self.get_cell(row + 1, col - 1), self.get_cell(row + 1, col), self.get_cell(row + 1, col + 1)],
        ]
        # print(f"subset at {row}, {col}: \n{subset[0][0].state}, {subset[0][1].state}, {subset[0][2].state}, \n{subset[1][0].state}, {subset[1][1].state}, {subset[1][2].state}, \n{subset[2][0].state}, {subset[2][1].state}, {subset[2][2].state}")
        return subset

    def get_living_neighbours_of(self, row: int, col: int):
        subfield = self.get_subset_at(row, col)
        living = 0
        for row_id, subrow in enumerate(subfield):
            for col_id, subcol in enumerate(subrow):
                if row_id == 1 and col_id == 1: continue
                if subcol.state == State.ALIVE: living = living + 1
        return living

    @staticmethod
    def from_seed(seed, alive_character):
        width = len(max(seed, key=len))
        height = len(seed)
        field = GameField(width, height)
        for row, line in enumerate(seed):
            for col, character in enumerate(line):
                if character == alive_character: field.set_cell_state(row, col, State.ALIVE)
        return field

    @staticmethod
    def from_file(file, alive_character):
        with open(file) as file:
            seed = file.read().splitlines()
        return GameField.from_seed(seed, alive_character)



