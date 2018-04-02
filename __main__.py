import re
import logging
import random
import json
from urllib.parse import quote
import asyncio as a
import discord as d
from discord.ext.commands import Bot
from discord.ext.commands import command
from discord.ext.commands import bot_has_permissions
from discord.ext import commands as c
from aiohttp import ClientSession

logfmt = logging.Formatter(
	fmt='{asctime} {invoker}: {message}',
	datefmt='%Y-%m-%dT%H:%M:%SZ',
	style='{'
)

class CustomHandler(logging.Handler):
	def emit(self, record):
		print(self.format(record))

handler = CustomHandler()
handler.setFormatter(logfmt)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

client = Bot(description="A testing Discord bot.", command_prefix=";")

class Regexes(object):
	"""Regex commands - Python flavored."""
	def __init__(self, bot):
		self.bot = bot

	@command()
	async def search(self, ctx, pattern, string, flags=None):
		"""Make a Python-flavored regex search! All groups are shown."""
		logger.info('Regexes.search: \"' + '\" \"'.join((pattern, string, flags)) + '\"', extra={'invoker': ctx.message.author.name})
		if flags is not None:
			exp = '(?' + flags.lower().replace('l', 'L') + ')(?:' + pattern + ')'
		else:
			exp = pattern
		try:
			m = re.search(exp, string)
		except Exception:
			m = False
		if m:
			result = '```\nGroups:\n' + m.group(0) + '\n'
			for group in m.groups():
				result += (group or '') + '\n'
			result += '```'
		elif m is False:
			result = '```\nError in flags or expression.\n```'
		else:
			result = '```\nNo match :(\n```'
		await ctx.send(result)

	@command()
	async def findall(self, ctx, pattern, string, flags=None):
		"""Use a Python-flavor regex to find all occurences of a pattern!"""
		logger.info('Regexes.findall: \"' + '\" \"'.join((pattern, string, flags)) + '\"', extra={'invoker': ctx.message.author.name})
		if flags is not None:
			exp = '(?' + flags.lower().replace('l', 'L') + ')(?:' + pattern + ')'
		else:
			exp = pattern
		gen = re.finditer(exp, string)
		result = '```\nResults:\n'
		try:
			for m in gen:
				result += m.group(0) + ('\t' if len(m.groups()) > 0 else '') + '\t'.join(m.groups()) + '\n'
		except Exception:
			result += 'Error in flags or expression.\n'
		if result == '```\nResults:\n':
			result += 'No results :(\n'
		if '\t' in result:
			ms = re.finditer('([^\t\n]*\t)+[^\t\n]*\n?', result)
			ms = [len(m.group(0).strip().split('\t')) for m in ms]
			ms = max(ms)
			result = result[:13] \
				 + '\t'.join(['Gp{}'.format(i) for i in range(ms-1)]) \
				 + '\n' + result[13:]
		result += '```'
		await ctx.send(result)

client.add_cog(Regexes(client))

DGHANGMANSHANPES = [
	'```\n_\n\n\n\n_```',
	'```\n_\n\n\n\u2500\u2500\u2500\u2500\u2500\n```',
	'```\n\u250c\u2500\u2500\u2500\u2510\n\u2502\n\u2502\n\u2502\n\u2514\u2500\u2500\u2500\u2500\n```',
	'```\n\u250c\u2500\u2500\u2500\u2510\n\u2502   O\n\u2502\n\u2502\n\u2514\u2500\u2500\u2500\u2500\n```',
	'```\n\u250c\u2500\u2500\u2500\u2510\n\u2502   O\n\u2502  /\n\u2502\n\u2514\u2500\u2500\u2500\u2500\n```',
	'```\n\u250c\u2500\u2500\u2500\u2510\n\u2502   O\n\u2502  / \\\n\u2502\n\u2514\u2500\u2500\u2500\u2500\n```',
	'```\n\u250c\u2500\u2500\u2500\u2510\n\u2502   O\n\u2502  /|\\\n\u2502\n\u2514\u2500\u2500\u2500\u2500\n```',
	'```\n\u250c\u2500\u2500\u2500\u2510\n\u2502   O\n\u2502  /|\\\n\u2502  /\n\u2514\u2500\u2500\u2500\u2500\n```',
	'```\n\u250c\u2500\u2500\u2500\u2510\n\u2502   O\n\u2502  /|\\\n\u2502  / \\\n\u2514\u2500\u2500\u2500\u2500\n```'
]

class Games(object):
	def __init__(self, bot):
		self.bot = bot

	@command()
	async def numguess(self, ctx):
		"""Play a fun number-guessing game!"""
		logger.info('Games.numguess', extra={'invoker': ctx.message.author.name})
		guess = None
		limDn = 0
		limUp = 100
		tries = 7
		secret = random.randint(1, 100)
		await ctx.send("""Arr! I'm the Dread Pirate Roberts, and I have a secret!
It's a number from {} to {}. I'll give you {} tries.
Send a number to guess it.""".format(limDn, limUp, tries))
		while guess != secret and tries > 0:
			await ctx.send("What's yer guess, matey?")
			result = ''
			guess = await ctx.bot.wait_for('message',
				check=lambda m: m.channel == ctx.channel and re.match('[0-9]+', m.content))
			guess = int(guess.content)
			if guess == secret:
				break
			elif guess < limDn or guess > limUp:
				result += "Out of range, ye swab!\n"
			elif guess < secret:
				result += "Too low, ye scurvy dog!\n"
				limDn = guess
			elif guess > secret:
				result += "Too high, landlubber!\n"
				limUp = guess
			tries -= 1
			result += "Yer range is {} to {}; ye have {} tries left.".format(limDn, limUp, tries)
			await ctx.send(result)
		if guess == secret:
			await ctx.send("Avast! Ye got it! Found my secret, ye did! With {} tries left!".format(tries))
		else:
			await ctx.send("No more tries, matey! Better luck next time! The secret number was {}.".format(secret))

	@staticmethod
	def substrs(sub, string):
		last_found = -1
		while 1:
			last_found = string.find(sub, last_found + 1)
			if last_found == -1:
				break
			yield last_found

	channels_occupied = set()

	@command()
	async def hangman(self, ctx):
		"""Yes, it's hangman!

		Use this first in the server, to start the game in that channel;
		Next, send the word in a DM with the bot, to set it.
		Once that's been done, guess a letter by sending it.
		"""
		logger.info('Games.hangman', extra={'invoker': ctx.message.author.name})
		if ctx.channel in self.channels_occupied:
			return await ctx.send("There is already a game going on in this channel!")
		self.channels_occupied.add(ctx.channel)
		await ctx.send("Awaiting DM with word...")
		WORD = await ctx.bot.wait_for('message',
			check=lambda m: isinstance(m.channel, d.DMChannel) and m.author == ctx.message.author)
		WORD = WORD.content.lower()
		letters = ['_'] * len(WORD)
		lowers = (
			'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
			'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
			'u', 'v', 'w', 'x', 'y', 'z'
		)
		for i in range(len(WORD)):
			if WORD[i] not in lowers:
				letters[i] = WORD[i]
		missed = []
		shanpe = 0
		await ctx.send(DGHANGMANSHANPES[shanpe] + '\n' + 'Missed:\nGotten: `' + "".join(letters) + '`')
		while "".join(letters) != WORD and shanpe < len(DGHANGMANSHANPES) - 1:
			letter = (await ctx.bot.wait_for('message',
				check=lambda m: m.channel == ctx.channel and m.content in lowers)).content
			if WORD.find(letter) != -1:
				for i in self.substrs(letter, WORD):
					letters[i] = letter
			else:
				if letter not in missed:
					missed.append(letter)
					shanpe += 1
			await ctx.send(DGHANGMANSHANPES[shanpe] + '\nMissed: ' + ','.join(missed) + '\nGotten: `' + "".join(letters) + '`')
		if "".join(letters) == WORD:
			await ctx.send('Congratulations! You have guessed the complete word!')
		else:
			await ctx.send('You lost! The word was \"{}\".'.format(WORD))
		self.channels_occupied.remove(ctx.channel)

	@command()
	@bot_has_permissions(manage_messages=True)
	async def localhangman(self, ctx):
		"""Hangman completely within one channel!

		Use this in the channel to start the game there,
		send the word to set it,
		then send letters to guess them.
		"""
		logger.info('Games.localhangman', extra={'invoker': ctx.message.author.name})
		if ctx.channel in self.channels_occupied:
			await ctx.send('There is already a game going on in this channel!')
		self.channels_occupied.add(ctx.channel)
		await ctx.send('Awaiting DM with word...')
		msg = await ctx.bot.wait_for('message',
			check=lambda m: isinstance(m.channel, d.DMChannel) and m.author == ctx.author)
		WORD = msg.content.lower()
		letters = ['_'] * len(WORD)
		lowers = (
			'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
			'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
			'w', 'x', 'y', 'z'
		)
		for i in range(len(WORD)):
			if WORD[i] not in lowers:
				letters[i] = WORD[i]
		missed = []
		shanpe = 0
		status = await ctx.send(DGHANGMANSHANPES[shanpe] + '\nMissed: ' + ', '.join(missed) + '\nGotten: `' + "".join(letters) + '`')
		while "".join(letters) != WORD and shanpe < len(DGHANGMANSHANPES) - 1:
			guess = await ctx.bot.wait_for('message',
				check=lambda m: m.channel == ctx.channel and m.content in lowers)
			letter = guess.content
			await guess.delete()
			if WORD.find(letter) != -1:
				for i in self.substrs(letter, WORD):
					letters[i] = letter
			else:
				if letter not in missed:
					missed.append(letter)
					shanpe += 1
			await status.edit(content=(DGHANGMANSHANPES[shanpe] + '\nMissed: ' + ', '.join(missed) + '\nGotten: `' + "".join(letters) + '`'))
		if "".join(letters) == WORD:
			await ctx.send('Congratulations! You have guessed the complete word!')
		else:
			await ctx.send('You lost! The word was \"{}\".'.format(WORD))
		self.channels_occupied.remove(ctx.channel)

	@localhangman.error
	async def on_localhangman_err(self, ctx, error):
		logger.error('Games.localhangman failed: ' + str(error), extra={'invoker': ctx.message.author.name})
		if isinstance(error, c.BotMissingPermissions):
			await ctx.send(str(error))

client.add_cog(Games(client))

SESH = None

class Wiki(object):
	def __init__(self, bot):
		self.bot = bot

	@staticmethod
	async def req(params):
		params['format'] = 'json'
		async with SESH.get('https://en.scratch-wiki.info/w/api.php', params=params) as resp:
			return await resp.json()

	@command()
	async def page(self, ctx, *, title):
		"""Get the contents of a page."""
		logger.info('Wiki.page: ' + title, extra={'invoker': ctx.message.author.name})
		async with ctx.channel.typing():
			try:
				content = await self.req({
					'action': 'query',
					'prop': 'revisions',
					'titles': title,
					'rvlimit': '1',
					'rvprop': 'content',
				})
			except Exception:
				await ctx.send('Fetching content failed. The page is likely too large. Sorry!')
				return
			content = list(content['query']['pages'].values())[0]['revisions'][0]['*']
			content = content.splitlines()
			contents = ['```\n']
			i = 0
			for line in content:
				contents[i] += line + '\n'
				if len(contents[i]) + 3 > 2000:
					contents.append('```')
					contents[i], contents[i+1] = contents[i].rsplit('\n', 1)
					contents[i] += '```'
					i += 1
					contents[i] = '```\n' + contents[i]
			contents[-1] += '```'
			for msg in contents:
				await ctx.send(msg)

	@command()
	async def recentchanges(self, ctx, limit=50):
		"""Get recent changes on the Wiki."""
		logger.info('Wiki.recentchanges: ' + str(limit), extra={'invoker': ctx.message.author.name})
		twenties, limit = divmod(limit, 20)
		async with ctx.channel.typing():
			result = ['']
			changes = []
			start = 'now'
			for i in [20 for j in range(twenties)] + [limit]:
				resp = await self.req({
					'action': 'query',
					'list': 'recentchanges',
					'rcprop': 'user|timestamp|comment|title|sizes|flags',
						'rctype': 'edit|new',
					'rclimit': i,
					'rcstart': start
				})
				changes.extend(resp['query']['recentchanges'])
				start = resp['query']['recentchanges'][-1]['timestamp']
			i = 0
			for ch in changes:
				change = '\n'
				change += ch['timestamp']
				change += ': '
				change += ch['title']
				change += '; '
				sizechange = ch['newlen'] - ch['oldlen']
				if sizechange <= -500 or sizechange >= 500:
					change += '**'
				change += '('
				if sizechange <= 0:
					change += str(sizechange)
				if sizechange > 0:
					change += '+' + str(sizechange)
				change += ')'
				if sizechange <= -500 or sizechange >= 500:
					change += '**'
				change += ' . . '
				change += ch['user']
				change += ' _('
				change += ch['comment'].replace('*', '\\*').replace('_', '\\_').replace('`', '\\`')
				change += ')_'
				result[i] += change
				if len(result[i]) > 2000:
					result.append('')
					result[i], result[i+1] = result[i].rsplit('\n', 1)
					i += 1
			for r in result:
				await ctx.send(r)

	@command()
	async def randompage(self, ctx):
		"""Get a link to a random Wiki page!"""
		logger.info('Wiki.randompage', extra={'invoker': ctx.message.author.name})
		rn = await self.req({
			'action': 'query',
			'list': 'random',
			'rnlimit': '1',
			'rnnamespace': '0'
		})
		title = rn['query']['random'][0]['title']
		title = title.replace(' ', '_').capitalize()
		title = quote(title, safe='/:')
		await ctx.send('https://en.scratch-wiki.info/wiki/' + title)

client.add_cog(Wiki(client))

class Scratch(object):
	def __init__(self, bot):
		self.bot = bot

	@staticmethod
	async def req(url):
		async with SESH.get(url) as resp:
			if resp.status >= 400:
				return None
			else:
				return await resp.text()

	@command()
	async def randomproject(self, ctx):
		"""Get a random project link!"""
		logger.info('Scratch.randomproject', extra={'invoker': ctx.message.author.name})
		async with ctx.channel.typing():
			count = json.loads(await self.req('https://api.scratch.mit.edu/projects/count/all'))['count']
			comments = None
			while comments is None:
				pid = random.randint(1, count)
				comments = await self.req('https://scratch.mit.edu/site-api/comments/project/' + str(pid))
			await ctx.send('https://scratch.mit.edu/projects/' + str(pid))

	@command()
	async def messagecount(self, ctx, name=None):
		"""How many messages do you have on Scratch?"""
		async with ctx.channel.typing():
			username = name
			if username is None:
				username = ctx.message.author.name
			resp = await self.req('https://api.scratch.mit.edu/users/' + username + '/messages/count')
			if resp is None and name is None:
				username = getattr(ctx.message.author, 'nick', '_')
				resp = await self.req('https://api.scratch.mit.edu/users/' + username + '/messages/count')
			logger.info('Scratch.messagecount: ' + username, extra={'invoker': ctx.message.author.name})
			if resp is None:
				await ctx.send("Couldn't get message count for " + username)
			else:
				await ctx.send('{} has {} messages'.format(
					username,
					json.loads(resp)['count']
				))

	@command()
	async def news(self, ctx):
		"""Get Scratch news."""
		logger.info('Scratch.news', extra={'invoker': ctx.message.author.name})
		content = await self.req('https://api.scratch.mit.edu/news')
		content = json.loads(content)
		for new in content[:5]:
			await ctx.send(
				'**' + new['headline'] + '**'
				+ '\n' + new['copy'] + '\n' + new['url']
			)

client.add_cog(Scratch(client))

@client.event
async def on_ready(*_, **__):
	global SESH
	logger.info('Ready!', extra={'invoker': '(core)'})
	SESH = ClientSession()
	await client.change_presence(game=d.Game(name=';help'))

@client.command()
async def repeat(ctx, *, arg):
	"""Repeat what you say, right back at ya."""
	logger.info('repeat: ' + arg, extra={'invoker': ctx.message.author.name})
	await ctx.send(arg)

@client.command()
async def hello(ctx):
	"""Test whether the bot is running! Simply says "Hello World!"."""
	logger.info('Hello World!', extra={'invoker': ctx.message.author.name})
	await ctx.send('Hello World!')

@client.command()
async def hmmst(ctx):
	"""hmmst"""
	logger.info('hmmst', extra={'invoker': ctx.message.author.name})
	await ctx.send('hmmst')

DGBANSERVERID = 328938947717890058
#DGBANSERVERID = 337100820371996675

@client.command()
@bot_has_permissions(ban_members=True, add_reactions=True, read_message_history=True)
async def votetoban(ctx, *, user: d.Member):
	"""Start a vote to ban someone from the server. Abuse results in a ban."""
	logger.info('votetoban: ' + user.mention, extra={'invoker': ctx.message.author.name})
	if ctx.guild.id != DGBANSERVERID:
		return
	for member in ctx.guild.members:
		if (not str(member.status) == 'offline') \
				and ctx.channel.permissions_for(member).administrator:
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
				and not str(m.status) == 'offline',
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
	logger.error('votetoban failed: ' + str(error), extra={'invoker': ctx.message.author.name})
	if isinstance(error, c.BotMissingPermissions):
		await ctx.send(str(error))
	else:
		raise error

print('Defined stuff')

with open('login.txt') as f:
	token = f.read().strip()

client.run(token)
