import re
import random
import asyncio as a
from discord.ext.commands import command
from .i18n import i18n

class Numguess(object):
	@command()
	async def numguess(self, ctx):
		"""Play a fun number-guessing game!"""
		guess = None
		limDn = 0
		limUp = 100
		tries = 7
		secret = random.randint(1, 100)
		await ctx.send(i18n(ctx, 'numguess/numguess-intro', limDn, limUp, tries))
		while guess != secret and tries > 0:
			await ctx.send(i18n(ctx, 'numguess/numguess-guess'))
			result = ''
			try:
				guess = await ctx.bot.wait_for('message',
					check=lambda m: (
						m.channel == ctx.channel
						and re.match('^[0-9]+$', m.content)
					),
					timeout=60.0)
			except a.TimeoutError:
				await ctx.send(i18n(ctx, 'numguess/numguess-timeout', 60))
				return
			guess = int(guess.content)
			if guess == secret:
				break
			elif guess < limDn or guess > limUp:
				result += i18n(ctx, 'numguess/numguess-oor')
			elif guess < secret:
				result += i18n(ctx, 'numguess/numguess-low')
				limDn = guess
			elif guess > secret:
				result += i18n(ctx, 'numguess/numguess-high')
				limUp = guess
			tries -= 1
			result += i18n(ctx, 'numguess/numguess-range', limDn, limUp, tries)
			await ctx.send(result)
		if guess == secret:
			await ctx.send(i18n(ctx, 'numguess/numguess-correct', tries))
		else:
			await ctx.send(i18n(ctx, 'numguess/numguess-oot', secret))
