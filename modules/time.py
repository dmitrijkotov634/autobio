import time
from typing import Optional

from .module import Module


class Time(Module):
    def __init__(self, format_="%H:%M:%S"):
        self.format = format_

    async def get(self) -> Optional[str]:
        return time.strftime(self.format)
