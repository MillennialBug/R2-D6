from discord.ext import commands
from random import seed, choice
from datetime import datetime


class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        seed(datetime.now())

    @client.event()
    async def on_member_join(self, member):
        print(f'{member} has joined the server.')
        user_name = member.name
        welcome_msg = [f"Help me, {user_name}. You're my only hope.",
                       f"{user_name}, the force will be with you. Always.",
                       f"Why, you stuck-up, half-witted, scruffy-looking {user_name}.",
                       f"\"I'm a simple person, trying to make my way in the universe\" - {user_name}.",
                       f"What if I told you the Republic was under the control of {user_name}.",
                       f"You were my brother, {user_name}. I loved you.",
                       f"{user_name}, we're home.",
                       f"{user_name}, I'll be there for you. @MillennialBug said I had to.",
                       f"Love won't save you, {user_name}. Only my new powers can do that.",
                       f"...Don't try it, {user_name}. I have the high ground!",
                       f"{user_name}? My goodness, you've grown",
                       f"Henceforth, you shall be known as Darth... {user_name}.",
                       f"I've got a bad feeling about this.",
                       f"Hello there.",
                       f"There force is strong with this one.",
                       f"Great, {user_name}. Don't get cocky!",
                       f"Hello. I don't believe we have been introduced, {user_name}? "
                       f"A pleasure to meet you. I am R2-D6, Human-Discord Relations.",
                       f"{user_name}. Now that's a name I've not heard in a long time. A long time.",
                       f"{user_name}, I don't want to lose you to the Emperor the same way I lost Vader.",
                       f"{user_name}, you're breaking my heart! And you're going down a path I cannot follow.",
                       f"{user_name}, let me give you some advice. Assume everyone will betray you and you will never "
                       f"be disappointed.",
                       f"I suggest a new strategy, {user_name}. Let the Wookiee win.",
                       f"{user_name}, we stand here amongst my achievements, not yours!",
                       f"Great shot {user_name}, that was one in a million.",
                       f"{user_name}'s not a system, they're a person!",
                       f"{user_name}, you're shorter than I expected.",
                       f"Be careful not to choke on your aspirations, {user_name}.",
                       f"Hmmm. Lost a planet, Master {user_name} has. How embarrassing."]
        channel = self.bot.get_channel(835883702562062396)
        await channel.send(f"{user_name} joined.\n{choice(welcome_msg)}")


def setup(bot):
    bot.add_cog(Welcome(bot))
