import traceback
from contextlib import redirect_stdout
import discord
from discord.ext import commands
from io import StringIO
from .i18n import embed

@commands.command('eval', description='eval-desc')
@commands.is_owner()
async def eval_(ctx, *, arg):
    env = {
        'ctx': ctx,
        'commands': commands,
        'discord': discord,
    }
    out = StringIO()
    arg = arg.strip('`').rstrip().lstrip('\n').splitlines()
    indent = '    '
    for line in arg:
        strp = line.lstrip()
        if strp != line:
            indent = line[:len(line) - len(strp)]
            break
    arg = ''.join(indent + line + '\n' for line in arg)
    try:
        with redirect_stdout(out):
            exec(f"async def func():\n{arg}", env)
            ret = await env['func']()
    except BaseException:
        trace = traceback.format_exc().replace(r'C:\Users\kenlh\Desktop\git\Kenny2github\\'[:-1], '')
        await ctx.send(f'```\n{out.getvalue()}```', embed=embed(ctx,
            title=('error',),
            description=f'```{trace}```',
            color=0xff0000
        ))
    else:
        await ctx.send(f'```\n{out.getvalue()}```', embed=embed(ctx,
            title=('success',),
            description=f'```{ret!r}```',
            color=0x55acee
        ))
