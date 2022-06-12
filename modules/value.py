from abc import abstractmethod, ABCMeta
from typing import Any


class Value(metaclass=ABCMeta):
    @abstractmethod
    async def get(self, **data: Any) -> Any:
        raise NotImplementedError()

    @staticmethod
    async def resolve(value: Any, **data: Any) -> Any:
        v = value
        while isinstance(v, Value):
            v = await v.get(**data)
        return v
