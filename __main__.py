import sys
import re
import os
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
import aiohttp

DGOWNERID = 329097918181146625

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

client = Bot(description="A testing Discord bot.", command_prefix=";")

DGDELETEHANDLERS = {}

@client.event
async def on_message_delete(msg):
	if msg.id in DGDELETEHANDLERS:
		await DGDELETEHANDLERS[msg.id](msg)
		del DGDELETEHANDLERS[msg.id]

def add_delete_handler(msg, handler):
	DGDELETEHANDLERS[msg.id] = handler

class Regexes(object):
	"""Regex commands - Python flavored."""
	def __init__(self, bot):
		self.bot = bot

	@command()
	async def search(self, ctx, pattern, string, flags=None):
		"""Make a Python-flavored regex search! All groups are shown."""
		logger.info('Regexes.search: \"' + '\" \"'.join(map(str, (pattern, string, flags))) + '\"', extra={'ctx': ctx})
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
		logger.info('Regexes.findall: \"' + '\" \"'.join(map(str, (pattern, string, flags))) + '\"', extra={'ctx': ctx})
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
		logger.info('Games.numguess', extra={'ctx': ctx})
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
			try:
				guess = await ctx.bot.wait_for('message',
					check=lambda m: m.channel == ctx.channel and re.match('^[0-9]+$', m.content),
					timeout=60.0)
			except a.TimeoutError:
				await ctx.send("Ye landlubberin' swabs didn't guess anythin' for a minute! Ye don't get to play with me no more!")
				return
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
	async def crudehangman(self, ctx):
		"""Hangman for less permissions

		Use this first in the server, to start the game in that channel;
		Next, send the word in a DM with the bot, to set it.
		Once that's been done, guess a letter by sending it.
		"""
		logger.info('Games.crudehangman', extra={'ctx': ctx})
		if ctx.channel in self.channels_occupied:
			await ctx.send("There is already a game going on in this channel!")
			if ctx.author.id != DGOWNERID:
				return
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
	@bot_has_permissions(manage_messages=True, add_reactions=True, read_message_history=True)
	async def hangman(self, ctx):
		"""Hangman!

		Use this in the channel to start the game there,
		DM the bot the word to set it
		then send letters to guess them.
		Requires the "Manage Messages" permission.
		"""
		REGS = '🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯 🇰 🇱 🇲 🇳 🇴 🇵 🇶 🇷 🇸 🇹 🇺 🇻 🇼 🇽 🇾 🇿'.split(' ')
		REGS1, REGS2 = REGS[:13], REGS[13:]
		NEIN = '❌'
		logger.info('Games.hangman', extra={'ctx': ctx})
		await ctx.send('Awaiting DM with word...')
		try:
			msg = await ctx.bot.wait_for('message',
				check=lambda m: isinstance(m.channel, d.DMChannel) and m.author == ctx.author,
				timeout=60.0)
		except a.TimeoutError:
			await ctx.send("The word didn't arrive for a minute! The game has been automatically cancelled.")
			return
		WORD = msg.content.lower()
		letters = ['_'] * len(WORD)
		lowers = (
			'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
			'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
			'w', 'x', 'y', 'z'
		)
		translate = {}
		for regn in range(len(REGS)):
			translate[REGS[regn]] = lowers[regn]
		for i in range(len(WORD)):
			if WORD[i] not in lowers:
				letters[i] = WORD[i]
		missed = []
		shanpe = 0
		status = await ctx.send(DGHANGMANSHANPES[shanpe] + '\nMissed: ' + ', '.join(missed) + '\nGotten: `' + "".join(letters) + '`\n**WAIT DON\'T GUESS YET**')
		reactionmsg1 = await ctx.send('_ _')
		reactionmsg2 = await ctx.send('_ _')
		await status.add_reaction(NEIN)
		for reg in REGS1:
			await reactionmsg1.add_reaction(reg)
		for reg in REGS2:
			await reactionmsg2.add_reaction(reg)
		await status.edit(content=status.content[:-25])
		while "".join(letters) != WORD and shanpe < len(DGHANGMANSHANPES) - 1:
			try:
				reaction, user = await ctx.bot.wait_for(
					'reaction_add',
					check=lambda r, u: \
						r.message.id in (status.id, reactionmsg1.id, reactionmsg2.id) \
						and str(r) in REGS + [NEIN] \
						and u.id != self.bot.user.id,
					timeout=600.0
				)
			except a.TimeoutError:
				await status.edit(content='Nobody guessed a letter for ten minutes! The game has been automatically cancelled.')
				await status.clear_reactions()
				await reactionmsg1.delete()
				await reactionmsg2.delete()
				return
			if str(reaction) == NEIN:
				if user.id == ctx.author.id:
					await status.edit(content='Game cancelled by starter.')
					await status.clear_reactions()
					await reactionmsg1.delete()
					await reactionmsg2.delete()
					return
				else:
					continue
			else:
				letter = translate[str(reaction)]
			await reaction.message.remove_reaction(reaction, user)
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

	@hangman.error
	async def on_hangman_err(self, ctx, error):
		logger.error('Games.hangman failed: ' + str(error), extra={'ctx': ctx})
		if isinstance(error, c.BotMissingPermissions):
			await ctx.send(str(error))

	@command()
	@bot_has_permissions(manage_messages=True, add_reactions=True, read_message_history=True)
	async def connect4(self, ctx, against: d.Member = None):
		"""Play some connect4!

		If you want to play against yourself or you have someone next to you,
		do ;connect4 and mention yourself.
		If you want to play against a specific person, do ;connect4 and mention them.
		"""
		logger.info('Games.connect4', extra={'ctx': ctx})
		BLUE, RED, BLACK, SHAKE, NEIN, DOWN = '🔵 🔴 ⚫ 🤝 ❌ ⬇'.split(' ')
		REGA, REGB, REGC, REGD, REGE, REGF, REGG = REGS = '1⃣ 2⃣ 3⃣ 4⃣ 5⃣ 6⃣ 7⃣'.split(' ')
		msg = await ctx.send(embed=d.Embed(
			title='Playing Connect 4',
			description='Player 1: {}'.format(
				ctx.author.nick or ctx.author.name
			) + (
				'\nReact with {} to join!'.format(SHAKE)
				if against is None
				else (
					'\nPlayer 2: {}'.format(
						ctx.author.nick or ctx.author.name
					)
				) if against.id == ctx.author.id
				else (
					'\nPlayer 2: {}'.format(
						against.nick or against.name
					) + '\nWaiting for Player 2 to join...'
				)
			)
		))
		player1 = ctx.author
		if against is None:
			await msg.add_reaction(SHAKE)
			try:
				reaction, user = await self.bot.wait_for(
					'reaction_add',
					check=lambda r, u: \
						r.emoji == SHAKE \
						and r.message.id == msg.id \
						and u.id != self.bot.user.id \
						and r.message.channel == ctx.channel,
					timeout=60.0
				)
			except a.TimeoutError:
				await msg.edit(content='Nobody joined after a minute! The game has been automatically cancelled.', embed=None)
				await msg.clear_reactions()
				return
			if user.id == ctx.author.id:
				await ctx.send('Game cancelled by starter.')
				return
			player2 = user
			del reaction, user
		elif ctx.author.id == against.id:
			player2 = player1
		elif against.bot:
			await ctx.send("Wait, you can't play against a bot! Game cancelled.")
			return
		elif str(against.status) == 'offline':
			await ctx.send("Wait, Player 2 is offline! Game cancelled.")
			return
		else:
			await msg.add_reaction(SHAKE)
			try:
				reaction, user = await self.bot.wait_for(
					'reaction_add',
					check=lambda r, u: \
						r.emoji == SHAKE \
						and r.message.id == msg.id \
						and u.id in (against.id, ctx.author.id) \
						and r.message.channel == ctx.channel,
					timeout=60.0
				)
			except a.TimeoutError:
				await msg.edit(content="Player 2 didn\'t join after a minute! The game has been automatically cancelled.", embed=None)
				await msg.clear_reactions()
				return
			if user.id == ctx.author.id:
				await ctx.send('Game cancelled by starter.')
				return
			player2 = user
			del reaction, user
		del msg
		board = []
		for i in range(7):
			board.append([])
			for j in range(7):
				board[i].append(BLACK)
		redwon, bluewon = False, False
		def checkwin(board, tile):
			BH = len(board[0])
			BW = len(board)
			#check -
			for y in range(BH):
				for x in range(BW - 3):
					if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
						return True
			#check |
			for x in range(BW):
				for y in range(BH - 3):
					if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
						return True
			#check \
			for x in range(BW - 3):
				for y in range(3, BH):
					if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
						return True
			#check /
			for x in range(BW - 3):
				for y in range(BH - 3):
					if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
						return True
			#all false
			return False

		def constructboard(board, players, whose):
			boardmsgcont = RED + ' = ' + (players[0].nick or players[0].name) + '\n'
			boardmsgcont += BLUE + ' = ' + (players[1].nick or players[1].name) + '\n'
			boardmsgcont += "".join(REGS) + '\n'
			for row in zip(*board):
				for column in row:
					boardmsgcont += column
				boardmsgcont += '\n'
			boardmsgcont += "It is currently {}'s turn".format(players[whose].nick or players[whose].name)
			return boardmsgcont

		boardmsg = await ctx.send('_ _')
		reaction, user = None, None

		while not (redwon or bluewon):
			boardmsgcont = constructboard(board, (player1, player2), 0)
			await boardmsg.edit(embed=d.Embed(
				title="Board",
				description=boardmsgcont,
				color=0xff0000
			))
			if reaction is None:
				await boardmsg.clear_reactions()
				for reg in REGS:
					await boardmsg.add_reaction(reg)
				await boardmsg.add_reaction(DOWN)
			else:
				await boardmsg.remove_reaction(reaction, user)
			reaction = DOWN
			while str(reaction) == DOWN:
				try:
					reaction, user = await self.bot.wait_for(
						'reaction_add',
						check=lambda r, u: \
							(r.message.id == boardmsg.id \
							and str(r) in REGS \
							and str(r) != NEIN \
							and u.id == player1.id) \
							or (r.message.id == boardmsg.id \
							and str(r) == DOWN \
							and u.id in (player1.id, player2.id)),
						timeout=600.0
					)
				except a.TimeoutError:
					await boardmsg.edit(content='Nobody made a move for ten minutes! The game has been cancelled.', embed=None)
					await boardmsg.clear_reactions()
					return
				if str(reaction) == DOWN:
					await boardmsg.delete()
					boardmsg = await ctx.send(embed=d.Embed(
						title="Board",
						description=boardmsgcont,
						color=0xff0000
					))
					for reg in REGS:
						await boardmsg.add_reaction(reg)
					await boardmsg.add_reaction(DOWN)
			idx = REGS.index(str(reaction))
			hit = False
			for rown in range(len(board[idx])):
				if board[idx][rown] != BLACK:
					board[idx][rown-1] = RED
					hit = True
					break
			if not hit:
				board[idx][-1] = RED
			if board[idx].count(BLACK) == 0:
				REGS[idx] = NEIN
			redwon, bluewon = checkwin(board, RED), checkwin(board, BLUE)
			if redwon or bluewon:
				break
			boardmsgcont = constructboard(board, (player1, player2), 1)
			await boardmsg.edit(embed=d.Embed(
				title="Board",
				description=boardmsgcont,
				color=0x55acee
			))
			await boardmsg.remove_reaction(reaction, user)
			reaction = DOWN
			while str(reaction) == DOWN:
				try:
					reaction, user = await self.bot.wait_for(
						'reaction_add',
						check=lambda r, u: \
							(r.message.id == boardmsg.id \
							and str(r) in REGS \
							and str(r) != NEIN \
							and u.id == player2.id) \
							or (r.message.id == boardmsg.id \
							and str(r) == DOWN \
							and u.id in (player1.id, player2.id)),
						timeout=600.0
					)
				except a.TimeoutError:
					await boardmsg.edit(content='Nobody made a move for ten minutes! The game has been cancelled.', embed=None)
					await boardmsg.clear_reactions()
					return
				if str(reaction) == DOWN:
					await boardmsg.delete()
					boardmsg = await ctx.send(embed=d.Embed(
						title="Board",
						description=boardmsgcont,
						color=0x55acee
					))
					for reg in REGS:
						await boardmsg.add_reaction(reg)
					await boardmsg.add_reaction(DOWN)
			idx = REGS.index(str(reaction))
			hit = False
			for rown in range(len(board[idx])):
				if board[idx][rown] != BLACK:
					board[idx][rown-1] = BLUE
					hit = True
					break
			if not hit:
				board[idx][-1] = BLUE
			if board[idx].count(BLACK) == 0:
				REGS[idx] = NEIN
			redwon, bluewon = checkwin(board, RED), checkwin(board, BLUE)
		boardmsgcont = constructboard(board, (player1, player2), int(bluewon))
		await boardmsg.edit(embed=d.Embed(
			title="Board",
			description=boardmsgcont,
		))
		await ctx.send(embed=d.Embed(
			title="Game Over!",
			description='''
The game is over!
Winner: {} ({})
Loser: {} ({})
'''.format(RED if redwon else BLUE, (player1.nick or player1.name) if redwon else (player2.nick or player2.name),
RED if bluewon else BLUE, (player1.nick or player1.name) if bluewon else (player2.nick or player2.name)),
			color=0xff0000 if redwon else 0x55acee
		))

	@connect4.error
	async def on_connect4_err(self, ctx, error):
		logger.error('Games.connect4 failed: ' + str(error), extra={'ctx': ctx})
		if isinstance(error, c.BotMissingPermissions):
			await ctx.send(str(error))

client.add_cog(Games(client))

class Wiki(object):
	def __init__(self, bot):
		self.bot = bot

	WIKIS = {
		'de': 'https://scratch-dach.info',
		'en': 'https://en.scratch-wiki.info',
		'id': 'https://scratch-indo.info',
		'nl': 'https://nl.scratch-wiki.info',
		'hu': 'https://hu.scratch-wiki.info',
		'ru': 'https://scratch-ru.info',
		'fr': 'https://fr.scratch-wiki.info',
		'ja': 'https://ja.scratch-wiki.info',
		'test': 'https://test.scratch-wiki.info',
	}

	@staticmethod
	async def req(params, wiki='en'):
		params['format'] = 'json'
		resp = await aiohttp.get(Wiki.WIKIS[wiki] + '/w/api.php', params=params)
		cont = await resp.json()
		resp.close()
		return cont

	@command()
	async def page(self, ctx, *, title):
		"""Get the contents of a page."""
		logger.info('Wiki.page: ' + title, extra={'ctx': ctx})
		async with ctx.channel.typing():
			try:
				content = await self.req({
					'action': 'query',
					'prop': 'revisions',
					'titles': title,
					'rvlimit': '1',
					'rvprop': 'content',
				})
			except Exception as exc:
				logger.error('Fetching page content failed: ' + str(exc), extra={'ctx': DummyCtx(author=DummyCtx(name='Wiki.page'))})
				await ctx.send('Fetching content failed. The page is likely too large. Sorry!')
				return
			content = list(content['query']['pages'].values())[0]['revisions'][0]['*']
			content = content.splitlines()
			contents = ['```html\n']
			i = 0
			for line in content:
				if len(contents[i]) + 11 > 2000:
					contents.append('```html\n')
					temp = contents[i][:1997].rsplit('\n', 1)
					contents[i], contents[i+1] = temp[0], temp[1] + contents[i][1997:]
					contents[i] += '```'
					i += 1
					contents[i] = '```html\n' + contents[i]
				contents[i] += line + '\n'
			contents[-1] += '```'
			for msg in contents:
				await ctx.send(msg)

	@command()
	async def recentchanges(self, ctx, limit=50):
		"""Get recent changes on the Wiki."""
		logger.info('Wiki.recentchanges: ' + str(limit), extra={'ctx': ctx})
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
		logger.info('Wiki.randompage', extra={'ctx': ctx})
		rn = await self.req({
			'action': 'query',
			'list': 'random',
			'rnlimit': '1',
			'rnnamespace': '0'
		})
		title = rn['query']['random'][0]['title']
		title = title.replace(' ', '_')
		title = quote(title, safe='/:')
		await ctx.send('https://en.scratch-wiki.info/wiki/' + title)

	@command()
	async def iwstats(self, ctx):
		"""Get statistics for the international wikis!"""
		logger.info('Wiki.wikistats', extra={'ctx': ctx})
		async with ctx.channel.typing():
			try:
				content = await self.req({
					'action': 'query',
					'prop': 'revisions',
					'titles': 'User:InterwikiBot/International Stats',
					'rvlimit': '1',
					'rvprop': 'content',
				})
			except Exception as exc:
				logger.error('Fetching wiki stats failed: ' + str(exc), extra={'ctx': DummyCtx(author=DummyCtx(name='Wiki.wikistats'))})
				await ctx.send('Fetching stats failed. Oops!')
				return
			content = list(content['query']['pages'].values())[0]['revisions'][0]['*']
		exp = re.compile(r"""\|-
\|(?P<Time>[^\|]+)
\|(?P<Pages>[0-9]+)
\|(?P<Articles>[0-9]+)
\|(?P<Edits>[0-9]+)
\|(?P<Images>[0-9]+)
\|(?P<Users>[0-9]+)
\|(?P<ActiveUsers>[0-9]+)
\|(?P<Admins>[0-9]+)
""")
		for match in re.finditer(r'(?P<cont>==\s*(?P<code>[a-z][a-z])\s*==[\s\S]+?\|\})', content, re.I|re.S):
			embed = d.Embed(
				title='{}wiki Stats'.format(match.group('code')),
				description='Here are stats for the {}wiki.'.format(match.group('code')),
				color=random.randint(0, 0xffffff)
			)
			for fieldtitle, value in list(
					re.finditer(exp, match.group('cont'))
					)[-1].groupdict().items():
				embed.add_field(
					name=re.sub('([a-z])([A-Z])', r'\1 \2', fieldtitle),
					value=value,
					inline=True
				)
			await ctx.send(embed=embed)
			await a.sleep(1)

	@command()
	async def wikistats(self, ctx, wiki):
		"""Get stats for the ``wiki``wiki."""
		async with ctx.channel.typing():
			try:
				data = await self.req({
					'action': 'query',
					'meta': 'siteinfo',
					'siprop': 'statistics'
				}, wiki)
			except Exception as exc:
				logger.error('Fetching wiki stats failed: ' + str(exc), extra={'ctx': DummyCtx(author=DummyCtx(name='Wiki.wikistats'))})
				await ctx.send('Fetching stats failed. You likely specified a nonexistent wiki.')
				return
			data = data['query']['statistics']
			embed = d.Embed(
				title='{}wiki Stats'.format(wiki),
				description='Here are some statistics for the {}wiki.'.format(wiki),
			)
			for fieldtitle, value in data.items():
				embed.add_field(
					name='Active Users' if fieldtitle == 'activeusers' else fieldtitle.title(),
					value=str(value),
				)
			await ctx.send(embed=embed)

async def embedtest(ctx):
	"""Testing embedded content..."""
	embed = d.Embed(
		title='Wiki Statistics',
		description='Here are some Scratch Wiki statistics:'
	)
	embed.add_field(
		name='Test block',
		value='asdf asdf',
		inline=False
	)
	embed.add_field(
		name='Test inline 1',
		value='asdf 1',
	)
	embed.add_field(
		name='Test inline 2',
		value='asdf 2',
	)
	embed.add_field(
		name='Test block 2',
		value='asdf 3',
		inline=False,
	)
	embed.add_field(
		name='Test inline 3',
		value='fdsa',
	)
	embed.add_field(
		name='Test inline 4',
		value='fdsa',
	)
	await ctx.send(embed=embed)

client.add_cog(Wiki(client))

class Scratch(object):
	def __init__(self, bot):
		self.bot = bot

	@staticmethod
	async def req(url):
		resp = await aiohttp.get(url)
		result = None
		if resp.status < 400:
			result = await resp.text()
		resp.close()
		return result

	@command()
	async def randomproject(self, ctx):
		"""Get a random project link!"""
		logger.info('Scratch.randomproject', extra={'ctx': ctx})
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
			if name is not None:
				logger.info('Scratch.messagecount: ' + name, extra={'ctx': ctx})
				resp = await self.req('https://api.scratch.mit.edu/users/' + name + '/messages/count')
				username = name
			else:
				resp = None
				if ctx.author.nick is not None:
					logger.info('Scratch.messagecount: ' + ctx.author.nick, extra={'ctx': ctx})
					resp = await self.req('https://api.scratch.mit.edu/users/' + ctx.author.nick + '/messages/count')
					username = ctx.author.nick
				if resp is None:
					logger.info('Scratch.messagecount: ' + ctx.author.name, extra={'ctx': ctx})
					resp = await self.req('https://api.scratch.mit.edu/users/' + ctx.author.name + '/messages/count')
					username = ctx.author.name
			if resp is None:
				await ctx.send("Couldn't get message count for " + username)
			else:
				await ctx.send('{} has {} message(s)'.format(
					username,
					json.loads(resp)['count']
				))

	@command()
	async def news(self, ctx):
		"""Get Scratch news."""
		logger.info('Scratch.news', extra={'ctx': ctx})
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

DGBANSERVERID = 328938947717890058
#DGBANSERVERID = 337100820371996675

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

WATCHED_FILES_MTIMES = [(f, os.path.getmtime(f)) for f in ('/home/pi/login.txt', __file__)]

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

client.loop.create_task(update_if_changed())
client.run(token)
