import unittest

from Cell import Cell
from GameField import GameField
from FieldPrinter import FieldPrinter
from Game import Game
from State import State


class TestGame(unittest.TestCase):
    def testCellInitialization(self):
        cell = Cell(State.ALIVE)
        self.assertEqual(cell.state, State.ALIVE, 'Cells state is wrongly initiated')
        self.assertEqual(cell.flag, None, 'Cells state is wrongly initiated')

    def testCellFlagResolution(self):
        cell = Cell(State.ALIVE)
        cell.flag = State.DEAD
        cell.resolve_flag()
        self.assertEqual(cell.state, State.DEAD, 'Cells state is wrongly initiated')
        self.assertEqual(cell.flag, None, 'Cells state is wrongly initiated')

        cell = Cell(State.ALIVE)
        cell.resolve_flag()
        self.assertEqual(cell.state, State.ALIVE, 'Cells state is wrongly initiated')
        self.assertEqual(cell.flag, None, 'Cells state is wrongly initiated')

    def testFieldInitialization(self):
        width = 50
        height = 50
        field = GameField(width, height)
        for row in range(height):
            for col in range(width):
                self.assertEqual(field.get_cell_state(row,col), State.DEAD)
        for row in range(height):
            field.set_cell_state(row, 0, State.ALIVE)
        self.assertEqual(field.get_cell_state(0, height), State.ALIVE)
        self.assertEqual(field.get_cell_state(width, 0), State.ALIVE)
        self.assertEqual(field.get_cell_state(width, height), State.ALIVE)
        self.assertEqual(field.get_cell_state(0, -1), State.DEAD)
        self.assertEqual(field.get_cell_state(-1, 0), State.ALIVE)
        self.assertEqual(field.get_cell_state(-1, -1), State.DEAD)

    def test_rule_01(self):
        seed = "X\n X \n\n".splitlines()
        field = GameField.from_seed(seed, "X")
        self.assertEqual(field.get_cell_state(1, 1), State.ALIVE)
        self.assertEqual(field.get_cell_state(0, 0), State.ALIVE)
        game = Game(field)
        game.tick()
        self.assertEqual(field.get_cell_state(1, 1), State.DEAD)
        self.assertEqual(field.get_cell_state(0, 0), State.DEAD)

    def test_rule_02(self):
        seed = "\n  XXX  \n\n\n".splitlines()
        field = GameField.from_seed(seed, "X")
        field_printer = FieldPrinter(field)
        field_printer.print_field()
        print("-------------------------------------------------------")
        self.assertEqual(field.get_cell_state(0, 3), State.DEAD)
        self.assertEqual(field.get_cell_state(2, 3), State.DEAD)
        self.assertEqual(field.get_cell_state(1, 2), State.ALIVE)
        self.assertEqual(field.get_cell_state(1, 3), State.ALIVE)
        self.assertEqual(field.get_cell_state(1, 4), State.ALIVE)
        game = Game(field)
        game.tick()
        field_printer.print_field()
        print("-------------------------------------------------------")
        self.assertEqual(field.get_cell_state(0, 3), State.ALIVE)
        self.assertEqual(field.get_cell_state(2, 3), State.ALIVE)
        self.assertEqual(field.get_cell_state(1, 2), State.DEAD)
        self.assertEqual(field.get_cell_state(1, 3), State.ALIVE)
        self.assertEqual(field.get_cell_state(1, 4), State.DEAD)
        game.tick()
        field_printer.print_field()
        self.assertEqual(field.get_cell_state(0, 3), State.DEAD)
        self.assertEqual(field.get_cell_state(2, 3), State.DEAD)
        self.assertEqual(field.get_cell_state(1, 2), State.ALIVE)
        self.assertEqual(field.get_cell_state(1, 3), State.ALIVE)
        self.assertEqual(field.get_cell_state(1, 4), State.ALIVE)

if __name__ == '__main__':
    unittest.main()
