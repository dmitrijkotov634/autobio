import httpx

from .value import Value


class WakaTime(Value):
    def __init__(self, api_key: str):
        """Value in which the amount of programming time is found according to wakatime statistics

        :param api_key: Api key
        """
        self.http_client = httpx.AsyncClient(
            params={
                "api_key": api_key
            })

    async def get(self, **data) -> int:
        response = (await self.http_client.get("https://wakatime.com/api/v1/users/current/status_bar/today")).json()
        return response["data"]["grand_total"]["text"]
