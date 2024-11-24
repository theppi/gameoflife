import pygame


class CellField:
    color = "Grey"
    def __init__(self, screen, x_0, y_0, size):
        self.screen = screen
        self.x_0 = x_0
        self.y_0 = y_0
        self.rect = pygame.Rect(x_0, y_0, size - 1, size - 1)
    def render(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
