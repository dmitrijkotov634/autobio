from typing import Any

from telethon.tl.functions.contacts import GetBlockedRequest

from .value import Value


class BlockedCount(Value):
    async def get(self, **data: Any) -> int:
        result = await data["client"](GetBlockedRequest(offset=0, limit=1))
        return result.count
