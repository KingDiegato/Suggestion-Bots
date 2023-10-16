import discord
from core import bot
from discord import Interaction

@bot.event
async def on_interaction(interaction: Interaction):
    try:
        if interaction.command.name != "suggestion":
            return
        print(interaction.command.name)
        print(interaction.user.display_name)
        print(interaction.data)
    except:
        pass
    