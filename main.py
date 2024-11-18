# This is a sample Python script.
import time

from src.GameOfLife import GameOfLife
from ConsoleRenderer import ConsoleRenderer, Area

def main():
    with open("seed.dat") as file:
        seed = file.read().splitlines()
    game = GameOfLife(seed, ConsoleRenderer(Area(12, 12, 7, 2), "▮", "▯", " "))
    for i in range(20):
        game.tick()
        time.sleep(0.1)

if __name__ == '__main__':
    main()
