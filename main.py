import os

import discord
import asyncio
from Internals.Application import Application
from Internals.Configuration import initialize, getConfig

async def main():
    initialize("configuration.json")

    configIntents = getConfig("intents")

    intents = discord.Intents.default()

    for key, value in configIntents.items():
        setattr(intents, key, value)

    views = []

    bot = Application(command_prefix=".", views=views, intents=intents)

    await bot.start(os.getenv("TOKEN"))

if __name__ == "__main__":
    asyncio.run(main())