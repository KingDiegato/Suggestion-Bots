from discord.ext import commands
from discord import Status, Activity, Intents, ActivityType

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents, status=Status.online,
                   activity=Activity(type=ActivityType.watching, name='Suggestions', details='Helping Everyone'))
