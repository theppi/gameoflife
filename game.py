from collections import defaultdict
from math import floor

import pygame

from CellField import CellField
from src.GameOfLife import GameOfLife
from src.State import State

DEAD_COLOR = "Grey"
ALIVE_COLOR = "Red"
BACKGROUND_COLOR = "white"

def noop(_ = None):
    pass

def snoop():
    pass

border = 10
cell_size = 10

class Game:
    dt = 0
    framerate = 1
    grid = {}

    _running = True
    _pause = True

    keymap = defaultdict(lambda: snoop)
    eventmap = defaultdict(lambda: noop)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.clock = pygame.time.Clock()

        with open("seed.dat") as file:
            seed = file.read().splitlines()

        self.game_logic = GameOfLife(seed)
        self._init_keymap()
        self._init_event_handler()

    def _init_keymap(self):
        self.keymap.update({
            pygame.K_ESCAPE:    self.quit,
            pygame.K_SPACE:     self.pause
        })

    def _init_event_handler(self):
        self.eventmap.update({
            pygame.QUIT:            lambda _: self.quit(),
            pygame.KEYDOWN:         lambda event: self.keymap[event.key](),
            pygame.MOUSEBUTTONDOWN: lambda event: self.revive_cell(event.pos)
        })

    def run(self):
        self.prepare()
        while self._running: self.loop()
        pygame.quit()

    def pause(self):
        self._pause = not self._pause

    def quit(self):
        self._running = False

    def prepare(self):
        self.screen.fill("white")
        count_width = floor((self.screen.get_width() - (2 * border)) / cell_size)
        count_height = floor((self.screen.get_height() - (2 * border)) / cell_size)
        for x in range(count_width):
            for y in range(count_height):
                self._create_field(x, y)

    def _create_field(self, x: int, y: int):
        field = CellField(self.screen, border + cell_size * x, border + cell_size * y, cell_size)
        if self.game_logic.field.get_cell_state(y, x) == State.ALIVE: field.color = "Red"
        self.grid[(x, y)] = field
        field.render()

    def loop(self):
        self.handle_events()
        self.render()
        self.update()

        pygame.display.flip()

        self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            self.eventmap[event.type](event)

    def render(self):
        self.screen.fill(BACKGROUND_COLOR)
        for (x, y) in self.grid:
            self.grid[(x,y)].render()

    def update(self):
        if self._pause: return
        self.dt = (self.dt + 1) % self.framerate
        if self.dt != 0:
            return
        self.game_logic.tick()
        self.__apply_state()

    def __apply_state(self):
        for (x, y) in self.grid:
            if self.game_logic.field.get_cell_state(y, x) == State.ALIVE:
                self.grid[(x, y)].color = ALIVE_COLOR
                continue
            else:
                self.grid[(x, y)].color = DEAD_COLOR

    def revive_cell(self, pos):
        x = round((pos[0]-border - 0.5 * cell_size) / cell_size)
        y = round((pos[1]-border - 0.5 * cell_size) / cell_size)
        self.game_logic.field.set_cell_state(y, x, State.ALIVE)
        self.grid[(x, y)].color = ALIVE_COLOR
        self.grid[(x, y)].render()

if __name__ == '__main__':
    new_game = Game()
    new_game.run()