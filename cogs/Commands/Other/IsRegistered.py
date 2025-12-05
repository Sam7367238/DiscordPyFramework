import discord
from discord.ext import commands
from discord import app_commands
from Internals.RepositoryBootstrap import repository
from Repository.UserRepository import UserRepository


class IsRegistered(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.userRepository = repository("UserRepository")

    @app_commands.command(name="is-registered", description="See if a user is registered to the app database or not.")
    async def registered(self, interaction: discord.Interaction, user: discord.User = None) -> None:
        if user is None:
            user = interaction.user
        elif user != None:
            if user.bot:
                await interaction.response.send_message("❌ Cannot perform operation on applications/programs/bots.", ephemeral=True)
                return
        
        result = await self.userRepository.isRegistered(user.id)
        await interaction.response.send_message(f"📝 {result}. A user will have to manually register to the database to use the app.", ephemeral=True)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(IsRegistered(bot))