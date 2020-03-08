from discord.ext import commands
from auth import discord_token
from os import listdir

bot = commands.Bot(command_prefix='!')


@bot.command()
async def load(ctx, ext):
    bot.load_extension(f'cogs.{ext}')


@bot.command()
async def unload(ctx, ext):
    bot.unload_extension(f'cogs.{ext}')


@bot.command()
async def reload(ctx, ext):
    bot.unload_extension(f'cogs.{ext}')
    bot.load_extension(f'cogs.{ext}')


for filename in listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! Latency is {round(bot.latency * 1000)}ms.')


bot.run(discord_token)
