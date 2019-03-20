import asyncio as a
import discord as d
from discord.ext.commands import Cog
from .i18n import embed
from .utils import DummyCtx

class Games(Cog):
	def __init__(self, bot, db):
		self.bot = bot
		self.db = db

	def cog_check(self, ctx):
		perms = ctx.channel.permissions_for(self.bot.user)
		return all(
			perms.manage_messages,
			perms.add_reactions,
			perms.read_message_history
		)

	_global_games = {}

	async def _join_global_game(
		self, ctx, name, coro, *,
		maxim=2, minim=2, scn=None, jcn=None
	):
		assert maxim >= minim
		if name in self._global_games:
			for c in self._global_games[name]['ctxs']:
				if c.author.id == ctx.author.id:
					await ctx.send(embed=embed(ctx,
						title=('error',),
						description=('games/already-joined',),
						color=0xff0000
					))
					return
			self._global_games[name]['ctxs'].append(ctx)
			startx = self._global_games[name]['ctxs'][0]
			ctlen = len(self._global_games[name]['ctxs'])
			await startx.send(embed=embed(startx,
				title=('games/player-joined-title',),
				description=(
					'games/player-joined',
					max(0, minim - ctlen),
					max(0, maxim - ctlen)
				),
				color=0x55acee
			))
			if ctlen >= minim and scn is not None:
				await startx.send(embed=embed(startx,
					title=('games/enough-players-title',),
					description=('games/enough-players', ctx.prefix + scn),
					color=0x55acee
				))
			elif ctlen >= maxim:
				await self._start_global_game(
					startx, name, maxim=maxim, minim=minim
				)
		else:
			self._global_games[name] = {
				'ctxs': [ctx],
				'coro': coro
			}
			coros = []
			for row in self.db.execute(
				'SELECT channel_id FROM channels WHERE games_ping LIKE ?',
				('%{}%'.format(name),)
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
					description=('games/game-waiting', name, ctx.prefix + jcn),
					color=0x55acee
				)))
			for row in self.db.execute(
				'SELECT user_id FROM users WHERE games_ping LIKE ?',
				('%{}%'.format(name),)
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
					description=('games/game-waiting', name, ctx.prefix + jcn),
					footer=('games/game-waiting-footer', name),
					color=0x55acee
				)))
			await a.gather(*coros, return_exceptions=True)
		await ctx.send(embed=embed(ctx,
			title=('games/joined', name),
			description=(
				'games/joined-waiting-minmax', name,
				maxim - len(self._global_games[name]['ctxs'])
			) if isinstance(maxim, int) and minim < maxim else ((
				'games/joined-waiting', name,
				maxim - len(self._global_games[name]['ctxs'])
			) if isinstance(maxim, int) else (
				'games/joined-waiting-nomax', name
			)),
			color=0x338acc
		))

	async def _start_global_game(self, ctx, name, *, maxim=2, minim=2):
		if name not in self._global_games:
			return
		if ctx.author.id != self._global_games[name]['ctxs'][0].author.id:
			return
		if len(self._global_games[name]['ctxs']) < minim:
			await ctx.send(embed=embed(ctx,
				title=('error',),
				description=(
					'games/not-enough-players',
					minim, len(self._global_games[name]['ctxs'])
				),
				color=0xff0000
			))
			return
		coro = self._global_games[name]['coro']
		ctxs = []
		if isinstance(maxim, int):
			for i in range(maxim):
				ctxs.append(self._global_games[name]['ctxs'].pop(0))
		else:
			ctxs = self._global_games[name]['ctxs'][:]
			self._global_games[name]['ctxs'] = []
		if not len(self._global_games[name]['ctxs']):
			del self._global_games[name]
		for c in ctxs:
			if not c.author.dm_channel:
				await c.author.create_dm()
		return await coro(ctxs)

	async def _unjoin_global_game(self, ctx, name):
		if name not in self._global_games:
			return
		for i, j in enumerate(self._global_games[name]['ctxs']):
			if j.author.id == ctx.author.id:
				del self._global_games[name]['ctxs'][i]
				break
		if not len(self._global_games[name]['ctxs']):
			del self._global_games[name]
		await ctx.send(embed=embed(ctx,
			title=('games/unjoined-title',),
			description=('games/unjoined', name),
			color=0
		))

	async def _gather_game(self, ctx, name, against, help=None):
		SHAKE, QUESTION = '\U0001f91d\u2753'
		msg = await ctx.send(embed=embed(ctx,
			title=('games/playing', name),
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
			elif against.status == d.Status.offline:
				await ctx.send(embed=embed(ctx,
					title=('error',),
					description=('games/no-offline',),
					color=0xff0000
				))
				return
		await msg.add_reaction(SHAKE)
		if help is not None:
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
					await user.dm_channel.send(embed=help(dmx)
						if callable(help)
						else embed(dmx,
							title=('games/help-title', name),
							description=(help,),
							color=0x55acee
						)
					)
		def clear_listener():
			if help is not None:
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
			except a.TimeoutError:
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
			except a.TimeoutError:
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

	async def _gather_multigame(self, ctx, name, help=None):
		SHAKE, CHECK, QUESTION = '\U0001f91d\u2705\u2753'
		msg = await ctx.send(embed=embed(ctx,
			title=('games/playing', name),
			description=(
				'games/ready-player-3', ctx.author.display_name,
				SHAKE, CHECK
			),
			color=0x55acee
		))
		players = [ctx.author]
		await msg.add_reaction(SHAKE)
		await msg.add_reaction(CHECK)
		if help is not None:
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
					await user.dm_channel.send(embed=help(dmx)
						if callable(help)
						else embed(dmx,
							title=('games/help-title', name),
							description=(help,),
							color=0x55acee
						)
					)
		def clear_listener():
			if help is not None:
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
		except a.TimeoutError:
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

	async def _game(self, ctx, name, against, coro1, coro2, **kwargs):
		player1, player2 = await self._gather_game(ctx, name, against)
		qyoo = a.Queue()
		await a.gather(
			coro1(ctx, player1, qyoo, **kwargs),
			coro2(ctx, player2, qyoo, **kwargs)
		)

	@staticmethod
	def unblock_me(qyoo):
		try:
			qyoo.get_nowait()
			qyoo.task_done()
		except a.QueueEmpty:
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
