import asyncio as a
import discord as d
from .i18n import i18n

class PrivateGames(object):
	def __init__(self, bot, logger, db):
		self.bot = bot
		self.logger = logger
		self.db = db

	def __local_check(self, ctx):
		perms = ctx.channel.permissions_for(self.bot.user)
		return all(
			perms.manage_messages,
			perms.add_reactions,
			perms.read_message_history
		)

	async def _gather_game(self, ctx, name, against):
		SHAKE = '\U0001f91d'
		msg = await ctx.send(embed=d.Embed(
			title=i18n(ctx, 'pm_games/playing', name),
			description=i18n(
				ctx, 'pm_games/ready-player-1', ctx.author.display_name
			) + (
				i18n(ctx, 'pm_games/react-to-join', SHAKE)
				if against is None
				else i18n(
					ctx, 'pm_games/ready-player-2', against.display_name
				)
			),
		))
		player1 = ctx.author
		if against is None:
			await msg.add_reaction(SHAKE)
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
					content=i18n(ctx, 'pm_games/game-timeout', 60),
					embed=None
				)
				await msg.clear_reactions()
				return
			if user.id == ctx.author.id:
				await ctx.send(i18n(ctx, 'pm_games/game-cancelled'))
				return
			player2 = user
			del reaction, user
		elif against.bot:
			await ctx.send(i18n(ctx, 'pm_games/no-bots'))
			return
		elif str(against.status) == 'offline':
			await ctx.send(i18n(ctx, 'pm_games/no-offline'))
			return
		else:
			await msg.add_reaction(SHAKE)
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
					content=i18n(ctx, 'pm_games/unready-player-2', 60),
					embed=None
				)
				await msg.clear_reactions()
				return
			if user.id == ctx.author.id:
				await ctx.send(i18n(ctx, 'pm_games/game-cancelled'))
				return
			player2 = user
			del reaction, user
		if not player1.dm_channel:
			await player1.create_dm()
		if not player2.dm_channel:
			await player2.create_dm()
		return (player1, player2)

	async def _gather_multigame(self, ctx, name):
		SHAKE = '\U0001f91d'
		CHECK = '\u2705'
		msg = await ctx.send(embed=d.Embed(
			title=i18n(ctx, 'pm_games/playing', name),
			description=i18n(
				ctx, 'pm_games/ready-player-1', ctx.author.display_name
			) + (
				i18n(
					ctx,
					'pm_games/react-to-join-mult',
					SHAKE,
					ctx.author.display_name,
					CHECK
				)
			),
		))
		players = [ctx.author]
		await msg.add_reaction(SHAKE)
		await msg.add_reaction(CHECK)
		try:
			reaction, user = await self.bot.wait_for('reaction_add',
				check=lambda r, u: \
					r.emoji in (CHECK, SHAKE) \
					and r.message.id == msg.id \
					and u.id == ctx.author.id,
				timeout=60.0
			)
			if reaction.emoji == SHAKE:
				await ctx.send(i18n(ctx, 'pm_games/game-cancelled'))
				return
		except a.TimeoutError:
			pass
		msg = await ctx.get_message(msg.id)
		for r in msg.reactions:
			if r.emoji == SHAKE:
				async for u in r.users():
					if u.id != self.bot.user.id:
						players.append(u)
		for player in players:
			if not player.dm_channel:
				await player.create_dm()
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
