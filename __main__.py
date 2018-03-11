import re
import random
import discord as d
from discord.ext.commands import Bot
from discord.ext.commands import command

client = Bot(description="A testing Discord bot.", command_prefix=";")

class Regexes(object):
	"""Regex commands - Python flavored."""
	def __init__(self, bot):
		self.bot = bot

	@command()
	async def search(self, ctx, pattern, string, flags=None):
		"""Make a Python-flavored regex search! All groups are shown."""
		print('re.search')
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
		print('re.findall')
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
	'```\n\n\n\n\n```',
	'```\n\n\n\n\u2500\u2500\u2500\u2500\u2500\n```',
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
		print("Numguess!")
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

	channels_occupied = []

	@command()
	async def hangman(self, ctx):
		"""Yes, it's hangman!

		Use this first in the server, to start the game in that channel;
		Next, use it in a DM with the bot, to set the word.
		Once that's been done, use ;hm to guess a letter.
		"""
		print("Hangman!")
		if ctx.channel in self.channels_occupied:
			return await ctx.send("There is already a game going on in this channel!")
		self.channels_occupied.append(ctx.channel)
		await ctx.send("Awaiting DM with word...")
		NONALPHABET = ','
		WORD = await ctx.bot.wait_for('message',
			check=lambda m: isinstance(m.channel, d.DMChannel) and m.author == ctx.message.author)
		WORD = re.sub('[^a-zA-Z]', NONALPHABET, WORD.content.lower())
		letters = ['_'] * len(WORD)
		for i in self.substrs(NONALPHABET, WORD):
			letters[i] = NONALPHABET
		missed = []
		shanpe = 0
		await ctx.send(DGHANGMANSHANPES[shanpe] + '\n' + 'Missed:\nGotten: `' + "".join(letters) + '`')
		while "".join(letters) != WORD and shanpe < len(DGHANGMANSHANPES) - 1:
			letter = (await ctx.bot.wait_for('message',
				check=lambda m: m.channel == ctx.channel and re.match('^[a-z]$', m.content))).content
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

client.add_cog(Games(client))

@client.event
async def on_ready(*_, **__):
	await client.change_presence(game=d.Game(name=';help'))

@client.command()
async def repeat(ctx, *, arg):
	"""Repeat what you say, right back at ya."""
	print('Repeating ' + arg)
	await ctx.send(arg)

@client.command()
async def hello(ctx):
	"""Test whether the bot is running! Simply says "Hello World!".
	Also checks permissions.
	"""
	print('Hello World!')
	await ctx.send('Hello World!')

@client.event
async def on_command_error(ctx, err):
	await ctx.send('```Error: {}```'.format(err.args[0]),)

@client.command()
async def hmmst(ctx):
	"""hmmst"""
	print('hmmst')
	await ctx.send('hmmst')

print('Defined stuff')

with open('login.txt') as f:
	token = f.read().strip()

client.run(token)
