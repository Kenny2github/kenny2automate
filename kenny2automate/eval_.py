import sys
import re
import traceback
from contextlib import redirect_stdout
import discord
from discord.ext import commands
from io import StringIO
from .i18n import embed

class Eval(commands.Cog):

    async def cog_check(self, ctx):
        return await ctx.bot.is_owner(ctx.author)

    @staticmethod
    def _init_env(ctx):
        def exit(*args):
            raise SystemExit(*args)
        env = {
            'ctx': ctx,
            'commands': commands,
            'discord': discord,
            'exit': exit,
        }
        out = StringIO()
        return env, out

    @staticmethod
    def _func_from_arg(arg, env):
        arg = arg.strip('`').rstrip().lstrip('\n').splitlines()
        indent = '    '
        for line in arg:
            strp = line.lstrip()
            if strp != line:
                indent = line[:len(line) - len(strp)]
                break
        arg = ''.join(indent * 2 + line + '\n' for line in arg)
        globline = ', '.join(i for i in env.keys() if i not in {
            'func', 'commands', 'discord', 'exit'
        })
        arg = f'''{indent}try:
{indent*2}global {globline}
{arg}
{indent}finally:
{indent*2}globals().update(locals())'''
        arg = f"async def func():\n{arg}"
        exec(arg, env)
        return env['func']

    @staticmethod
    def _trace():
        return re.sub(r'".*?kenny2github\\', '"', traceback.format_exc(), re.I)

    @commands.command('eval', description='eval-desc')
    async def eval_(self, ctx, *, arg):
        env, out = self._init_env(ctx)
        func = self._func_from_arg(arg, env)
        try:
            with redirect_stdout(out):
                ret = await func()
        except SystemExit:
            await ctx.send(f'```\n{out.getvalue()}```')
        except BaseException:
            trace = self._trace()
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

    @commands.command('exec', aliases=['py'], description='exec-desc')
    async def exec_(self, ctx):
        env, out = self._init_env(ctx)
        await ctx.send(f'```\nPython {sys.version} on {sys.platform}\n>>>\n```')
        while 1:
            arg = (await ctx.bot.wait_for('message', check=lambda m: (
                m.author.id == ctx.author.id
                and m.channel.id == ctx.channel.id
            ))).content
            out = StringIO()
            func = self._func_from_arg(arg, env)
            put = ''
            try:
                with redirect_stdout(out):
                    ret = await func()
            except SystemExit:
                break
            except BaseException:
                put = self._trace()
            else:
                put = repr(ret)
            finally:
                put = (out.getvalue() + put + '\n>>>').splitlines()
                i = 0
                while i < len(put):
                    j = 0
                    while len(put[i]) > 1992: #2000 - ```\n\n```
                        j += 1
                        put.insert(i+j, put[i][1992:])
                        put[i] = put[i][:1992]
                    i += 1
                puts = ['```\n']
                for line in put:
                    if len(puts[-1]) + len(line) + len('\n```') > 2000:
                        puts[-1] += '```'
                        puts.append('```\n')
                    puts[-1] += line + '\n'
                puts[-1] += '```'
                for put in puts:
                    await ctx.send(put)
