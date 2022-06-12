from typing import Any

import httpx

from .value import Value


class LastFm(Value):
    def __init__(self, api_key: str, username: str):
        """Value that gives the current track being played on last.fm

        :param api_key: API key for last.fm service
        :param username: Last.fm username
        """

        self.http_client = httpx.AsyncClient(
            base_url="https://ws.audioscrobbler.com/2.0",
            params={
                "method": "user.getrecenttracks",
                "user": username,
                "api_key": api_key,
                "format": "json"
            })

    async def get(self, **data: Any) -> Any:
        response = (await self.http_client.get("/")).json()
        if "error" in response:
            return

        last = response["recenttracks"]["track"][0]
        if "@attr" in last and last["@attr"]["nowplaying"] == "true":
            return f"{last['artist']['#text']} — {last['name']}"
