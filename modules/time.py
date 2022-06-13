import time
from typing import Union

from .value import Value


class Time(Value):
    def __init__(self, format_: Union[str, Value] = "%H:%M:%S"):
        """The value that gives the formatted current time

        :param format_: Time format according to 1989 C standard
        """
        self.format = format_

    async def get(self, **data) -> str:
        return time.strftime(await Value.resolve(self.format, **data))
