from abc import ABCMeta, abstractmethod
from typing import Optional

from telethon import TelegramClient


class Module(metaclass=ABCMeta):
    client: TelegramClient

    def setup(self, client: TelegramClient):
        self.client = client

    @abstractmethod
    async def get(self) -> Optional[str]:
        raise NotImplementedError()
