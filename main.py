# This is a sample Python script.
from Game import Game
from GameField import GameField
from FieldPrinter import FieldPrinter


def main():
    field = GameField.from_file("seed.dat", "X")
    printer = FieldPrinter(field)
    printer.print_field()
    game = Game(field)
    for i in range(20):
        game.tick()
        printer.print_sep()
        printer.print_field()


if __name__ == '__main__':
    main()
