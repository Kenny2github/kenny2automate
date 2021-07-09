import discord
from discord.ext import commands
from .config import PREFIX
from .help import AbyxHelp
from .i18n import Embed, Msg
from .logger import getLogger
from .prefix import Prefix

SIGNALLED_EXCS = (
    commands.BotMissingPermissions,
    commands.MissingPermissions,
    commands.MissingRequiredArgument,
    commands.BadArgument,
    commands.CommandOnCooldown,
)
UNLOGGED_EXCS = (
    commands.CheckFailure,
    commands.CommandNotFound,
    commands.TooManyArguments
)

logger = getLogger('client')

client = commands.Bot(
    description="description",
    command_prefix=Prefix.get_command_prefix,
    help_command=AbyxHelp(),
    intents=discord.Intents.all()
)

@client.event
async def on_command_error(ctx: commands.Context, exc: Exception):
    logger.error('Ignoring exception in command %s - %s: %s',
                 ctx.command, type(exc).__name__, exc)
    if hasattr(ctx.command, 'on_error'):
        return
    if ctx.cog:
        meth = commands.Cog._get_overridden_method(ctx.cog.cog_command_error)
        if meth is not None:
            return
        del meth
    if isinstance(exc, SIGNALLED_EXCS):
        await ctx.send(embed=Embed(
            ctx, Msg('error'), str(exc), color=0xff0000))
        return
    if isinstance(exc, UNLOGGED_EXCS):
        return
    logger.error('', exc_info=exc)

@client.before_invoke
async def before_invoke(ctx: commands.Context):
    logger.info('User %s\t(%18d) in channel %s\t(%18d) running %s%s',
                ctx.author, ctx.author.id, ctx.channel,
                ctx.channel.id, ctx.prefix, ctx.command)

@client.event
async def on_ready():
    logger.info('Ready!')