from telethon import TelegramClient, errors
from telethon.tl.functions.account import UpdateProfileRequest
from string import Template

import config
import asyncio
import logging

logging.basicConfig(level=logging.WARNING)

client = TelegramClient(config.SESSION_NAME, config.API_ID, config.API_HASH)

for module in config.MODULES.values():
    module.setup(client)

templates = {}
for name, template in config.TEMPLATES.items():
    if template:
        templates[name] = Template(template)

async def main():
    await client.start()

    responses = {}
    while True:
        for name, module in config.MODULES.items():
            response = await module.get()
            responses[name] = response if response else config.PLACEHODER

        result = {}
        for name, template in templates.items():
            result[name] = template.substitute(responses)

        if 'about' in result and len(result['about']) > 70:
            result['about'] = result['about'][:67] + '...'
            logging.warning('Too long about')

        try:
            await client(UpdateProfileRequest(**result))
        except errors.FloodWaitError as e:
            logging.warning('Flood wait for %d seconds', e.seconds)
            await asyncio.sleep(e.seconds)

        await asyncio.sleep(config.INTERVAL)

asyncio.run(main())