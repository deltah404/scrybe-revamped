import discord
from fetch import get_config
from discord.ext import commands

guilds = get_config("guilds")

class Basic:
    def __init__(self, bot):
        self.bot = bot

    @bot.slash_command(guild_ids = guilds)
    async def ping(self, ctx: commands.Context):
        await ctx.respond('Pong')

bot.add_cog(Basic(bot))