#low-level
import os
import re
import math
import random
#mid-level
import asyncio
from enum import IntEnum
#3rd-party
from pygame import Surface, SRCALPHA
import pygame.image
import discord
from discord.ext.commands import group
#relative
from .games import Games
from .i18n import i18n, embed
from .utils import DummyCtx, lone_group, background
from .tmpfiles import sendsurf

UNO_CARDS = os.path.join('resources', 'card_games', 'uno')
UNO_SIZE = UNO_WIDTH, UNO_HEIGHT = 241, 361
SET_CARDS = os.path.join('resources', 'card_games', 'set')
SET_SIZE = SET_WIDTH, SET_HEIGHT = 320, 180

def unoimg(name):
	return os.path.join(UNO_CARDS, name + '.png')

def setimg(name):
	return os.path.join(SET_CARDS, name + '.png')

class Card:
	SUITS = ('<:spades:701646576153526353>', '<:clubs:701646604347637801>',
			 '\u2665', '\u2666')
	NUMBERS = ('\U0001f1e6', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3',
		'6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f', '\U0001f1ef',
		'\U0001f1f6', '\U0001f1f0')
	ASCII_NUMBERS = (
		'A', '2', '3', '4', '5', '6', '7',
		'8', '9', '10', 'J', 'Q', 'K'
	)

	suit = 0
	number = 0

	def __init__(self, suit=0, number=0):
		self.suit = suit
		self.number = number

	def __repr__(self):
		return self.ASCII_NUMBERS[self.number] + ('S', 'C', 'H', 'D')[self.suit]

	def __str__(self):
		return self.NUMBERS[self.number] + '\u2060' + self.SUITS[self.suit]

	def __hash__(self):
		return hash((self.suit, self.number))

	def __eq__(self, other):
		return hash(self) == hash(other)

class UnoCard(Card):
	SUITS = ('red', 'yellow', 'green', 'blue')
	COLORS = ((255, 0, 0), (0xff, 0xdd, 0), (0, 0xdd, 0), (0x55, 0x55, 0xff))
	NUMBERS = tuple(map(str, range(10))) + ('skip', 'reverse', 'draw2')

	suit = 0
	number = 0

	def __init__(self, suit=0, number=0):
		super().__init__(suit, number)
		self.image = pygame.image.load(unoimg(
			self.SUITS[suit] + '-' + self.NUMBERS[number]
		))

	@property
	def worth(self):
		if self.number < 10:
			return self.number
		return 10

class SpecialUnoCard(UnoCard):
	draw4 = False
	suit = number = 13
	def __init__(self, draw4: bool):
		self.image = pygame.image.load(unoimg('draw4' if draw4 else 'wild'))
		self.draw4 = draw4

class SetCard:
	SHADES = ('filled', 'empty', 'cross')
	SHAPES = ('circle', 'square', 'octagon')
	COLORS = ('red', 'green', 'blue')
	NUMBERS = ('1', '2', '3')

	shape = 0
	color = 0
	number = 0
	shade = 0

	def __init__(self, shade=0, shape=0, color=0, number=0):
		if not isinstance(shade, int):
			shade = self.SHADES.index(shade)
		if not isinstance(shape, int):
			shape = self.SHAPES.index(shape)
		if not isinstance(color, int):
			color = self.COLORS.index(color)
		if not isinstance(number, int):
			number = self.NUMBERS.index(number)
		self.shade = shade
		self.shape = shape
		self.color = color
		self.number = number
		self.image = pygame.image.load(setimg(
			'{}-{}-{}-{}'.format(
				self.SHADES[self.shade],
				self.SHAPES[self.shape],
				self.COLORS[self.color],
				self.NUMBERS[self.number]
			)
		))

	def __repr__(self):
		return '{0}({1.shade}, {1.shape}, {1.color}, {1.number})'.format(
			type(self).__name__, self
		)

	def __str__(self):
		return '{}({!r}, {!r}, {!r}, {!r})'.format(
			type(self).__name__,
			self.SHADES[self.shade],
			self.SHAPES[self.shape],
			self.COLORS[self.color],
			self.NUMBERS[self.number]
		)

	def __hash__(self):
		return hash((self.shade, self.shape, self.color, self.number))

	def __eq__(self, other):
		return hash(self) == hash(other)

	def isset(self, other1, other2):
		for attr in ('shade', 'shape', 'color', 'number'):
			if len({getattr(self, attr), getattr(other1, attr),
					getattr(other2, attr)}) not in {1, 3}:
				return False
		return True

class BigTwoCard(Card):
	_SUITS = (3, 1, 2, 0) # indexes in Card.SUITS, in Big Two precedence order
	_NUMBERS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 1) # likewise

	@property
	def _suit(self):
		return self._SUITS.index(self.suit)
	@property
	def _number(self):
		return self._NUMBERS.index(self.number)
	def __lt__(self, other):
		if not isinstance(other, type(self)):
			return NotImplemented
		if self.number == other.number:
			return self._suit < other._suit
		return self._number < other._number
	def __le__(self, other):
		if not isinstance(other, type(self)):
			return NotImplemented
		return self < other or self == other
	def __gt__(self, other):
		if not isinstance(other, type(self)):
			return NotImplemented
		return not self <= other
	def __ge__(self, other):
		if not isinstance(other, type(self)):
			return NotImplemented
		return not self < other

class BigTwoTricks(IntEnum):
	SINGLE = 0
	PAIR = 1
	TRIPLET = 2
	STRAIGHT = 3
	FLUSH = 4
	FULLHOUSE = 5
	QUADRUPLET = 6
	STRAIGHTFLUSH = 7

class BigTwoTrick:
	cards = []
	trick = 0
	def __init__(self, cards, trick):
		self.cards = cards
		self.cards.sort()
		self.trick = BigTwoTricks(trick)
		getattr(self, 'check_' + self.trick.name.casefold(), self.error)()

	def error(self):
		raise ValueError('Invalid trick')

	def check_straightflush(self):
		if len(self.cards) != 5:
			raise ValueError('Straight flush consists of 5 cards')
		self.check_straight()
		self.check_flush()

	def check_quadruplet(self):
		if len(self.cards) != 5:
			raise ValueError('Four-of-a-kind consists of 5 cards')
		if self.cards[0].number == self.cards[1].number:
			cards = self.cards[:-1]
		else:
			cards = self.cards[1:]
		if any(cards[i].number != cards[i+1].number for i in range(3)):
			raise ValueError('Not four-of-a-kind')

	def check_fullhouse(self):
		if len(self.cards) != 5:
			raise ValueError('Full house consists of 5 cards')
		cards = self.cards
		if cards[0].number != cards[1].number \
				or cards[-1].number != cards[-2].number:
			# after sorting, the first two and last two must each be equal
			# only the middle can differ from one side
			raise ValueError('Not full house')
		if cards[2].number not in (cards[0].number, cards[-1].number):
			# middle card must be same as start or end card
			raise ValueError('Not full house')

	def check_flush(self):
		if len(self.cards) != 5:
			raise ValueError('Flush consists of 5 cards')
		if any(self.cards[i].suit != self.cards[i+1].suit for i in range(4)):
			# not same suit
			raise ValueError('Not flush')

	def check_straight(self):
		if len(self.cards) != 5:
			raise ValueError('Straight consists of 5 cards')
		if any(self.cards[i]._number + 1 != self.cards[i+1]._number
				for i in range(4)):
			raise ValueError('Not straight') # must be sequential
		if sum(card.number in range(3) for card in self.cards) >= 3:
			raise ValueError('Straight cannot have A, 2, and 3 at once')

	def check_triplet(self):
		if len(self.cards) != 3:
			raise ValueError('Triplet consists of 3 cards')
		if any(self.cards[i].number != self.cards[i].number for i in range(2)):
			raise ValueError('Not triplet')

	def check_pair(self):
		if len(self.cards) != 2:
			raise ValueError('Pair consists of 2 cards')
		if self.cards[0].number != self.cards[1].number:
			raise ValueError('Not pair')

	def check_single(self):
		if len(self.cards) != 1:
			raise ValueError('dude a single is one card, how hard can it be')

	def __eq__(self, other):
		return self is other

	def __lt__(self, other):
		if not isinstance(other, type(self)):
			return NotImplemented
		if self.trick != other.trick:
			return self.trick < other.trick
		if self.trick in (
				BigTwoTricks.SINGLE, BigTwoTricks.PAIR, BigTwoTricks.TRIPLET
		):
			return max(self.cards) < max(other.cards)
		if self.trick in (
				BigTwoTricks.STRAIGHT, BigTwoTricks.FLUSH,
				BigTwoTricks.STRAIGHTFLUSH
		):
			return any(i < j for i, j in
					   zip(self.cards[::-1], other.cards[::-1]))
		if self.trick in (BigTwoTricks.FULLHOUSE, BigTwoTricks.QUADRUPLET):
			return self.cards[2]._number < other.cards[2]._number

	def __le__(self, other):
		return self == other or self < other

	def __gt__(self, other):
		return not self <= other

	def __ge__(self, other):
		return not self < other

class Fish(Games):
	"""fish/cog-desc"""

	DECK = [Card(i, j) for i in range(4) for j in range(13)]

	async def do_fish(self, ctxs, specs):
		players = [ctx.author for ctx in ctxs]
		deck = self.DECK[:]
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
				title=('fish/fish-stats-title',),
				description=(
					i18n(dmx[pid], *desc)
					if desc
					else ('fish/fish-stats-description',)
				),
				color=0x0000FF,
			)
			emb.add_field(
				name=i18n(dmx[pid], 'fish/fish-stats-hand-title'),
				value=' '.join(str(c) for c in hands[pid]) \
					or i18n(dmx[pid], 'fish/fish-stats-empty-hand'),
				inline=False
			)
			emb.add_field(
				name=i18n(dmx[pid], 'fish/fish-stats-books-title'),
				value='\n'.join(
					' '.join(str(c) for c in b)
					for b in books[pid]
				) or i18n(dmx[pid], 'fish/fish-stats-no-books'),
				inline=False
			)
			if len(players) <= 2:
				emb.add_field(
					name=i18n(dmx[pid], 'fish/fish-stats-status-title'),
					value=i18n(dmx[pid], footer),
					inline=False
				)
			return emb
		async def playerchoose(pid):
			msg = await dmx[pid].send(embed=embed(dmx[pid],
				title=('fish/fish-player-choice-title',),
				description='\n'.join(
					'{}: {}'.format(
						chr(48 + i) + chr(8419),
						str(j)
					) for i, j in enumerate(players)
					if i != pid
				),
				footer=('fish/fish-player-choice',),
				color=0xffff00
			))
			for i in range(len(players)):
				if i == pid:
					continue
				background(msg.add_reaction(chr(48 + i) + chr(8419)))
			return msg.id
		async def chooseplayer(pid, msgid):
			msg = await dmx[pid].channel.fetch_message(msgid)
			for r in msg.reactions:
				if r.count > 1:
					return ord(str(r)[0]) - 48
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
				background(dmx[pid].send(embed=embed(dmx[pid],
					title=('fish/fish-checkbooks-title',),
					description='\n'.join(
						' '.join(map(str, b))
						for b in newbooks
					),
					color=0x55acee
				)))
		await asyncio.gather(*(checkbooks(pid) for pid in range(len(players))))
		for i, dm in enumerate(dmx[1:]):
			background(dm.send(embed=stats(i+1, 'fish/fish-m-wait')))
		pid = 0
		while all(hands) and deck and len(players) > 1:
			pid %= len(players)
			player = players[pid]
			matches = True
			for player2 in players:
				if player2 == player:
					continue
				background(player2.send(embed=embed(player2,
					title=('fish/fish-turn-title',),
					description=(
						'fish/fish-turn',
						str(player)
					),
					color=0xfffffe
				)))
			await dmx[pid].send(embed=stats(
				pid, 'fish/fish-m-card'
			))
			timedout = False
			while matches and hands[pid]:
				num = Card.ASCII_NUMBERS
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
				chosen_pid = None
				if len(players) > 2:
					rmsg = await playerchoose(pid)
				try:
					while chosen_pid is None:
						msg = await self.bot.wait_for(
							'message',
							check=checc,
							timeout=600.0
						)
						if len(players) > 2:
							chosen_pid = await chooseplayer(pid, rmsg)
						else:
							chosen_pid = int(not pid)
				except asyncio.TimeoutError:
					background(player.send(embed=embed(dmx[pid],
						title=('fish/fish-timed-out-title',),
						description=('fish/fish-timed-out', 600),
						color=0xff0000
					)))
					del players[pid]
					del dmx[pid]
					deck.extend(hands[pid])
					random.shuffle(deck)
					del hands[pid]
					del books[pid]
					timedout = True
					break
				num = num.index(msg.content.upper().strip())
				matches = [c for c in hands[chosen_pid] if c.number == num]
				count = len(matches)
				hands[chosen_pid] = [
					c
					for c in hands[chosen_pid]
					if c.number != num
				]
				if matches:
					background(dmx[chosen_pid].send(embed=embed(dmx[chosen_pid],
						title=('fish/fish-card-taken-title',),
						description=(
							'fish/fish-card-taken',
							str(player),
							Card.NUMBERS[num],
							count
						),
						color=0xff0000
					)))
					for pid2, player2 in enumerate(players):
						if pid2 in {pid, chosen_pid}:
							continue
						background(dmx[pid2].send(embed=embed(dmx[pid2],
							title=('fish/fish-card-taken-title',),
							description=(
								'fish/fish-other-card-taken',
								str(player),
								str(players[chosen_pid]),
								Card.NUMBERS[num],
								count
							),
							color=0xff8080
						)))
				hands[pid].extend(matches)
				if matches:
					hands[pid].sort(key=lambda c: c.number)
					await checkbooks(pid)
					if not hands[pid]:
						break
					background(dmx[pid].send(
						embed=stats(pid, 'fish/fish-m-card', (
							'fish/fish-card-got',
							' '.join(str(c) for c in matches)
						))
					))
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
							if pid2 == pid:
								continue
							if pid2 != chosen_pid:
								background(dmx[pid2].send(embed=embed(dmx[pid2],
									title=('fish/fish-card-missed-title',),
									description=(
										'fish/fish-other-card-missed-unsafe',
										str(player),
										str(players[chosen_pid]),
										Card.NUMBERS[num],
										count
									),
									color=0xff8080
								)))
							else:
								background(dmx[pid2].send(embed=embed(dmx[pid2],
									title=('fish/fish-card-missed-title',),
									description=(
										'fish/fish-card-missed-unsafe',
										str(player),
										Card.NUMBERS[num],
										count
									),
									color=0xff8080
								)))
						background(dmx[pid].send(embed=stats(pid,
							'fish/fish-m-card', (
								'fish/fish-fish-got',
								Card.NUMBERS[num]
							)
						)))
					else:
						for pid2, player2 in enumerate(players):
							if pid2 == pid:
								continue
							if pid2 != chosen_pid:
								background(dmx[pid2].send(embed=embed(dmx[pid2],
									title=('fish/fish-card-missed-title',),
									description=(
										'fish/fish-other-card-missed',
										str(player),
										str(players[chosen_pid]),
										Card.NUMBERS[num],
										count
									),
									color=0x55acee
								)))
							else:
								background(dmx[pid2].send(embed=embed(dmx[pid2],
									title=('fish/fish-card-missed-title',),
									description=(
										'fish/fish-card-missed',
										str(player),
										Card.NUMBERS[num],
										count
									),
									color=0x55acee
								)))
						background(dmx[pid].send(
							embed=stats(pid, 'fish/fish-m-wait', (
								'fish/fish-fish', draw
							))
						))
			if not timedout:
				pid += 1
		if not (len(players) > 1):
			for dm in dmx:
				background(dm.send(embed=embed(dm,
					title=('fish/fish-all-timed-out-title',),
					description=('fish/fish-all-timed-out',),
					color=0xff0000
				)))
			return
		points = tuple(map(len, books))
		max_points = max(points)
		winners = {
			i for i, j in enumerate(points)
			if j == max_points
		}
		for player in players:
			background(player.send(embed=embed(player,
				title=('uno/uno-winners-title',),
				description=(
					'uno/winners',
					'\n'.join(
						i18n(player, 'fish/point', str(players[i]), points[i])
						for i in winners
					)
				),
				fields=((
					('uno/points',),
					'\n'.join(
						i18n(player, 'fish/point', str(p), points[i])
						for i, p in enumerate(players)
						if i not in winners
					) or i18n(player, 'none'),
					False
				),),
				color=0x55acee
			)))

	name = 'Go Fish'
	coro = 'do_fish'
	maxim = 10
	minim = 2
	scn = 'fish start'
	jcn = 'fish join'

	@group(invoke_without_command=True, description='fish/fish-cmd-desc')
	@lone_group(True)
	async def fish(self, ctx):
		"""fish/fish-cmd-help"""
		pass

	@fish.command(name='here', description='fish/fish-here-desc')
	async def fish_here(self, ctx):
		players = await self._gather_multigame(ctx)
		if players:
			await self.do_fish(players, ())

	@fish.command(name='join', description='fish/fish-join-desc')
	async def fish_join(self, ctx):
		await self._join_global_game(ctx)

	@fish.command(name='leave', description='fish/fish-leave-desc')
	async def fish_leave(self, ctx):
		await self._unjoin_global_game(ctx)

	@fish.command(name='start', description='fish/fish-start-desc')
	async def fish_start(self, ctx):
		await self._start_global_game(ctx)

	@fish.command(name='help', description='fish/fish-help-desc')
	async def fish_help(self, ctx):
		await ctx.author.send(embed=embed(ctx,
			title=('games/help-title', self.name),
			description=('fish/fish-help', ctx.prefix),
			color=0x55acee
		))

class Uno(Games):
	"""uno/cog-desc"""

	DECK = [UnoCard(i, j) for i in range(4) for j in range(1, 13)]
	DECK.extend([UnoCard(i, 0) for i in range(4)])
	DECK.extend([SpecialUnoCard(True) for i in range(4)])
	DECK.extend([SpecialUnoCard(False) for i in range(4)])

	async def do_uno(self, ctxs, specs):
		players = [ctx.author for ctx in ctxs]
		deck = self.DECK[:]
		for i in deck[-8:]:
			i.suit = 13 #reset suits of wilds
		random.shuffle(deck)
		discard = [None]
		card = deck.pop()
		while card.worth == 10:
			deck.insert(random.randrange(108), card)
			card = deck.pop()
		discard[0] = card
		hands = [[deck.pop() for _ in range(7)] for _ in players]
		points = [0] * len(players)
		def handsurf(pid, bare=False):
			handlen = len(hands[pid])
			if handlen <= 0:
				return
			padding = UNO_WIDTH // 4
			surf = Surface(
				(UNO_WIDTH * handlen + UNO_WIDTH + padding, UNO_HEIGHT),
				SRCALPHA, 32
			)
			assert surf.get_width() > 0
			surf.fill((0, 0, 0, 0))
			color = UnoCard.COLORS[discard[0].suit]
			surf.fill(color, rect=(
				UNO_WIDTH - padding // 2, 0,
				padding * 2, UNO_HEIGHT
			))
			for i, j in enumerate(hands[pid]):
				surf.blit(j.image, (UNO_WIDTH + padding + UNO_WIDTH * i, 0))
			surf.blit(discard[0].image, (0, 0))
			background(sendsurf(
				players[pid].send, surf, 'uno', 'hand.png',
				embed=embed(players[pid],
					title=('uno/hand-title',),
					description=('uno/hand', points[pid]),
					fields=((
						('uno/card-numbers-title',),
						('uno/card-numbers',),
						False
					),) if not bare else None,
					footer=(
						('uno/waiting-for-card',)
						if can_turn(pid)
						else ('uno/cannot-turn',)
					) if not bare else None,
					color=discord.Color.from_rgb(*color)
				).set_image(url='attachment://hand.png')
			))
		def cards_drawn(cards, pid):
			player = players[pid]
			surf = Surface((UNO_WIDTH * len(cards), UNO_HEIGHT), SRCALPHA, 32)
			assert surf.get_width() > 0
			for i, j in enumerate(cards):
				surf.blit(j.image, (UNO_WIDTH * i, 0))
			background(sendsurf(
				player.send, surf, 'uno', 'cards.png',
				embed=embed(player,
					title=('uno/cards-drawn-title',),
					description=('uno/cards-drawn',),
					color=discord.Color.blurple()
				).set_image(url='attachment://cards.png')
			))
		def can_card(card, pid=None, chain=None):
			if isinstance(card, SpecialUnoCard):
				if not card.draw4:
					return True
				if pid is not None:
					for i in hands[pid]:
						if i == card or chain and i in chain:
							continue
						if can_card(i, pid, (chain or []) + [card]):
							return False
				return True
			if isinstance(discard[0], SpecialUnoCard):
				return card.suit == discard[0].suit
			if card.number == discard[0].number:
				return True
			if card.suit == discard[0].suit:
				return True
			return False
		def can_turn(pid):
			for i in hands[pid]:
				if can_card(i, pid):
					return True
			return False
		pid = 0
		dpid = 1
		for i in range(1, len(players)):
			handsurf(i, bare=True)
		while (deck or any(
			can_turn(i) for i in range(len(players))
		)) and len(players) > 1:
			pid %= len(players)
			player = players[pid]
			if not can_turn(pid):
				try:
					hands[pid].append(deck.pop())
					cards_drawn([hands[pid][-1]], pid)
				except IndexError:
					pass
			for hand in hands:
				hand.sort(key=lambda c: c.number)
				hand.sort(key=lambda c: c.suit)
			handsurf(pid)
			skipped = False
			turned = can_turn(pid)
			if turned:
				try:
					def checc(m):
						if not isinstance(m.channel, discord.DMChannel):
							return False
						if m.author.id != player.id:
							return False
						if not m.content.strip().lstrip('-+').isdecimal():
							return False
						num = int(m.content.strip())
						if num == 0 or abs(num) > len(hands[pid]):
							return False
						return can_card(hands[pid][
							(num - 1)
							if num > 0
							else num
						], pid)
					msg = await self.bot.wait_for(
						'message', check=checc,
						timeout=600.0
					)
					num = int(msg.content)
					card = hands[pid].pop((num - 1) if num > 0 else num)
					discard[0] = card
					if card.number > 9: #special function!
						if card.number == 10: #skip
							skipped = True
						if card.number == 11: #reverse
							if len(players) <= 2: #reverse is a skip for 2p
								skipped = True
							else:
								dpid = -dpid
						if card.number == 12: #draw2
							new_cards = [
								deck.pop()
								for _ in range(min(len(deck), 2))
							]
							if new_cards:
								hands[
									(pid + dpid) % len(players)
								].extend(new_cards)
								cards_drawn(new_cards, (pid + dpid) % len(players))
							skipped = True
						if card.number == 13: #wild of some sort
							msg = await player.send(embed=embed(player,
								title=('uno/choose-color-title',),
								description=('uno/choose-color',),
								color=0x55acee
							))
							HEARTS = '\u2764\U0001f49b\U0001f49a\U0001f499'
							for i in HEARTS:
								background(msg.add_reaction(i))
							reaction, user = await self.bot\
								.wait_for('reaction_add', check=lambda r, u: (
									u.id == player.id
									and r.message.id == msg.id
									and str(r) in HEARTS
								))
							color = HEARTS.index(str(reaction))
							card.suit = color
							if card.draw4: #it's a draw4!
								new_cards = [
									deck.pop()
									for _ in range(min(len(deck), 4))
								]
								if new_cards:
									hands[
										(pid + dpid) % len(players)
									].extend(new_cards)
									cards_drawn(new_cards, (pid+dpid) % len(players))
								skipped = True
				except asyncio.TimeoutError:
					background(player.send(embed=embed(player,
						title=('uno/uno-timed-out-title',),
						description=('uno/uno-timed-out', 600),
						color=0xff0000
					)))
					del players[pid]
					deck.extend(hands[pid])
					random.shuffle(deck)
					del hands[pid]
					del points[pid]
					continue
			if len(hands[pid]) == 1:
				for p in players:
					if p == player:
						continue
					background(p.send(embed=embed(p,
						title=('uno/uno-title',),
						description=('uno/uno', str(player)),
						color=0xff8080
					)))
			elif turned and len(hands[pid]) <= 0:
				points[pid] += 10
				hands[pid].extend(deck.pop() for _ in range(min(len(deck), 7)))
				for p in players:
					if p == player:
						continue
					background(p.send(embed=embed(p,
						title=('uno/empty-title',),
						description=('uno/empty', str(player)),
						color=0xff0000
					)))
			if turned:
				for p in players:
					if p == player:
						continue
					background(sendsurf(
						p.send, discard[0].image, 'uno', 'card.png',
						embed=embed(p,
							title=('uno/card-played-title',),
							description=('uno/card-played', str(player)),
							footer=('uno/turn', str(players[
								(pid + dpid + dpid * skipped) % len(players)
							])),
							color=discord.Color.from_rgb(*UnoCard.COLORS[discard[0].suit])
						).set_image(url='attachment://card.png')
					))
			else:
				for p in players:
					if p == player:
						continue
					background(p.send(embed=embed(p,
						title=('uno/turn-title',),
						description=(
							'uno/next-turn', str(player),
								str(players[
								(pid + dpid + dpid * skipped) % len(players)
							])
						),
						color=discord.Color.greyple()
					)))
			background(player.send(embed=embed(player,
				title=('uno/turn-title',),
				description=('uno/turn', str(players[
					(pid + dpid + dpid * skipped) % len(players)
				])),
				color=discord.Color.greyple()
			)))
			if skipped:
				pid += dpid
			pid += dpid
		for pid in range(len(players)):
			points[pid] -= sum(i.worth for i in hands[pid])
		max_points = max(points)
		winners = {
			i for i, j in enumerate(points)
			if j == max_points
		}
		for player in players:
			background(player.send(embed=embed(player,
				title=('uno/uno-winners-title',),
				description=(
					'uno/winners',
					'\n'.join(
						i18n(player, 'uno/point', str(players[i]), points[i])
						for i in winners
					)
				),
				fields=((
					('uno/points',),
					'\n'.join(
						i18n(player, 'uno/point', str(p), points[i])
						for i, p in enumerate(players)
						if i not in winners
					) or i18n(player, 'none'),
					False
				),),
				color=0x55acee
			)))

	name = 'Uno'
	coro = 'do_uno'
	maxim = float('inf')
	minim = 2
	scn = 'uno start'
	jcn = 'uno join'

	@group(invoke_without_command=True, description='uno/uno-cmd-desc')
	@lone_group(True)
	async def uno(self, ctx):
		"""uno/uno-cmd-help"""
		pass

	@uno.command(name='here', description='uno/uno-here-desc')
	async def uno_here(self, ctx):
		players = await self._gather_multigame(ctx)
		if players:
			await self.do_uno(players, ())

	@uno.command(name='join', description='uno/uno-join-desc')
	async def uno_join(self, ctx):
		await self._join_global_game(ctx)

	@uno.command(name='leave', description='uno/uno-leave-desc')
	async def uno_leave(self, ctx):
		await self._unjoin_global_game(ctx)

	@uno.command(name='start', description='uno/uno-start-desc')
	async def uno_start(self, ctx):
		"""uno/uno-start-help"""
		await self._start_global_game(ctx)

	@uno.command(name='help', description='uno/uno-help-desc')
	async def uno_help(self, ctx):
		await ctx.author.send(embed=embed(ctx,
			title=('games/help-title', self.name),
			description=('uno/uno-help', ctx.prefix),
			color=0x55acee
		))

class Blackjack(Games):
	"""blackjack/cog-desc"""

	DECK = Fish.DECK[:]

	async def do_blackjack(self, ctxs, specs):
		players = [ctx.author for ctx in ctxs]
		timedout = set()
		deck = self.DECK[:]
		random.shuffle(deck)
		cards = [[] for _ in players]
		pool = set()
		def pointpair(hand):
			sum1 = sum2 = 0
			for c in hand:
				if c.number == 0:
					sum1 += 1
					sum2 += 11
				elif c.number > 9:
					sum1 += 10
					sum2 += 10
				else:
					sum1 += c.number + 1
					sum2 += c.number + 1
			return (sum1, sum2)
		def cand(sum1, sum2):
			if sum1 > 21:
				return sum2
			if sum2 > 21:
				return sum1
			return max(sum1, sum2)
		async def foreach(pid):
			PLUS, CHEK = '\u2795\u2714'
			player = players[pid]
			cancelled = False
			try:
				done = False
				while not done:
					msg = await player.send(embed=embed(player,
						title=('blackjack/hand-title',),
						description=(
							'blackjack/hand',
							' '.join(map(str, hands[pid]))
						),
						color=0x0000ff
					))
					pts = cand(*pointpair(hands[pid]))
					if pts >= 21: #over even if A is 1
						return
					background(msg.add_reaction(PLUS))
					background(msg.add_reaction(CHEK))
					reaction, user = await self.bot.wait_for('reaction_add',
															 timeout=600.0,
															 check=lambda r, u: (
						r.message.id == msg.id
						and u.id == players[pid].id
						and str(r) in {PLUS, CHEK}
					))
					if str(reaction) == CHEK:
						return
					try:
						hands[pid].append(deck.pop())
					except IndexError:
						return
			except asyncio.TimeoutError:
				cancelled = True
				background(player.send(embed=embed(player,
					title=('fish/fish-timed-out-title',),
					description=('fish/fish-timed-out', 600),
					color=0xff0000
				)))
				deck.extend(hands[pid])
				deck.extend(cards[pid])
				hands[pid] = cards[pid] = []
				timedout.add(pid)
				random.shuffle(deck)
			except asyncio.CancelledError:
				cancelled = True
			finally:
				if not cancelled:
					await player.send(embed=embed(player,
						title=('blackjack/done-title',),
						description=('blackjack/done',),
						color=0xff8080
					))
		while len(players) - len(timedout) >= 2 and len(deck) >= len(players) * 2:
			hands = [
				[deck.pop(), deck.pop()]
				if i not in timedout
				else [] for i in players
			]
			for h in hands:
				h.sort(key=lambda c: c.number)
			msg = '\n'.join(
				'{}: {}'.format(str(p), hands[i][1])
				for i, p in enumerate(players)
				if i not in timedout
			)
			await asyncio.gather(*(p.send(embed=embed(p,
				title=('blackjack/starting-cards',),
				description=msg,
				color=0xfffffe
			)) for i, p in enumerate(players) if i not in timedout))
			await asyncio.gather(*(
				foreach(i)
				for i in range(len(players))
				if i not in timedout
			))
			max_points = 0
			poolq = False
			for i, h in enumerate(hands):
				if i in timedout:
					continue
				sum1, sum2 = pointpair(h)
				pts = cand(sum1, sum2)
				if pts > 21:
					continue
				if pts > max_points:
					max_points = pts
			if max_points == 0:
				poolq = True
			else:
				mpc = 0
				idx = 0
				for i, h in enumerate(hands):
					if i in timedout:
						continue
					if cand(*pointpair(h)) == max_points:
						idx = i
						mpc += 1
					if mpc > 1:
						poolq = True
						break
			for h in hands:
				for c in h:
					pool.add(c)
			if not poolq:
				cards[idx].extend(pool)
				pool = set()
				for i, p in enumerate(players):
					if i in timedout:
						continue
					background(p.send(embed=embed(p,
						title=('blackjack/round-over-title',),
						description=(
							'blackjack/round-over',
							str(players[idx]), max_points
						),
						color=0xff0000
					)))
			else:
				for i, p in enumerate(players):
					if i in timedout:
						continue
					background(p.send(embed=embed(p,
						title=('blackjack/round-over-title',),
						description=(
							'blackjack/round-over-pool', ' '.join(map(str, pool))
						),
						color=0xff8080
					)))
		points = tuple(map(len, cards))
		max_points = max(points)
		winners = {
			i for i, j in enumerate(points)
			if i not in timedout and j == max_points
		}
		for pid, player in enumerate(players):
			if pid in timedout:
				continue
			background(player.send(embed=embed(player,
				title=('uno/uno-winners-title',),
				description=(
					'uno/winners',
					'\n'.join(
						i18n(
							player, 'blackjack/point',
							str(players[i]), points[i]
						)
						for i in winners
						if i not in timedout
					)
				),
				fields=((
					('uno/points',),
					'\n'.join(
						i18n(player, 'blackjack/point', str(p), points[i])
						for i, p in enumerate(players)
						if i not in winners and i not in timedout
					) or i18n(player, 'none'),
					False
				),),
				color=0x55acee
			)))

	name = 'Blackjack'
	coro = 'do_blackjack'
	minim = 2
	maxim = float('inf')
	scn = 'blackjack start'
	jcn = 'blackjack join'

	@group(invoke_without_command=True, description='blackjack/blackjack-desc')
	@lone_group(True)
	async def blackjack(self, ctx):
		"""blackjack/blackjack-cmd-help"""
		pass

	@blackjack.command(name='here', description='blackjack/blackjack-here-desc')
	async def here(self, ctx):
		players = await self._gather_multigame(ctx)
		if players:
			await self.do_blackjack(players, ())

	@blackjack.command(description='blackjack/join-desc')
	async def join(self, ctx):
		await self._join_global_game(ctx)

	@blackjack.command(description='blackjack/leave-desc')
	async def leave(self, ctx):
		await self._unjoin_global_game(ctx)

	@blackjack.command(description='blackjack/start-desc')
	async def start(self, ctx):
		await self._start_global_game(ctx)

	@blackjack.command(description='blackjack/help-desc')
	async def help(self, ctx):
		await ctx.author.send(embed=embed(ctx,
			title=('games/help-title', self.name),
			description=('blackjack/help', ctx.prefix),
			color=0x55acee
		))

class SetGame(Games):
	"""setgame/cog-desc"""

	DECK = [
		SetCard(i, j, k, l)
		for i in range(3)
		for j in range(3)
		for k in range(3)
		for l in range(3)
	]

	COORD_REGEX = re.compile(r'^([a-c][0-9]+|[0-9]+[a-c])[,\s]+([a-c][0-9]+|[0-9]+[a-c])[,\s]+([a-c][0-9]+|[0-9]+[a-c])$', re.I)

	async def do_setgame(self, ctxs, specs):
		players = [ctx.author for ctx in ctxs]
		specs = [ctx.author for ctx in specs]
		deck = self.DECK[:]
		random.shuffle(deck)
		table = [deck.pop() for _ in range(9)]
		points = {p.id: 0 for p in players}
		def tablesurf(tab):
			tablen = len(tab)
			rows = math.ceil(tablen / 3)
			surf = Surface((SET_WIDTH * 3, SET_HEIGHT * rows), SRCALPHA, 32)
			assert surf.get_height() > 0
			surf.fill((0, 0, 0, 0))
			for i in range(rows):
				for j in range(3):
					if i * 3 + j > tablen:
						break
					surf.blit(tab[i * 3 + j].image, (SET_WIDTH * j, SET_HEIGHT * i))
			return surf
		def hasset(tab):
			for i in tab:
				for j in tab:
					for k in tab:
						if i is j or j is k or i is k:
							continue
						if i.isset(j, k):
							return True
			return False
		def sendcards(surf, hs):
			for p in players + specs:
				background(sendsurf(
					p.send, surf, 'set', 'table.png',
					embed=embed(p,
						title=('setgame/table-title',),
						description=(
							('setgame/table', points[p.id])
							if p in players else None
						),
						fields=(((
							('setgame/instructions-title',),
							('setgame/instructions',),
							False
						),) if hs else None) if p in players else None,
						footer=None if hs else ('setgame/nosets',),
						color=0xfffffe
					).set_image(url='attachment://table.png')
				))
		while deck:
			while len(table) < 12:
				try:
					table.append(deck.pop())
				except IndexError:
					pass
			surf = tablesurf(table)
			hs = hasset(table)
			sendcards(surf, hs)
			while deck and not hasset(table):
				for i in range(min(3, len(deck))):
					table.append(deck.pop())
				surf = tablesurf(table)
				hs = hasset(table)
				sendcards(surf, hs)
			if not deck and not hasset(table):
				break
			cards = []
			while not cards or not cards[0].isset(cards[1], cards[2]):
				try:
					msg = await self.bot.wait_for('message', check=lambda m: (
						self.COORD_REGEX.match(m.content)
						and m.author in players
						and isinstance(m.channel, discord.DMChannel)
					), timeout=600.0)
				except asyncio.TimeoutError:
					for p in players:
						background(p.send(embed=embed(p,
							title=('games/game-timeout-title',),
							description=('setgame/timed-out',),
							color=0xff0000
						)))
					return
				cards = [
					table[
						(int(re.search('[0-9]+', i).group(0)) - 1) * 3 #row
						+ 'abc'.index(re.search('[a-c]', i).group(0)) #col
					] for i in re.split(r'[,\s]+', msg.content.casefold())[:3]
				]
			for p in players:
				if p.id == msg.author.id:
					continue
				background(p.send(embed=embed(p,
					title=('setgame/set-called-title',),
					description=('setgame/set-called',
								 str(msg.author), msg.content),
					color=0xffff00
				)))
			for c in cards:
				table.remove(c)
			points[msg.author.id] += 1
			background(msg.author.send(embed=embed(msg.author,
				title=('setgame/added-points-title',),
				description=('setgame/added-points', points[msg.author.id]),
				color=0x55acee
			)))
		max_points = max(points.values())
		winners = {
			i: j for i, j in points.items()
			if j == max_points
		}
		for player in players + specs:
			background(player.send(embed=embed(player,
				title=('uno/uno-winners-title',),
				description=(
					'uno/winners',
					'\n'.join(
						i18n(
							player, 'uno/point',
							str(p), points[p.id]
						)
						for p in players
						if p.id in winners
					)
				),
				fields=((
					('uno/points',),
					'\n'.join(
						i18n(player, 'uno/point', str(p), points[p.id])
						for p in players
						if p.id not in winners
					) or i18n(player, 'none'),
					False
				),),
				color=0x55acee
			)))

	name = 'Set'
	coro = 'do_setgame'
	maxim = float('inf')
	minim = 1 #you can just try to beat your score
	scn = 'setgame start'
	jcn = 'setgame join'
	specs = float('inf')
	spec = True

	@group(invoke_without_command=True, description='setgame/setgame-cmd-desc')
	@lone_group(True)
	async def setgame(self, ctx):
		"""setgame/setgame-cmd-help"""
		pass

	@setgame.command(name='here', description='setgame/setgame-here-desc')
	async def here(self, ctx):
		players, specs = await self._gather_multigame(ctx)
		if players:
			await self.do_setgame(players, specs)

	@setgame.command(description='setgame/setgame-join-desc')
	async def join(self, ctx):
		await self._join_global_game(ctx)

	@setgame.command(aliases=['spec'], description='setgame/setgame-spec-desc')
	async def spectate(self, ctx):
		await self._spec_global_game(ctx)

	@setgame.command(description='setgame/setgame-leave-desc')
	async def leave(self, ctx):
		await self._unjoin_global_game(ctx)

	@setgame.command(description='setgame/setgame-start-desc')
	async def start(self, ctx):
		await self._start_global_game(ctx)

class BigTwo(Games):
	"""bigtwo/cog-desc"""

	DECK = [BigTwoCard(i, j) for i in range(4) for j in range(13)]

	async def do_bigtwo(self, ctxs, specs):
		players = [ctx.author for ctx in ctxs]
		deck = self.DECK[:]
		# redeal this situation
		def two_face_no_ace(hand):
			faces = 0
			for card in hand:
				if card._number > 10:
					return False
				if card._number > 7:
					faces += 1
					if faces > 2:
						return False
			return True
		while 1:
			random.shuffle(deck)
			# deal, split the deck with 2 people
			# but get rid of one hand with 3
			if len(players) == 2:
				hands = [deck[:26], deck[26:]]
			else:
				hands = [deck[:13], deck[13:26], deck[26:39], deck[39:]]
				hands = hands[:len(players)]
			for hand in hands:
				if two_face_no_ace(hand):
					break # break from for loop
			else:
				break # break from while loop
		# figure out who goes first
		idx = None
		suit = 0
		number = 0
		while idx is None:
			for i, hand in enumerate(hands):
				for card in hand:
					if card._suit == suit and card._number == number:
						idx = i
						break
				if idx is not None:
					break
			number += 1
			if number > 12:
				number = 0
				suit += 1
		hands.insert(0, hands.pop(idx))
		players.insert(0, players.pop(idx))
		# done with that
		discard = None
		last_player = None
		pid = 0
		for p in players:
			background(p.send(embed=embed(p,
				title=('bigtwo/game-started-title',),
				description=('bigtwo/game-started',),
				footer=('bigtwo/your-turn',)
					   if p is players[pid]
					   else ('bigtwo/turn-footer', str(players[pid])),
				color=0x55acee
			)))
		while all(hands):
			hands[pid].sort()
			background(players[pid].send(embed=embed(players[pid],
				title=('bigtwo/hand-title',),
				description=' '.join(('\n' if i % 7 == 0 else '')
									 + f'`{i+1:02}`:\xa0{card!s}'
									 for i, card in enumerate(hands[pid])),
				fields=((
					('bigtwo/instructions-title',),
					('bigtwo/instructions',),
					False
				),),
				color=0xffff00
			)))
			def checc(m):
				if not isinstance(m.channel, discord.DMChannel):
					return False
				if m.author.id != players[pid].id:
					return False
				if not re.match(r'^([0-9]+(\s[0-9]+){,4}|pass)$',
								m.content, re.I):
					return False
				return True
			while 1:
				msg = await self.bot.wait_for('message', check=checc)
				if msg.content.casefold() == 'pass':
					break
				idxes = list(map(int, msg.content.split()))
				if discard is not None and len(idxes) != len(discard.cards):
					continue
				idxes = [i - 1 for i in idxes]
				cards = [hands[pid][i] for i in idxes]
				for i in range(8)[::-1]:
					try:
						trick = BigTwoTrick(cards, i)
						if discard is not None and not discard < trick:
							continue
					except ValueError:
						continue # invalid trick, try next
					else:
						break # valid trick, we're done
				else:
					continue # no valid tricks, invalid message
				break # valid trick, stop asking for messages
			if msg.content.casefold() == 'pass':
				pass # lol
			else:
				discard = trick
				last_player = players[pid]
				hands[pid] = [card for i, card in enumerate(hands[pid])
							  if i not in idxes]
				if len(hands[pid]) == 1:
					for p in players:
						if p is players[pid]:
							continue
						background(p.send(embed=embed(p,
							title=('bigtwo/last-card-title',),
							description=('bigtwo/last-card', str(players[pid])),
							color=0xff0000
						)))
			pid += 1
			pid %= len(players)
			if last_player is players[pid]:
				discard = None
			for p in players:
				background(p.send(embed=embed(p,
					title=('bigtwo/next-turn-title',),
					description=('bigtwo/player-passed'
								 if msg.content.casefold() == 'pass'
								 else 'bigtwo/player-played',
								 str(players[pid-1])),
					fields=(('\1', ' '.join(map(str, discard.cards))
								   if discard is not None
								   else ('none',), False),),
					footer=('bigtwo/your-turn',)
						   if p is players[pid]
						   else ('bigtwo/turn-footer', str(players[pid]))
				)))
		points = [len(hands[i]) for i in range(len(players))]
		winners = {
			i: points[i] for i in range(len(points))
			if points[i] == 0
		}
		for i in range(len(points)):
			if points[i] >= 13:
				points[i] *= 3
			elif points[i] > 10:
				points[i] *= 2
		for pid, player in enumerate(players):
			background(player.send(embed=embed(player,
				title=('uno/uno-winners-title',),
				description=(
					'uno/winners',
					'\n'.join(
						i18n(
							player, 'uno/point',
							str(p), points[i]
						)
						for i, p in enumerate(players)
						if i in winners
					)
				),
				fields=((
					('uno/points',),
					'\n'.join(
						i18n(player, 'uno/point', str(p), points[i])
						for i, p in enumerate(players)
						if i not in winners
					) or i18n(player, 'none'),
					False
				),),
				color=0x55acee
			)))

	name = 'Big Two'
	coro = 'do_bigtwo'
	maxim = 4
	minim = 2
	scn = 'bigtwo start'
	jcn = 'bigtwo join'

	@group(invoke_without_command=True, description='bigtwo/cmd-desc')
	@lone_group(True)
	async def bigtwo(self, ctx):
		"""bigtwo/cmd-help"""
		pass

	@bigtwo.command(name='here', description='bigtwo/here-desc')
	async def here(self, ctx):
		players = await self._gather_multigame(ctx)
		if players:
			await self.do_bigtwo(players, ())

	@bigtwo.command(name='join', description='bigtwo/join-desc')
	async def join(self, ctx):
		await self._join_global_game(ctx)

	@bigtwo.command(name='leave', description='bigtwo/leave-desc')
	async def leave(self, ctx):
		await self._unjoin_global_game(ctx)

	@bigtwo.command(name='start', description='bigtwo/start-desc')
	async def start(self, ctx):
		await self._start_global_game(ctx)
