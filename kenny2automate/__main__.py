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
			self.level(message.strip(),
				extra={'ctx': DummyCtx(author=DummyCtx(name='(logger)'))})
	def flush(self):
		pass

handler = logging.FileHandler('runbot.log', 'w', 'utf8')
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
	res = db.execute('SELECT prefix FROM users WHERE user_id=?', (msg.author.id,)).fetchone()
	if res is None or res['prefix'] is None:
		return ';'
	return (res['prefix'], ';')

client = Bot(
	description="The most awesome bot to walk(?) the earth.",
	command_prefix=get_command_prefix,
	pm_help=True,
	activity=d.Activity(type=d.ActivityType.watching, name=';help')
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

@client.before_invoke
async def before_invoke(ctx):
	logger.info(ctx.command, extra={'ctx': ctx})

from kenny2automate.i18n import i18n, I18n
from kenny2automate.scratch import Scratch
from kenny2automate.numguess import Numguess
from kenny2automate.wiki import Wiki
from kenny2automate.regexes import Regexes
from kenny2automate.connect4 import Connect4
from kenny2automate.hangman import Hangman
from kenny2automate.card_games import CardGames
from kenny2automate.battleship import Battleship
from kenny2automate.fight import Fight

client.add_cog(I18n(client, db))
client.add_cog(Scratch(client))
client.add_cog(Numguess())
client.add_cog(Wiki(client, logger, DGBANSERVERID))
client.add_cog(Regexes())
client.add_cog(Connect4(client, db))
client.add_cog(Hangman(client, db))
client.add_cog(CardGames(client, db))
client.add_cog(Battleship(client, db))
client.add_cog(Fight(client, db))

@client.event
async def on_ready(*_, **__):
	logger.info('Ready!', extra={'ctx': DummyCtx(author=DummyCtx(name='(core)'))})

@client.command('eval')
@c.is_owner()
async def eval_(ctx, *, arg):
	"""Execute Python code. Only available to owner."""
	try:
		await eval(arg, globals(), locals())
	except BaseException as e:
		await ctx.send(e)

@client.command()
async def repeat(ctx, *, arg):
	"""Repeat what you say, right back at ya."""
	msg = await ctx.send(arg)
	@client.listen()
	async def on_message_delete(msg2):
		if msg2.id == msg.id:
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
	await ctx.send(i18n(ctx, 'prefix-reset', leuser.mention))

@prefix.command('set')
async def prefix_set(ctx, *, prefix):
	"""Set your own prefix."""
	res = db.execute(
		'SELECT prefix FROM users WHERE user_id=?',
		(ctx.author.id,)
	).fetchone()
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
	await ctx.send(i18n(ctx, 'prefix-set', ctx.author.mention, prefix))

@prefix.command('get')
async def prefix_get(ctx):
	"""Get your own prefix."""
	res = db.execute(
		'SELECT prefix FROM users WHERE user_id=?',
		(ctx.author.id,)
	).fetchone()
	if res is None or res['prefix'] is None:
		await ctx.send(i18n(ctx, 'prefix-unset'))
	else:
		await ctx.send(res['prefix'])

@client.command()
@c.is_owner()
async def resetprefix(ctx, user: d.Member):
	"""Reset someone's prefix."""
	db.execute(
		'UPDATE users SET prefix=NULL WHERE user_id=?',
		(user.id,)
	)
	await ctx.send(i18n(ctx, 'resetprefix', user.mention))

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
async def whois(ctx, *, user: d.User):
	await ctx.send(embed=d.Embed(description=user.mention))

@client.command()
async def whereis(ctx, *, channel: d.TextChannel):
	await ctx.send(channel.mention)

@client.command()
@bot_has_permissions(ban_members=True, add_reactions=True, read_message_history=True)
async def votetoban(ctx, *, user: d.Member):
	"""Start a vote to ban someone from the server. Abuse results in a ban."""
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
