from typing import Optional

from telethon.tl.functions.contacts import GetBlockedRequest

from .module import Module


class BlockedCount(Module):
    async def get(self) -> Optional[str]:
        result = await self.client(GetBlockedRequest(offset=0, limit=1))
        return result.count
