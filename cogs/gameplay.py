from discord.ext import commands
from random import seed, randint, choice
from datetime import datetime
from re import search, split, sub, IGNORECASE
import sqlite3
from discord import Embed, Webhook, RequestsWebhookAdapter
from colours import colours
from cogs.charsheets import add_char
import pygsheets
from asyncio import TimeoutError


def check_for_role(roles, role_id):
    for role in roles:
        if role_id == role.id:
            return True

    return False


def roll_dice(num_dice, total=0):
    roll_str = ''
    rolls = []
    for i in range(num_dice - 1):
        temp = randint(1, 6)
        rolls.append(temp)
        total += temp
        if temp == 6:
            roll_str += f'**{temp}**'
        else:
            roll_str += f'{temp}'

        if i < num_dice - 2:
            roll_str += ', '

    return roll_str, total, rolls


def roll_wild(total):
    # Roll the Wild Die at least once.
    # When the die lands on 6 a re-roll is permitted and the total accumulates.
    # If the die lands on 1 there is a chance for a negative consequence for the player.
    wild = 6
    wild_str = ''
    rolls = []
    while wild == 6:
        wild = randint(1, 6)
        rolls.append(wild)
        total += wild
        if wild == 6:
            wild_str += f'**{wild}**, '
        else:
            wild_str += f'{wild}'

    return wild_str, total, rolls


def get_roll_params(dice_code):
    num_dice = mod = 0
    # Remove D if included in roll parameter
    dice_code = sub(r'D', '', dice_code, flags=IGNORECASE)

    # Decode the input. Expects either an integer or 2 integers separated by a +
    # Also required integer after + to be either 1 or 2 only.
    if search(r'^\d*\+[1-2]$', dice_code):
        parts = split(r'\+', dice_code)
        if len(parts) == 2:
            num_dice = int(parts[0])
            mod = int(parts[1])
    # Single integer input is also accepted i.e Just dice rolls with no modifier.
    elif search(r'^\d*$', dice_code):
        num_dice = dice_code
    # else:
    #     provide help

    return int(num_dice), mod


def chk_mod(mod, total):
    if mod > 0:
        mod_str = f'+ {mod}'
        total += mod
    else:
        mod_str = ''

    return mod_str, total


def do_roll(dice_code):
    success = False
    roll_str = mod_str = wild_str = ''
    rolls = wild_rolls = []
    total = 0

    num_dice, mod = get_roll_params(dice_code)

    if int(num_dice) > 0:
        roll_str, total, rolls = roll_dice(num_dice)
        mod_str, total = chk_mod(mod, total)
        wild_str, total, wild_rolls = roll_wild(total)
        success = True

    return [num_dice, roll_str, mod_str, wild_str,
            rolls, wild_rolls, total, success]


async def send_roll(ctx, roll_res, gm=False):
    if roll_res[0] > 1:
        dice_str = f'**Dice:** ({roll_res[1]})\n'
    else:
        dice_str = ''

    # Create and send the response message.
    message = f'<@{ctx.author.id}> {roll_res[0]} 🎲 {roll_res[2]}\n' \
              f'{dice_str}' \
              f'**Wild Die:** ({roll_res[3]})\n' \
              f'**Total:** {roll_res[6]}'

    if not gm:
        await ctx.send(message)
    else:
        gm_message = f'GM Roll 🎲\n**Total:** {roll_res[6]}'
        if roll_res[5][0] == 1:
            gm_message += '\n**Wild Die Failure!**'
        await ctx.author.send(message)
        await ctx.send(gm_message)


class Gameplay(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        seed(datetime.now())
        self.gs = pygsheets.authorize(service_account_file='service-account-credentials.json')

        try:
            self.conn = sqlite3.connect('swrpg.db')
            self.cur = self.conn.cursor()
        except sqlite3.Error as e:
            print(e)

        self.webhooks = {687306755813670945: Webhook.partial(692337923462529025,
                                                             "0tc-ONxBoRp5XYYf1kW2QQd1WOeNgfy56_"
                                                             "9csaMTXSHDGmgu6JsWDQBxdclfift6xUa-",
                                                             adapter=RequestsWebhookAdapter()),
                         685777376549928962: Webhook.partial(692351160572444683,
                                                             "jb2uuDdfktJ6uXetfo3KHzWL2C5XhTpOic"
                                                             "DFieoCPL0D1-jUNxSjv5YgfsExQvegayE6",
                                                             adapter=RequestsWebhookAdapter())}

    def get_npc(self, name, system):
        if system == 'SWD6':
            self.cur.execute('SELECT char_id, avatar FROM npcs WHERE name=?', (name,))
        elif system == 'DND':
            self.cur.execute('SELECT 0, avatar, fullname FROM dnd_npcs WHERE name=?', (name,))
        return self.cur.fetchone()

    async def get_db_skill(self, ctx, skill):
        self.cur.execute('SELECT id, name, attribute_id '
                         'FROM skills '
                         'WHERE LOWER(name) LIKE ?', ('%' + skill.lower() + '%',))
        skills = self.cur.fetchall()

        if len(skills) > 1:
            skill_pick = 'Which one were you looking for? (Type the number or "c" to cancel)\n'
            skill_num = 0
            for db_skill in skills:
                skill_num += 1
                skill_pick += f'**[{skill_num}]** - {db_skill[1]}\n'

            skill_list = Embed(title='Multiple matches found.\n',
                               description=skill_pick,
                               colour=choice(colours))
            skill_msg = await ctx.send(embed=skill_list)

            def check(m):
                if m.content == 'c':
                    return m
                elif len(m.content) == 1 and not m.content.isalpha():
                    if int(m.content) <= skill_num:
                        return m

            try:
                reply = await self.bot.wait_for('message', check=check, timeout=20.0)
            except TimeoutError:
                await skill_msg.delete()
                await ctx.send('Selection timed out or was cancelled.')
                return

            if reply.content == 'c':
                await skill_msg.delete()
                await ctx.send('Selection timed out or was cancelled.')
                return
            else:
                await skill_msg.delete()
                return skills[int(reply.content) - 1]
        elif len(skills) == 1:
            return skills[0]
        else:
            return None

    def get_char_skill(self, member, guild, skill):
        self.cur.execute(f'SELECT char_skills.dice_code, chars.name, '
                         f'chars.portrait_url FROM char_skills '
                         f'INNER JOIN active_chars ON active_chars.char_id = char_skills.char_id '
                         f'INNER JOIN chars ON chars.id = active_chars.char_id '
                         f'WHERE char_skills.skill_id=? '
                         f'AND active_chars.guild_id=? AND active_chars.user_id=?',
                         (skill[0], guild, member))

        row = self.cur.fetchone()

        if row is None:
            return self.get_char_skill(member, guild, (skill[2],))
        else:
            return row

    @commands.command(aliases=['r'])
    async def roll(self, ctx, dnm):
        roll_res = do_roll(dnm)

        if not roll_res[7]:
            return

        await send_roll(ctx, roll_res)

        # Delete the request message to keep chat clean.
        await ctx.message.delete()

    @commands.command(aliases=['att', 'attr'])
    async def attribute(self, ctx, attr):

        self.cur.execute('SELECT name, descr FROM skills WHERE (name=? OR short_name=?) '
                         'AND type = "attr"', (attr.lower(), attr.lower()))
        row = self.cur.fetchone()

        if row is not None:
            attribute = Embed(title=row[0].capitalize(),
                              colour=choice(colours),
                              description=row[1])
            await ctx.send(embed=attribute)
        # else:
        #     get attribute help

        await ctx.message.delete()

    @commands.command(aliases=['c'])
    async def check(self, ctx, skill):

        if len(skill) < 3:
            await ctx.send(content='Input must be at least 3 characters.\n'
                                   f'**Input:** {skill}', delete_after=20.0)
            await ctx.message.delete()
            return

        db_skill = await self.get_db_skill(ctx, skill)

        if db_skill is None:
            await ctx.send(content='No skill found.\n'
                                   f'**Input:** {skill}', delete_after=20.0)
            await ctx.message.delete()
            return

        char_skill = self.get_char_skill(ctx.message.author.id, ctx.message.guild.id, db_skill)

        if char_skill is not None:
            roll_res = do_roll(char_skill[0])

            if not roll_res[7]:
                return

            if roll_res[0] > 1:
                dice_str = f'({roll_res[1]}) +'
            else:
                dice_str = ''

            attr_chk_msg = Embed(title=f'**{char_skill[1]} makes a {db_skill[1].capitalize()} check!**',
                                 colour=choice(colours),
                                 description=f'{char_skill[0]}\n'
                                             f'{dice_str} ({roll_res[3]}) {roll_res[2]} = '
                                             f'`{roll_res[6]}`')
            attr_chk_msg.set_thumbnail(url=char_skill[2])
            await ctx.send(embed=attr_chk_msg)
            await ctx.message.delete()

    @commands.command(aliases=['dm'])
    async def gm(self, ctx, *args):
        if not check_for_role(ctx.author.roles, 691606404615897098) or \
                not (check_for_role(ctx.author.roles, 836213625974816770)):
            await ctx.message.delete()
            await ctx.send(content='Sorry, you are not marked as a GM.', delete_after=5.00)
            return

        if args[0] in ('r', 'roll'):
            await ctx.message.delete()

            roll_res = do_roll(args[1])

            if not roll_res[7]:
                return

            await send_roll(ctx, roll_res, True)

        elif args[0] == 'npc':
            await ctx.message.delete()
            if args[1] == 'add':
                char = [False]
                if len(args) == 5:
                    sheet = self.gs.open_by_key(args[4])
                    wks = sheet[0]
                    char = add_char(wks, args[4], ctx.message.author.id, ctx.message.guild.id)
                if char[0]:
                    self.cur.execute(f'INSERT INTO npcs (name, avatar, char_id) VALUES ({args[2]}, {args[3]},'
                                     f'{char[2]})')
                    self.conn.commit()
                else:
                    self.cur.execute(f"INSERT INTO npcs (name, avatar) VALUES (?,?)", (args[2], args[3] + '.png'))
                    self.conn.commit()
                    await ctx.send(content=f'{args[2]} added.', delete_after=5.00)
            elif args[1] == 'del':
                npc = self.get_npc(args[2], 'SWD6')
                if npc is not None:
                    self.cur.execute(f'DELETE FROM npcs WHERE name=?', (args[2],))
                    self.cur.execute(f'DELETE FROM chars where id=?', (npc,))
                    self.cur.execute(f'DELETE FROM char_skills WHERE char_id=?', (npc,))
                    self.conn.commit()
                    await ctx.send(content=f'{args[2]} deleted.', delete_after=5.00)
                else:
                    await ctx.send(content='NPC not found.', delete_after=5.00)

    @commands.command()
    async def say(self, ctx, name, *, args):
        await ctx.message.delete()

        if not check_for_role(ctx.author.roles, 691606404615897098) or \
                not (check_for_role(ctx.author.roles, 836213625974816770)):
            await ctx.send(content='Sorry, you are not marked as a GM.', delete_after=5.00)
            return

        char = self.get_npc(name, 'DND')
        if char is not None:
            webhook = self.webhooks[ctx.message.channel.id]
            webhook.send(username=f'{char[2]}', content=args,
                         avatar_url=char[1])


def setup(bot):
    bot.add_cog(Gameplay(bot))
