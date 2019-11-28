import asyncio as a
import discord as d
from discord.ext.commands import command, Cog
from discord.ext.commands import bot_has_permissions
from discord.ext import commands as c
from .i18n import i18n, embed

DGHANGMANSHANPES = [
	'```\n_\n\n\n\n_```',
	'```\n_\n\n\n\u2500\u2500\u2500\u2500\u2500\n```',
	'```\n\u250c\u2500\u2500\u2500\u2510\n\u2502\n\u2502\n\u2502\n\u2514\u2500\
\u2500\u2500\u2500\n```',
	'```\n\u250c\u2500\u2500\u2500\u2510\n\u2502   O\n\u2502\n\u2502\n\u2514\
\u2500\u2500\u2500\u2500\n```',
	'```\n\u250c\u2500\u2500\u2500\u2510\n\u2502   O\n\u2502  /\n\u2502\n\u2514\
\u2500\u2500\u2500\u2500\n```',
	'```\n\u250c\u2500\u2500\u2500\u2510\n\u2502   O\n\u2502  / \\\n\u2502\n\
\u2514\u2500\u2500\u2500\u2500\n```',
	'```\n\u250c\u2500\u2500\u2500\u2510\n\u2502   O\n\u2502  /|\\\n\u2502\n\
\u2514\u2500\u2500\u2500\u2500\n```',
	'```\n\u250c\u2500\u2500\u2500\u2510\n\u2502   O\n\u2502  /|\\\n\u2502  /\n\
\u2514\u2500\u2500\u2500\u2500\n```',
	'```\n\u250c\u2500\u2500\u2500\u2510\n\u2502   O\n\u2502  /|\\\n\u2502  / \
\\\n\u2514\u2500\u2500\u2500\u2500\n```'
]

class Hangman(Cog):
	"""hangman/cog-desc"""
	def __init__(self, bot, db):
		self.bot = bot
		self.db = db

	@staticmethod
	def substrs(sub, string):
		last_found = -1
		while 1:
			last_found = string.lower().find(sub, last_found + 1)
			if last_found == -1:
				break
			yield last_found

	@command(description='hangman/crudehangman-desc')
	@c.check(lambda ctx: \
		ctx.guild \
		and (not ctx.channel.permissions_for(ctx.guild.me).manage_messages)
	)
	async def crudehangman(self, ctx):
		"""hangman/crudehangman-help"""
		res = self.db.execute(
			'SELECT ch_occupied FROM channels WHERE channel_id=?',
			(ctx.channel.id,)
		).fetchone()
		if res is not None and not res['ch_occupied']:
			await ctx.send(embed=embed(ctx,
				title=('error',),
				description=('hangman/crudehangman-occupied',),
				color=0xff0000
			))
			ownerq = await self.bot.is_owner(ctx.author)
			if not ownerq:
				return
		if res is None:
			self.db.execute(
				'INSERT INTO channels (channel_id, ch_occupied) VALUES (?, 1)',
				(ctx.channel.id,)
			)
		else:
			self.db.execute(
				'UPDATE channels SET ch_occupied=1 WHERE channel_id=',
				(ctx.channel.id,)
			)
		await ctx.send(embed=embed(ctx,
			title=('hangman/awaiting-dm-title',),
			description=('hangman/awaiting-dm',),
			color=0xffff00
		))
		try:
			msg = await ctx.bot.wait_for('message',
				check=lambda m: \
					isinstance(m.channel, d.DMChannel) \
					and m.author == ctx.author,
				timeout=60.0)
		except a.TimeoutError:
			await ctx.send(embed=embed(ctx,
				title=('hangman/timeout-title',),
				description=('hangman/timeout',),
				color=0xff0000
			))
			return
		WORD = msg.content
		letters = ['_'] * len(WORD)
		lowers = (
			'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
			'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
			'u', 'v', 'w', 'x', 'y', 'z'
		)
		for i in range(len(WORD)):
			if WORD[i].lower() not in lowers:
				letters[i] = WORD[i]
		missed = []
		shanpe = 0
		await ctx.send(embed=embed(ctx,
			title=('hangman/main-title',),
			description=(
				'hangman/main',
				DGHANGMANSHANPES[shanpe], ''
			),
			fields=(
				(('hangman/missed',), 'None', True),
				(('hangman/gotten',), '`{0}`'.format(''.join(letters)), True)
			),
			color=0xfffffe
		))
		while "".join(letters) != WORD and shanpe < len(DGHANGMANSHANPES) - 1:
			try:
				letter = (await ctx.bot.wait_for('message',
					check=lambda m: \
						m.channel == ctx.channel \
						and m.content in lowers,
					timeout=600.0
				)).content
			except a.TimeoutError:
				await ctx.send(embed=embed(ctx,
					title=('hangman/timeout-title',),
					description=('hangman/timeout2',),
					color=0xff0000
				))
				return
			if WORD.lower().find(letter) != -1:
				for i in self.substrs(letter, WORD):
					letters[i] = WORD[i]
			else:
				if letter not in missed:
					missed.append(letter)
					shanpe += 1
			await ctx.send(embed=embed(ctx,
				title=('hangman/main-title',),
				description=(
					'hangman/main', DGHANGMANSHANPES[shanpe], ''
				),
				fields=(
					(('hangman/missed',), i18n(ctx, 'comma-sep').join(missed), True),
					(('hangman/gotten',), '`{0}`'.format(''.join(letters)), True)
				),
				color=0xfffffe
			))
		await ctx.send(embed=embed(ctx,
			title=('hangman/end',),
			description=(
				('hangman/won',)
				if ''.join(letters) == WORD
				else ('hangman/lost', WORD)
			),
			color=0x55acee if ''.join(letters) == WORD else 0xff0000
		))
		self.db.execute(
			'UPDATE channels SET ch_occupied=0 WHERE channel_id=?',
			(ctx.channel.id,)
		)

	@command(description='hangman/hangman-desc')
	@bot_has_permissions(
		manage_messages=True, add_reactions=True, read_message_history=True
	)
	async def hangman(self, ctx):
		"""hangman/hangman-help"""
		REGS = '\U0001f1e6 \U0001f1e7 \U0001f1e8 \U0001f1e9 \U0001f1ea \
\U0001f1eb \U0001f1ec \U0001f1ed \U0001f1ee \U0001f1ef \U0001f1f0 \U0001f1f1 \
\U0001f1f2 \U0001f1f3 \U0001f1f4 \U0001f1f5 \U0001f1f6 \U0001f1f7 \U0001f1f8 \
\U0001f1f9 \U0001f1fa \U0001f1fb \U0001f1fc \U0001f1fd \U0001f1fe \U0001f1ff' \
.split(' ')
		REGS1, REGS2 = REGS[:13], REGS[13:]
		NEIN = '\u274c'
		await ctx.send(embed=embed(ctx,
			title=('hangman/awaiting-dm-title',),
			description=('hangman/awaiting-dm',),
			color=0xffff00
		))
		try:
			msg = await ctx.bot.wait_for('message',
				check=lambda m: \
					isinstance(m.channel, d.DMChannel) \
					and m.author == ctx.author,
				timeout=60.0)
		except a.TimeoutError:
			await ctx.send(embed=embed(ctx,
				title=('hangman/timeout-title',),
				description=('hangman/timeout',),
				color=0xff0000
			))
			return
		WORD = msg.content
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
			if WORD[i].lower() not in lowers:
				letters[i] = WORD[i]
		missed = []
		shanpe = 0
		status = await ctx.send(embed=embed(ctx,
			title=('hangman/main-title',),
			description=(
				'hangman/main',
				DGHANGMANSHANPES[shanpe],
				'**{0}**\n'.format(i18n(ctx, 'hangman/wait'))
			),
			fields=(
				(('hangman/missed',), 'None', True),
				(('hangman/gotten',), '`{0}`'.format(''.join(letters)), True)
			),
			color=0xfffffe
		))
		reactionmsg1 = await ctx.send('_ _')
		reactionmsg2 = await ctx.send('_ _')
		await status.add_reaction(NEIN)
		async def regs1():
			for reg in REGS1:
				await reactionmsg1.add_reaction(reg)
		async def regs2():
			for reg in REGS2:
				await reactionmsg2.add_reaction(reg)
		await a.gather(regs1(), regs2())
		await status.edit(embed=embed(ctx,
			title=('hangman/main-title',),
			description=(
				'hangman/main',
				DGHANGMANSHANPES[shanpe], ''
			),
			fields=(
				(('hangman/missed',), 'None', True),
				(('hangman/gotten',), '`{0}`'.format(''.join(letters)), True)
			),
			color=0xfffffe
		))
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
				await status.edit(embed=embed(ctx,
					title=('hangman/timeout-title',),
					description=('hangman/timeout2',),
					color=0xff0000
				))
				await status.clear_reactions()
				await reactionmsg1.delete()
				await reactionmsg2.delete()
				return
			if str(reaction) == NEIN:
				if user.id == ctx.author.id:
					await status.edit(embed=embed(ctx,
						title=('games/game-cancelled-title',),
						description=('games/game-cancelled',),
						color=0xff0000
					))
					await status.clear_reactions()
					await reactionmsg1.delete()
					await reactionmsg2.delete()
					return
				else:
					continue
			else:
				letter = translate[str(reaction)]
			await reaction.message.remove_reaction(reaction, user)
			if WORD.lower().find(letter) != -1:
				for i in self.substrs(letter, WORD):
					letters[i] = WORD[i]
			else:
				if letter not in missed:
					missed.append(letter)
					shanpe += 1
			await status.edit(embed=embed(ctx,
				title=('hangman/main-title',),
				description=(
					'hangman/main', DGHANGMANSHANPES[shanpe], ''
				),
				fields=(
					(('hangman/missed',), i18n(ctx, 'comma-sep').join(missed) or '\1', True),
					(('hangman/gotten',), '`{0}`'.format(''.join(letters)), True)
				),
				color=0xfffffe
			))
		await ctx.send(embed=embed(ctx,
			title=('hangman/end',),
			description=(
				('hangman/won',)
				if ''.join(letters) == WORD
				else ('hangman/lost', WORD)
			),
			color=0x55acee if ''.join(letters) == WORD else 0xff0000
		))
