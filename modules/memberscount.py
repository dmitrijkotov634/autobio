from .module import Module

class MembersCount(Module):
    def __init__(self, entity):
        self.entity = entity

    async def get(self):
        return str((await self.client.get_participants(self.entity,
                                                       limit=0)).total)
