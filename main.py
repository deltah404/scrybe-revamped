import os
import discord

token = os.environ['TOKEN']
client = discord.Client()

@client.event
async def on_ready():
    print(f'Booted as {client.user}')

client.run(token)