import discord
from discord.ext import tasks, commands
from .config import PREFIX

class SetStatus:
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.task = tasks.loop(minutes=5.0)(self.set_status)
        self.task.before_loop(self.before)

    async def set_status(self):
        if self.task.current_loop & 1:
            message = f'{len(self.bot.users)} people'
        else:
            message = PREFIX + 'help'
        await self.bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching, name=message))

    async def before(self):
        await self.bot.wait_until_ready()

    def start(self):
        self.task.start()

    def cancel(self):
        self.task.cancel()

    __del__ = cancel