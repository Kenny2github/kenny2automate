from typing import Iterable, Literal, Union
from discord.ext import commands
from .db import db

class Disabling:

    cache: dict[int, dict[
        Union[Literal['cmd'], Literal['cog']], set[str]]] = {}

    @classmethod
    async def check_enabled(cls, ctx: commands.Context) -> bool:
        """Check if the command being run is disabled. Return False if so."""
        if ctx.guild is None:
            return True # no disabled commands in DMs
        if cls.cache.get(ctx.guild.id, None) is None:
            return True # this guild has disabled no commands
        if (ctx.command.cog_name or 'None') in cls.cache[ctx.guild.id]['cog']:
            return False # disabled by cog
        parent: commands.Command = ctx.command
        while parent:
            if parent.qualified_name in cls.cache[ctx.guild.id]['cmd']:
                return False # disabled specifically or by parent
            parent = parent.parent
        return True

    @classmethod
    async def load_disabled(cls, guild_id: int = None):
        """Load disabled commands, either globally or for a specific guild."""
        cls.cache.update(await db.disabled_commands(guild_id))

    @classmethod
    async def update_guild(
        cls, guild_id: int,
        cmds: Iterable[str],
        cogs: Iterable[str]
    ):
        """Update or set guild disabled commands and cogs."""
        await db.set_disabled_commands(guild_id, cmds)
        await db.set_disabled_cogs(guild_id, cogs)
        await cls.load_disabled(guild_id)

def setup(bot: commands.Bot):
    bot.loop.run_until_complete(Disabling.load_disabled())
    bot.add_check(Disabling.check_enabled)