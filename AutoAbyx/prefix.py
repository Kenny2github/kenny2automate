import discord
from discord.ext import commands
from .chars import DONE
from .config import PREFIX
from .db import db
from .i18n import Embed, Msg
from .utils import lone_group

class Prefix(commands.Cog):
    """prefix/cog-desc"""

    cache: dict = {}

    @classmethod
    async def get_command_prefix(
        cls,
        bot: commands.Bot,
        msg: discord.Message
    ) -> tuple[str]:
        """Get the command prefix(es) for this message."""
        return (cls.cache.get(msg.author.id, None) or PREFIX, PREFIX)

    @classmethod
    async def load_prefixes(cls):
        """Load command prefixes into memory from DB."""
        cls.cache.update(await db.get_prefixes())

    @commands.group(brief='prefix/desc')
    @lone_group
    async def prefix(self, ctx):
        pass

    @prefix.command(brief='prefix/get-desc')
    async def get(self, ctx: commands.Context):
        await ctx.send(embed=Embed(
            ctx, description=Msg(
                'prefix/get',
                self.cache.get(ctx.author.id, None) or PREFIX),
            color=discord.Color.blue()
        ))

    @prefix.command(brief='prefix/set-desc')
    async def set(self, ctx: commands.Context, *, prefix: str):
        """prefix/set-help"""
        if prefix.startswith('"') and prefix.endswith('"'):
            prefix = prefix[1:-1]
            footer = Msg('prefix/set-footer')
        else:
            footer = None
        prefix = prefix.lstrip()
        self.cache[ctx.author.id] = prefix
        await db.set_prefix(ctx.author.id, prefix)
        await ctx.send(embed=Embed(
            ctx, description=Msg('prefix/set', prefix),
            color=discord.Color.blue(), footer=footer
        ))

    @prefix.command(brief='prefix/reset-desc')
    async def reset(self, ctx: commands.Context):
        self.cache.pop(ctx.author.id, None)
        await db.set_prefix(ctx.author.id, None)
        await ctx.message.add_reaction(DONE)

def setup(bot: commands.Bot):
    bot.loop.run_until_complete(Prefix.load_prefixes())
    bot.add_cog(Prefix())