import sys
import os
import re
import logging
import traceback
import sqlite3 as sql
import asyncio as a
import discord as d
from discord.ext.commands import Bot
from discord.ext.commands import bot_has_permissions
from discord.ext.commands import has_permissions
from discord.ext import commands as c

DGBANSERVERID = 328938947717890058
#DGBANSERVERID = 337100820371996675

logfmt = logging.Formatter(
	fmt='{asctime} {ctx.author.name}: {message}',
	datefmt='%Y-%m-%dT%H:%M:%SZ',
	style='{'
)

class DummyCtx(object):
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)

class LoggerWriter(object):
	def __init__(self, level):
		self.level = level
	def write(self, message):
		if message.strip():
			self.level(message.encode('unicode-escape').decode('ascii'),
				extra={'ctx': DummyCtx(author=DummyCtx(name='(logger)'))})
	def flush(self):
		pass

handler = logging.FileHandler('runbot.log', 'w')
handler.setFormatter(logfmt)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO if len(sys.argv) < 2 else logging.DEBUG)
logger.addHandler(handler)
sys.stderr = LoggerWriter(logger.error)
sys.stdout = LoggerWriter(logger.debug)

dbw = sql.connect('kenny2automate.db')
dbw.row_factory = sql.Row
db = dbw.cursor()
with open(os.path.join(os.path.dirname(__file__), 'start.sql')) as f:
	db.executescript(f.read())

def get_command_prefix(bot, msg):
	res = db.execute('SELECT prefix FROM user_prefixes WHERE user_id=?', (msg.author.id,)).fetchone()
	if res is None:
		return ';'
	return (res['prefix'], ';')

client = Bot(
	description="The most awesome bot to walk(?) the earth.",
	command_prefix=get_command_prefix,
	pm_help=True,
	activity=d.Activity(type=d.ActivityType.watching, name=';help')
)

DGDELETEHANDLERS = {}

@client.event
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
	await client.invoke(ctx)

@client.event
async def on_message_delete(msg):
	if msg.mentions:
		logger.info('Message with mentions deleted: {}'.format(msg.content), extra={'ctx': DummyCtx(author=DummyCtx(name=msg.author.name))})
	if msg.id in DGDELETEHANDLERS:
		await DGDELETEHANDLERS[msg.id](msg)
		del DGDELETEHANDLERS[msg.id]

def add_delete_handler(msg, handler):
	DGDELETEHANDLERS[msg.id] = handler

@client.event
async def on_command_error(ctx, exc):
	logger.error('{} failed: {}'.format(ctx.command, exc), extra={'ctx': ctx})
	if isinstance(exc, (
		c.BotMissingPermissions,
		c.MissingPermissions,
		c.MissingRequiredArgument,
		c.BadArgument,
		c.CommandOnCooldown,
	)):
		return await ctx.send(exc)
	if isinstance(exc, (
		c.CheckFailure,
		c.CommandNotFound,
		c.TooManyArguments,
	)):
		return
	if hasattr(ctx.command, 'on_error'):
		return
	cog = ctx.cog
	if cog:
		attr = '_{0.__class__.__name__}__error'.format(cog)
		if hasattr(cog, attr):
			return
	print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
	traceback.print_exception(type(exc), exc, exc.__traceback__, file=sys.stderr)

from kenny2automate.i18n import i18n, I18n
from kenny2automate.scratch import Scratch
from kenny2automate.games import Games
from kenny2automate.wiki import Wiki
from kenny2automate.regexes import Regexes
from kenny2automate.connect4 import Connect4
from kenny2automate.hangman import Hangman
from kenny2automate.card_games import CardGames
from kenny2automate.battleship import Battleship

client.add_cog(I18n(client, logger, db))
client.add_cog(Scratch(client, logger, client.loop))
client.add_cog(Games(client, logger, db))
client.add_cog(Wiki(client, logger, client.loop, DGBANSERVERID))
client.add_cog(Regexes(client, logger))
client.add_cog(Connect4(client, logger, db))
client.add_cog(Hangman(client, logger, db))
client.add_cog(CardGames(client, logger, db))
client.add_cog(Battleship(client, logger, db))

@client.event
async def on_ready(*_, **__):
	logger.info('Ready!', extra={'ctx': DummyCtx(author=DummyCtx(name='(core)'))})

@client.command('eval')
@c.is_owner()
async def eval_(ctx, *, arg):
	"""Execute Python code. Only available to owner."""
	logger.info('eval: ' + arg, extra={'ctx': ctx})
	try:
		await eval(arg, globals(), locals())
	except BaseException as e:
		await ctx.send(e)

@client.command()
async def repeat(ctx, *, arg):
	"""Repeat what you say, right back at ya."""
	logger.info('repeat: ' + arg, extra={'ctx': ctx})
	msg = await ctx.send(arg)
	async def handle_delete(m):
		await msg.delete()
	add_delete_handler(ctx.message, handle_delete)

@client.command()
async def hello(ctx):
	"""Test whether the bot is running! Simply says "Hello World!"."""
	logger.info('Hello World!', extra={'ctx': ctx})
	await ctx.send(i18n(ctx, 'hello'))

@client.command()
async def hmmst(ctx):
	"""hmmst"""
	logger.info('hmmst', extra={'ctx': ctx})
	await ctx.send(i18n(ctx, 'hmmst'))

@client.command()
async def whoami(ctx):
	"""Get some information about yourself."""
	embed = d.Embed(
		title=i18n(ctx, 'whoami-title', ctx.author.display_name),
		description=i18n(
			ctx,
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
		embed.add_field(name=name, value=getattr(value, 'name', value))
	role_list = []
	for role in ctx.author.roles:
		role_list.append(role.name.replace('@', '\\@'))
	embed.add_field(
		name=i18n(ctx, 'whoami-roles'),
		value=', '.join(role_list), inline=False
	)
	await ctx.send(embed=embed)

@client.command()
async def prefix(ctx, *, prefix: str=None):
	"""Change the bot's prefix for yourself.

	Omit the `prefix` parameter to reset it to default.
	"""
	logger.info('prefix: ' + str(prefix), extra={'ctx': ctx})
	if prefix is None:
		db.execute(
			'DELETE FROM user_prefixes WHERE user_id=?',
			(ctx.author.id,)
		)
		await ctx.send(i18n(ctx, 'prefix-reset', ctx.author.mention))
		return
	res = db.execute(
		'SELECT prefix FROM user_prefixes WHERE user_id=?',
		(ctx.author.id,)
	).fetchone()
	if res is None:
		db.execute(
			'INSERT INTO user_prefixes VALUES (?, ?)',
			(ctx.author.id, prefix)
		)
	else:
		db.execute(
			'UPDATE user_prefixes SET prefix=? WHERE user_id=?',
			(prefix, ctx.author.id)
		)
	await ctx.send(i18n(ctx, 'prefix-set', ctx.author.mention, prefix))

@client.command()
@c.is_owner()
async def resetprefix(ctx, user: d.Member):
	"""Reset someone's prefix."""
	logger.info('resetprefix: ' + str(user.mention), extra={'ctx': ctx})
	db.execute(
		'DELETE FROM user_prefixes WHERE user_id=?',
		(user.id,)
	)
	await ctx.send(i18n(ctx, 'resetprefix', user.mention))

@client.command()
@has_permissions(manage_messages=True, read_message_history=True)
@bot_has_permissions(manage_messages=True, read_message_history=True)
async def purge(ctx, limit: int = 100, user: d.Member = None, *, matches: str = None):
	"""Purge all messages, optionally from ``user``
	or contains ``matches``."""
	logger.info('purge', extra={'ctx': ctx})
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
	msg = await ctx.send(i18n(ctx, 'purge', len(deleted)))
	await a.sleep(2)
	await msg.delete()

@client.command(name='8ball')
async def ball(ctx, *, question: str):
	choice = sum(question.encode('utf8')) % 20
	await ctx.send((
		i18n(ctx, '8ball/a1'),
		i18n(ctx, '8ball/a2'),
		i18n(ctx, '8ball/a3'),
		i18n(ctx, '8ball/a4'),
		i18n(ctx, '8ball/a5'),
		i18n(ctx, '8ball/a6'),
		i18n(ctx, '8ball/a7'),
		i18n(ctx, '8ball/a8'),
		i18n(ctx, '8ball/a9'),
		i18n(ctx, '8ball/a10'),
		i18n(ctx, '8ball/u1'),
		i18n(ctx, '8ball/u2'),
		i18n(ctx, '8ball/u3'),
		i18n(ctx, '8ball/u4'),
		i18n(ctx, '8ball/u5'),
		i18n(ctx, '8ball/n1'),
		i18n(ctx, '8ball/n2'),
		i18n(ctx, '8ball/n3'),
		i18n(ctx, '8ball/n4'),
		i18n(ctx, '8ball/n5')
	)[choice])

@client.command()
@bot_has_permissions(ban_members=True, add_reactions=True, read_message_history=True)
async def votetoban(ctx, *, user: d.Member):
	"""Start a vote to ban someone from the server. Abuse results in a ban."""
	logger.info('votetoban: ' + user.mention, extra={'ctx': ctx})
	for member in ctx.guild.members:
		if (str(member.status) == 'online') \
				and ctx.channel.permissions_for(member).administrator \
				and not member.bot:
			await ctx.send(i18n(ctx, 'votetoban-ping-admin', member.mention, user.mention))
			return
	DOBAN = '\U0001f6ab'
	NOBAN = '\U0001f607'
	msg = await ctx.send(i18n(ctx, 'votetoban-msg', user.mention, DOBAN, NOBAN))
	await msg.add_reaction(DOBAN)
	await msg.add_reaction(NOBAN)
	try:
		await ctx.bot.wait_for('member_update',
			check=lambda o, m: \
				ctx.channel.permissions_for(m).administrator \
				and not m.bot \
				and str(m.status) == 'online',
			timeout=180.0
		)
		await msg.delete()
		await ctx.send(i18n(ctx, 'votetoban-cancelled'))
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
			await ctx.send(i18n(ctx, 'votetoban-few', dos + nos))
		elif dos > nos:
			await ctx.send(i18n(ctx, 'votetoban-banned', dos, nos))
			await ctx.guild.ban(
				user,
				reason=i18n(ctx, 'votetoban-ban-reason', dos, nos)
			)
		else:
			await ctx.send(i18n(ctx, 'votetoban-innocent', dos, nos))

WATCHED_FILES_MTIMES = [
	(f, os.path.getmtime(f))
	for f in ('login.txt',)
	+ tuple(
		os.path.join(os.path.dirname(__file__), i)
		for i in os.listdir(os.path.dirname(__file__) or '.')
		if i.endswith('.py')
	)
]

async def update_if_changed():
	await client.wait_until_ready()
	while 1:
		for f, mtime in WATCHED_FILES_MTIMES:
			if os.path.getmtime(f) > mtime:
				await client.close()
		await a.sleep(1)

print('Defined stuff')

with open('login.txt') as f:
	token = f.read().strip()

try:
	client.loop.create_task(update_if_changed())
	client.run(token)
finally:
	dbw.commit()
	dbw.close()
