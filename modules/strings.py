from itertools import cycle
from typing import Optional

from .module import Module


class Cycle(Module):
    def __init__(self, *strings: str):
        self.iter = iter(cycle(strings))

    async def get(self) -> Optional[str]:
        return next(self.iter)


class Ticker(Module):
    def __init__(self, string: str):
        self.iter = iter(cycle(range(len(string))))
        self.string = string

    async def get(self) -> Optional[str]:
        index = next(self.iter)
        return self.string[index:] + self.string[:index]
