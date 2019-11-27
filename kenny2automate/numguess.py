import re
import random
import asyncio as a
import discord as d
from discord.ext.commands import command, Cog
from .i18n import i18n, embed

class Numguess(Cog):
	"""numguess/cog-desc"""
	@command(description='numguess/numguess-desc')
	async def numguess(self, ctx):
		guess = None
		limDn = 0
		limUp = 100
		tries = 7
		secret = random.randint(1, 100)
		await ctx.send(embed=embed(ctx,
			description=('numguess/numguess-intro', limDn, limUp, tries),
			color=0
		))
		while guess != secret and tries > 0:
			await ctx.send(embed=embed(ctx,
				title=('numguess/numguess-guess-title',),
				description=('numguess/numguess-guess',),
				color=0xffff00
			))
			result = ''
			try:
				guess = await ctx.bot.wait_for('message',
					check=lambda m: (
						m.channel == ctx.channel
						and re.match('^[0-9]+$', m.content)
					),
					timeout=60.0)
			except a.TimeoutError:
				await ctx.send(embed=embed(ctx,
					title=('hangman/timeout',),
					description=('numguess/numguess-timeout', 60),
					color=0xff0000
				))
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
			await ctx.send(embed=d.Embed(description=result, color=0xfffffe))
		await ctx.send(embed=embed(ctx,
			title=('numguess/numguess-end',),
			description=(
				('numguess/numguess-correct', tries)
				if guess == secret
				else ('numguess/numguess-oot', secret)
			),
			color=0x55acee if guess == secret else 0xff0000
		))
