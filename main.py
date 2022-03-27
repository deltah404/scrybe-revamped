import os
import discord
from discord.ext import commands

token = os.environ['TOKEN']
bot = discord.Bot()

# load extensions
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print(f'Booted as: {client.user}') # state when booted

bot.run(token)