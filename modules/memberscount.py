from typing import Optional

from .module import Module


class MembersCount(Module):
    def __init__(self, entity: str):
        self.entity = entity

    async def get(self) -> Optional[str]:
        return str((await self.client.get_participants(self.entity,
                                                       limit=0)).total)
