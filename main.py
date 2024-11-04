# This is a sample Python script.
from GameField import GameField
from FieldPrinter import FieldPrinter


def main():
    field = GameField.from_file("seed.dat", "X")
    printer = FieldPrinter()
    printer.print_field(field)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
