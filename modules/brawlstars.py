from .module import Module
import httpx


class BrawlStarsTrophies(Module):
    def __init__(self, tag, token):
        self.hclient = httpx.AsyncClient(
            base_url='https://api.brawlstars.com/v1/',
            headers={
                'Accept': 'application/json',
                'authorization': 'Bearer ' + token
            })

        self.tag = tag

    async def get(self) -> str:
        response = (await self.hclient.get('players/%23' + self.tag)).json()
        return response.get('trophies', 0)
