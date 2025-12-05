import time

import discord
from discord import app_commands
from discord.ext import commands
import traceback
from Includes import Functions

class CommandError(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def cog_load(self):
        tree = self.bot.tree
        tree.on_error = self.tree_on_error

    async def tree_on_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        print(error)
        traceback.print_exc()

        if isinstance(error, app_commands.CommandOnCooldown):
            ETA = int(time.time() + round(error.retry_after))
            embed = discord.Embed(description=f"⏱ This command is on cooldown, you can use it again <t:{ETA}:R>.", color=Functions.mainCommandColors)
            await interaction.response.send_message(embed=embed, ephemeral=True)
        if isinstance(error, app_commands.MissingRole):
            embed = discord.Embed(description=f"❌ <@&{error.missing_role}> is required to operate this command.", color=Functions.mainCommandColors)
            await interaction.response.send_message(embed=embed, ephemeral=True)
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message(f"❌ {error}", ephemeral=True)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CommandError(bot))