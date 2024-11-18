from operator import truediv

from src.Cell import Cell
from src.State import State

class GameField:
    def __init__(self):
        self.map = {}

    def set_cell_state(self, row: int, col: int, state: State):
        cell = self.__fetch_cell(row, col)
        cell.state = state
        self.__create_missing_neighbours_of(row, col)

    def __fetch_cell(self, row: int, col: int):
        if (row, col) not in self.map:
            self.map[(row, col)] = Cell(State.DEAD)
        return self.map[(row,col)]

    def get_cell_state(self, row: int, col: int):
        if (row, col) not in self.map:
            return None
        return self.map[(row, col)].state

    def get_living_neighbours_of(self, row: int, col: int):
        living = 0
        for _row in range(row-1, row+2):
            for _col in range(col-1, col+2):
                if not (_row == row and _col == col) and self.get_cell_state(_row, _col) == State.ALIVE:
                    living = living + 1
        return living

    @staticmethod
    def from_seed(seed: list[str], alive_character: str):
        field = GameField()
        for row, line in enumerate(seed):
            for col, character in enumerate(line):
                if character == alive_character[0]: field.set_cell_state(row, col, State.ALIVE)
        return field

    def __create_missing_neighbours_of(self, row, col):
        for _row in range(row - 1, row + 2):
            for _col in range(col - 1, col + 2):
                self.__fetch_cell(_row, _col)

    def resolve_flags(self):
        _map = dict(self.map)
        for (row, col) in _map:
            cell_state = self.map[(row, col)].resolve_flag()
            if cell_state == State.ALIVE:
                self.__create_missing_neighbours_of(row, col)
            del cell_state
        del _map

    def cleanup(self):
        _map = dict(self.map)
        for (row, col) in _map:
            cell_state = self.map[(row, col)].state
            if cell_state == State.DEAD:
                if not self.__has_living_neighbours(row, col):
                    del self.map[(row, col)]
            del cell_state
        del _map

    def __has_living_neighbours(self, row, col):
        for _row in range(row - 1, row + 2):
            for _col in range(col - 1, col + 2):
                if not (_row == row and _col == col) and self.get_cell_state(_row, _col) == State.ALIVE:
                    return True
        return False
