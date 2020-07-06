import asyncio
from discord.ext.commands import Cog, command
from .emoji import CHECK, CROSS, SHAKE, QUESTION, MAG
from .i18n import i18n, embed
from .utils import DummyCtx, background
from .dms import needs_dms, check_dms_open

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

	@needs_dms()
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
		await self._base_needs(ctx)
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
		REMATCH = '\U0001f502' # loop with 1 overlay
		STOP = '\N{BLACK SQUARE FOR STOP}'
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

	def _starting(self, ctx):
		background(ctx.send(embed=embed(
			title=('games/game-starting-title',),
			description=('games/game-starting',),
			color=0x55acee
		)))

	@needs_dms(react=False)
	async def _gather_multigame(self, ctx, against = ()):
		msg = await ctx.send(embed=embed(ctx,
			title=('games/playing', self.name),
			description=(
				'games/ready-player-3', ctx.author.mention,
				SHAKE, CHECK
			),
			color=0x55acee
		))
		players = [ctx.author]
		specs = []
		background(msg.add_reaction(SHAKE))
		background(msg.add_reaction(CHECK))
		if self.specs > 0:
			background(msg.add_reaction(MAG))
		if self.help is not None:
			background(msg.add_reaction(QUESTION))
		fut = self.bot.loop.create_future()
		@self.bot.listen()
		async def on_reaction_add(reaction, user):
			if not all((
				reaction.message.id == msg.id,
				not user.bot
			)):
				return
			dmx = DummyCtx(
				send=ctx.send, author=user,
				channel=user.dm_channel
			)
			if reaction.emoji == QUESTION and self.help is not None:
				background(user.send(embed=self.help(dmx)
					if callable(self.help)
					else embed(user,
						title=('games/help-title', self.name),
						description=(self.help,),
						color=0x55acee
					)
				))
			elif reaction.emoji in {SHAKE, MAG}:
				if user.id == ctx.author.id:
					fut.cancel()
				elif await check_dms_open(dmx):
					if reaction.emoji == SHAKE:
						if (
							len(players) < self.maxim
							and (not against or user in against)
						):
							players.append(user)
					elif self.specs > 0 and len(specs) < self.specs:
						specs.append(user)
					if (
						len(players) >= self.maxim
						and (not self.spec or len(specs) >= self.specs)
					):
						fut.set_result(True)
			elif reaction.emoji == CHECK and user.id == ctx.author.id:
				if len(players) >= self.minim:
					fut.set_result(True)
		@self.bot.listen()
		async def on_reaction_remove(reaction, user):
			if not all((
				reaction.message.id == msg.id,
				not user.bot
			)):
				return
			try:
				if reaction.emoji == SHAKE:
					players.remove(user)
				elif reaction.emoji == MAG and self.specs > 0:
					specs.remove(user)
			except ValueError:
				pass # lists can't discard fsr
		def clear_listener():
			self.bot.remove_listener(on_reaction_add)
			self.bot.remove_listener(on_reaction_remove)
		try:
			await asyncio.wait_for(fut, 60.0)
		except asyncio.TimeoutError:
			if len(players) < self.minim:
				background(ctx.send(embed=embed(ctx,
					title=('games/game-cancelled-title',),
					description=('games/game-cancelled',),
					color=0xff0000
				)))
				clear_listener()
				return
		except asyncio.CancelledError:
			background(ctx.send(embed=embed(ctx,
				title=('games/game-cancelled-title',),
				description=('games/game-cancelled',),
				color=0xff0000
			)))
			clear_listener()
			return
		players = [DummyCtx(author=u, send=u.send) for u in players]
		specs = [DummyCtx(author=u, send=u.send) for u in specs]
		clear_listener()
		return (players, specs) if self.specs > 0 else players

	async def _choice(self, user, emb):
		msg = await user.send(embed=emb)
		await msg.add_reaction(CHECK)
		await msg.add_reaction(CROSS)
		reaction, user = await self.bot.wait_for('reaction_add', check=lambda r, u: (
			str(r) in (CHECK, CROSS)
			and r.message.id == msg.id
			and u.id == user.id
		))
		return str(reaction) == CHECK

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
			str(i.author) for i in Games._global_games[game]['ctxs']
		) or ('none',),
		color=0x55acee
	)))
