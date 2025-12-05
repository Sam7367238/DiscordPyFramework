import discord
from discord.ext import commands
from discord import app_commands
import datetime
# from Middleware.TestIntercept import testIntercept

class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Receive app latency.")
    # @app_commands.check(testIntercept)
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)

        if latency < 250:
            color = discord.Color.blue()
        elif latency < 450 and latency > 250:
            color = discord.Color.green()
        elif latency < 600 and latency > 450:
            color = discord.Color.orange()
        elif latency < 800 and latency > 600:
            color = discord.Color.red()
        else:
            color = discord.Color.dark_red()

        embed = discord.Embed(title=f":ping_pong: Pong!", color=color, timestamp=datetime.datetime.now())
        embed.add_field(name="Websocket", value=f"```json\n{latency} ms```", inline=False)
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Ping(bot))