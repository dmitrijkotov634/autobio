from .module import Module
from itertools import cycle


class Cycle(Module):
    def __init__(self, *strings):
        self.iter = iter(cycle(strings))

    async def get(self) -> str:
        return next(self.iter)
