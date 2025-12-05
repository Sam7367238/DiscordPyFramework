import discord
from discord.ext import commands
from discord import app_commands
import aiosqlite
import Utilities.DeprecatedDatabase as Database

class EditStat(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="edit-stat", description="Edit a user's stat value, such as money.")
    async def edit_column(self, interaction:discord.Interaction, user: discord.User, stat: str, new_value: str) -> None:
        if user.bot:
            await interaction.response.send_message("❌ Cannot perform operation on applications/programs/bots.", ephemeral=True)
        
        interrogation = await self.bot.application_info()
        
        if not interaction.user.id == interrogation.team.owner.id:
            await interaction.response.send_message("❌ Only the application owner can use this command.", ephemeral=True)
            return
        
        async with aiosqlite.connect('AppDatabase.db') as db:
            async with db.cursor() as cursor:
                await cursor.execute(f'''UPDATE Statistics SET {stat} = ? WHERE User_ID = ?''', (new_value, user.id))
            
            await db.commit()
            
        await interaction.response.send_message("✅ Edited.", ephemeral=True)
        
    @edit_column.autocomplete("stat")
    async def column_autocomplete(self, interaction: discord.Interaction, current: str):
        try:
            columns = await Database.get_columns("Statistics")
            filtered_columns = [col for col in columns if col != 'User_ID']
            return [discord.app_commands.Choice(name=col, value=col) for col in filtered_columns if current.lower() in col.lower()]
        except Exception as e:
            return [discord.app_commands.Choice(name="Error", value=e)]

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(EditStat(bot))