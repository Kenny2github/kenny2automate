import discord
from discord.ext import commands
from .config import PREFIX
from .logger import getLogger

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

async def get_command_prefix(
    bot: commands.Bot,
    msg: discord.Message
) -> tuple[str]:
    # get custom prefix
    return (PREFIX)

client = commands.Bot(
    description="description",
    command_prefix=get_command_prefix,
    # TODO: help command
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
        await ctx.send(exc) # i18n TODO
        return
    if isinstance(exc, UNLOGGED_EXCS):
        return
    logger.error('', exc_info=exc)

@client.before_invoke
async def before_invoke(ctx: commands.Context):
    logger.info('User %s\t(% 17d) in channel %s\t(% 17d) running %s%s',
                ctx.author, ctx.author.id, ctx.channel,
                ctx.channel.id, ctx.prefix, ctx.command)
