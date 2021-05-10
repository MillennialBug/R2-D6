from discord.ext import commands
from discord import Intents
from auth import discord_token
from os import listdir

intents = Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command('help')


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
    await ctx.message.delete()


for filename in listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! Latency is {round(bot.latency * 1000)}ms.')


bot.run(discord_token)
