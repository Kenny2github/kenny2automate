import re
import random
import asyncio as a
import discord as d
from discord.ext.commands import command
from discord.ext.commands import bot_has_permissions
from .pm_games import PrivateGames
from .i18n import i18n

class DummyCtx(object):
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)

class Battleship(PrivateGames):
	@command()
	@bot_has_permissions(add_reactions=True, read_message_history=True)
	async def battleship(
		self, ctx, ascii: lambda x: x == 'yes' = 'no', against: d.Member = None
	):
		"""You sunk my battleship!
		Usage: ;battleship [ascii:yes|no] [@user]"""
		self.logger.info('battleship', extra={'ctx': ctx})
		try:
			player1, player2 = await self._gather_game(ctx, 'Battleship',
				against)
		except (TypeError, ValueError):
			return
		dmx1, dmx2 = (
			DummyCtx(
				send=player.dm_channel.send,
				channel=player.dm_channel,
				author=player
			)
			for player in (player1, player2)
		)
		LETTERS = list(
			chr(0x1f1e6 + i) for i in range(10)
		) if not ascii else 'ABCDEFGHIJ'
		NUMBERS = list(
			'{}\u20e3'.format(i) for i in range(10)
		) if not ascii else '0123456789'
		RED, BLUE, ORANGE = '\U0001f6a9\U0001f535\u26f5' if not ascii else '!~1'
		(
			LEFT, DBLLEFT, UP, DBLUP, DOWN, DBLDOWN,
			RIGHT, DBLRIGHT, LR, UD, CHECK
		) = CONTROLS = (
			'\u2b05', '\U0001f91b', '\u2b06', '\u23eb', '\u2b07', '\u23ec',
			'\u27a1', '\U0001f91c', '\u2194', '\u2195', '\u2705'
		)
		BLACK = '\u2b1b' if not ascii else '_'
		HIT, MISS = '\u274c\u2b55' if not ascii else 'XO'
		def boardmsg(board):
			descrip = ('`{}`' if ascii else '{}').format(
				BLACK + (' ' if ascii else '')
				+ (' ' if ascii else '').join(NUMBERS)
			)
			for i, let in enumerate(LETTERS):
				descrip += ('\n`{} {}`' if ascii else '\n{}{}').format(
					let, (' ' if ascii else '').join(board[i])
				)
			return descrip
		async def set_ships(dmx):
			board = [[BLUE for _ in range(10)] for _ in range(10)]
			embed = d.Embed(
				title=i18n(dmx, 'connect4/board-title'),
				description=boardmsg(board),
				footer=i18n(dmx, 'battleship/place-instructions')
			)
			msg = await dmx.send(embed=embed)
			for e in CONTROLS:
				await msg.add_reaction(e)
			for i in (2, 3, 3, 4, 5):
				x, y, dq = 0, 0, True
				while 1:
					tmpboard = [[a for a in b] for b in board]
					for j in range(i):
						if dq:
							tmpboard[y][x + j] = ORANGE
						else:
							tmpboard[y + j][x] = ORANGE
					embed.description = boardmsg(tmpboard)
					await msg.edit(embed=embed)
					reaction, _ = await self.bot.wait_for('reaction_remove',
						check=lambda r, u: (
							r.emoji in CONTROLS
							and r.message.id == msg.id
						)
					)
					if reaction.emoji == CHECK:
						board = tmpboard
						break
					elif reaction.emoji == UP:
						if y > 0:
							y -= 1
					elif reaction.emoji == DBLUP:
						if (y - 2) >= 0:
							y -= 2
					elif reaction.emoji == LEFT:
						if x > 0:
							x -= 1
					elif reaction.emoji == DBLLEFT:
						if (x - 2) >= 0:
							x -= 2
					elif reaction.emoji == RIGHT:
						if not dq:
							if x < 9:
								x += 1
						else:
							if x < (10 - i):
								x += 1
					elif reaction.emoji == DBLRIGHT:
						if not dq:
							if (x + 2) <= 9:
								x += 2
						else:
							if (x + 2) <= (10 - i):
								x += 2
					elif reaction.emoji == DOWN:
						if not dq:
							if y < (10 - i):
								y += 1
						else:
							if y < 9:
								y += 1
					elif reaction.emoji == DBLDOWN:
						if not dq:
							if (y + 2) <= (10 - i):
								y += 2
						else:
							if (y + 2) <= 9:
								y += 2
					elif reaction.emoji == LR:
						if x < (10 - i):
							dq = True
					elif reaction.emoji == UD:
						if y < (10 - i):
							dq = False
			await msg.delete()
			return (board, embed)
		(board1, embed1), (board2, embed2) = await a.gather(
			set_ships(dmx1), set_ships(dmx2)
		)
		embed1.set_footer()
		embed2.set_footer()
		msg1 = await dmx1.send(embed=embed1)
		msg2 = await dmx2.send(embed=embed2)
		hit1, hit2 = [
			[BLUE for _ in range(10)] for _ in range(10)
		], [
			[BLUE for _ in range(10)] for _ in range(10)
		]
		embed3, embed4 = d.Embed(
			title='Hitboard',
			description=boardmsg(hit1)
		), d.Embed(
			title='Hitboard',
			description=boardmsg(hit2)
		)
		embed3.set_footer(text=i18n(dmx1, 'battleship/fire-instructions'))
		embed4.set_footer(text=i18n(dmx2, 'battleship/wait-instructions'))
		msg3 = await dmx1.send(embed=embed3)
		msg4 = await dmx2.send(embed=embed4)
		def checklost(board):
			for i in board:
				for j in i:
					if j == ORANGE:
						return False
			return True
		exp = re.compile('^(?:[a-j][0-9]|[0-9][a-j])$')
		def checc1(m):
			if m.channel.id != dmx1.channel.id:
				return False
			match = re.search(exp, m.content.lower())
			if not match:
				return False
			letter, number = (
				re.search('[a-j]', m.content.lower()).group(0),
				re.search('[0-9]', m.content.lower()).group(0)
			)
			letter, number = (
				'abcdefghij'.index(letter),
				'0123456789'.index(number)
			)
			return hit1[letter][number] == BLUE
		def checc2(m):
			if m.channel.id != dmx2.channel.id:
				return False
			match = re.search(exp, m.content.lower())
			if not match:
				return False
			letter, number = (
				re.search('[a-j]', m.content.lower()).group(0),
				re.search('[0-9]', m.content.lower()).group(0)
			)
			letter, number = (
				'abcdefghij'.index(letter),
				'0123456789'.index(number)
			)
			return hit2[letter][number] == BLUE
		def idxes(s):
			letter, number = (
				re.search('[a-j]', s.lower()).group(0),
				re.search('[0-9]', s.lower()).group(0)
			)
			letter, number = (
				'abcdefghij'.index(letter),
				'0123456789'.index(number)
			)
			return (letter, number)
		lost1, lost2 = checklost(board1), checklost(board2)
		while not any((lost1, lost2)):
			msg = await self.bot.wait_for('message', check=checc1)
			letter, number = idxes(msg.content)
			if board2[letter][number] == BLUE:
				hit1[letter][number] = MISS
				board2[letter][number] = MISS
			elif board2[letter][number] == ORANGE:
				hit1[letter][number] = HIT
				board2[letter][number] = RED
			embed2.description = boardmsg(board2)
			await msg2.edit(embed=embed2)
			embed3.description = boardmsg(hit1)
			embed3.set_footer(text=i18n(dmx1, 'battleship/wait-instructions'))
			embed4.set_footer(text=i18n(dmx2, 'battleship/fire-instructions'))
			await msg3.edit(embed=embed3)
			await msg4.edit(embed=embed4)
			lost1, lost2 = checklost(board1), checklost(board2)
			if lost1 or lost2:
				break
			msg = await self.bot.wait_for('message', check=checc2)
			letter, number = idxes(msg.content)
			if board1[letter][number] == BLUE:
				hit2[letter][number] = MISS
				board1[letter][number] = MISS
			elif board1[letter][number] == ORANGE:
				hit2[letter][number] = HIT
				board1[letter][number] = RED
			embed1.description = boardmsg(board1)
			await msg1.edit(embed=embed1)
			embed4.description = boardmsg(hit2)
			embed3.set_footer(text=i18n(dmx1, 'battleship/fire-instructions'))
			embed4.set_footer(text=i18n(dmx2, 'battleship/wait-instructions'))
			await msg4.edit(embed=embed4)
			await msg3.edit(embed=embed3)
			lost1, lost2 = checklost(board1), checklost(board2)
		del msg1, msg2, msg3, msg4, embed1, embed2, embed3, embed4
		won_embed = d.Embed(
			title=i18n(dmx2 if lost1 else dmx1, 'battleship/won-title'),
			description=i18n(dmx2 if lost1 else dmx1, 'battleship/won')
		)
		lost_embed = d.Embed(
			title=i18n(dmx1 if lost1 else dmx2, 'battleship/lost-title'),
			description=i18n(dmx1 if lost1 else dmx2, 'battleship/lost')
		)
		embed1 = lost_embed if lost1 else won_embed
		embed2 = lost_embed if lost2 else won_embed
		await dmx1.send(embed=embed1)
		await dmx2.send(embed=embed2)
