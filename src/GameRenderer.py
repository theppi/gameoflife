from abc import ABC, abstractmethod

from src.GameField import GameField


class GameRenderer(ABC):
    @abstractmethod
    def render(self, field: GameField):
        pass
