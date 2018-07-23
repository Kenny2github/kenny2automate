import traceback
import asyncio as a
import discord as d
from discord.ext.commands import command
from discord.ext.commands import bot_has_permissions
from discord.ext.commands import has_permissions
from discord.ext import commands as c

class Connect4(object):
	def __init__(self, bot, logger, db):
		self.bot = bot
		self.logger = logger
		self.db = db

	@command()
	@has_permissions(administrator=True)
	async def connect4_config(self, ctx, operation='get', channel: d.TextChannel = None, role: d.Role = None):
		"""Get or set global connect4 configuration for this server.

		If specified without parameters, gets the current configuration.
		To set the channel to announce global connect4 games, run ;connect4_config <channel mention>
		To set a role to mention when a game is happening as well, run ;connect4_config <channel mention> <role name or mention>
		"""
		if operation == 'get':
			res = self.db.execute('SELECT channel_id, role_id FROM gcf_guilds WHERE guild_id=?', (ctx.guild.id,)).fetchone()
			if res is None:
				await ctx.send('Nothing is set for this server! Run ;help connect4_config to see how to set it.')
				return
			channel = self.bot.get_channel(res['channel_id'])
			if res['role_id'] != 0:
				for r in ctx.guild.roles:
					if r.id == res['role_id']:
						role = r
				await ctx.send('Channel for global connect4: {}\nRole to mention: {}'.format(channel.mention, role.name))
			else:
				await ctx.send('Channel for global connect4: {}'.format(channel.mention))
		elif operation == 'reset':
			self.db.execute('DELETE FROM gcf_guilds WHERE guild_id=?', (ctx.guild.id,))
			await ctx.send('Successfully removed config for this server.')
		elif channel is None and role is None:
			await ctx.send('Cannot set config with no parameters...')
		else:
			res = self.db.execute('SELECT (channel_id) FROM gcf_guilds WHERE guild_id=?', (ctx.guild.id,)).fetchone()
			if channel is not None:
				if res is not None:
					self.db.execute('UPDATE gcf_guilds SET channel_id=? WHERE guild_id=?', (channel.id, ctx.guild.id))
				else:
					self.db.execute('INSERT INTO gcf_guilds (guild_id, channel_id) VALUES (?, ?)', (ctx.guild.id, channel.id))
				await ctx.send('Successfully set channel for global connect4 to {}'.format(channel.mention))
			if role is not None:
				if res is not None:
					self.db.execute('UPDATE gcf_guilds SET role_id=? WHERE guild_id=?', (role.id, ctx.guild.id))
				elif channel is not None:
					self.db.execute('INSERT INTO gcf_guilds (guild_id, channel_id, role_id) VALUES (?, ?, ?)', (ctx.guild.id, channel.id, role.id))
				else:
					await ctx.send('Cannot set global connect4 mention without setting a channel.')
					return
				await ctx.send('Successfully set role for global connect4 to {}'.format(role.name))

	@command()
	@bot_has_permissions(manage_messages=True, add_reactions=True, read_message_history=True)
	async def connect4(self, ctx, against: d.Member = None):
		"""Play some connect4!

		If you want to play against yourself or you have someone next to you,
		do ;connect4 and mention yourself.
		If you want to play against a specific person, do ;connect4 and mention them.
		If you want to play a global game (cross-server), do ;connect4 and mention the bot.
		"""
		self.logger.info('Games.connect4', extra={'ctx': ctx})
		BLUE, RED, BLACK, SHAKE, NEIN, DOWN = '\U0001f535 \U0001f534 \u2b1b \U0001f91d \u274c \u2b07'.split(' ')
		REGA, REGB, REGC, REGD, REGE, REGF, REGG = REGS = '1\u20e3 2\u20e3 3\u20e3 4\u20e3 5\u20e3 6\u20e3 7\u20e3'.split(' ')
		msg = await ctx.send(embed=d.Embed(
			title='Playing Connect 4',
			description='Player 1: {}'.format(ctx.author.display_name) + (
				'\nReact with {} to join!'.format(SHAKE)
				if against is None
				else (
					'\nPlayer 2: {}'.format(ctx.author.display_name)
				) if against.id == ctx.author.id
				else (
					'\nWaiting for someone from another server to join...'
				) if against.id == self.bot.user.id
				else (
					'\nPlayer 2: {}'.format(against.display_name) + '\nWaiting for Player 2 to join...'
				)
			)
		))
		player1 = ctx.author
		global_ = against is not None and against.id == self.bot.user.id
		if against is None:
			await msg.add_reaction(SHAKE)
			try:
				reaction, user = await self.bot.wait_for(
					'reaction_add',
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
		elif ctx.author.id == against.id:
			player2 = player1
		elif global_:
			MESSAGES = []
			MESSAGE_IDS = []
			await msg.add_reaction(NEIN)
			for row in self.db.execute('SELECT channel_id, role_id FROM gcf_guilds'):
				channel = self.bot.get_channel(row['channel_id'])
				if channel.guild.id == ctx.guild.id:
					continue
				gmsg = await channel.send(embed=d.Embed(
					title='Playing Connect 4',
					description='Somebody in another server has requested to play connect4! React with {} to join.'.format(SHAKE)
				))
				await gmsg.add_reaction(SHAKE)
				MESSAGES.append(gmsg)
				MESSAGE_IDS.append(gmsg.id)
			try:
				reaction, user = await self.bot.wait_for(
					'reaction_add',
					check=lambda r, u: \
						r.emoji in (SHAKE, NEIN) \
						and r.message.id in MESSAGE_IDS + [msg.id] \
						and u.id != self.bot.user.id,
					timeout=60.0
				)
			except a.TimeoutError:
				await msg.edit(content='Nobody joined after a minute! The game has been automatically cancelled.', embed=None)
				await msg.clear_reactions()
				for m in MESSAGES:
					print('deleting', m)
					await m.delete()
				return
			if reaction.emoji == NEIN and user.id == ctx.author.id:
				await ctx.send('Game cancelled by starter.')
				for m in MESSAGES:
					await m.delete()
				return
			player2 = user
			ctx2 = await self.bot.get_context(reaction.message)
			for m in MESSAGES:
				if m.id != reaction.message.id:
					await m.delete()
			del reaction, user
			print(player2, '(we got this far)')
		elif against.bot:
			await ctx.send("Wait, you can't play against a bot! Game cancelled.")
			return
		elif str(against.status) == 'offline':
			await ctx.send("Wait, Player 2 is offline! Game cancelled.")
			return
		else:
			await msg.add_reaction(SHAKE)
			try:
				reaction, user = await self.bot.wait_for(
					'reaction_add',
					check=lambda r, u: \
						r.emoji == SHAKE \
						and r.message.id == msg.id \
						and u.id in (against.id, ctx.author.id) \
						and r.message.channel == ctx.channel,
					timeout=60.0
				)
			except a.TimeoutError:
				await msg.edit(content="Player 2 didn\'t join after a minute! The game has been automatically cancelled.", embed=None)
				await msg.clear_reactions()
				return
			if user.id == ctx.author.id:
				await ctx.send('Game cancelled by starter.')
				return
			player2 = user
			del reaction, user
		del msg
		board = [[BLACK for _ in range(7)] for _ in range(7)]
		redwon, bluewon = False, False
		def checkwin(board, tile):
			BH = len(board[0])
			BW = len(board)
			#check -
			for y in range(BH):
				for x in range(BW - 3):
					if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
						return True
			#check |
			for x in range(BW):
				for y in range(BH - 3):
					if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
						return True
			#check \
			for x in range(BW - 3):
				for y in range(3, BH):
					if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
						return True
			#check /
			for x in range(BW - 3):
				for y in range(BH - 3):
					if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
						return True
			#check + because if it's full and no 4s everyone won
			for row in board:
				for i in row:
					if i == BLACK:
						return False
			#all full and no rows
			return True

		def constructboard(board, players, whose):
			#only add names if not global to avoid inappropriate names x-server
			boardmsgcont = ''
			if not global_:
				boardmsgcont += RED + ' = ' + (players[0].nick or players[0].name) + '\n'
				boardmsgcont += BLUE + ' = ' + (players[1].nick or players[1].name) + '\n'
			boardmsgcont += "".join(REGS) + '\n'
			for row in zip(*board):
				for column in row:
					boardmsgcont += column
				boardmsgcont += '\n'
			boardmsgcont += "It is currently {}'s turn".format(
				(players[whose].nick or players[whose].name)
				if not global_
				else (RED, BLUE)[whose])
			return boardmsgcont

		boardmsg = await ctx.send('_ _')
		if global_:
			boardmsg2 = await ctx2.send('_ _')
		reaction, user = None, None

		while not (redwon or bluewon):
			if reaction is None:
				await boardmsg.clear_reactions()
				for reg in REGS:
					await boardmsg.add_reaction(reg)
				await boardmsg.add_reaction(DOWN)
				if global_:
					await boardmsg2.clear_reactions()
					for reg in REGS:
						await boardmsg2.add_reaction(reg)
					await boardmsg2.add_reaction(DOWN)
			else:
				try:
					await boardmsg.remove_reaction(reaction, user)
					if global_:
						await boardmsg2.remove_reaction(reaction, user)
				except d.NotFound:
					pass
			boardmsgcont = constructboard(board, (player1, player2), 0)
			await boardmsg.edit(embed=d.Embed(
				title="Board",
				description=boardmsgcont + (
					'\nYou are {}'.format(RED)
					if global_
					else ''
				),
				color=0xff0000
			))
			if global_:
				await boardmsg2.edit(embed=d.Embed(
					title="Board",
					description=boardmsgcont + '\nYou are {}'.format(BLUE),
					color=0xff0000
				))
			reaction = DOWN
			while str(reaction) == DOWN:
				try:
					reaction, user = await self.bot.wait_for(
						'reaction_add',
						check=lambda r, u: \
							(r.message.id in (
								(boardmsg.id,)
								+ ((boardmsg2.id,)
								if global_
								else ())
							) \
							and str(r) in REGS \
							and str(r) != NEIN \
							and u.id == player1.id) \
							or (r.message.id in (
								(boardmsg.id,)
								+ ((boardmsg2.id,)
								if global_
								else ())
							) \
							and str(r) == DOWN \
							and u.id in (player1.id, player2.id)),
						timeout=600.0
					)
				except a.TimeoutError:
					await boardmsg.edit(content='Nobody made a move for ten minutes! The game has been cancelled.', embed=None)
					await boardmsg.clear_reactions()
					if global_:
						await boardmsg2.edit(content='Nobody made a move for ten minutes! The game has been cancelled.', embed=None)
						await boardmsg2.clear_reactions()
					return
				if str(reaction) == DOWN:
					msg = await reaction.message.channel.send(embed=d.Embed(
						title="Board",
						description=boardmsgcont,
						color=0xff0000
					))
					for reg in REGS:
						await msg.add_reaction(reg)
					await msg.add_reaction(DOWN)
					if global_ and reaction.message.id == boardmsg2.id:
						boardmsg2 = msg
					else:
						boardmsg = msg
					await reaction.message.delete()
			idx = REGS.index(str(reaction))
			hit = False
			for rown in range(len(board[idx])):
				if board[idx][rown] != BLACK:
					board[idx][rown-1] = RED
					hit = True
					break
			if not hit:
				board[idx][-1] = RED
			if board[idx].count(BLACK) == 0:
				REGS[idx] = NEIN
			redwon, bluewon = checkwin(board, RED), checkwin(board, BLUE)
			if redwon or bluewon:
				break
			boardmsgcont = constructboard(board, (player1, player2), 1)
			await boardmsg.edit(embed=d.Embed(
				title="Board",
				description=boardmsgcont + (
					'\nYou are {}'.format(RED)
					if global_
					else ''
				),
				color=0x55acee
			))
			if global_:
				await boardmsg2.edit(embed=d.Embed(
					title="Board",
					description=boardmsgcont + '\nYou are {}'.format(BLUE),
					color=0x55acee
				))
			try:
				await boardmsg.remove_reaction(reaction, user)
				if global_:
					await boardmsg2.remove_reaction(reaction, user)
			except d.NotFound:
				pass
			reaction = DOWN
			while str(reaction) == DOWN:
				try:
					reaction, user = await self.bot.wait_for(
						'reaction_add',
						check=lambda r, u: \
							(r.message.id in (
								(boardmsg.id,)
								+ ((boardmsg2.id,)
								if global_
								else ())
							) \
							and str(r) in REGS \
							and str(r) != NEIN \
							and u.id == player2.id) \
							or (r.message.id in (
								(boardmsg.id,)
								+ ((boardmsg2.id,)
								if global_
								else ())
							) \
							and str(r) == DOWN \
							and u.id in (player1.id, player2.id)),
						timeout=600.0
					)
				except a.TimeoutError:
					await boardmsg.edit(content='Nobody made a move for ten minutes! The game has been cancelled.', embed=None)
					await boardmsg.clear_reactions()
					if global_:
						await boardmsg.edit(content='Nobody made a move for ten minutes! The game has been cancelled.', embed=None)
						await boardmsg.clear_reactions()
					return
				if str(reaction) == DOWN:
					msg = await reaction.message.channel.send(embed=d.Embed(
						title="Board",
						description=boardmsgcont,
						color=0x55acee
					))
					for reg in REGS:
						await msg.add_reaction(reg)
					await msg.add_reaction(DOWN)
					if global_ and reaction.message.id == boardmsg2.id:
						boardmsg2 = msg
					else:
						boardmsg = msg
					await reaction.message.delete()
			idx = REGS.index(str(reaction))
			hit = False
			for rown in range(len(board[idx])):
				if board[idx][rown] != BLACK:
					board[idx][rown-1] = BLUE
					hit = True
					break
			if not hit:
				board[idx][-1] = BLUE
			if board[idx].count(BLACK) == 0:
				REGS[idx] = NEIN
			redwon, bluewon = checkwin(board, RED), checkwin(board, BLUE)
		boardmsgcont = constructboard(board, (player1, player2), int(bluewon))
		await boardmsg.edit(embed=d.Embed(
			title="Board",
			description=boardmsgcont,
		))
		if redwon and bluewon:
			embed = d.Embed(
				title="Game Over!",
				description="The game is tied! The board is full and no 4-in-a-rows have been made."
			)
		else:
			embed = d.Embed(
				title="Game Over!",
				description='The game is over!\nWinner: {}{}\nLoser: {}{}\n'.format(
					RED if redwon else BLUE, (' (' + ((player1.nick or player1.name) if redwon else (player2.nick or player2.name)) + ')') if not global_ else '',
					RED if bluewon else BLUE, (' (' + ((player1.nick or player1.name) if bluewon else (player2.nick or player2.name)) + ')') if not global_ else ''
				),
				color=0xff0000 if redwon else 0x55acee
			)
		await ctx.send(embed=embed)
		if global_:
			await boardmsg2.edit(embed=d.Embed(
				title="Board",
				description=boardmsgcont
			))
			await ctx2.send(embed=embed)
