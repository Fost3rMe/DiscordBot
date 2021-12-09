import discord
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix=settings['prefix'])


@bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send('{}, hi'.format(author.mention))


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says hello when someone joined the chat"""
    await ctx.send('{} вкатился в чат'.format(member))

bot.run(settings['token'])
