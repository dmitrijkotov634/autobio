import time
from typing import Any

from .value import Value


class Time(Value):
    def __init__(self, format_: Any = "%H:%M:%S"):
        """The value that gives the formatted current time

        :param format_: Time format according to 1989 C standard
        """

        self.format = format_

    async def get(self, **data: Any) -> Any:
        return time.strftime(await Value.resolve(self.format, **data))
