import discord
import os
import dotenv
from core import bot
from suggestions.command import suggestion
from suggestions.event import on_interaction
from config.configChannel import *

dotenv.load_dotenv(dotenv_path='.env')
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("=" * 40)
    print("Online!")
    print("=" * 40)
    commands = await bot.tree.sync()
    print (f"comandos sincronizados {str(len(commands))}")
    
@bot.command()
async def init(ctx):
    await bot.tree.sync()
    await ctx.reply("Done!")


@bot.tree.command(name="pineado", description="Llama a una persona por su tag")
async def pineado(interaction: discord.Interaction, nombre: discord.Member):
    await interaction.response.send_message(nombre.mention)

bot.run(TOKEN)
