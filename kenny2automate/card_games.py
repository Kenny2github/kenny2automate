import re
import random
import discord as d
from discord.ext.commands import command, group
from discord.ext.commands import bot_has_permissions
from .games import Games, DummyCtx
from .i18n import i18n

class Card(object):
	SUITS = tuple('\u2660 \u2663 \u2665 \u2666'.split(' '))
	NUMBERS = tuple('\U0001f1e6 2\u20e3 3\u20e3 4\u20e3 5\u20e3 6\u20e3 7\u20e3 8\u20e3 9\u20e3 \U0001f51f \U0001f1ef \U0001f1f6 \U0001f1f0'.split(' '))

	suit = 0
	number = 0

	def __init__(self, suit=0, number=0):
		self.suit = suit
		self.number = number

	def __repr__(self):
		return self.NUMBERS[self.number] + self.SUITS[self.suit]

	__str__ = __repr__

	def __hash__(self):
		return hash((self.suit, self.number))

	def __eq__(self, other):
		return hash(self) == hash(other)

class CardGames(Games):
	async def do_fish(self, ctxs):
		players = [ctx.author for ctx in ctxs]
		deck = [Card(i, j) for i in range(4) for j in range(13)]
		random.shuffle(deck)
		dmx = [
			DummyCtx(
				send=player.dm_channel.send,
				channel=player.dm_channel,
				author=player
			)
			for player in players
		]
		hands = [[deck.pop() for _ in range(7)] for _ in players]
		for hand in hands:
			hand.sort(key=lambda c: c.number)
		books = [[] for _ in players]
		def stats(pid, footer):
			embed = d.Embed(
				title=i18n(dmx[pid], 'card_games/fish-stats-title'),
				description=i18n(dmx[pid], 'card_games/fish-stats-description'),
				color=0x0000FF,
			)
			embed.add_field(
				name=i18n(dmx[pid], 'card_games/fish-stats-hand-title'),
				value=' '.join(str(c) for c in hands[pid]) \
					or i18n(dmx[pid], 'card_games/fish-stats-empty-hand'),
				inline=False
			)
			embed.add_field(
				name=i18n(dmx[pid], 'card_games/fish-stats-books-title'),
				value='\n'.join(
					' '.join(str(c) for c in b)
					for b in books[pid]
				) or i18n(dmx[pid], 'card_games/fish-stats-no-books'),
				inline=False
			)
			embed.add_field(
				name=i18n(dmx[pid], 'card_games/fish-stats-status-title'),
				value=footer,
				inline=False
			)
			return embed
		async def checkbooks(pid):
			counts = {}
			newbooks = []
			for card in hands[pid]:
				if card.number not in counts:
					counts[card.number] = 1
				else:
					counts[card.number] += 1
			for num, count in counts.items():
				if count >= 4:
					newbook = [c for c in hands[pid] if c.number == num]
					newbook.sort(key=lambda c: c.suit)
					newbooks.append(newbook)
					books[pid].append(newbook)
					hands[pid] = [
						c
						for c in hands[pid]
						if c.number != num
					]
			if newbooks:
				await dmx[pid].send(embed=d.Embed(
					title=i18n(dmx[pid], 'card_games/fish-checkbooks-title'),
					description='\n'.join(
						' '.join(str(c) for c in b)
						for b in newbooks
					)
				))
		for pid in range(len(players)):
			await checkbooks(pid)
		for i, dm in enumerate(dmx[1:]):
			await dm.send(embed=stats(i+1, i18n(dm, 'card_games/fish-m-wait')))
		while all(hands) and deck:
			for pid, player in enumerate(players):
				matches = True
				for pid2, player2 in enumerate(players):
					if player2 == player:
						continue
					await dmx[pid2].send(i18n(
						dmx[pid2],
						'card_games/fish-turn',
						player.display_name
					))
				await dmx[pid].send(embed=stats(
					pid, i18n(dmx[pid], 'card_games/fish-m-card')
				))
				while matches and hands[pid]:
					def checc(m):
						if (
							m.channel.id != dmx[pid].channel.id
							or m.author.id != player.id
						):
							return False
						if not re.fullmatch(
							'(?:[JQKA2-9]|10)',
							m.content,
							re.I
						):
							return False
						num = (
							'A', '2', '3', '4', '5', '6', '7', '8', '9',
							'10', 'J', 'Q', 'K'
						).index(m.content.upper())
						for card in hands[pid]:
							if card.number == num:
								return True
						return False
					msg = await ctx.bot.wait_for('message', check=checc)
					num = (
						'A', '2', '3', '4', '5', '6', '7', '8', '9',
						'10', 'J', 'Q', 'K'
					).index(msg.content.upper().strip())
					matches = []
					for pid2, player2 in enumerate(players):
						if player2 == player:
							continue
						matches2 = [c for c in hands[pid2] if c.number == num]
						matches.extend(matches2)
						count = len(matches2)
						hands[pid2] = [
							c
							for c in hands[pid2]
							if c.number != num
						]
						if matches2:
							await dmx[pid2].send(i18n(
								dmx[pid2],
								'card_games/fish-card-taken',
								player.display_name,
								Card.NUMBERS[num],
								count
							))
							hands[pid].extend(matches)
					if matches:
						hands[pid].sort(key=lambda c: c.number)
						await checkbooks(pid)
						if not hands[pid]:
							break
						await dmx[pid].send(
							content=i18n(
								dmx[pid],
								'card_games/fish-card-got',
								' '.join(str(c) for c in matches)),
							embed=stats(pid, i18n(dmx[pid], 'card_games/fish-m-card'))
						)
					else:
						draw = deck.pop()
						hands[pid].append(draw)
						hands[pid].sort(key=lambda c: c.number)
						await checkbooks(pid)
						if not hands[pid]:
							break
						if draw.number == num:
							matches = True
							for pid2, player2 in enumerate(players):
								if player2 == player:
									continue
								await dmx[pid2].send(i18n(
									dmx[pid2],
									'card_games/fish-card-missed-unsafe',
									player.display_name,
									Card.NUMBERS[num],
									count
								))
							await dmx[pid].send(
								content=i18n(
									dmx[pid],
									'card_games/fish-fish-got',
									Card.NUMBERS[num]
								),
								embed=stats(pid, i18n(
									dmx[pid], 'card_games/fish-m-card'
								))
							)
						else:
							for pid2, player2 in enumerate(players):
								if player2 == player:
									continue
								await dmx[pid2].send(i18n(
									dmx[pid2],
									'card_games/fish-card-missed',
									player.display_name,
									Card.NUMBERS[num],
									count
								))
							await dmx[pid].send(
								content=i18n(
									dmx[pid], 'card_games/fish-fish', draw
								),
								embed=stats(pid, i18n(
									dmx[pid], 'card_games/fish-m-wait'
								))
							)
				if not (all(hands) and deck):
					break
		books = tuple(map(len, books))
		max_books = max(books)
		winners = [i for i, j in enumerate(books) if j == max_books]
		winners = tuple(players[i] for i in winners)
		if len(winners) > 1:
			for dm in dmx:
				await dm.send(embed=d.Embed(
					title=i18n(dm, 'card_games/fish-winners-title'),
					description=i18n(
						dm,
						'card_games/fish-winners',
						i18n(dm, 'card_games/fish-winners-sep').join(
							player.display_name for player in winners[:-1]
						)
						+ i18n(dm, 'card_games/fish-winners-lastsep')
					)
				))
		else:
			for dm in dmx:
				await dm.send(embed=d.Embed(
					title=i18n(dm, 'card_games/fish-winner-title'),
					description=i18n(dm, 'card_games/fish-winner', winners[0].display_name)
				))

#	@group()
#	async def fish(self, ctx):
#		"""Play Go Fish!"""
#		await ctx.send(i18n(ctx, 'fish/fish-join'))
#
#	@fish.command(name='join')
#	async def fish_join(self, ctx):
#		await self._join_global_game(ctx, 'Go Fish', self.do_fish, float('inf'))
#
#	@fish.command(name='leave')
#	async def fish_leave(self, ctx):
#		await self._unjoin_global_game(ctx, 'Go Fish')
#
#	@fish.command(name='start')
#	async def fish_start(self, ctx):
#		if ctx.author.id != self._global_games['Go Fish']['ctxs'][0].author.id:
#			return
#		await self._start_global_game(ctx, 'Go Fish', float('inf'))
