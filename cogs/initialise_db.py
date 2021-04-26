from discord.ext import commands
import sqlite3
from sql_stmts import table_creates, table_insert
import dict


class Initialise(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        try:
            self.conn = sqlite3.connect('swrpg.db')
        except sqlite3.Error as e:
            print(e)

        self.cur = self.conn.cursor()
        self.clear_db()  # TEST ONLY!!!
        self.create_tables()
        self.insert_data()

    def clear_db(self):
        tables = ('users', 'skills', 'species', 'chars', 'active_chars', 'char_skills', 'characters')
        for table in tables:
            self.cur.execute(f'DROP TABLE IF EXISTS {table};')
            self.conn.commit()

    def create_tables(self):
        for stmt in table_creates:
            self.cur.execute(stmt)
        self.conn.commit()

    def insert_data(self):
        for values in dict.skills.values():
            self.cur.execute(table_insert.format('skills', values))
        self.conn.commit()

        for values in dict.species.values():
            self.cur.execute(table_insert.format('species', values))
        self.conn.commit()


def setup(bot):
    bot.add_cog(Initialise(bot))
