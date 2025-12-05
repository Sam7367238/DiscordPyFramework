import discord
from discord.ext import commands
from discord import app_commands
import Includes.Functions as Other

class Restart(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="restart", description="Restarts the bot completely, in case of a crash.")
    async def restart(self, interaction: discord.Interaction):
        botInfo = await self.bot.application_info()

        if not interaction.user.id == botInfo.owner.id:
            await interaction.response.send_message("❌ Only the app creator can use this command.", ephemeral=True)
            return
        
        await interaction.response.send_message("⏱️ The bot has restarted ✅")

        Other.restartbot()

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Restart(bot))