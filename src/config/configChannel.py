import discord
from core import bot

@bot.tree.command(name="config", description="Configura el canal de sugerencias")
@discord.app_commands.guild_only()
async def config(interaction: discord.Interaction, channel: discord.TextChannel):
    roles = interaction.user.roles
    avaliable: bool
    for role in roles:
        if role.permissions.administrator:
            avaliable = True
            break
        else: avaliable = False
    if avaliable:
        await interaction.response.send_message(content=f"Configurado el bot en el canal {channel.mention}", ephemeral=True)
    else: 
        await interaction.response.send_message(content=f"Usted no tiene permisos para configurar el bot", ephemeral=True)
