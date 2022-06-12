import asyncio
import logging

from telethon import TelegramClient, errors
from telethon.tl.functions.account import UpdateProfileRequest

import config
from modules.value import Value

logging.basicConfig(level=logging.INFO)

client = TelegramClient(config.SESSION_NAME, config.API_ID, config.API_HASH)


async def main():
    responses = {}
    while True:
        for variable, value in config.MODULES.items():
            responses[variable] = await Value.resolve(value, client=client)

        params = {}
        for param, template in config.TEMPLATES.items():
            if template:
                params[param] = template.substitute(responses)

        if len(params.get("about", "")) > 70:
            params["about"] = params["about"][:67] + "..."
            logging.warning("Too long about")

        try:
            await client(UpdateProfileRequest(**params))
        except errors.FloodWaitError as e:
            logging.warning("Flood wait for %d seconds", e.seconds)
            await asyncio.sleep(e.seconds)

        await asyncio.sleep(config.INTERVAL)


with client:
    client.loop.run_until_complete(main())
