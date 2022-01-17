from .module import Module
from telethon.tl.functions.users import GetFullUserRequest

class EntityInfo(Module):
    FIRST_NAME = lambda o: o.first_name
    LAST_NAME = lambda o: o.last_name
    ABOUT = lambda o: o.about

    def __init__(self, entity, getter=ABOUT):
        self.entity = entity
        self.getter = getter

    async def get(self):
        return getter(await self.client(GetFullUserRequest(self.entity)))
