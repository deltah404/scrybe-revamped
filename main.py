import os
import discord

token = os.environ['TOKEN']
client = discord.Client()

client.run(token)