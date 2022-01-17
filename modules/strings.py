from .module import Module
from itertools import cycle

class Cycle(Module):
    def __init__(self, *strings):
        self.iter = iter(cycle(strings))

    async def get(self):
        return next(self.iter)

class Ticker(Module):
    def __init__(self, string):
        self.iter = iter(cycle(range(len(string))))
        self.string = string

    async def get(self):
        index = next(self.iter)
        return self.string[index:] + self.string[:index]
