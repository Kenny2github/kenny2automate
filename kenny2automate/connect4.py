import asyncio as a
import discord as d
from discord.ext.commands import command, group
from discord.ext.commands import bot_has_permissions
from discord.ext.commands import has_permissions
from .games import Games
from .i18n import i18n

BLUE, RED, BLACK, SHAKE, NEIN, DOWN = \
	'\U0001f535 \U0001f534 \u2b1b \U0001f91d \u274c \u2b07'.split(' ')
REGA, REGB, REGC, REGD, REGE, REGF, REGG = REGS = \
	'1\u20e3 2\u20e3 3\u20e3 4\u20e3 5\u20e3 6\u20e3 7\u20e3'.split(' ')

class Connect4(Games):
	@command()
	async def connect4_leave(self, ctx):
		await self._unjoin_global_game(ctx, 'Connect 4')

	async def connect4_global(self, ctxs):
		"""Global connect4 coroutine!"""
		ctx1, ctx2 = ctxs
		regs = REGS[:]
		board = self.genboard()
		redwon, bluewon = False, False
		checkwin = self.checkwin
		constructboard = self.constructboard

		boardmsg1 = await ctx1.send('_ _')
		boardmsg2 = await ctx2.send('_ _')
		reaction, user = None, None

		while not (redwon or bluewon):
			if reaction is None:
				await boardmsg1.clear_reactions()
				for reg in regs:
					await boardmsg1.add_reaction(reg)
				await boardmsg1.add_reaction(DOWN)
				await boardmsg2.clear_reactions()
				for reg in regs:
					await boardmsg2.add_reaction(reg)
				await boardmsg2.add_reaction(DOWN)
			else:
				try:
					await boardmsg2.remove_reaction(reaction, user)
				except d.NotFound:
					pass
			boardmsgcont1 = constructboard(ctx1, board, (ctx1.author, ctx2.author), 0, True)
			boardmsgcont2 = constructboard(ctx2, board, (ctx1.author, ctx2.author), 0, True)
			await boardmsg1.edit(embed=d.Embed(
				title=i18n(ctx1, 'connect4/board-title'),
				description=boardmsgcont1 + i18n(
					ctx1, 'connect4/board-you-are', RED
				),
				color=0xff0000
			))
			await boardmsg2.edit(embed=d.Embed(
				title=i18n(ctx2, 'connect4/board-title'),
				description=boardmsgcont2 + i18n(
					ctx2, 'connect4/board-you-are', BLUE
				),
				color=0xff0000
			))
			reaction = DOWN
			while str(reaction) == DOWN:
				try:
					reaction, user = await self.bot.wait_for(
						'reaction_add',
						check=lambda r, u: (
							r.message.id == boardmsg1.id
							and str(r) in regs
							and str(r) != NEIN
							and u.id == ctx1.author.id
							or r.message.id in (boardmsg1.id, boardmsg2.id)
							and str(r) == DOWN
							and u.id in (ctx1.author.id, ctx2.author.id)
						),
						timeout=600.0
					)
				except a.TimeoutError:
					await boardmsg1.edit(
						content=i18n(ctx1, 'connect4/game-timeout', 600), embed=None
					)
					await boardmsg1.clear_reactions()
					await boardmsg2.edit(
						content=i18n(ctx2, 'connect4/game-timeout', 600), embed=None
					)
					return
				if str(reaction) == DOWN:
					whose = int(ctx2.channel.id == reaction.message.channel.id)
					msg = await reaction.message.channel.send(embed=d.Embed(
						title=i18n(ctxs[whose], 'connect4/board-title'),
						description=(boardmsgcont1, boardmsgcont2)[whose] + i18n(
							ctxs[whose], 'connect4/board-you-are', (RED, BLUE)[whose]
						),
						color=0xff0000
					))
					for reg in regs:
						await msg.add_reaction(reg)
					await msg.add_reaction(DOWN)
					if whose:
						boardmsg2 = msg
					else:
						boardmsg1 = msg
					await reaction.message.delete()
			idx = regs.index(str(reaction))
			hit = False
			for rown in range(len(board[idx])):
				if board[idx][rown] != BLACK:
					board[idx][rown-1] = RED
					hit = True
					break
			if not hit:
				board[idx][-1] = RED
			if board[idx].count(BLACK) == 0:
				regs[idx] = NEIN
			redwon, bluewon = checkwin(board, RED), checkwin(board, BLUE)
			if redwon or bluewon:
				break
			boardmsgcont1 = constructboard(ctx1, board, (ctx1.author, ctx2.author), 1, True)
			boardmsgcont2 = constructboard(ctx2, board, (ctx1.author, ctx2.author), 1, True)
			await boardmsg1.edit(embed=d.Embed(
				title=i18n(ctx1, 'connect4/board-title'),
				description=boardmsgcont1 + i18n(
					ctx1, 'connect4/board-you-are', RED
				),
				color=0x55acee
			))
			await boardmsg2.edit(embed=d.Embed(
				title=i18n(ctx2, 'connect4/board-title'),
				description=boardmsgcont2 + i18n(
					ctx2, 'connect4/board-you-are', BLUE
				),
				color=0x55acee
			))
			try:
				await boardmsg1.remove_reaction(reaction, user)
			except d.NotFound:
				pass
			reaction = DOWN
			while str(reaction) == DOWN:
				try:
					reaction, user = await self.bot.wait_for(
						'reaction_add',
						check=lambda r, u: (
							r.message.id == boardmsg2.id
							and str(r) in regs
							and str(r) != NEIN
							and u.id == ctx2.author.id
							or r.message.id in (boardmsg1.id, boardmsg2.id)
							and str(r) == DOWN
							and u.id in (ctx1.author.id, ctx2.author.id)
						),
						timeout=600.0
					)
				except a.TimeoutError:
					await boardmsg1.edit(
						content=i18n(ctx1, 'connect4/game-timeout', 600),
						embed=None
					)
					await boardmsg1.clear_reactions()
					await boardmsg2.edit(
						content=i18n(ctx2, 'connect4/game-timeout', 600),
						embed=None
					)
					await boardmsg2.clear_reactions()
					return
				if str(reaction) == DOWN:
					whose = int(ctx2.channel.id == reaction.message.channel.id)
					msg = await reaction.message.channel.send(embed=d.Embed(
						title=i18n(ctxs[whose], 'connect4/board-title'),
						description=(boardmsgcont1, boardmsgcont2)[whose] + i18n(
							ctxs[whose], 'connect4/board-you-are', (RED, BLUE)[whose]
						),
						color=0x55acee
					))
					for reg in regs:
						await msg.add_reaction(reg)
					await msg.add_reaction(DOWN)
					if whose == 0:
						boardmsg1 = msg
					else:
						boardmsg2 = msg
					await reaction.message.delete()
			idx = regs.index(str(reaction))
			hit = False
			for rown in range(len(board[idx])):
				if board[idx][rown] != BLACK:
					board[idx][rown-1] = BLUE
					hit = True
					break
			if not hit:
				board[idx][-1] = BLUE
			if board[idx].count(BLACK) == 0:
				regs[idx] = NEIN
			redwon, bluewon = checkwin(board, RED), checkwin(board, BLUE)
		boardmsgcont1 = constructboard(ctx1, board, (ctx1.author, ctx2.author), int(bluewon), True)
		boardmsgcont2 = constructboard(ctx2, board, (ctx1.author, ctx2.author), int(bluewon), True)
		await boardmsg1.edit(embed=d.Embed(
			title=i18n(ctx1, 'connect4/board-title'),
			description=boardmsgcont1
		))
		await boardmsg2.edit(embed=d.Embed(
			title=i18n(ctx2, 'connect4/board-title'),
			description=boardmsgcont2
		))
		if redwon and bluewon:
			embed1 = d.Embed(
				title=i18n(ctx1, 'connect4/game-over-title'),
				description=i18n(ctx1, 'connect4/game-over-tied')
			)
			embed2 = d.Embed(
				title=i18n(ctx2, 'connect4/game-over-title'),
				description=i18n(ctx2, 'connect4/game-over-tied')
			)
		else:
			embed1 = d.Embed(
				title=i18n(ctx1, 'connect4/game-over-title'),
				description=i18n(ctx1, 'connect4/game-over-description',
					RED if redwon else BLUE, '', RED if bluewon else BLUE, ''),
				color=0xff0000 if redwon else 0x55acee
			)
			embed2 = d.Embed(
				title=i18n(ctx2, 'connect4/game-over-title'),
				description=i18n(ctx2, 'connect4/game-over-description',
					RED if redwon else BLUE, '', RED if bluewon else BLUE, ''),
				color=0xff0000 if redwon else 0x55acee
			)
		await ctx1.send(embed=embed1)
		await ctx2.send(embed=embed2)

	@staticmethod
	def genboard():
		return [[BLACK for _ in range(7)] for _ in range(7)]

	@staticmethod
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

	@staticmethod
	def constructboard(ctx, board, players, whose, safe=False):
		#only add names if not global to avoid inappropriate names x-server
		boardmsgcont = ''
		if not safe:
			boardmsgcont += RED + ' = ' + (players[0].display_name) + '\n'
			boardmsgcont += BLUE + ' = ' + (players[1].display_name) + '\n'
		boardmsgcont += "".join(REGS) + '\n'
		for row in zip(*board):
			for column in row:
				boardmsgcont += column
			boardmsgcont += '\n'
		boardmsgcont += i18n(
			ctx, 'connect4/board-turn', (
				players[whose].display_name
				if not safe
				else (RED, BLUE)[whose]
			)
		)
		return boardmsgcont

	@command()
	@bot_has_permissions(manage_messages=True, add_reactions=True, read_message_history=True)
	async def connect4(self, ctx, against: d.Member = None):
		"""Play some connect4!

		If you want to play against yourself or you have someone next to you,
		do ;connect4 and mention yourself.
		If you want to play against a specific person, do ;connect4 and mention them.
		If you want to play a global game (cross-server), do ;connect4 and mention the bot.
		"""
		if against and against.id == self.bot.user.id:
			return await self._join_global_game(
				ctx, 'Connect 4', self.connect4_global
			)
		regs = REGS[:]
		if against and against.id == ctx.author.id:
			player1 = player2 = against
		else:
			player1, player2 = await self._gather_game(ctx, 'Connect 4', against)
		board = self.genboard()
		redwon, bluewon = False, False
		checkwin = self.checkwin
		constructboard = self.constructboard

		boardmsg = await ctx.send('_ _')
		reaction, user = None, None

		while not (redwon or bluewon):
			if reaction is None:
				await boardmsg.clear_reactions()
				for reg in regs:
					await boardmsg.add_reaction(reg)
				await boardmsg.add_reaction(DOWN)
			else:
				try:
					await boardmsg.remove_reaction(reaction, user)
				except d.NotFound:
					pass
			boardmsgcont = constructboard(ctx, board, (player1, player2), 0)
			await boardmsg.edit(embed=d.Embed(
				title=i18n(ctx, 'connect4/board-title'),
				description=boardmsgcont,
				color=0xff0000
			))
			reaction = DOWN
			while str(reaction) == DOWN:
				try:
					reaction, user = await self.bot.wait_for(
						'reaction_add',
						check=lambda r, u: \
							r.message.id == boardmsg.id \
							and str(r) in regs \
							and str(r) != NEIN \
							and u.id == player1.id \
							or r.message.id == boardmsg.id \
							and str(r) == DOWN \
							and u.id in (player1.id, player2.id),
						timeout=600.0
					)
				except a.TimeoutError:
					await boardmsg.edit(
						content=i18n(ctx, 'connect4/game-timeout', 600), embed=None
					)
					await boardmsg.clear_reactions()
					return
				if str(reaction) == DOWN:
					msg = await reaction.message.channel.send(embed=d.Embed(
						title=i18n(ctx, 'connect4/board-title'),
						description=boardmsgcont,
						color=0xff0000
					))
					for reg in regs:
						await msg.add_reaction(reg)
					await msg.add_reaction(DOWN)
					boardmsg = msg
					await reaction.message.delete()
			idx = regs.index(str(reaction))
			hit = False
			for rown in range(len(board[idx])):
				if board[idx][rown] != BLACK:
					board[idx][rown-1] = RED
					hit = True
					break
			if not hit:
				board[idx][-1] = RED
			if board[idx].count(BLACK) == 0:
				regs[idx] = NEIN
			redwon, bluewon = checkwin(board, RED), checkwin(board, BLUE)
			if redwon or bluewon:
				break
			boardmsgcont = constructboard(ctx, board, (player1, player2), 1)
			await boardmsg.edit(embed=d.Embed(
				title=i18n(ctx, 'connect4/board-title'),
				description=boardmsgcont,
				color=0x55acee
			))
			try:
				await boardmsg.remove_reaction(reaction, user)
			except d.NotFound:
				pass
			reaction = DOWN
			while str(reaction) == DOWN:
				try:
					reaction, user = await self.bot.wait_for(
						'reaction_add',
						check=lambda r, u: \
							r.message.id == boardmsg.id \
							and str(r) in regs \
							and str(r) != NEIN \
							and u.id == player2.id \
							or r.message.id == boardmsg.id \
							and str(r) == DOWN \
							and u.id in (player1.id, player2.id),
						timeout=600.0
					)
				except a.TimeoutError:
					await boardmsg.edit(
						content=i18n(ctx, 'connect4/game-timeout', 600),
						embed=None
					)
					await boardmsg.clear_reactions()
					return
				if str(reaction) == DOWN:
					msg = await reaction.message.channel.send(embed=d.Embed(
						title=i18n(ctx, 'connect4/board-title'),
						description=boardmsgcont,
						color=0x55acee
					))
					for reg in regs:
						await msg.add_reaction(reg)
					await msg.add_reaction(DOWN)
					boardmsg = msg
					await reaction.message.delete()
			idx = regs.index(str(reaction))
			hit = False
			for rown in range(len(board[idx])):
				if board[idx][rown] != BLACK:
					board[idx][rown-1] = BLUE
					hit = True
					break
			if not hit:
				board[idx][-1] = BLUE
			if board[idx].count(BLACK) == 0:
				regs[idx] = NEIN
			redwon, bluewon = checkwin(board, RED), checkwin(board, BLUE)
		boardmsgcont = constructboard(ctx, board, (player1, player2), int(bluewon))
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
					' (' + (
						(player1.display_name)
						if redwon
						else (player2.display_name)
					) + ')',
					RED if bluewon else BLUE,
					' (' + (
						(player1.display_name)
						if bluewon
						else (player2.display_name)
					) + ')'
				),
				color=0xff0000 if redwon else 0x55acee
			)
		await ctx.send(embed=embed)
