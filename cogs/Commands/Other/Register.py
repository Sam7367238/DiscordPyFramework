import discord
from discord.ext import commands
from discord import app_commands
import Includes.Functions as Other
import Internals.DeprecatedDatabase as Database
from Internals.RepositoryBootstrap import repository

class Register(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.userRepository = repository("UserRepository")

    @app_commands.command(name="register", description="Register to the database to use the application.")
    async def registering(self, interaction: discord.Interaction) -> None:
        if await self.userRepository.isRegistered(interaction.user.id):
            await interaction.response.send_message("❌ You have already registered to the database.", ephemeral=True)
            return
        
        await self.userRepository.create(interaction.user.id)
        embed = discord.Embed(description="> 💾 Successfully registered! Use the help command for a quick guide.", color=Other.mainCommandColors)
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Register(bot))