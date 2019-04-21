import re
import random
import asyncio
from discord.ext.commands import group
from .games import Games
from .i18n import i18n, embed
from .utils import DummyCtx

GO_FISH_NAME = 'Go Fish'

class Card(object):
	SUITS = tuple('\u2660 \u2663 \u2665 \u2666'.split(' '))
	NUMBERS = tuple(('\U0001f1e6 2\u20e3 3\u20e3 4\u20e3 5\u20e3 6\u20e3'
		' 7\u20e3 8\u20e3 9\u20e3 \U0001f51f \U0001f1ef'
		' \U0001f1f6 \U0001f1f0').split(' '))

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
	"""card_games/cog-desc"""
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
		def stats(pid, footer, desc=None):
			emb = embed(dmx[pid],
				title=('card_games/fish-stats-title',),
				description=(
					i18n(dmx[pid], *desc)
					if desc
					else ('card_games/fish-stats-description',)
				),
				color=0x0000FF,
			)
			emb.add_field(
				name=i18n(dmx[pid], 'card_games/fish-stats-hand-title'),
				value=' '.join(str(c) for c in hands[pid]) \
					or i18n(dmx[pid], 'card_games/fish-stats-empty-hand'),
				inline=False
			)
			emb.add_field(
				name=i18n(dmx[pid], 'card_games/fish-stats-books-title'),
				value='\n'.join(
					' '.join(str(c) for c in b)
					for b in books[pid]
				) or i18n(dmx[pid], 'card_games/fish-stats-no-books'),
				inline=False
			)
			emb.add_field(
				name=i18n(dmx[pid], 'card_games/fish-stats-status-title'),
				value=i18n(dmx[pid], footer),
				inline=False
			)
			return emb
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
				await dmx[pid].send(embed=embed(dmx[pid],
					title=('card_games/fish-checkbooks-title',),
					description='\n'.join(
						' '.join(str(c) for c in b)
						for b in newbooks
					),
					color=0x55acee
				))
		for pid in range(len(players)):
			await checkbooks(pid)
		for i, dm in enumerate(dmx[1:]):
			await dm.send(embed=stats(i+1, 'card_games/fish-m-wait'))
		pid = 0
		while all(hands) and deck and len(players) > 1:
			pid %= len(players)
			player = players[pid]
			matches = True
			for pid2, player2 in enumerate(players):
				if player2 == player:
					continue
				await player2.send(embed=embed(dmx[pid2],
					title=('card_games/fish-turn-title',),
					description=(
						'card_games/fish-turn',
						player.display_name
					),
					color=0xffffff
				))
			await dmx[pid].send(embed=stats(
				pid, 'card_games/fish-m-card'
			))
			timedout = False
			while matches and hands[pid]:
				num = (
					'A', '2', '3', '4', '5', '6', '7', '8', '9',
					'10', 'J', 'Q', 'K'
				)
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
					n = num.index(m.content.upper().strip())
					for card in hands[pid]:
						if card.number == n:
							return True
					return False
				try:
					msg = await self.bot.wait_for(
						'message',
						check=checc,
						timeout=600.0
					)
				except asyncio.TimeoutError:
					await player.send(embed=embed(dmx[pid],
						title=('card_games/fish-timed-out-title',),
						description=('card_games/fish-timed-out', 600),
						color=0xff0000
					))
					del players[pid]
					del dmx[pid]
					deck.extend(hands[pid])
					random.shuffle(deck)
					del hands[pid]
					del books[pid]
					timedout = True
					break
				num = num.index(msg.content.upper().strip())
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
						await dmx[pid2].send(embed=embed(dmx[pid2],
							title=('card_games/fish-card-taken-title',),
							description=(
								'card_games/fish-card-taken',
								player.display_name,
								Card.NUMBERS[num],
								count
							),
							color=0xff0000
						))
						hands[pid].extend(matches)
				if matches:
					hands[pid].sort(key=lambda c: c.number)
					await checkbooks(pid)
					if not hands[pid]:
						break
					await dmx[pid].send(
						embed=stats(pid, 'card_games/fish-m-card', (
							'card_games/fish-card-got',
							' '.join(str(c) for c in matches)
						))
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
							await dmx[pid2].send(embed=embed(dmx[pid2],
								title=('card_games/fish-card-missed-title',),
								description=(
									'card_games/fish-card-missed-unsafe',
									player.display_name,
									Card.NUMBERS[num],
									count
								),
								color=0xff8080
							))
						await dmx[pid].send(embed=stats(pid,
							'card_games/fish-m-card', (
								'card_games/fish-fish-got',
								Card.NUMBERS[num]
							)
						))
					else:
						for pid2, player2 in enumerate(players):
							if player2 == player:
								continue
							await dmx[pid2].send(embed=embed(dmx[pid2],
								title=('card_games/fish-card-missed-title',),
								description=(
									'card_games/fish-card-missed',
									player.display_name,
									Card.NUMBERS[num],
									count
								),
								color=0x55acee
							))
						await dmx[pid].send(
							embed=stats(pid, 'card_games/fish-m-wait', (
								'card_games/fish-fish', draw
							))
						)
			if not timedout:
				pid += 1
		if not (len(players) > 1):
			for dm in dmx:
				await dm.send(embed=embed(dm,
					title=('card_games/fish-all-timed-out-title',),
					description=('card_games/fish-all-timed-out',),
					color=0xff0000
				))
			return
		books = tuple(map(len, books))
		max_books = max(books)
		winners = [i for i, j in enumerate(books) if j == max_books]
		winners = tuple(players[i] for i in winners)
		if len(winners) > 1:
			for dm in dmx:
				await dm.send(embed=embed(dm,
					title=('card_games/fish-winners-title',),
					description=(
						'card_games/fish-winners',
						i18n(dm, 'comma-sep').join(
							player.display_name for player in winners[:-1]
						)
						+ i18n(dm, 'and-sep')
						+ winners[-1].display_name
					),
					color=0x55acee
				))
		else:
			for dm in dmx:
				await dm.send(embed=embed(dm,
					title=('card_games/fish-winner-title',),
					description=(
						'card_games/fish-winner',
						winners[0].display_name
					),
					color=0x55acee
				))

	@group(invoke_without_command=True, description='card_games/fish-cmd-desc')
	async def fish(self, ctx):
		"""card_games/fish-cmd-help"""
		await ctx.send(embed=embed(ctx,
			title=('error',),
			description=('card_games/fish-join', ctx.prefix),
			color=0xff0000
		))

	@fish.command(name='join', description='card_games/fish-join-desc')
	async def fish_join(self, ctx):
		await self._join_global_game(
			ctx, GO_FISH_NAME, self.do_fish,
			maxim=float('inf'), scn='fish start', jcn='fish join'
		)

	@fish.command(name='leave', description='card_games/fish-leave-desc')
	async def fish_leave(self, ctx):
		await self._unjoin_global_game(ctx, GO_FISH_NAME)

	@fish.command(name='start', description='card_games/fish-start-desc')
	async def fish_start(self, ctx):
		"""card_games/fish-start-help"""
		await self._start_global_game(ctx, GO_FISH_NAME, maxim=float('inf'))

	@fish.command(name='help', description='card_games/fish-help-desc')
	async def fish_help(self, ctx):
		if not ctx.author.dm_channel:
			await ctx.author.create_dm()
		await ctx.author.dm_channel.send(embed=embed(ctx,
			title=('games/help-title', GO_FISH_NAME),
			description=('card_games/fish-help', ctx.prefix),
			color=0x55acee
		))
