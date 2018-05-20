import re
import random
from itertools import accumulate
from bisect import bisect
import asyncio as a
from discord.ext.commands import command
from discord.ext.commands import bot_has_permissions

class Games(object):
	def __init__(self, bot, logger, db):
		self.bot = bot
		self.logger = logger
		self.db = db

	@command()
	async def numguess(self, ctx):
		"""Play a fun number-guessing game!"""
		self.logger.info('Games.numguess', extra={'ctx': ctx})
		guess = None
		limDn = 0
		limUp = 100
		tries = 7
		secret = random.randint(1, 100)
		await ctx.send("Arr! I'm the Dread Pirate Roberts, and I have a secret!\nIt's a number from {} to {}. I'll give you {} tries.\nSend a number to guess it.".format(limDn, limUp, tries))
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

	@bot_has_permissions(manage_messages=True)
	async def memory(self, ctx):
		#raise NotImplementedError('stub')
		EMOJI_RANGES_UNICODE = (
			('\U0001F300', '\U0001F320'),
			('\U0001F330', '\U0001F335'),
			('\U0001F337', '\U0001F37C'),
			('\U0001F380', '\U0001F393'),
			('\U0001F3A0', '\U0001F3C4'),
			('\U0001F3C6', '\U0001F3CA'),
			('\U0001F3E0', '\U0001F3F0'),
			('\U0001F400', '\U0001F43E'),
			('\U0001F440', '\U0001F4F7'),
			('\U0001F4F9', '\U0001F4FC'),
			('\U0001F500', '\U0001F53C'),
			('\U0001F540', '\U0001F543'),
			('\U0001F550', '\U0001F567'),
			('\U0001F5FB', '\U0001F5FF')
		)
		def random_emoji():
			# Weighted distribution
			count = [ord(r[-1]) - ord(r[0]) + 1 for r in EMOJI_RANGES_UNICODE]
			weights = list(accumulate(count))

			# Get one point in ranges
			point = random.randrange(weights[-1])

			# Select correct range
			emridx = bisect(weights, point)
			emr = EMOJI_RANGES_UNICODE[emridx]

			# Calculate index in range
			point_ = point
			if emridx is not 0:
				point_ = point - weights[emridx - 1]

			# Emoji
			emoji = chr(ord(emr[0]) + point_)
			return emoji

		self.logger.info('Games.memory', extra={'ctx': ctx})
		#if self.db.execute('SELECT channel_id FROM mem_channels_occupied WHERE channel_id=?', (ctx.channel.id,)).fetchone() is not None:
		#	await ctx.send("There is already a game going on in this channel!")
		#	ownerq = await self.bot.is_owner(ctx.author)
		#	if not ownerq:
		#		return
		#self.db.execute('INSERT INTO mem_channels_occupied VALUES (?)', (ctx.channel.id,))
		BLACK = '\u2b1b'.split(' ')
		NUMBERS = '1\u20e3 2\u20e3 3\u20e3 4\u20e3 5\u20e3 6\u20e3 7\u20e3 8\u20e3 9\u20e3 \U0001f51f'.split(' ')
		LETTERS = '\U0001f1e6 \U0001f1e7 \U0001f1e8 \U0001f1e9 \U0001f1ea \U0001f1eb \U0001f1ec \U0001f1ed \U0001f1ee \U0001f1ef'.split(' ')
		_emojis_used = []
		_emojis_used_twice = []
		board = []
		for row in range(7):
			board.append([])
			for __ in range(7):
				_em = random_emoji()
				while _em in _emojis_used_twice:
					_em = random_emoji()
					if _em in _emojis_used:
						_emojis_used_twice.append(_em)
					else:
						_emojis_used.append(_em)
				board[row].append(_em)
		del _emojis_used, _emojis_used_twice
		def constructboard(board):
			boardmsg = ''
			for row in board:
				for column in row:
					if column[-1]:
						boardmsg += column[0]
					else:
						boardmsg += BLACK
				boardmsg += '\n'
			return boardmsg
		await ctx.send(constructboard(board))
		#self.db.execute('DELETE FROM mem_channels_occupied WHERE channel_id=?', (ctx.channel.id,))