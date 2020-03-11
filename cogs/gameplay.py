from discord.ext import commands
from random import seed, randint
from datetime import datetime
from re import search, split
import sqlite3
from discord import Embed, Colour


class Gameplay(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        seed(datetime.now())

        try:
            self.conn = sqlite3.connect('swrpg.db')
            self.cur = self.conn.cursor()
        except sqlite3.Error as e:
            print(e)

    @commands.command(aliases=['r'])
    async def roll(self, ctx, dnm):
        num_dice = mod = total = 0
        wild = 6
        roll_str = mod_str = wild_str = ''

        # Decode the input. Expects either an integer or 2 integers separated by a +
        if search(r'^\d*\+\d*$', dnm):
            parts = split(r'\+', dnm)
            if len(parts) == 2:
                num_dice = int(parts[0])
                mod = int(parts[1])
        else:
            num_dice = int(dnm)

        # Roll regular dice. This is the total number of dice - 1.
        for i in range(num_dice - 1):
            temp = randint(1, 6)
            total += temp
            if temp == 6:
                roll_str += f'**{temp}**'
            else:
                roll_str += f'{temp}'

            if i < num_dice - 2:
                roll_str += ', '

        # Add the modifier to the total if there is one.
        if mod > 0:
            mod_str = f'+ {mod}'
            total += mod

        '''
            Roll the Wild Die at least once. 
            When the die lands on 6 a re-roll is permitted and the total accumulates.
            If the die lands on 1 there is a chance for a negative consequence for the player.
        '''
        while wild == 6:
            wild = randint(1, 6)
            total += wild
            if wild == 6:
                wild_str += f'**{wild}**, '
            else:
                wild_str += f'{wild}'

        # Create and send the response message.
        await ctx.send(f'<@{ctx.author.id}> {num_dice} 🎲 {mod_str}\n '
                       f'**Dice:** ({roll_str})\n '
                       f'**Wild Die:** ({wild_str})\n '
                       f'**Total:** {total}')

        # Delete the request message to keep chat clean.
        await ctx.message.delete()

    @commands.command(aliases=['att', 'attr'])
    async def attribute(self, ctx, attr):
        self.cur.execute('SELECT name, descr FROM attributes WHERE name=? OR short_name=?', (attr.lower(),
                                                                                             attr.lower()))
        row = self.cur.fetchone()

        attribute = Embed(title=row[0].capitalize(),
                          colour=Colour.dark_purple(),
                          description=row[1])

        await ctx.send(embed=attribute)
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Gameplay(bot))
