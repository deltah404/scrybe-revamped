import discord
from fetch import get_config
from discord.ext import commands
from discord.commands import slash_command

guilds = get_config("guilds")

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids = guilds)
    async def ping(self, ctx: commands.Context):
        await self.ctx.respond('Pong')

def setup(bot):
    bot.add_cog(Basic(bot))