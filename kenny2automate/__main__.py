import sys
import os
import re
import logging
import traceback
import pickle
import sqlite3 as sql
import asyncio as a
import argparse
import discord as d
from discord.ext.commands import Bot
from discord.ext.commands import bot_has_permissions
from discord.ext.commands import has_permissions
from discord.ext import commands as c
from kenny2automate.utils import DummyCtx

DGBANSERVERID = 328938947717890058
#DGBANSERVERID = 337100820371996675

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
parser.add_argument('--disable', nargs='*', metavar='module',
	help='modules not to run')
parser.add_argument('-v', action='store_true', help='let print() calls through')
cmdargs = parser.parse_args()

handler = logging.FileHandler('runbot.log', 'w', 'utf8')
handler.setFormatter(logfmt)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG if cmdargs.v else logging.INFO)
logger.addHandler(handler)
sys.stderr = LoggerWriter(logger.error)
sys.stdout = LoggerWriter(logger.debug)

sql.register_converter('pickle', pickle.loads)
if not os.path.isfile('kenny2automate.db'):
	dbv = -1
else:
	dbv = None
dbw = sql.connect('kenny2automate.db', detect_types=sql.PARSE_DECLTYPES)
dbw.row_factory = sql.Row
db = dbw.cursor()
LATEST_DBV = 1
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
	res = db.execute('SELECT prefix FROM users WHERE user_id=?', (msg.author.id,)).fetchone()
	if res is None or res['prefix'] is None:
		return cmdargs.prefix
	return (res['prefix'], cmdargs.prefix)

client = Bot(
	description="The most awesome bot to walk(?) the earth.",
	command_prefix=get_command_prefix,
	pm_help=True,
	activity=d.Activity(type=d.ActivityType.watching, name=cmdargs.prefix + 'help')
)

@client.listen()
async def on_message(msg):
	ctx = await client.get_context(msg)
	if (ctx.guild
		and ctx.channel.permissions_for(ctx.guild.me).manage_messages
		and ctx.guild.id == DGBANSERVERID
	):
		if re.search(r'https?://discord(\.gg|app\.com/invite)',
				msg.content, re.I):
			await msg.delete()
			return

@client.event
async def on_message_delete(msg):
	if msg.mentions:
		logger.info('Message with mentions deleted: {}'.format(msg.content),
			extra={'ctx': DummyCtx(author=DummyCtx(name=msg.author.name))})

@client.event
async def on_command_error(ctx, exc):
	logger.error('{} failed: {}'.format(ctx.command, exc), extra={'ctx': ctx})
	if hasattr(ctx.command, 'on_error'):
		return
	cog = ctx.cog
	if cog:
		attr = '_{0.__class__.__name__}__error'.format(cog)
		if hasattr(cog, attr):
			return
	if isinstance(exc, (
		c.BotMissingPermissions,
		c.MissingPermissions,
		c.MissingRequiredArgument,
		c.BadArgument,
		c.CommandOnCooldown,
	)):
		return await ctx.send(embed=embed(ctx,
			title=('error',),
			description=str(exc),
			color=0xff0000
		))
	if isinstance(exc, (
		c.CheckFailure,
		c.CommandNotFound,
		c.TooManyArguments,
	)):
		return
	print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
	traceback.print_exception(type(exc), exc, exc.__traceback__, file=sys.stderr)

@client.before_invoke
async def before_invoke(ctx):
	logger.info(ctx.command, extra={'ctx': ctx})

from kenny2automate.i18n import i18n, I18n, embed
client.add_cog(I18n(client, db))

if cmdargs.disable is not None:
	if 'scratch' not in cmdargs.disable:
		from kenny2automate.scratch import Scratch
		client.add_cog(Scratch(client))
	if 'numguess' not in cmdargs.disable:
		from kenny2automate.numguess import Numguess
		client.add_cog(Numguess())
	if 'wiki' not in cmdargs.disable:
		from kenny2automate.wiki import Wiki
		client.add_cog(Wiki(client, logger, DGBANSERVERID))
	if 'regexes' not in cmdargs.disable:
		from kenny2automate.regexes import Regexes
		client.add_cog(Regexes())
	if 'connect4' not in cmdargs.disable:
		from kenny2automate.connect4 import Connect4
		client.add_cog(Connect4(client, db))
	if 'hangman' not in cmdargs.disable:
		from kenny2automate.hangman import Hangman
		client.add_cog(Hangman(client, db))
	if 'cardgames' not in cmdargs.disable:
		from kenny2automate.card_games import CardGames
		client.add_cog(CardGames(client, db))
	if 'battleship' not in cmdargs.disable:
		from kenny2automate.battleship import Battleship
		client.add_cog(Battleship(client, db))
	if 'fight' not in cmdargs.disable:
		from kenny2automate.fight import Fight
		client.add_cog(Fight(client, db))
	if 'evolution' not in cmdargs.disable:
		from kenny2automate.evolution import Evolution
		client.add_cog(Evolution(client, db))

@client.event
async def on_ready(*_, **__):
	logger.info('Ready!', extra={'ctx': DummyCtx(author=DummyCtx(name='(startup)'))})

@client.command('eval')
@c.is_owner()
async def eval_(ctx, *, arg):
	"""Execute Python code. Only available to owner."""
	try:
		await eval(arg, globals(), locals())
	except BaseException as e:
		await ctx.send(embed=embed(ctx,
			title=('error',),
			description=str(e),
			color=0xff0000
		))

@client.command()
async def repeat(ctx, *, arg):
	"""Repeat what you say, right back at ya."""
	msg = await ctx.send(arg)
	@client.listen()
	async def on_message_delete(msg2):
		if msg2.id == ctx.message.id:
			await msg.delete()
			client.remove_listener(on_message_delete)

@client.command()
async def hello(ctx):
	"""Test whether the bot is running! Simply says "Hello World!"."""
	await ctx.send(i18n(ctx, 'hello'))

@client.command()
async def hmmst(ctx):
	"""hmmst"""
	await ctx.send(i18n(ctx, 'hmmst'))

@client.command()
async def whoami(ctx):
	"""Get some information about yourself."""
	emb = embed(ctx,
		title=('whoami-title', ctx.author.display_name),
		description=(
			'whoami-description',
			ctx.author.display_name
		)
	)
	embed.set_thumbnail(url=ctx.author.avatar_url)
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

@client.group()
async def prefix(ctx):
	"""Bot prefix-related commands."""
	pass

@prefix.command('reset')
async def prefix_reset(ctx, user: d.Member = None):
	"""Reset your own prefix.

	The owner of the bot can also reset other users' prefixes.
	"""
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

@prefix.command('set')
async def prefix_set(ctx, *, prefix):
	"""Set your own prefix.
	If you need a space at the start or end of the prefix, quote the prefix by
	adding the same character at the start and end of the prefix. For example,
	`;prefix set hello ` will set your prefix to "hello" but
	`;prefix set %hello %` will set your prefix to "hello " (note the trailing
	space)."""
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

@prefix.command('get')
async def prefix_get(ctx):
	"""Get your own prefix."""
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

@client.command()
@c.is_owner()
async def resetprefix(ctx, user: d.Member):
	"""Reset someone's prefix."""
	db.execute(
		'UPDATE users SET prefix=NULL WHERE user_id=?',
		(user.id,)
	)
	await ctx.send(embed=embed(ctx,
		title=('prefix-reset-title,'),
		description=('prefix-reset', user.mention),
		color=0xff0000
	))

@client.command()
@has_permissions(manage_messages=True, read_message_history=True)
@bot_has_permissions(manage_messages=True, read_message_history=True)
async def purge(ctx, limit: int = 100, user: d.Member = None, *, matches: str = None):
	"""Purge all messages, optionally from ``user``
	or contains ``matches``."""
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
	await a.sleep(2)
	await msg.delete()

@client.command(name='8ball')
async def ball(ctx, *, question: str):
	choice = sum(question.encode('utf8')) % 20
	await ctx.send(embed(ctx, description=((
		'8ball/a1', '8ball/a2', '8ball/a3', '8ball/a4',
		'8ball/a5', '8ball/a6', '8ball/a7', '8ball/a8',
		'8ball/a9', '8ball/a10', '8ball/u1', '8ball/u2',
		'8ball/u3', '8ball/u4', '8ball/u5', '8ball/n1',
		'8ball/n2', '8ball/n3', '8ball/n4', '8ball/n5'
	)[choice],)))

@client.command()
async def whois(ctx, *, user: d.User):
	await ctx.send(embed=d.Embed(description=user.mention))

@client.command()
async def whereis(ctx, *, channel: d.TextChannel):
	await ctx.send(embed=d.Embed(description=channel.mention))

@client.command()
@bot_has_permissions(ban_members=True, add_reactions=True, read_message_history=True)
async def votetoban(ctx, *, user: d.Member):
	"""Start a vote to ban someone from the server. Abuse results in a ban."""
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
	except a.TimeoutError:
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

WATCHED_FILES_MTIMES = [('login.txt', os.path.getmtime('login.txt'))]
def recurse_mtimes(dir, *s):
	for i in os.listdir(os.path.join(*s, dir)):
		if os.path.isdir(os.path.join(*s, dir, i)):
			recurse_mtimes(i, *s, dir)
		elif i.endswith('.pyc'):
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
				await client.close()
		await a.sleep(1)

@client.command()
@c.is_owner()
async def stop(ctx):
	"""Stop the bot."""
	await client.close()

print('Defined stuff')

with open('login.txt') as f:
	token = f.read().strip()

try:
	client.loop.create_task(update_if_changed())
	client.run(token)
finally:
	dbw.commit()
	dbw.close()
