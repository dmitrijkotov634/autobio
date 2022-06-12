from itertools import cycle
from typing import Any, Callable, Union

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
    def __init__(self, pattern: Union[str, Value], *args: Any):
        """The value that returns the formatted string

        :param pattern: Printf-style string formatting pattern
        :param args: Arguments
        """
        self.string = pattern
        self.args = args

    async def get(self, **data: Any) -> str:
        return (await Value.resolve(self.string, **data)) % tuple(
            [await Value.resolve(arg, **data) for arg in self.args])


class Apply(Value):
    def __init__(self, value: Any, function: Callable):
        """Applies function to value

        :param value: Value
        :param function: Function
        """
        self.value = value
        self.function = function

    async def get(self, **data: Any) -> Any:
        return self.function(await Value.resolve(self.value, **data))


class Default(Value):
    def __init__(self, value: Any, default: Any):
        """Returns the default value if the value is false

        :param value: Value
        :param default: Default value
        """
        self.value = value
        self.default = default

    async def get(self, **data: Any) -> Any:
        data = await Value.resolve(self.value, **data)
        return data if data else await Value.resolve(self.default, **data)
