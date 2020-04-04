from discord.ext import commands
import pygsheets
import sqlite3
from random import seed
from datetime import datetime
from re import search, split
import db_interact as dbi


def add_char(wks, sheet_id, user_id, guild_id):
    next_id = dbi.get_next_id('chars')
    species_id = dbi.get_id('species', 'name', wks.cell('C4').value_unformatted)
    name = wks.cell('C2').value_unformatted
    insert = False

    if species_id is not None:
        char = (next_id, sheet_id, user_id, guild_id,
                wks.cell('L19').value_unformatted,
                name,
                wks.cell('C3').value_unformatted,
                species_id,
                wks.cell('C5').value_unformatted,
                '',
                '',
                '',
                wks.cell('D21').value_unformatted,
                wks.cell('F21').value_unformatted,
                '',
                wks.cell('H21').value_unformatted,
                wks.cell('J21').value_unformatted,
                '',
                '',
                '',
                '')
        insert = dbi.table_insert('chars', char)

    if insert:
        skills = wks.range('E2:J19', returnas='range')

        for x in range(0, 4, 2):
            for y in range(0, 17):
                if skills[y][x].value_unformatted != '' and skills[y][x+1].value_unformatted != '':
                    skill_id = dbi.get_id('skills', 'name', skills[y][x].value_unformatted.lower())
                    if skill_id is not None:
                        dbi.table_insert('char_skills', (next_id, skill_id, skills[y][x+1].value_unformatted))

        # Set active_char
        dbi.set_active_char(next_id, user_id, guild_id)

    return True, name, next_id


class CharSheets(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        seed(datetime.now())
        self.gs = pygsheets.authorize()

        try:
            self.conn = sqlite3.connect('swrpg.db')
        except sqlite3.Error as e:
            print(e)

        self.cur = self.conn.cursor()

    def char_exists(self, user_id, guild_id, sheet_id):
        self.cur.execute('SELECT id '
                         'FROM chars '
                         'WHERE user_id=? AND guild_id=? AND sheet_id=?;',
                         (user_id, guild_id, sheet_id))

        row = self.cur.fetchone()

        if row is None:
            return False
        else:
            return True

    @commands.command()
    async def gsheet(self, ctx, sheet_id):
        # Open the GSheet by ID. Translate url to ID if needed.
        if search(r'^https://docs.google.com/spreadsheets/d/.*/.*$', sheet_id):
            url_parts = split('/', sheet_id)
            sheet_id = url_parts[5]

        sheet = self.gs.open_by_key(sheet_id)

        # Character profile is on the first worksheet.
        wks = sheet[0]

        # Other useful variables
        user_id = ctx.message.author.id
        guild_id = ctx.message.guild.id
        channel = ctx.channel

        # Check if character already exists.
        if self.char_exists(user_id, guild_id, sheet_id):
            await channel.send(f'<@{user_id}> this character already exists. Please use '
                               f'`!update <character_name>` to update it.')
        else:
            msg = await channel.send('Adding character...')
            result = add_char(wks, sheet_id, user_id, guild_id)
            if result[0]:
                await ctx.message.delete()
                await msg.edit(content='Character added.', delete_after=30.00)
            else:
                await msg.edit(content='Failed. Please check your sheet and try again.')


def setup(bot):
    bot.add_cog(CharSheets(bot))
