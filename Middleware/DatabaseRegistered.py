import discord
from Internals.RepositoryBootstrap import repository

async def registered(interaction: discord.Interaction):
    user = interaction.user
    userRepository = repository("UserRepository")

    if await userRepository.isRegistered(user.id):
        return True
    else:
        await interaction.response.send_message("❌ You must be registered to the database to use this command.", ephemeral=True)
        return False