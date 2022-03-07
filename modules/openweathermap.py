import logging
from typing import Optional

import httpx

from .module import Module


class OpenWeatherMap(Module):
    icons = {
        "01": "☀",
        "02": "⛅",
        "03": "☁",
        "04": "☁",
        "09": "🌧",
        "10": "🌦",
        "11": "⛈",
        "13": "❄",
        "50": "🌫"
    }

    def __init__(self, app_id: str, city: str, city_id: int = None, lang: str = "ru"):
        self.city = city
        self.city_id = city_id
        self.lang = lang
        self.hclient = httpx.AsyncClient(
            base_url="http://api.openweathermap.org/data/2.5/",
            params={
                "APPID": app_id,
            })

    async def get(self) -> Optional[str]:
        if self.city_id is None:
            response = (
                await self.hclient.get("find", params={"q": self.city, "type": "like", "units": "metric"})).json()

            logging.info("City found %s (%s)", response["list"][0]["name"], response["list"][0]["sys"]["country"])

            self.city_id = response["list"][0]["id"]

        response = (
            await self.hclient.get("weather", params={"id": self.city_id, "units": "metric", "lang": self.lang})).json()

        return "{}{}°C".format(OpenWeatherMap.icons[response["weather"][0]["icon"][:2]], response["main"]["temp"])
