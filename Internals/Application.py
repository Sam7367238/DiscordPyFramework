import discord
import os
from discord.ext import commands
from colorama import Back, Fore, Style
import time
import platform

class Application(commands.Bot):
    def __init__(self, command_prefix, views, intents):
        super().__init__(command_prefix, intents=intents, help_command=None)
        self.views = views

    async def on_ready(self):
        prfx = (
                Back.BLACK +
                Fore.GREEN +
                time.strftime(
                    "%H:%M:%S UTC",
                    time.gmtime()
                ) +
                Back.RESET +
                Fore.WHITE +
                Style.BRIGHT
        )

        print(prfx + " Logged in as " + Fore.YELLOW + self.user.name)
        print(prfx + " Bot ID " + Fore.YELLOW + str(self.user.id))
        print(prfx + " Discord Version " + Fore.YELLOW + discord.__version__)
        print(prfx + " Python Version " + Fore.YELLOW + str(platform.python_version()))

        # for guild in bot.guilds:
        # print(f"- {guild.name} ({guild.id})")

    async def setup_hook(self) -> None:
        for view in self.views:
            self.add_view(view)

        for root, _, files in os.walk("./cogs"):
            for filename in files:
                if not filename.endswith(".py"): continue

                cog_path = os.path.join(root, filename)
                module = cog_path.replace("\\", "/").replace("/", ".")[2:].removesuffix(".py")
                try:
                    await self.load_extension(module)
                    print(f"Loaded extension: {module}")
                except Exception as e:
                    print(f"Failed to load extension {module}: {e}")