import asyncio
import logging
from string import Template

from telethon import TelegramClient, errors
from telethon.tl.functions.account import UpdateProfileRequest

import config

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
        for template_name, m in config.MODULES.items():
            response = await m.get()
            responses[template_name] = response if response else config.PLACEHOLDER

        result = {}
        for template_name, prepared_template in templates.items():
            result[template_name] = prepared_template.substitute(responses)

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
