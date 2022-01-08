from .module import Module

import time


class Time(Module):
    def __init__(self, format: str = "%H:%M:%S"):
        self.format = format

    async def get(self) -> str:
        return time.strftime(self.format)
