from .module import Module

import httpx

class LastFm(Module):
    def __init__(self, api_key, username):
        self.hclient = httpx.AsyncClient(
            base_url='https://ws.audioscrobbler.com/2.0',
            params={
                'method': 'user.getrecenttracks',
                'user': username,
                'api_key': api_key,
                'format': 'json'
            })

    async def get(self):
        response = await self.hclient.get('/').json()
        if 'error' in response:
            return

        last = response['recenttracks']['track'][0]
        if '@attr' in last and last['@attr']['nowplaying'] == 'true':
            return f'{last["artist"]["#text"]} — {last["name"]}'
