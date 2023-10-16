import discord
from core import bot
from discord import Interaction, Member

@bot.tree.command(name='suggestion', description='Suggest something')
@discord.app_commands.guild_only()
async def suggestion(interaction: Interaction , suggestion: str):
    member = interaction.user.display_name
    avatar = interaction.user.display_avatar
    embed = discord.Embed(title="Nueva Sugerencia!", 
                          description=f"{suggestion}", 
                          color=0xffff00,
                          timestamp=interaction.created_at,
    )
    embed.set_author(name=member, icon_url=avatar)
    embed.set_footer(text=f"Sugerido por: {member}")
    
    await interaction.response.send_message(embed=embed)
    message = await interaction.original_response()
    await message.add_reaction('👍')
    await message.add_reaction('👎')
    await message.create_thread(name=f"Nueva sugerencia de {member}", reason="Command Triggered")
    
    