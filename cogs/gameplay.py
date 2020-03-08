from discord.ext import commands
from random import seed, randint
from datetime import datetime
from re import search, split


class Gameplay(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        seed(datetime.now())

    @commands.command(aliases=['r'])
    async def roll(self, ctx, dnm):
        num_dice = mod = total = 0
        wild = 6
        roll_str = mod_str = wild_str = ''

        if search('^\d*\+\d*$', dnm):
            parts = split('\+', dnm)
            if len(parts) == 2:
                num_dice = int(parts[0])
                mod = int(parts[1])
        else:
            num_dice = int(dnm)

        for i in range(num_dice - 1):
            temp = randint(1, 6)
            total += temp
            if temp == 6:
                roll_str += f'**{temp}**'
            else:
                roll_str += f'{temp}'

            if i < num_dice - 2:
                roll_str += ', '

            if mod > 0:
                mod_str = f' + {mod}'
                total += mod

        while wild == 6:
            wild = randint(1, 6)
            total += wild
            if wild == 6:
                wild_str += f'**{wild}**, '
            else:
                wild_str += f'{wild}'

        await ctx.send(f'<@{ctx.author.id}> {num_dice}🎲{mod_str}\n **Dice:** ({roll_str})\n **Wild'
                       f' Die:** ({wild_str})\n **Total:** {total}')
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Gameplay(bot))
