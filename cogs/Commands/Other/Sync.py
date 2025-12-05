import discord
from discord.ext import commands
from discord import app_commands
import time
from colorama import Back, Fore, Style

class Sync(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="sync", description="Sync all app commands.")
    @app_commands.checks.cooldown(1, 120, key=lambda i: (i.guild.id, i.user.id))
    async def sync(self, interaction: discord.Interaction):
        botInfo = await self.bot.application_info()

        if not interaction.user.id == botInfo.owner.id:
            await interaction.response.send_message("❌ Only the app creator can use this command.", ephemeral=True)
            return
        
        synced = await self.bot.tree.sync()
        prfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S UTC", time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
        print(prfx + " App CMDs Synced " + Fore.YELLOW + str(len(synced)) + " Commands")

        await interaction.response.send_message(f"{str(len(synced))} App CMDs synced.")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Sync(bot))