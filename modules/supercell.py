from typing import Optional

import httpx

from .module import Module


class Supercell(Module):
    base_url: str
    base_key: str

    def __init__(self, tag: str, token: str):
        self.hclient = httpx.AsyncClient(
            base_url=self.base_url,
            headers={
                "Accept": "application/json",
                "authorization": "Bearer " + token
            })

        self.tag = tag

    async def get(self) -> Optional[str]:
        response = (await self.hclient.get("players/%23" + self.tag)).json()
        return response.get(self.base_key)


class BrawlStarsTrophies(Supercell):
    base_url = "https://api.brawlstars.com/v1/"
    base_key = "trophies"


class ClashRoyaleTrophies(Supercell):
    base_url = "https://api.clashroyale.com/v1/"
    base_key = "trophies"
