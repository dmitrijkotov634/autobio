from typing import Any

import httpx

from .value import Value


class Supercell(Value):
    base_url: str
    base_key: str

    def __init__(self, tag: Any, api_token: str):
        """
        Value that stores the number of achievements in Supercell games

        :param tag: Player tag
        :param api_token: Token
        """

        self.http_client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={
                "Accept": "application/json",
                "authorization": "Bearer " + api_token
            })

        self.tag = tag

    async def get(self, **data: Any) -> Any:
        response = (await self.http_client.get("players/%23" + await Value.resolve(self.tag, **data))).json()
        return response.get(self.base_key)


class BrawlStarsTrophies(Supercell):
    base_url = "https://api.brawlstars.com/v1/"
    base_key = "trophies"


class ClashRoyaleTrophies(Supercell):
    base_url = "https://api.clashroyale.com/v1/"
    base_key = "trophies"
