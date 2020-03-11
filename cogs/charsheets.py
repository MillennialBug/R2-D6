from discord.ext import commands
import pygsheets
from discord import Embed, Colour
import sqlite3


class CharSheets(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        try:
            self.conn = sqlite3.connect('swrpg.db')
        except sqlite3.Error as e:
            print(e)

        self.cur = self.conn.cursor()

    # def add_char(self, ):
    # Add character details to the db
    
    # def char_exists(self, ):
    # Check the database to see if this character exists for this user/guild combo
    
    # def del_char(self, ):
    # Delete character from database

    @commands.command()
    async def gsheet(self, ctx, sheet_id):
        gc = pygsheets.authorize()
        sheet = gc.open_by_key(sheet_id)
        wks = sheet[0]

        profile = Embed(title=wks[2][3],
                        colour=Colour.dark_purple(),
                        description=f'{wks[5][3]} {wks[4][3]} {wks[3][3]}')

        profile.set_thumbnail(url=f'{wks[19][12]}')
        profile.set_footer(text='Character added.')

        await ctx.send(embed=profile)


def setup(bot):
    bot.add_cog(CharSheets(bot))
