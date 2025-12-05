import discord

async def selfUsage(interaction: discord.Interaction):
    member = interaction.namespace.member if hasattr(interaction.namespace, 'member') else None

    if member.id == interaction.user.id:
        await interaction.response.send_message("❌ You cannot use this command on yourself.", ephemeral=True)
        return False
    else:
        return True