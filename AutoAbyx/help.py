from typing import Iterable
import discord
from discord.errors import DiscordServerError
from discord.ext import commands
from .chars import ZWNJ
from .i18n import Msg, Embed

class AbyxHelp(commands.HelpCommand):
    context: commands.Context

    async def send_it(self, embed: discord.Embed):
        await self.context.send(embed=embed)

    def command_string(self, cmd: commands.Command) -> str:
        """Get the title of a command field."""
        ctx = self.context
        title = ctx.prefix + cmd.qualified_name
        title += ' ' + (Msg(ctx, cmd.usage) if cmd.usage else cmd.signature)
        return f'`{title.strip()}`'

    def command_desc(self, cmd: commands.Command) -> str:
        """Get the complete description of a command."""
        ctx = self.context
        desc = Msg(ctx, cmd.brief, ctx.prefix) if cmd.brief else ''
        if cmd.help:
            desc += '\n\n' + Msg(ctx, cmd.help, ctx.prefix)
        return desc or ZWNJ

    def command_fields(self, filtered: Iterable[commands.Command]) \
            -> Iterable[tuple[str, Msg, False]]:
        """List commands as Embed fields."""
        return ((
            self.command_string(cmd),
            Msg(cmd.brief, self.context.prefix)
            if cmd.brief else ZWNJ,
            False
        ) for cmd in filtered)

    async def send_bot_help(self, mapping):
        """The root ;help message."""
        ctx = self.context
        filtered: list[commands.Command] \
            = await self.filter_commands(ctx.bot.commands)
        categories: set[commands.Cog] = set()
        for cmd in filtered:
            if cmd.cog not in categories:
                categories.add(cmd.cog)
        embed = Embed(
            ctx,
            description=Msg(ctx.bot.description),
            color=discord.Color.blue(),
            fields=(
                *((
                    cog.qualified_name,
                    Msg(cog.description, ctx.prefix)
                    if cog.description else ZWNJ,
                    True
                ) for cog in categories if cog is not None),
                (ZWNJ, Msg('help-cmds'), False),
                *self.command_fields(
                    cmd for cmd in filtered if cmd.cog is None)
            ),
            footer=Msg('help-footer', ctx.prefix)
        )
        await self.send_it(embed)

    async def send_cog_help(self, cog: commands.Cog):
        ctx = self.context
        filtered: list[commands.Command] \
            = await self.filter_commands(cog.get_commands())
        embed = Embed(
            ctx,
            description=(Msg(cog.description, ctx.prefix)
                         if cog.description else None),
            color=discord.Color.blue(),
            fields=self.command_fields(filtered)
        )
        await self.send_it(embed)

    async def send_group_help(self, group: commands.Group):
        ctx = self.context
        filtered: list[commands.Command] \
            = await self.filter_commands(group.commands)
        embed = Embed(
            ctx,
            self.command_string(group),
            self.command_desc(group),
            color=discord.Color.blue(),
            fields=self.command_fields(filtered)
        )
        await self.send_it(embed)

    async def send_command_help(self, command: commands.Command):
        ctx = self.context
        embed = Embed(
            ctx,
            self.command_string(command),
            self.command_desc(command),
            color=discord.Color.blue()
        )
        await self.send_it(embed)