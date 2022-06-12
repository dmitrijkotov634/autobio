from typing import Any

from .value import Value


class MembersCount(Value):
    def __init__(self, entity: Any):
        """
        Value that gives the number of members in a group or channel

        :param entity: Entity
        """

        self.entity = entity

    async def get(self, **data: Any) -> Any:
        return str((await data["client"].get_participants(await Value.resolve(self.entity, **data),
                                                          limit=0)).total)
