from telethon import TelegramClient, errors
from telethon.tl.functions.account import UpdateProfileRequest
from string import Template

import config
import asyncio

client = TelegramClient(config.SESSION_NAME, config.API_ID, config.API_HASH)

templates = {}
for name, template in config.TEMPLATES.items():
    if template:
        templates[name] = Template(template)


async def main():
    await client.start()

    for module in config.MODULES.values():
        module.setup(client)

    response = {}
    while True:
        for name, module in config.MODULES.items():
            response[name] = await module.get()

        result = {}
        for name, template in templates.items():
            result[name] = template.substitute(response)

        try:
            await client(UpdateProfileRequest(**result))
        except errors.FloodWaitError as e:
            await asyncio.sleep(e.seconds)

        await asyncio.sleep(config.INTERVAL)


asyncio.run(main())
