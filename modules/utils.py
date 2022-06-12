from itertools import cycle
from typing import Any, Callable

from modules.value import Value


class Cycle(Value):
    def __init__(self, *values: Any):
        """A value that returns one value after another value

        :param values: Values to be iterated
        """
        self.iter = iter(cycle(values))

    async def get(self, **data: Any) -> Any:
        return next(self.iter)


class Format(Value):
    def __init__(self, pattern: Any, *args: Any):
        """The value that returns the formatted string

        :param pattern: Printf-style string formatting pattern
        :param args: Arguments
        """
        self.string = pattern
        self.args = args

    async def get(self, **data: Any) -> Any:
        return (await Value.resolve(self.string, **data)) % tuple(
            [await Value.resolve(arg, **data) for arg in self.args])


class Apply(Value):
    def __init__(self, value: Any, function: Callable):
        """Applies function to value

        :param value: Value
        :param function: Function
        """
        self.values = value
        self.function = function

    async def get(self, **data: Any) -> Any:
        return self.function(await Value.resolve(self.values, **data))


def placeholder(value: Any) -> Callable:
    return lambda v: v if v else value
