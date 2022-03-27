import os
import discord
from discord.ext import commands

token = os.environ['TOKEN']
client = commands.Bot()

# load extensions
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename}')

@client.event
async def on_ready():
    print(f'Booted as: {client.user}') # state when booted

client.run(token)