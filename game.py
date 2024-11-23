import pygame

from src.GameOfLife import GameOfLife
from src.State import State


class CellField:
    color = "Grey"
    def __init__(self, screen, x_0, y_0):
        self.screen = screen
        self.x_0 = x_0
        self.y_0 = y_0
        self.rect = pygame.Rect(x_0, y_0, 29, 29)
    def render(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Game:
    grid = {}
    framerate = 20
    running = True
    dt = 0
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.clock = pygame.time.Clock()
        with open("seed.dat") as file:
            seed = file.read().splitlines()
        self.game_logic = GameOfLife(seed)

    def run(self):
        self.prepare()
        while self.running:
            self.loop()
        pygame.quit()

    def prepare(self):
        self.screen.fill("white")
        count_width = round((self.screen.get_width() - 20) / 30) - 1
        count_height = round((self.screen.get_height() - 20) / 30)
        for x in range(count_width):
            for y in range(count_height):
                field = CellField(self.screen, 10 + 30 * x, 10 + 30 * y)
                if self.game_logic.field.get_cell_state(y, x) == State.ALIVE:
                    field.color = "Red"
                self.grid[(x,y)] = field
                field.render()

    def loop(self):
        self.check_inputs()
        self.render()
        self.update()

        pygame.display.flip()

        self.clock.tick(60)

    def check_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.running = False
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def render(self):
        self.screen.fill("white")
        for (x, y) in self.grid:
            self.grid[(x,y)].render()

    def update(self):
        self.dt = (self.dt + 1) % self.framerate
        if self.dt != 0:
            return
        self.game_logic.tick()
        self.__apply_state()

    def __apply_state(self):
        for (x, y) in self.game_logic.field.map:
            if (y, x) not in self.grid:
                continue
            if self.game_logic.field.get_cell_state(x, y) == State.ALIVE:
                self.grid[(y, x)].color = "Red"
                continue
            else:
                self.grid[(y, x)].color = "Grey"

if __name__ == '__main__':
    game = Game()
    game.run()