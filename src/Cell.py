from src.State import State

class Cell:
    def __init__(self, state: State):
        self._flag = None
        self.state = state

    @property
    def flag(self): return self._flag

    @flag.setter
    def flag(self, value: State): self._flag = value

    def resolve_flag(self):
        if self._flag is None: return
        self.state = self._flag
        self._flag = None
        return self.state
