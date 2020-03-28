import asyncio
import discord
from discord.ext.commands import Cog, command
from .i18n import i18n, embed
from .utils import DummyCtx, background

class Games(Cog):
	def __init__(self, bot, db):
		self.bot = bot
		self.db = db
		if hasattr(self, 'coro'):
			self._global_games[self.name] = {
				'ctxs': [],
				'spec': [],
				'coro': getattr(self, self.coro),
				'vote': 0
			}

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
	def maxim(self) -> (int, float('inf')):
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
	def specs(self) -> (int, float('inf')):
		"""Number of spectators allowed (NOT INCLUDING PLAYERS).

		If greater than 0, unless `spec` is False, the game won't auto-start
		upon hitting maxim, and will instead auto-start upon hitting `specs`
		spectators AND `maxim` players. If the game hits one limit or the other
		but not both, `scn` comes into play, unless `spec` is False, in which
		case `maxim` acts as normal.
		"""
		return 0

	@property
	def spec(self) -> bool:
		"""Whether to wait for maximum spectator capacity
		before auto-starting.
		"""
		return True

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
	def help(self) -> str:
		"""Extended help for question mark reaction.
		If this is a callable, it is awaited to send help.
		"""
		return None

	async def _global_game_created(self, ctx):
		if self.jcn is not None:
			coros = []
			for row in self.db.execute(
				'SELECT channel_id FROM channels WHERE games_ping LIKE ?',
				(f'%{self.name}%',)
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

	async def _base_needs(self, ctx):
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

	async def _join_global_game(self, ctx):
		await self._base_needs(ctx)
		game = self._global_games[self.name]
		for c in game['ctxs'] + game['spec']:
			if c.author.id == ctx.author.id:
				background(ctx.author.send(embed=embed(ctx,
					title=('error',),
					description=('games/already-joined',),
					color=0xff0000
				)))
				return
		if not game['ctxs'] and not game['spec']:
			await self._global_game_created(ctx)
		game['ctxs'].append(ctx)
		startx = game['ctxs'][0]
		ctlen = len(game['ctxs'])
		splen = len(game['spec'])
		if ctlen >= self.maxim and (not self.spec or splen >= self.specs):
			return await self._start_global_game(startx)
		if ctx.author.id != startx.author.id:
			background(startx.author.send(embed=embed(startx,
				title=('games/player-joined-title',),
				description=(
					'games/player-joined',
					max(0, self.minim - ctlen),
					max(0, self.maxim - ctlen)
				),
				color=0x55acee
			)))
		if (ctlen == self.minim or ctlen >= self.maxim) \
				and self.scn is not None:
			background(startx.author.send(embed=embed(startx,
				title=('games/enough-players-title',),
				description=('games/enough-players', ctx.prefix + self.scn),
				color=0x55acee
			)))
		if ctx.author.id == startx.author.id:
			footer = None
			if self.minim < self.maxim:
				desc = 'games/joined-owner'
			else:
				desc = 'games/joined-faux-owner'
		else:
			if self.minim > ctlen:
				desc = 'games/joined-waiting-missing'
			elif isinstance(self.maxim, int) and isinstance(self.specs, int):
				if ctlen >= self.maxim:
					desc = 'games/joined-waiting-specs'
				else:
					desc = 'games/joined-waiting-minmax'
			else:
				desc = 'games/joined-waiting-nomax'
			if self.scn is not None:
				footer = ('games/vote-to-start', ctx.prefix + self.scn)
			else:
				footer = None
		background(ctx.author.send(embed=embed(ctx,
			title=('games/joined', self.name),
			description=(desc, self.name, (
				self.minim
				if self.minim > ctlen
				else (self.maxim if self.maxim > ctlen else self.specs)
			) - (ctlen if self.maxim > ctlen else splen), str(startx.author)),
			footer=footer,
			color=0x338acc
		)))

	async def _spec_global_game(self, ctx):
		if not self.specs > 0:
			return await ctx.send(embed=embed(ctx,
				title=('error',),
				description=('games/no-spectating', self.name),
				color=0xff0000
			))
		await self._base_needs(ctx)
		game = self._global_games[self.name]
		for c in game['spec'] + game['ctxs']:
			if c.author.id == ctx.author.id:
				background(ctx.author.send(embed=embed(ctx,
					title=('error',),
					description=('games/already-spectating',),
					color=0xff0000
				)))
				return
		if not game['ctxs'] and not game['spec']:
			await self._global_game_created(ctx)
		game['spec'].append(ctx)
		try:
			startx = game['ctxs'][0]
		except IndexError: # could be empty game
			startx = ctx # pretend to be starter
		ctlen = len(game['ctxs'])
		splen = len(game['spec'])
		if ctlen >= self.maxim and (not self.spec or splen >= self.specs):
			return await self._start_global_game(startx)
		if ctx.author.id != startx.author.id:
			background(startx.author.send(embed=embed(startx,
				title=('games/player-spectating-title',),
				description=(
					'games/player-spectating',
					max(0, self.minim - ctlen),
					max(0, self.maxim - ctlen)
				),
				color=0x55acee
			)))
		# don't care about minim because that's only for when ctlen changes
		if ctlen >= self.maxim and self.scn is not None:
			background(startx.author.send(embed=embed(startx,
				title=('games/enough-players-title',),
				description=('games/enough-players', ctx.prefix + self.scn),
				color=0x55acee
			)))
		return await ctx.author.send(embed=embed(ctx,
			title=('games/spectating-title', self.name),
			description=('games/spectating',),
			color=0x338acc
		))

	async def _start_global_game(self, ctx):
		game = self._global_games[self.name]
		if self.name not in self._global_games:
			return
		if len(game['ctxs']) < self.minim:
			background(ctx.send(embed=embed(ctx,
				title=('error',),
				description=(
					'games/not-enough-players',
					self.minim, len(game['ctxs'])
				),
				color=0xff0000
			)))
			return
		if ctx.author.id != game['ctxs'][0].author.id:
			game['vote'] += 1
			if game['vote'] < len(game['ctxs']) // 2:
				return background(ctx.send(embed=embed(ctx,
					title=('games/voted-title',),
					description=(
						'games/voted',
						self.name,
						len(game['ctxs']) // 2 - game['vote']
					),
					color=0x55acee
				)))
		coro = game['coro']
		ctxs = game['ctxs']
		if isinstance(self.maxim, int):
			ctxs, game['ctxs'] = ctxs[:self.maxim], ctxs[self.maxim:]
		else:
			game['ctxs'] = []
		specs = game['spec']
		if isinstance(self.specs, int):
			specs, game['spec'] = specs[:self.specs], specs[self.specs:]
		else:
			game['spec'] = []
		await asyncio.gather(*(
			c.author.create_dm()
			for c in ctxs
			if not c.author.dm_channel
		))
		return background(coro(ctxs, specs))

	async def _unjoin_global_game(self, ctx):
		if self.name not in self._global_games:
			return
		for i, j in enumerate(self._global_games[self.name]['ctxs']):
			if j.author.id == ctx.author.id:
				del self._global_games[self.name]['ctxs'][i]
				break
		background(ctx.send(embed=embed(ctx,
			title=('games/unjoined-title',),
			description=('games/unjoined', self.name),
			color=0
		)))

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

	async def _rematch(self, messages, ctxs):
		messages = list(messages)
		ctxs = list(ctxs)
		REMATCH, STOP = '\U0001f502\u23f9'
		await asyncio.gather(*[m.add_reaction(REMATCH) for m in messages],
							 *[m.add_reaction(STOP) for m in messages])
		ts = set()
		def _check(msg, ctx):
			def check(r, u):
				return (
					r.message.id == msg.id
					and u.id == ctx.author.id
					and str(r).startswith((REMATCH, STOP))
				)
			return check
		for msg, ctx in zip(messages, ctxs):
			ts.add(self.bot.wait_for(
				'reaction_add',
				check=_check(msg, ctx)
			))
		for f in asyncio.as_completed(ts):
			r, u = await f
			if str(r).startswith(REMATCH):
				for c in ctxs:
					if c.author.id == u.id:
						ctx = c
						break
				ctxs.remove(ctx)
				await self._join_global_game(ctx)
				for c in ctxs:
					background(c.author.send(embed=embed(c,
						title=('games/player-rematching-title',),
						description=(
							'games/player-rematching',
							str(ctx.author)
						),
						color=0x55acee
					)))
			else:
				await u.send(embed=embed(u,
					title=('games/no-rematch-title',),
					description=('games/no-rematch',),
					color=0x808080
				))
				for c in ctxs:
					if c.author.id == u.id:
						ctxs.remove(c)
						break

	async def _gather_game(self, ctx, against):
		SHAKE, QUESTION, MAG = '\U0001f91d\u2753\U0001f50d'
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
				background(ctx.send(embed=embed(ctx,
					title=('error',),
					description=('games/no-bots',),
					color=0xff0000
				)))
				return
			elif against.status == discord.Status.offline:
				background(ctx.send(embed=embed(ctx,
					title=('error',),
					description=('games/no-offline',),
					color=0xff0000
				)))
				return
		background(msg.add_reaction(SHAKE))
		if self.specs > 0:
			background(msg.add_reaction(MAG))
		if self.help is not None:
			background(msg.add_reaction(QUESTION))
			@self.bot.listen()
			async def on_reaction_add(reaction, user):
				if all((
					reaction.emoji == QUESTION,
					reaction.message.id == msg.id,
					not user.bot
				)):
					dmx = DummyCtx(author=user, channel=user.dm_channel)
					background(user.send(embed=self.help(dmx)
						if callable(self.help)
						else embed(user,
							title=('games/help-title', self.name),
							description=(self.help,),
							color=0x55acee
						)
					))
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
				background(msg.edit(
					embed=embed(ctx,
						title=('games/game-timeout-title',),
						description=('games/game-timeout', 60),
						color=0xff0000
					)
				))
				background(msg.clear_reactions())
				clear_listener()
				return
			if user.id == ctx.author.id:
				background(ctx.send(embed=embed(ctx,
					title=('games/game-cancelled-title',),
					description=('games/game-cancelled',),
					color=0xff0000
				)))
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
				background(msg.edit(
					embed=embed(ctx,
						title=('games/game-timeout-title',),
						description=('games/unready-player-2', 60),
						color=0xff0000
					)
				))
				background(msg.clear_reactions())
				clear_listener()
				return
			if user.id == ctx.author.id:
				background(ctx.send(embed=embed(ctx,
					title=('games/game-cancelled-title',),
					description=('games/game-cancelled',),
					color=0xff0000
				)))
				clear_listener()
				return
			player2 = user
			del reaction, user
		msg = await ctx.fetch_message(msg.id)
		specs = await self._spectators(msg, ctx)
		if not player1.dm_channel:
			background(player1.create_dm())
		if not player2.dm_channel:
			background(player2.create_dm())
		clear_listener()
		return (player1, player2, specs) if self.specs>0 else (player1, player2)

	async def _spectators(self, msg, ctx):
		if self.specs > 0:
			specs = []
			for r in msg.reactions:
				if r.emoji == '\U0001f50d':
					async for u in r.users():
						if u.id != self.bot.user.id:
							specs.append(DummyCtx(author=u))
					break
			return specs
		return None

	async def _gather_multigame(self, ctx):
		SHAKE, CHECK, QUESTION, MAG = '\U0001f91d\u2705\u2753\U0001f50d'
		msg = await ctx.send(embed=embed(ctx,
			title=('games/playing', self.name),
			description=(
				'games/ready-player-3', ctx.author.mention,
				SHAKE, CHECK
			),
			color=0x55acee
		))
		players = [ctx]
		background(msg.add_reaction(SHAKE))
		background(msg.add_reaction(CHECK))
		if self.specs > 0:
			background(msg.add_reaction(MAG))
		if self.help is not None:
			background(msg.add_reaction(QUESTION))
			@self.bot.listen()
			async def on_reaction_add(reaction, user):
				if all((
					reaction.emoji == QUESTION,
					reaction.message.id == msg.id,
					not user.bot
				)):
					dmx = DummyCtx(author=user, channel=user.dm_channel)
					background(user.send(embed=self.help(dmx)
						if callable(self.help)
						else embed(user,
							title=('games/help-title', self.name),
							description=(self.help,),
							color=0x55acee
						)
					))
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
				background(ctx.send(embed=embed(ctx,
					title=('games/game-cancelled-title',),
					description=('games/game-cancelled',),
					color=0xff0000
				)))
				clear_listener()
				return
		except asyncio.TimeoutError:
			pass
		msg = await ctx.fetch_message(msg.id)
		for r in msg.reactions:
			if r.emoji == SHAKE:
				async for u in r.users():
					if u.id != self.bot.user.id:
						players.append(DummyCtx(author=u))
				break
		specs = await self._spectators(msg, ctx)
		await asyncio.gather(*(
			self._base_needs(player)
			for player in players
		))
		clear_listener()
		return (players, specs) if self.specs > 0 else players

	async def _game(self, ctx, against, coro1, coro2, **kwargs):
		player1, player2 = await self._gather_game(ctx, against)
		qyoo = asyncio.Queue()
		background(coro1(ctx, player1, qyoo, **kwargs))
		background(coro2(ctx, player2, qyoo, **kwargs))

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

	async def _choice(self, user, emb):
		msg = await user.send(embed=emb)
		YEA, NAY = '\u2705\u274e'
		await msg.add_reaction(YEA)
		await msg.add_reaction(NAY)
		reaction, user = await self.bot.wait_for('reaction_add', check=lambda r, u: (
			str(r) in (YEA, NAY)
			and r.message.id == msg.id
			and u.id == user.id
		))
		return str(reaction) == YEA

@command(description='games/players-desc')
async def players(ctx, *, game: str):
	game = game.title()
	if game not in Games._global_games:
		return background(ctx.send(embed=embed(ctx,
			title=('error',),
			description=('games/no-such-game', game),
			footer=('games/possibly-such-game',),
			color=0xff0000
		)))
	background(ctx.author.send(embed=embed(ctx,
		title=('games/players-title', game),
		description=i18n(ctx, 'comma-sep').join(
			i.author.name + '#' + i.author.discriminator
			for i in Games._global_games[game]['ctxs']
		) or ('none',),
		color=0x55acee
	)))
