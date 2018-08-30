import asyncio as a
import discord as d
from discord.ext.commands import command
from discord.ext.commands import bot_has_permissions
from discord.ext.commands import has_permissions
from .i18n import i18n

class Connect4(object):
	def __init__(self, bot, logger, db):
		self.bot = bot
		self.logger = logger
		self.db = db

	@command()
	@has_permissions(administrator=True)
	async def connect4_config(
		self,
		ctx,
		operation='get',
		channel: d.TextChannel = None,
		*,
		role: d.Role = None
	):
		"""Get or set global connect4 configuration for this server.

		If specified without parameters, gets the current configuration.
		To set the channel to announce global connect4 games, run ;connect4_config set <channel mention>
		To set a role to mention when a game is happening as well, run ;connect4_config set <channel mention> <role name or mention>
		To remove all configuration, run ;connect4_config reset
		"""
		if operation == 'get':
			res = self.db.execute(
				'SELECT channel_id, role_id FROM gcf_guilds WHERE guild_id=?',
				(ctx.guild.id,)
			).fetchone()
			if res is None:
				await ctx.send(i18n(ctx, 'connect4/config-nothing-set'))
				return
			channel = self.bot.get_channel(res['channel_id'])
			if res['role_id'] != 0:
				for r in ctx.guild.roles:
					if r.id == res['role_id']:
						role = r
				await ctx.send(i18n(
					ctx, 'connect4/config-all-set', channel.mention, role.name
				))
			else:
				await ctx.send(i18n(ctx, 'connect4/config-channel-set', channel.mention))
		elif operation == 'reset':
			self.db.execute(
				'DELETE FROM gcf_guilds WHERE guild_id=?',
				(ctx.guild.id,)
			)
			await ctx.send(i18n(ctx, 'connect4/config-reset'))
		elif channel is None and role is None:
			await ctx.send(i18n(ctx, 'connect4/config-no-empty'))
		else:
			res = self.db.execute(
				'SELECT (channel_id) FROM gcf_guilds WHERE guild_id=?',
				(ctx.guild.id,)
			).fetchone()
			if channel is not None and role is None:
				if res is not None:
					self.db.execute(
						'UPDATE gcf_guilds SET channel_id=? WHERE guild_id=?',
						(channel.id, ctx.guild.id)
					)
				else:
					self.db.execute(
						'INSERT INTO gcf_guilds (guild_id, channel_id) VALUES \
(?, ?)',
						(ctx.guild.id, channel.id)
					)
				await ctx.send(i18n(ctx, 'connect4/config-set-channel', channel.mention))
			if role is not None:
				if res is not None:
					self.db.execute(
						'UPDATE gcf_guilds SET role_id=? WHERE guild_id=?',
						(role.id, ctx.guild.id)
					)
				elif channel is not None:
					self.db.execute(
						'INSERT INTO gcf_guilds (guild_id, channel_id, \
role_id) VALUES (?, ?, ?)',
						(ctx.guild.id, channel.id, role.id)
					)
				else:
					await ctx.send(i18n(ctx, 'connect4/config-no-channel-but-role'))
					return
				await ctx.send(i18n(
					ctx, 'connect4/config-set-role', channel.mention, role.name
				))

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
		BLUE, RED, BLACK, SHAKE, NEIN, DOWN = \
			'\U0001f535 \U0001f534 \u2b1b \U0001f91d \u274c \u2b07'.split(' ')
		REGA, REGB, REGC, REGD, REGE, REGF, REGG = REGS = \
			'1\u20e3 2\u20e3 3\u20e3 4\u20e3 5\u20e3 6\u20e3 7\u20e3'.split(' ')
		msg = await ctx.send(embed=d.Embed(
			title=i18n(ctx, 'pm_games/playing', 'Connect 4'),
			description=i18n(
				ctx, 'pm_games/ready-player-1', ctx.author.display_name
			) + (
				i18n(ctx, 'pm_games/react-to-join', SHAKE)
				if against is None
				else (
					i18n(ctx, 'connect4/ready-player-self', ctx.author.display_name)
				) if against.id == ctx.author.id
				else (
					i18n(ctx, 'connect4/ready-player-global')
				) if against.id == self.bot.user.id
				else (
					i18n(ctx, 'pm_games/ready-player-2', against.display_name)
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
		elif ctx.author.id == against.id:
			player2 = player1
		elif global_:
			MESSAGES = []
			MESSAGE_IDS = []
			await msg.add_reaction(NEIN)
			for row in self.db.execute(
				'SELECT channel_id, role_id FROM gcf_guilds'
			):
				channel = self.bot.get_channel(row['channel_id'])
				if channel.guild.id == ctx.guild.id:
					continue
				role = None
				if row['role_id'] != 0:
					role = d.utils.get(channel.guild.roles, id=row['role_id'])
				# not translated because other guild might not be language-open
				gmsg = await channel.send(embed=d.Embed(
					title='Playing Connect 4',
					description='Somebody in another server has requested to \
play connect4! React with {} to join.'.format(SHAKE)
				), content=role.mention if role is not None else None)
				await gmsg.add_reaction(SHAKE)
				MESSAGES.append(gmsg)
				MESSAGE_IDS.append(gmsg.id)
			try:
				reaction, user = await self.bot.wait_for(
					'reaction_add',
					check=lambda r, u: \
						(
							r.emoji == SHAKE
							and r.message.id in MESSAGE_IDS + [msg.id]
							and u.id != self.bot.user.id
						) or (
							r.emoji == NEIN
							and r.message.id == msg.id
							and u.id == ctx.author.id
						),
					timeout=60.0
				)
			except a.TimeoutError:
				await msg.edit(
					content=i18n(ctx, 'pm_games/game-timeout', 60),
					embed=None
				)
				await msg.clear_reactions()
				for m in MESSAGES:
					print('deleting', m)
					await m.delete()
				return
			if reaction.emoji == NEIN and user.id == ctx.author.id:
				await ctx.send(i18n(ctx, 'pm_games/game-cancelled'))
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
			await ctx.send(i18n(ctx, 'pm_games/no-bots'))
			return
		elif str(against.status) == 'offline':
			await ctx.send(i18n(ctx, 'pm_games/no-offline'))
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
			boardmsgcont += (
				i18n(ctx, 'connect4/board-turn', '{0}')
				if not global_
				else "It is currently {0}'s turn."
			).format(
				(players[whose].display_name)
				if not global_
				else (RED, BLUE)[whose]
			)
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
				title=i18n(ctx, 'connect4/board-title'),
				description=boardmsgcont + (i18n(
					ctx, 'connect4/board-you-are', RED
				) if global_ else ''),
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
					await boardmsg.edit(
						content=i18n(ctx, 'connect4/game-timeout', 600), embed=None
					)
					await boardmsg.clear_reactions()
					if global_:
						await boardmsg2.edit(
							content='Nobody made a move for ten minutes! The \
game has been cancelled.', embed=None
						)
						await boardmsg2.clear_reactions()
					return
				if str(reaction) == DOWN:
					msg = await reaction.message.channel.send(embed=d.Embed(
						title=i18n(ctx, 'connect4/board-title') \
							if reaction.message.id == boardmsg.id \
							else "Board",
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
				title=i18n(ctx, 'connect4/board-title'),
				description=boardmsgcont + (i18n(
					ctx, 'connect4/board-you-are', RED
				) if global_ else ''),
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
					await boardmsg.edit(
						content=i18n(ctx, 'connect4/game-timeout', 600),
						embed=None
					)
					await boardmsg.clear_reactions()
					if global_:
						await boardmsg2.edit(
							content='Nobody made a move for ten minutes! The \
game has been cancelled.', embed=None
						)
						await boardmsg2.clear_reactions()
					return
				if str(reaction) == DOWN:
					msg = await reaction.message.channel.send(embed=d.Embed(
						title=i18n(ctx, 'connect4/board-title') \
							if reaction.message.id == boardmsg.id \
							else "Board",
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
			title=i18n(ctx, 'connect4/board-title'),
			description=boardmsgcont,
		))
		if redwon and bluewon:
			embed = d.Embed(
				title=i18n(ctx, 'connect4/game-over-title'),
				description=i18n(ctx, 'connect4/game-over-tied')
			)
		else:
			embed = d.Embed(
				title=i18n(ctx, 'connect4/game-over-title'),
				description=i18n(ctx, 'connect4/game-over-description',
					RED if redwon else BLUE,
					(' (' + (
						(player1.display_name)
						if redwon
						else (player2.display_name)
					) + ')') if not global_ else '',
					RED if bluewon else BLUE,
					(' (' + (
						(player1.display_name)
						if bluewon
						else (player2.display_name)
					) + ')') if not global_ else ''
				),
				color=0xff0000 if redwon else 0x55acee
			)
		await ctx.send(embed=embed)
		if global_:
			await boardmsg2.edit(embed=d.Embed(
				title="Board",
				description=boardmsgcont
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
						RED if redwon else BLUE,
						(' (' + (
							(player1.display_name)
							if redwon
							else (player2.display_name)
						) + ')') if not global_ else '',
						RED if bluewon else BLUE,
						(' (' + (
							(player1.display_name)
							if bluewon
							else (player2.display_name)
						) + ')') if not global_ else ''
					),
					color=0xff0000 if redwon else 0x55acee
				)
			await ctx2.send(embed=embed)
