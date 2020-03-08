import discord
from discord.ext import commands


class Manage(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged on as {self.bot.user}')
        await self.bot.change_presence(activity=discord.Game(name='Star Wars D6'))

    @commands.command()
    async def shutdown(self, ctx):
        if ctx.message.author.id == 470937192789966850:
            try:
                await self.bot.logout()
            except:
                print("EnvironmentError")
                self.bot.clear()
        else:
            await ctx.send("You're not my real dad!")


def setup(bot):
    bot.add_cog(Manage(bot))
