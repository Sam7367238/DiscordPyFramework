import discord

async def checkApp(interaction: discord.Interaction):
    member = interaction.namespace.member if hasattr(interaction.namespace, 'member') else None
    
    if member.bot:
        await interaction.response.send_message("❌ Cannot perform operation on applications/programs/bots.", ephemeral=True)
        return False
    else:
        return True