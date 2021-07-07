from discord.ext.commands import command, Cog, Context, Bot

class Miscellaneous(Cog):
    """misc/cog-desc"""

    @command(description='misc/hello-desc')
    async def hello(self, ctx: Context):
        await ctx.send('Hello World!')

    @command(description='misc/hmmst-desc')
    async def hmmst(self, ctx: Context):
        await ctx.send('hmmst')

def setup(bot: Bot):
    bot.add_cog(Miscellaneous())