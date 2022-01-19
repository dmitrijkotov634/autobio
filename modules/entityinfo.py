from typing import Optional, Callable

from telethon.tl.functions.users import GetFullUserRequest

from .module import Module


class EntityInfo(Module):
    def __init__(self, entity, getter: Callable = lambda o: o.about):
        self.entity = entity
        self.getter = getter

    async def get(self) -> Optional[str]:
        return self.getter(await self.client(GetFullUserRequest(self.entity)))
