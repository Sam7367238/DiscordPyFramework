import discord

async def testIntercept(interaction: discord.Interaction):
    await interaction.response.send_message("Usage of this command has been intercepted by middleware.", ephemeral=True)
    return False