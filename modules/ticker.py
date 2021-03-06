from itertools import cycle

from .value import Value


class Ticker(Value):
    def __init__(self, string: str):
        """The value that gives each time the text shifted to the right

        :param string: String
        """
        self.iter = iter(cycle(range(len(string))))
        self.string = string

    async def get(self, **data) -> str:
        index = next(self.iter)
        return self.string[index:] + self.string[:index]
