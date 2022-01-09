import httpx

from .module import Module


class LastFm(Module):
    def __init__(self, api_key: str, username: str, nothing_playing: str):
        self.nothing = nothing_playing
        self.hclient = httpx.AsyncClient(
            base_url='https://ws.audioscrobbler.com/2.0',
            params={
                'method': 'user.getrecenttracks',
                'user': username,
                'api_key': api_key,
                'format': 'json'
            }
        )

    async def get(self) -> str:
        response = await self.hclient.get('/')
        data = response.json()
        if 'error' in data:
            return self.nothing
        last = data['recenttracks']['track'][0]
        if '@attr' in last and last['@attr']['nowplaying'] == 'true':
            return f'{last["artist"]["#text"]} — {last["name"]}'
        else:
            return self.nothing
