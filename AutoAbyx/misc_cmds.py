from discord.ext.commands import command, Cog, Context, Bot
from .i18n import Msg

class Miscellaneous(Cog):
    """misc/cog-desc"""

    @command(description='misc/hello-desc')
    async def hello(self, ctx: Context):
        await ctx.send(Msg(ctx, 'hello'))

    @command(description='misc/hmmst-desc')
    async def hmmst(self, ctx: Context):
        await ctx.send(Msg(ctx, 'hmmst'))

def setup(bot: Bot):
    bot.add_cog(Miscellaneous())