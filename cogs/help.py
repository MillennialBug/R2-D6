from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.send('Help coming soon.')


def setup(bot):
    bot.add_cog(Help(bot))
