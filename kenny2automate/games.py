import asyncio
import discord
from discord.ext.commands import Cog, command
from .i18n import i18n, embed
from .utils import DummyCtx

class Games(Cog):
	def __init__(self, bot, db):
		self.bot = bot
		self.db = db

	def cog_check(self, ctx):
		try:
			me = ctx.guild.me
		except AttributeError: #not in guild
			me = ctx.channel.me
		perms = ctx.channel.permissions_for(me)
		return all((
			perms.add_reactions,
			perms.read_message_history
		))

	_global_games = {}

	# These must be defined in subclasses
	@property
	def name(self) -> str:
		"""self.name of the game."""
		raise NotImplementedError

	@property
	def maxim(self) -> int:
		"""Number of players needed to automatically start the game.
		If inf, game will only start manually.
		Do not set this to inf and scn to None!
		"""
		return 2

	@property
	def minim(self) -> int:
		"""Number of players needed to start the game at all."""
		return 2

	@property
	def scn(self) -> str:
		"""Command to start the game.
		If None, game will only start when maxim is reached.
		"""
		return None

	@property
	def jcn(self) -> str:
		"""Command to join the game."""
		return None

	@property
	def singleton(self) -> bool:
		"""Whether this game is only 1 per user."""
		return False

	@property
	def help(self) -> str:
		"""Extended help for question mark reaction.
		If this is a callable, it is awaited to send help.
		"""
		return None

	async def _join_global_game(self, ctx, coro):
		assert self.maxim >= self.minim
		res = self.db.execute(
			'SELECT user_id FROM users WHERE user_id=?',
			(ctx.author.id,)
		).fetchone()
		if res is None:
			self.db.execute(
				'INSERT INTO users (user_id) VALUES (?)',
				(ctx.author.id,)
			)
		if not ctx.author.dm_channel:
			await ctx.author.create_dm()
		if self.singleton:
			res = self.db.execute(
				'SELECT games_games FROM users WHERE user_id=?',
				(ctx.author.id,)
			).fetchone()[0] #row can't not be present, we inserted it already
			if res is not None:
				legames = set(res.split(','))
				if self.name in legames:
					await ctx.author.send(embed=embed(ctx,
						title=('error',),
						description=('games/already-playing', self.name),
						color=0xff0000
					))
					return
				legames.add(self.name)
				self.db.execute(
					'UPDATE users SET games_games=? WHERE user_id=?',
					(','.join(legames), ctx.author.id)
				)
				del legames
			else: #games_games is NULL
				self.db.execute(
					'UPDATE users SET games_games=? WHERE user_id=?',
					(self.name, ctx.author.id)
				)
		if self.name in self._global_games:
			for c in self._global_games[self.name]['ctxs']:
				if c.author.id == ctx.author.id:
					await ctx.author.send(embed=embed(ctx,
						title=('error',),
						description=('games/already-joined',),
						color=0xff0000
					))
					return
			self._global_games[self.name]['ctxs'].append(ctx)
			startx = self._global_games[self.name]['ctxs'][0]
			ctlen = len(self._global_games[self.name]['ctxs'])
			await startx.author.send(embed=embed(startx,
				title=('games/player-joined-title',),
				description=(
					'games/player-joined',
					max(0, self.minim - ctlen),
					max(0, self.maxim - ctlen)
				),
				color=0x55acee
			))
			if ctlen == self.minim and self.scn is not None:
				await startx.author.send(embed=embed(startx,
					title=('games/enough-players-title',),
					description=('games/enough-players', ctx.prefix + self.scn),
					color=0x55acee
				))
			elif ctlen >= self.maxim:
				return await self._start_global_game(startx)
		else:
			self._global_games[self.name] = {
				'ctxs': [ctx],
				'coro': coro,
				'vote': 0
			}
			if self.jcn is not None:
				coros = []
				for row in self.db.execute(
					'SELECT channel_id FROM channels WHERE games_ping LIKE ?',
					('%{}%'.format(self.name),)
				).fetchall():
					channel = self.bot.get_channel(row[0])
					if channel is None:
						continue
					if channel.id == ctx.channel.id:
						continue
					coros.append(channel.send(embed=embed(
						DummyCtx(
							author=DummyCtx(id=0),
							channel=channel
						),
						title=('games/game-waiting-title',),
						description=('games/game-waiting', self.name, ctx.prefix + self.jcn),
						color=0x55acee
					)))
				for row in self.db.execute(
					'SELECT user_id FROM users WHERE games_ping LIKE ?',
					('%{}%'.format(self.name),)
				).fetchall():
					user = self.bot.get_user(row[0])
					if user is None:
						continue
					if user.id == ctx.author.id:
						continue
					for i in self.bot.guilds:
						member = i.get_member(user.id)
						if member is not None:
							break
					if str(member.status) != 'online':
						continue
					if user.dm_channel is None:
						await user.create_dm()
					coros.append(user.dm_channel.send(embed=embed(
						DummyCtx(
							author=user,
							channel=user.dm_channel
						),
						title=('games/game-waiting-title',),
						description=('games/game-waiting', self.name, ctx.prefix + self.jcn),
						footer=('games/game-waiting-footer', self.name),
						color=0x55acee
					)))
				await asyncio.gather(*coros, return_exceptions=True)
		playercount = len(self._global_games[self.name]['ctxs'])
		owner = self._global_games[self.name]['ctxs'][0]
		if ctx.author.id == owner.author.id:
			footer = None
			if self.minim < self.maxim:
				desc = 'games/joined-owner'
			else:
				desc = 'games/joined-faux-owner'
		else:
			if self.minim > playercount:
				desc = 'games/joined-waiting-missing'
			elif isinstance(self.maxim, int):
				desc = 'games/joined-waiting-minmax'
			else:
				desc = 'games/joined-waiting-nomax'
			if self.scn is not None:
				footer = ('games/vote-to-start', ctx.prefix + self.scn)
			else:
				footer = None
		await ctx.author.send(embed=embed(ctx,
			title=('games/joined', self.name),
			description=(desc, self.name, (
				self.minim
				if self.minim > playercount
				else self.maxim
			) - playercount, owner.author.name
			+ '#' + owner.author.discriminator),
			footer=footer,
			color=0x338acc
		))

	async def _start_global_game(self, ctx):
		if self.name not in self._global_games:
			return
		if len(self._global_games[self.name]['ctxs']) < self.minim:
			await ctx.send(embed=embed(ctx,
				title=('error',),
				description=(
					'games/not-enough-players',
					self.minim, len(self._global_games[self.name]['ctxs'])
				),
				color=0xff0000
			))
			return
		gam = self._global_games[self.name]
		if ctx.author.id != gam['ctxs'][0].author.id:
			gam['vote'] += 1
			if gam['vote'] < len(gam['ctxs']) // 2:
				return await ctx.send(embed=embed(ctx,
					title=('games/voted-title',),
					description=(
						'games/voted',
						self.name,
						len(gam['ctxs']) // 2 - gam['vote']
					),
					color=0x55acee
				))
		coro = gam['coro']
		ctxs = []
		if isinstance(self.maxim, int):
			for i in range(self.maxim):
				try:
					ctxs.append(gam['ctxs'].pop(0))
				except IndexError:
					break
		else:
			ctxs = gam['ctxs'][:]
			gam['ctxs'] = []
		if not len(gam['ctxs']):
			del self._global_games[self.name], gam
		for c in ctxs:
			if not c.author.dm_channel:
				await c.author.create_dm()
		return asyncio.create_task(coro(ctxs))

	async def _unjoin_global_game(self, ctx):
		if self.name not in self._global_games:
			return
		for i, j in enumerate(self._global_games[self.name]['ctxs']):
			if j.author.id == ctx.author.id:
				del self._global_games[self.name]['ctxs'][i]
				break
		if not len(self._global_games[self.name]['ctxs']):
			del self._global_games[self.name]
		await ctx.send(embed=embed(ctx,
			title=('games/unjoined-title',),
			description=('games/unjoined', self.name),
			color=0
		))

	def _kick_global_game(self, user):
		if not isinstance(user, int):
			user = user.id
		res = self.db.execute(
			'SELECT games_games FROM users WHERE user_id=?',
			(user,)
		).fetchone()
		if res is None or res[0] is None:
			return
		legames = set(res[0].split(','))
		legames.discard(self.name)
		self.db.execute(
			'UPDATE users SET games_games=? WHERE user_id=?',
			(','.join(legames), user)
		)

	def _done_global_game(self, users):
		for i, u in users:
			if not isinstance(u, int):
				users[i] = u.id
		for u in users:
			self._kick_global_game(u)

	async def _gather_game(self, ctx, against):
		SHAKE, QUESTION = '\U0001f91d\u2753'
		msg = await ctx.send(embed=embed(ctx,
			title=('games/playing', self.name),
			description=(
				'games/ready-player-1', ctx.author.mention, SHAKE
			) if against is None else (
				'games/ready-player-2', ctx.author.mention, against.mention
			),
			color=0x55acee
		))
		player1 = ctx.author
		if against is not None:
			if against.bot:
				await ctx.send(embed=embed(ctx,
					title=('error',),
					description=('games/no-bots',),
					color=0xff0000
				))
				return
			elif against.status == discord.Status.offline:
				await ctx.send(embed=embed(ctx,
					title=('error',),
					description=('games/no-offline',),
					color=0xff0000
				))
				return
		await msg.add_reaction(SHAKE)
		if self.help is not None:
			await msg.add_reaction(QUESTION)
			@self.bot.listen()
			async def on_reaction_add(reaction, user):
				if all((
					reaction.emoji == QUESTION,
					reaction.message.id == msg.id,
					not user.bot
				)):
					if not user.dm_channel:
						await user.create_dm()
					dmx = DummyCtx(author=user, channel=user.dm_channel)
					await user.dm_channel.send(embed=self.help(dmx)
						if callable(self.help)
						else embed(dmx,
							title=('games/help-title', self.name),
							description=(self.help,),
							color=0x55acee
						)
					)
		def clear_listener():
			if self.help is not None:
				self.bot.remove_listener(on_reaction_add)
		if against is None:
			try:
				reaction, user = await self.bot.wait_for('reaction_add',
					check=lambda r, u: \
						r.emoji == SHAKE \
						and r.message.id == msg.id \
						and u.id != self.bot.user.id \
						and r.message.channel == ctx.channel,
					timeout=60.0
				)
			except asyncio.TimeoutError:
				await msg.edit(
					embed=embed(ctx,
						title=('games/game-timeout-title',),
						description=('games/game-timeout', 60),
						color=0xff0000
					)
				)
				await msg.clear_reactions()
				clear_listener()
				return
			if user.id == ctx.author.id:
				await ctx.send(embed=embed(ctx,
					title=('games/game-cancelled-title',),
					description=('games/game-cancelled',),
					color=0xff0000
				))
				clear_listener()
				return
			player2 = user
			del reaction, user
		else:
			try:
				reaction, user = await self.bot.wait_for('reaction_add',
					check=lambda r, u: \
						r.emoji == SHAKE \
						and r.message.id == msg.id \
						and u.id in (against.id, ctx.author.id) \
						and r.message.channel == ctx.channel,
					timeout=60.0
				)
			except asyncio.TimeoutError:
				await msg.edit(
					embed=embed(ctx,
						title=('games/game-timeout-title',),
						description=('games/unready-player-2', 60),
						color=0xff0000
					)
				)
				await msg.clear_reactions()
				clear_listener()
				return
			if user.id == ctx.author.id:
				await ctx.send(embed=embed(ctx,
					title=('games/game-cancelled-title',),
					description=('games/game-cancelled',),
					color=0xff0000
				))
				clear_listener()
				return
			player2 = user
			del reaction, user
		if not player1.dm_channel:
			await player1.create_dm()
		if not player2.dm_channel:
			await player2.create_dm()
		clear_listener()
		return (player1, player2)

	async def _gather_multigame(self, ctx):
		SHAKE, CHECK, QUESTION = '\U0001f91d\u2705\u2753'
		msg = await ctx.send(embed=embed(ctx,
			title=('games/playing', self.name),
			description=(
				'games/ready-player-3', ctx.author.mention,
				SHAKE, CHECK
			),
			color=0x55acee
		))
		players = [ctx.author]
		await msg.add_reaction(SHAKE)
		await msg.add_reaction(CHECK)
		if self.help is not None:
			await msg.add_reaction(QUESTION)
			@self.bot.listen()
			async def on_reaction_add(reaction, user):
				if all((
					reaction.emoji == QUESTION,
					reaction.message.id == msg.id,
					not user.bot
				)):
					if not user.dm_channel:
						await user.create_dm()
					dmx = DummyCtx(author=user, channel=user.dm_channel)
					await user.dm_channel.send(embed=self.help(dmx)
						if callable(self.help)
						else embed(dmx,
							title=('games/help-title', self.name),
							description=(self.help,),
							color=0x55acee
						)
					)
		def clear_listener():
			if self.help is not None:
				self.bot.remove_listener(on_reaction_add)
		try:
			reaction, user = await self.bot.wait_for('reaction_add',
				check=lambda r, u: \
					r.emoji in (CHECK, SHAKE) \
					and r.message.id == msg.id \
					and u.id == ctx.author.id,
				timeout=60.0
			)
			if reaction.emoji == SHAKE:
				await ctx.send(embed=embed(ctx,
					title=('games/game-cancelled-title',),
					description=('games/game-cancelled',),
					color=0xff0000
				))
				clear_listener()
				return
		except asyncio.TimeoutError:
			pass
		msg = await ctx.get_message(msg.id)
		for r in msg.reactions:
			if r.emoji == SHAKE:
				async for u in r.users():
					if u.id != self.bot.user.id:
						players.append(u)
				break
		for player in players:
			if not player.dm_channel:
				await player.create_dm()
		clear_listener()
		return players

	async def _game(self, ctx, against, coro1, coro2, **kwargs):
		player1, player2 = await self._gather_game(ctx, against)
		qyoo = asyncio.Queue()
		await asyncio.gather(
			coro1(ctx, player1, qyoo, **kwargs),
			coro2(ctx, player2, qyoo, **kwargs)
		)

	@staticmethod
	def unblock_me(qyoo):
		try:
			qyoo.get_nowait()
			qyoo.task_done()
		except asyncio.QueueEmpty:
			pass
	@staticmethod
	async def snr(qyoo, data, whoami):
		if whoami == 1:
			qyoo.put_nowait(data)
			await qyoo.join()
			data2 = await qyoo.get()
			qyoo.task_done()
		else:
			data2 = await qyoo.get()
			qyoo.task_done()
			qyoo.put_nowait(data)
			await qyoo.join()
		return data2

@command(description='games/players-desc')
async def players(ctx, *, game: str):
	game = game.title()
	if game not in Games._global_games:
		return await ctx.send(embed=embed(ctx,
			title=('error',),
			description=('games/no-such-game', game),
			footer=('games/possibly-such-game',),
			color=0xff0000
		))
	await ctx.author.send(embed=embed(ctx,
		title=('games/players-title', game),
		description=i18n(ctx, 'comma-sep').join(
			i.author.name + '#' + i.author.discriminator
			for i in Games._global_games[game]['ctxs']
		) or ('none',),
		color=0x55acee
	))
