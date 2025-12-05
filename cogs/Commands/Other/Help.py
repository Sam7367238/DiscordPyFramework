import discord
from discord.ext import commands
from discord import app_commands
from Includes import AppTutorial, Functions

class GuideView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=120)

    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True
        await self.Message.edit(view=self)

    async def on_timeout(self) -> None:
        await self.disable_all_items()

    @discord.ui.button(
        label="Application Guide/Tutorial",
        style=discord.ButtonStyle.green,
        custom_id="learning",
        emoji="📚"
    )
    async def guideCallback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="📘 Guide/Tutorial", description=AppTutorial.guide, color=Functions.mainCommandColors)
        await interaction.response.send_message(embed=embed, ephemeral=True)

class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="help", description="Receive help on proper usage of the application and information about, along with notes.")
    async def help(self, interaction: discord.Interaction):
        prefix_commands = [command for command in self.bot.commands]

        if len(prefix_commands) == 0:
            prefixCmdList = "❌ There are no prefix commands."
        else:
            prefixCmdList = "\n".join([f"{cmd.name} - {cmd.help}" for cmd in prefix_commands])

        appinfo = await self.bot.application_info()
        embed = discord.Embed(title="📕 General Information About The App",
                              description=f"👤 **App Name:** {self.bot.user.name}\n📑 **App Description:** {appinfo.description}\n🔢 **Guild Count:** {len(self.bot.guilds)}\n👑 **Owner:** {appinfo.owner.mention}\n📒 **Note(s):** To see all app commands, check your application menu.\n💾 **__Database__**: Use the register command to register to the database to be able to use certain commands.",
                          color=Functions.mainCommandColors)
        if self.bot.user.avatar is not None:
            embed.set_thumbnail(url=self.bot.user.avatar.url)

        embed.add_field(name=f"🔑 Prefix Commands ({len(prefix_commands)})",
                        value=f"__Prefix Is '{self.bot.command_prefix}'__\n{prefixCmdList}")
        view = GuideView()
        await interaction.response.send_message(embed=embed, view=view)
        view.Message = await interaction.original_response()

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Help(bot))