from src.GameField import GameField
from src.GameRenderer import GameRenderer


class NoopRenderer(GameRenderer):
    def render(self, field: GameField):
        pass