from .module import Module
from telethon.tl.functions.contacts import GetBlockedRequest


class BlockedCount(Module):
    async def get(self) -> str:
        result = await self.client(GetBlockedRequest(offset=0, limit=1))
        return result.count
