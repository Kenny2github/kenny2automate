#low-level
import sys
import os
import subprocess
import time
import random
#mid-level
import logging
import traceback
import pickle
import json
import sqlite3 as sql
#high-level
import asyncio
import argparse
#3rd-party
import discord
from discord.ext.commands import Bot
from discord.ext.commands import bot_has_permissions
from discord.ext.commands import has_permissions
from discord.ext import commands
from kenny2automate.utils import DummyCtx, lone_group
from kenny2automate.server import Handler
from kenny2automate.help import Kenny2help

VERSION = subprocess.check_output(
    "cd kenny2automate && git rev-parse --short HEAD",
    shell=True
).decode('ascii').strip()

logfmt = logging.Formatter(
    fmt='{asctime} {ctx.author.name}: {message}',
    datefmt='%Y-%m-%dT%H:%M:%SZ',
    style='{'
)

class LoggerWriter(object):
    def __init__(self, level):
        self.level = level
    def write(self, message):
        if message.strip():
            self.level(message.strip(),
                extra={'ctx': DummyCtx(author=DummyCtx(name='(logger)'))})
    def flush(self):
        pass

parser = argparse.ArgumentParser(description='Run the bot.')
parser.add_argument('prefix', nargs='?', help='the bot prefix', default=';')
parser.add_argument(
    '--disable', nargs='*', metavar='module',
    help='modules not to run'
)
parser.add_argument(
    '--loop', action='store_true', default=False,
    help='re-run on file change'
)
parser.add_argument(
    '--stdout', action='store_true', default=False,
    help='log to stdout instead of a file'
)
parser.add_argument('-v', action='store_true', help='let print() calls through')
cmdargs = parser.parse_args()

if not os.path.isdir('kenny2automate.log'):
    os.mkdir('kenny2automate.log')

handler = (
    logging.StreamHandler()
    if cmdargs.stdout
    else logging.FileHandler('kenny2automate.log/{}.log'.format(
        time.strftime('%Y-%m-%dT%H-%M-%SZ')
    ), 'w', 'utf8')
)
handler.setFormatter(logfmt)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG if cmdargs.v else logging.INFO)
logger.addHandler(handler)
if not cmdargs.stdout:
    sys.stderr = LoggerWriter(logger.error)
    sys.stdout = LoggerWriter(logger.debug)

sql.register_converter('pickle', pickle.loads)
sql.register_converter('json', json.loads)
sql.register_adapter(dict, json.dumps)
sql.register_adapter(list, pickle.dumps)
if not os.path.isfile('kenny2automate.db'):
    dbv = -1
else:
    dbv = None
dbw = sql.connect('kenny2automate.db', detect_types=sql.PARSE_DECLTYPES)
dbw.row_factory = sql.Row
db = dbw.cursor()
LATEST_DBV = 4
dbv = dbv or db.execute('PRAGMA user_version').fetchone()[0]
if dbv < LATEST_DBV:
    logger.info('Current dbv {} is less than latest {}, upgrading...'.format(
        dbv, LATEST_DBV
    ), extra={'ctx': DummyCtx(author=DummyCtx(name='(startup)'))})
    for i in range(dbv + 1, LATEST_DBV + 1):
        if not os.path.isfile(os.path.join(
                os.path.dirname(__file__), 'sql', 'v{}.sql'.format(i)
        )):
            logger.info('No script for v{}, skipping'.format(i),
                extra={'ctx': DummyCtx(author=DummyCtx(name='(startup)'))})
            continue
        with open(os.path.join(
                os.path.dirname(__file__), 'sql', 'v{}.sql'.format(i)
        )) as f:
            logger.info('Running script from v{} to v{}'.format(i - 1, i),
                extra={'ctx': DummyCtx(author=DummyCtx(name='(startup)'))})
            try:
                db.executescript(f.read())
            except sql.OperationalError as exc:
                logger.error('Running script failed: {}'.format(exc))
    db.execute('PRAGMA user_version = {}'.format(LATEST_DBV))
del dbv

def get_command_prefix(bot, msg):
    if msg is None:
        return cmdargs.prefix
    res = db.execute('SELECT prefix FROM users WHERE user_id=?', (msg.author.id,)).fetchone()
    if res is None or res['prefix'] is None:
        return cmdargs.prefix
    return (res['prefix'], cmdargs.prefix)

client = Bot(
    description="description",
    command_prefix=get_command_prefix,
    help_command=Kenny2help(command_attrs={'description': 'help-desc'}),
    activity=discord.Activity(type=discord.ActivityType.watching, name=cmdargs.prefix + 'help')
)

@client.event
async def on_command_error(ctx, exc):
    if hasattr(ctx.command, 'on_error'):
        return
    cog = ctx.cog
    if cog:
        attr = '_{0.__class__.__name__}__error'.format(cog)
        if hasattr(cog, attr):
            return
    if isinstance(exc, (
        commands.BotMissingPermissions,
        commands.MissingPermissions,
        commands.MissingRequiredArgument,
        commands.BadArgument,
        commands.CommandOnCooldown,
    )):
        return await ctx.send(embed=embed(ctx,
            title=('error',),
            description=str(exc),
            color=0xff0000
        ))
    if isinstance(exc, (
        commands.CheckFailure,
        commands.CommandNotFound,
        commands.TooManyArguments,
    )):
        return
    logger.error('Ignoring exception in command {}:\n'.format(ctx.command)
        + ''.join(traceback.format_exception(
            type(exc), exc, exc.__traceback__
        )),
        extra={'ctx': ctx}
    )

@client.before_invoke
async def before_invoke(ctx):
    logger.info(ctx.command, extra={'ctx': ctx})

@client.check
async def check_disabled_things(ctx):
    if ctx.guild is None:
        return True #no disabled commands in DMs
    res = db.execute(
        'SELECT guild_disabled_commands, guild_disabled_cogs FROM guilds \
WHERE guild_id=?',
        (ctx.guild.id,)
    ).fetchone()
    if res is None:
        return True #not even a guild row for that guild
    commands, cogs = res
    commands = (commands or '').split(',')
    cogs = (cogs or '').split(',')
    if res['guild_disabled_cogs'] is not None:
        if (ctx.command.cog_name or 'None') in cogs:
            return False #disabled by cog
    if res['guild_disabled_commands'] is not None:
        if ctx.command.qualified_name in commands:
            return False #specific
        parent = ctx.command.parent
        while parent:
            if parent.qualified_name in commands:
                return False #parent group was disabled, all subcommands ded
            parent = parent.parent
        return True #not disabled by cog or command
    return True #neither was specified

deleters = {}
@client.event
async def on_raw_message_delete(payload):
    msgid = payload.message_id
    if msgid in deleters:
        try:
            msg = await client.get_channel(payload.channel_id).fetch_message(deleters[msgid])
            await msg.delete()
        except Exception: #silence errors, might not be able to do stuff
            pass
        del deleters[msgid]

from kenny2automate.i18n import i18n, I18n, embed
client.add_cog(I18n(client, db, deleters))

if cmdargs.disable is None:
    cmdargs.disable = ()
dmx = DummyCtx(author=DummyCtx(name='(loader)'))
if 'numguess' not in cmdargs.disable:
    logger.info('Loading Numguess', extra={'ctx': dmx})
    from kenny2automate.numguess import Numguess
    client.add_cog(Numguess())
if 'regexes' not in cmdargs.disable:
    logger.info('Loading Regexes', extra={'ctx': dmx})
    from kenny2automate.regexes import Regexes
    client.add_cog(Regexes())
if 'connect4' not in cmdargs.disable:
    logger.info('Loading Connect4', extra={'ctx': dmx})
    from kenny2automate.connect4 import Connect4
    client.add_cog(Connect4(client, db))
if 'hangman' not in cmdargs.disable:
    logger.info('Loading Hangman', extra={'ctx': dmx})
    from kenny2automate.hangman import Hangman
    client.add_cog(Hangman(client, db))
if 'fish' not in cmdargs.disable:
    logger.info('Loading Fish', extra={'ctx': dmx})
    from kenny2automate.card_games import Fish
    client.add_cog(Fish(client, db))
if 'battleship' not in cmdargs.disable:
    logger.info('Loading Battleship', extra={'ctx': dmx})
    from kenny2automate.battleship import Battleship
    client.add_cog(Battleship(client, db))
if 'fight' not in cmdargs.disable:
    logger.info('Loading Fight', extra={'ctx': dmx})
    from kenny2automate.fight import Fight
    client.add_cog(Fight(client, db))
if 'evolution' not in cmdargs.disable:
    logger.info('Loading Evolution', extra={'ctx': dmx})
    from kenny2automate.evolution import Evolution
    client.add_cog(Evolution(client, db))
if 'units' not in cmdargs.disable:
    logger.info('Loading Units', extra={'ctx': dmx})
    from kenny2automate.units import Units
    client.add_cog(Units())
if 'words' not in cmdargs.disable:
    logger.info('Loading Words', extra={'ctx': dmx})
    from kenny2automate.words import Words
    client.add_cog(Words(client, db))
if 'boggle' not in cmdargs.disable:
    logger.info('Loading Boggle', extra={'ctx': dmx})
    from kenny2automate.boggle import Boggle
    client.add_cog(Boggle(client, db))

logger.info('Loading Eval', extra={'ctx': dmx})
from kenny2automate.eval_ import eval_
client.add_command(eval_)

@client.event
async def on_ready(*_, **__):
    logger.info('Ready!', extra={'ctx': DummyCtx(author=DummyCtx(name='(startup)'))})

@client.command(description='repeat-desc')
async def repeat(ctx, *, arg):
    msg = await ctx.send(arg)
    deleters[ctx.message.id] = msg.id

@client.command(description='hello-desc')
async def hello(ctx):
    await ctx.send(i18n(ctx, 'hello'))

@client.command(description='hmmst-desc')
async def hmmst(ctx):
    await ctx.send(i18n(ctx, 'hmmst'))

@client.command(description='whoami-desc')
async def whoami(ctx):
    emb = embed(ctx,
        title=('whoami-title', ctx.author.display_name),
        description=(
            'whoami-description',
            ctx.author.display_name
        )
    )
    emb.set_thumbnail(url=ctx.author.avatar_url)
    things = {
        'status': i18n(ctx, 'whoami-status'),
        'activity': i18n(ctx, 'whoami-activity'),
        'id': i18n(ctx, 'whoami-id'),
        'created_at': i18n(ctx, 'whoami-created-at'),
        'joined_at': i18n(ctx, 'whoami-joined-at'),
    }
    for key, name in things.items():
        value = getattr(ctx.author, key)
        emb.add_field(name=name, value=getattr(value, 'name', value))
    role_list = []
    for role in ctx.author.roles:
        role_list.append(role.name.replace('@', '\\@'))
    emb.add_field(
        name=i18n(ctx, 'whoami-roles'),
        value=', '.join(role_list), inline=False
    )
    await ctx.send(embed=emb)

@client.group(invoke_without_command=True, description='prefix-desc')
@lone_group(False)
async def prefix(ctx):
    pass

@prefix.command('reset', description='reset-desc')
async def prefix_reset(ctx, user: discord.Member = None):
    """reset-help"""
    leuser = (user or ctx.author) if (await client.is_owner(ctx.author)) else ctx.author
    db.execute(
        'UPDATE users SET prefix=NULL WHERE user_id=?',
        (leuser.id,)
    )
    await ctx.send(embed=embed(ctx,
        title=('prefix-reset-title',),
        description=('prefix-reset', leuser.mention),
        color=0x0000ff
    ))

@prefix.command('set', description='set-desc')
async def prefix_set(ctx, *, prefix):
    """set-help"""
    res = db.execute(
        'SELECT prefix FROM users WHERE user_id=?',
        (ctx.author.id,)
    ).fetchone()
    if len(prefix) > 2 and prefix[0] == prefix[-1]:
        prefix = prefix[1:-1]
    if res is None:
        db.execute(
            'INSERT INTO users (user_id, prefix) VALUES (?, ?)',
            (ctx.author.id, prefix)
        )
    else:
        db.execute(
            'UPDATE users SET prefix=? WHERE user_id=?',
            (prefix, ctx.author.id)
        )
    await ctx.send(embed=embed(ctx,
        title=('prefix-set-title',),
        description=('prefix-set', ctx.author.mention, prefix),
        color=0x55acee
    ))

@prefix.command('get', description='get-desc')
async def prefix_get(ctx):
    res = db.execute(
        'SELECT prefix FROM users WHERE user_id=?',
        (ctx.author.id,)
    ).fetchone()
    if res is None or res['prefix'] is None:
        await ctx.send(embed=embed(ctx,
            description=('prefix-unset',)
        ))
    else:
        await ctx.send(embed=embed(ctx,
            title=('prefix',),
            description=res['prefix']
        ))

@client.command(description='someone-desc')
async def someone(ctx):
    await ctx.send(embed=discord.Embed(
        description=random.choice(ctx.guild.members).mention
    ))

@client.command(description='ping-desc')
async def ping(ctx):
    await ctx.send(embed=embed(ctx,
        title=('ping-title',),
        description='{}ms'.format(round(client.latency * 1000, 3))
    ))

@client.command(description='purge-desc')
@has_permissions(manage_messages=True, read_message_history=True)
@bot_has_permissions(manage_messages=True, read_message_history=True)
async def purge(ctx, limit: int = 100, user: discord.Member = None, *, matches: str = None):
    def check_msg(msg):
        if msg.id == ctx.message.id:
            return True
        if user is not None:
            if msg.author.id != user.id:
                return False
        if matches is not None:
            if matches not in msg.content:
                return False
        return True
    deleted = await ctx.channel.purge(limit=limit, check=check_msg)
    msg = await ctx.send(embed=embed(ctx,
        title=('purge-title',),
        description=('purge', len(deleted)),
        color=0xff0000
    ))
    await asyncio.sleep(2)
    await msg.delete()

@client.command(name='8ball', description='8ball-desc')
async def ball(ctx, *, question: str):
    choice = sum(question.encode('utf8')) % 20
    await ctx.send(embed=embed(ctx, description=((
        '8ball/a1', '8ball/a2', '8ball/a3', '8ball/a4',
        '8ball/a5', '8ball/a6', '8ball/a7', '8ball/a8',
        '8ball/a9', '8ball/a10', '8ball/u1', '8ball/u2',
        '8ball/u3', '8ball/u4', '8ball/u5', '8ball/n1',
        '8ball/n2', '8ball/n3', '8ball/n4', '8ball/n5'
    )[choice],)))

@client.command(description='whois-desc')
async def whois(ctx, *, user: discord.User):
    await ctx.send(embed=discord.Embed(description=user.mention))

@client.command(description='whereis-desc')
async def whereis(ctx, *, channel: discord.TextChannel):
    await ctx.send(embed=discord.Embed(description=channel.mention))

@client.command(description='version-desc')
async def version(ctx):
    await ctx.send(embed=discord.Embed(description='`{}`'.format(VERSION)))

@client.command(description='votetoban-desc')
@bot_has_permissions(ban_members=True, add_reactions=True, read_message_history=True)
async def votetoban(ctx, *, user: discord.Member):
    for member in ctx.guild.members:
        if (str(member.status) == 'online') \
                and ctx.channel.permissions_for(member).ban_members \
                and not member.bot:
            await ctx.send(i18n(ctx, 'votetoban-ping-admin', member.mention, user.mention))
            return
    DOBAN = '\U0001f6ab'
    NOBAN = '\U0001f607'
    msg = await ctx.send(embed=embed(ctx,
        title=('votetoban-title', user.mention),
        description=('votetoban-msg', DOBAN, NOBAN),
        color=0
    ))
    await msg.add_reaction(DOBAN)
    await msg.add_reaction(NOBAN)
    try:
        o, m = await ctx.bot.wait_for('member_update',
            check=lambda o, m: \
                ctx.channel.permissions_for(m).ban_members \
                and not m.bot \
                and str(m.status) == 'online',
            timeout=180.0
        )
        await msg.delete()
        await ctx.send(embed=embed(ctx,
            title=('votetoban-cancelled-title',),
            description=('votetoban-cancelled', m.mention),
        ))
    except asyncio.TimeoutError:
        msg = await ctx.get_message(msg.id)
        dos = 0
        nos = 0
        for r in msg.reactions:
            if r.emoji == DOBAN:
                dos = r.count - 1
            elif r.emoji == NOBAN:
                nos = r.count - 1
        await msg.delete()
        if dos + nos < 3:
            await ctx.send(embed=embed(ctx,
                title=('votetoban-ended',),
                description=('votetoban-few', dos + nos),
                color=0xff0000
            ))
        elif dos > nos:
            await ctx.guild.ban(
                user,
                reason='Banned after vote {0} against {1} \
when admins were gone.'.format(dos, nos)
            )
            await ctx.send(embed=embed(ctx,
                title=('votetoban-ended',),
                description=('votetoban-banned', dos, nos),
                color=0
            ))
        else:
            await ctx.send(embed=embed(ctx,
                title=('votetoban-ended',),
                description=('votetoban-innocent', dos, nos),
                color=0x55acee
            ))

WATCHED_FILES_MTIMES = [('kenny2automate.txt', os.path.getmtime('kenny2automate.txt'))]
def recurse_mtimes(dir, *s):
    for i in os.listdir(os.path.join(*s, dir)):
        if os.path.isdir(os.path.join(*s, dir, i)):
            recurse_mtimes(i, *s, dir)
        elif not i.endswith(('.py', '.sql', '.json')):
            pass
        else:
            WATCHED_FILES_MTIMES.append((
                os.path.join(*s, dir, i),
                os.path.getmtime(
                    os.path.join(*s, dir, i)
                )
            ))
recurse_mtimes(os.path.abspath(os.path.dirname(__file__)))

async def update_if_changed():
    await client.wait_until_ready()
    while 1:
        for f, mtime in WATCHED_FILES_MTIMES:
            if os.path.getmtime(f) > mtime:
                if cmdargs.loop:
                    os.system('./discordapp restart')
                raise KeyboardInterrupt
        try:
            await asyncio.sleep(1)
        except (KeyboardInterrupt, asyncio.CancelledError):
            return

@client.command(description='stop-desc')
@commands.is_owner()
async def stop(ctx):
    await client.close()

with open('kenny2automate.txt') as f:
    token = f.readline().strip()
    client_id = f.readline().strip()
    client_secret = f.readline().strip()
    web_root = f.readline().strip()

try:
    wakeup = client.loop.create_task(update_if_changed())
    if cmdargs.loop:
        others = subprocess.check_output("ps aux | grep -v grep | grep 'kenny2automate' | awk '{print $2}'", shell=True).splitlines()
        for i in others:
            if int(i) == os.getpid():
                continue
            os.system('kill -2 {}'.format(i.decode('ascii')))
    server = Handler(
        client, db, logger, cmdargs.prefix,
        client_id, client_secret, web_root
    )
    client.loop.run_until_complete(server.run())
    client.loop.run_until_complete(client.start(token))
except KeyboardInterrupt:
    pass
finally:
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    try:
        wakeup.cancel()
    except RuntimeError as exc:
        print(exc) #probably already closed?
    client.loop.run_until_complete(client.close())
    client.loop.run_until_complete(server.stop())
    client.loop.stop()
    client.loop.close()
    dbw.commit()
    dbw.close()
