from discord.ext import commands
from random import seed, choice
from datetime import datetime


class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        seed(datetime.now())

    @commands.Cog.listener()
    async def on_message(self, message):
        # print(message.content)
        if message.author == self.bot.user:
            return

        if self.bot.user.mentioned_in(message) and message.mention_everyone is False:
            if ':pray:' in message.content.lower() or '\u1F64F' in message.content or '🙏' in message.content:
                responses = [f"Prayers won't help you here, <@{message.author.id}>",
                             f"Praying? Really? A person of your talents, <@{message.author.id}>?",
                             f"I find your lack of faith disturbing, <@{message.author.id}>."]
                await message.channel.send(choice(responses))


def setup(bot):
    bot.add_cog(Misc(bot))
