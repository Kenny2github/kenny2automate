from functools import wraps
import asyncio
import discord
from discord.ext import commands
from .emoji import SEE_DM
from .utils import DummyCtx, background
from .i18n import i18n, embed

def needs_dms(react=True):
    def wrapper(func):
        @wraps(func)
        async def replacement(*args, **kwargs):
            for arg in args + tuple(kwargs.values()):
                if isinstance(arg, (commands.Context, DummyCtx)):
                    ctx = arg
                    break
            else:
                return await func(*args, **kwargs)
            try:
                msg = await ctx.author.send(i18n(ctx.author, 'checking-dms'))
            except discord.Forbidden as exc:
                if exc.code == 50007: # "can't dm this user"
                    background(ctx.send(embed=embed(ctx,
                        title=('error',),
                        description=('cant-dm', ctx.author.mention),
                        color=0xff0000
                    )))
                raise
            async def waitanddel():
                await asyncio.sleep(5)
                await msg.delete()
            background(waitanddel())
            if react and hasattr(ctx, 'message'):
                background(ctx.message.add_reaction(SEE_DM))
            return await func(*args, **kwargs)
        return replacement
    return wrapper

async def check_dms_open(ctx):
	@needs_dms(react=False)
	async def dummy(context):
		return True
	try:
		return await dummy(ctx)
	except discord.Forbidden as exc:
		if exc.code == 50007:
			return False
		raise
