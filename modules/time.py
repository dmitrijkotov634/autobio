from .module import Module

import time

class Time(Module):
    def __init__(self, format="%H:%M:%S"):
        self.format = format

    async def get(self):
        return time.strftime(self.format)
