from typing import Optional

import httpx

from .module import Module


class BrawlStarsTrophies(Module):
    def __init__(self, tag: str, token: str):
        self.hclient = httpx.AsyncClient(
            base_url='https://api.brawlstars.com/v1/',
            headers={
                'Accept': 'application/json',
                'authorization': 'Bearer ' + token
            })

        self.tag = tag

    async def get(self) -> Optional[str]:
        response = (await self.hclient.get('players/%23' + self.tag)).json()
        return response.get('trophies')
