from abc import ABCMeta, abstractmethod
from telethon import TelegramClient


class Module(metaclass=ABCMeta):
    def setup(self, client: TelegramClient):
        self.client = client

    @abstractmethod
    async def get(self) -> str:
        raise NotImplemented()
