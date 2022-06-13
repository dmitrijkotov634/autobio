from typing import Callable, Any

from telethon.tl.functions.users import GetFullUserRequest

from .value import Value


class EntityInfo(Value):
    def __init__(self, entity: Any, getter: Callable = lambda o: o.about):
        """Value that returns information about the entity

        :param entity: Entity
        :param getter: Function that parses the output value
        """
        self.entity = entity
        self.getter = getter

    async def get(self, **data) -> str:
        return self.getter(await data["client"](GetFullUserRequest(await Value.resolve(self.entity, **data))))
