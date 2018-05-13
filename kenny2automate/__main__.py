import sys
import os
import logging
import sqlite3 as sql
import asyncio as a
import discord as d
from discord.ext.commands import Bot
from discord.ext.commands import bot_has_permissions
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
			self.level(message, extra={'ctx': DummyCtx(author=DummyCtx(name='(logger)'))})
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
	return res['prefix']

client = Bot(
	description="The most awesome bot to walk(?) the earth.",
	command_prefix=get_command_prefix,
	pm_help=True,
	activity=d.Game(name=';help')
)

DGDELETEHANDLERS = {}

@client.event
async def on_message_delete(msg):
	if msg.id in DGDELETEHANDLERS:
		await DGDELETEHANDLERS[msg.id](msg)
		del DGDELETEHANDLERS[msg.id]

def add_delete_handler(msg, handler):
	DGDELETEHANDLERS[msg.id] = handler

from kenny2automate.scratch import Scratch
from kenny2automate.games import Games
from kenny2automate.wiki import Wiki
from kenny2automate.regexes import Regexes

client.add_cog(Scratch(client, logger, client.loop))
client.add_cog(Games(client, logger, db))
client.add_cog(Wiki(client, logger, client.loop, DGBANSERVERID))
client.add_cog(Regexes(client, logger))

@client.event
async def on_ready(*_, **__):
	logger.info('Ready!', extra={'ctx': DummyCtx(author=DummyCtx(name='(core)'))})
	await client.change_presence(game=d.Game(name=';help'))

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
	await ctx.send('Hello World!')

@client.command()
async def hmmst(ctx):
	"""hmmst"""
	logger.info('hmmst', extra={'ctx': ctx})
	await ctx.send('hmmst')

@client.command()
async def whoami(ctx):
	"""Get some information about yourself."""
	embed = d.Embed(
		title="User information for {}".format(ctx.author.nick or ctx.author.name),
		description="Here is some information about {}".format(ctx.author.nick or ctx.author.name)
	)
	embed.set_thumbnail(url=ctx.author.avatar_url)
	things = {
		'status': 'Status',
		'game': 'Game',
		'id': 'ID',
		'created_at': 'Created at',
		'joined_at': 'Joined at',
	}
	for key, name in things.items():
		value = getattr(ctx.author, key)
		embed.add_field(name=name, value=getattr(value, 'name', value))
	role_list = []
	for role in ctx.author.roles:
		role_list.append(role.name.replace('@', '\\@'))
	embed.add_field(name='Roles', value=', '.join(role_list), inline=False)
	await ctx.send(embed=embed)

#@client.command()
async def timer(ctx, *, seconds=0):
	"""Mention you after `seconds` seconds."""
	seconds = int(seconds)
	logger.info('timer: ' + str(seconds), extra={'ctx': ctx})
	if seconds > 18000:
		await ctx.send("Sorry, it's a waste of resources to wait more than 5 hours.")
		return
	await ctx.send("I'll mention you in {} seconds...".format(seconds))
	await a.sleep(seconds)
	await ctx.send("{}, time's up!".format(ctx.author.mention))

@client.command()
async def prefix(ctx, *, prefix: str=None):
	"""Change the bot's prefix for yourself.

	Omit the `prefix` parameter to reset it to default.
	"""
	logger.info('prefix: ' + str(prefix), extra={'ctx': ctx})
	if prefix is None:
		db.execute('DELETE FROM user_prefixes WHERE user_id=?', (ctx.author.id,))
		await ctx.send('Successfully reset prefix for {}'.format(ctx.author.mention))
		return
	res = db.execute('SELECT prefix FROM user_prefixes WHERE user_id=?', (ctx.author.id,)).fetchone()
	if res is None:
		db.execute('INSERT INTO user_prefixes VALUES (?, ?)', (ctx.author.id, prefix))
	else:
		db.execute('UPDATE user_prefixes SET prefix=? WHERE user_id=?', (prefix, ctx.author.id))
	await ctx.send('Successfully set prefix for {} to `{}`'.format(ctx.author.mention, prefix))

@client.command()
@c.is_owner()
async def resetprefix(ctx, user: d.Member):
	db.execute('DELETE FROM user_prefixes WHERE user_id=?', (user.id,))
	await ctx.send('Successfully reset prefix for {}'.format(user.mention))

@client.command()
@bot_has_permissions(ban_members=True, add_reactions=True, read_message_history=True)
async def votetoban(ctx, *, user: d.Member):
	"""Start a vote to ban someone from the server. Abuse results in a ban."""
	logger.info('votetoban: ' + user.mention, extra={'ctx': ctx})
	if ctx.guild.id != DGBANSERVERID:
		return
	for member in ctx.guild.members:
		if (str(member.status) == 'online') \
				and ctx.channel.permissions_for(member).administrator \
				and not member.bot:
			await ctx.send(member.mention + ', someone requests for ' + user.mention + ' to be banned!')
			return
	DOBAN = '🚫'
	NOBAN = '😇'
	msg = await ctx.send('**Vote to ban ' + user.mention + '**\nReact ' + DOBAN + ' to vote to ban; react ' + NOBAN + ' to vote to keep.')
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
		await ctx.send('An admin has come online! The vote has been cancelled. Please ask them instead.')
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
			await ctx.send('Not enough people voted! ({} total, minimum is 3.) The user stays.'.format(dos + nos))
		elif dos > nos:
			await ctx.send('{} votes for and {} votes against. The user has been banned.'.format(dos, nos))
			await user.ban(reason='Banned after vote'
					+ ' {} against {}'.format(dos, nos)
					+ ' when admins were gone.')
		else:
			await ctx.send('{} votes for and {} votes against. The user stays.'.format(dos, nos))

@votetoban.error
async def on_votetoban_err(ctx, error):
	logger.error('votetoban failed: ' + str(error), extra={'ctx': ctx})
	if isinstance(error, c.BotMissingPermissions):
		await ctx.send(str(error))
	else:
		raise error

WATCHED_FILES_MTIMES = [
	(f, os.path.getmtime(f))
	for f in ('/home/pi/login.txt',)
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

with open('/home/pi/login.txt') as f:
	token = f.read().strip()

try:
	client.loop.create_task(update_if_changed())
	client.run(token)
finally:
	dbw.commit()
	dbw.close()
