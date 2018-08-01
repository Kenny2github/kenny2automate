import re
import random
from itertools import accumulate
from bisect import bisect
import asyncio as a
import discord as d
from discord.ext.commands import command
from discord.ext.commands import bot_has_permissions

class PrivateGames(object):
	def __init__(self, bot, logger, db):
		self.bot = bot
		self.logger = logger
		self.db = db

	def __local_check(self, ctx):
		perms = ctx.channel.permissions_for(self.bot.user)
		return perms.manage_messages and perms.add_reactions and perms.read_message_history

	async def _gather_game(self, ctx, name, against):
		SHAKE = '\U0001f91d'
		msg = await ctx.send(embed=d.Embed(
			title='Playing {}'.format(name),
			description='Player 1: {}'.format(ctx.author.display_name) + (
				'\nReact with {} to join!'.format(SHAKE)
				if against is None
				else (
					'\nPlayer 2: {}'.format(against.display_name)
					+ '\nWaiting for Player 2 to join...'
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
				await msg.edit(content='Nobody joined after a minute! The game has been automatically cancelled.', embed=None)
				await msg.clear_reactions()
				return
			if user.id == ctx.author.id:
				await ctx.send('Game cancelled by starter.')
				return
			player2 = user
			del reaction, user
		elif against.bot:
			await ctx.send("Wait, you can't play against a bot! Game cancelled.")
			return
		elif str(against.status) == 'offline':
			await ctx.send('Wait, Player 2 is offline! Game cancelled.')
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
				await msg.edit(content="Player 2 didn't join after a minute! The game has been automatically cancelled.", embed=None)
				await msg.clear_reactions()
				return
			if user.id == ctx.author.id:
				await ctx.send('Game cancelled by starter.')
				return
			player2 = user
			del reaction, user
		if not player1.dm_channel:
			await player1.create_dm()
		if not player2.dm_channel:
			await player2.create_dm()
		return (player1, player2)

	async def _game(self, ctx, name, against, coro1, coro2, **kwargs):
                player1, player2 = await self._gather_game(ctx, name, against)
		qyoo = a.Queue()
		await a.gather(coro1(ctx, player1, qyoo, **kwargs), coro2(ctx, player2, qyoo, **kwargs))

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

#	@command()
	async def test_game(self, ctx, against: d.Member = None):
		async def player1_coro(ctx, player1, player2, qyoo):
			await a.sleep(2)
			qyoo.put_nowait('player1')
			dmx = await ctx.bot.get_context(await player1.dm_channel.send('test: player1'))
			msg = await ctx.bot.wait_for('message', check=lambda m: m.channel == player1.dm_channel and m.author == player1)
			self.unblock_me(qyoo)
			await qyoo.join()
			await dmx.send('player1: {.content}'.format(msg))
		async def player2_coro(ctx, player1, player2, qyoo):
			await a.sleep(2)
			qyoo.put_nowait('player2')
			dmx = await ctx.bot.get_context(await player2.dm_channel.send('test: player2'))
			msg = await ctx.bot.wait_for('message', check=lambda m: m.channel == player2.dm_channel and m.author == player2)
			self.unblock_me(qyoo)
			await qyoo.join()
			await dmx.send('player2: {.content}'.format(msg))
		await self._game(ctx, 'test', against, player1_coro, player2_coro)
