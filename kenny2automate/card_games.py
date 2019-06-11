#low-level
import os
import re
import random
#mid-level
import asyncio
#3rd-party
from pygame import Surface, SRCALPHA
import pygame.image
import discord
from discord.ext.commands import group
#relative
from .games import Games
from .i18n import i18n, embed
from .utils import DummyCtx, lone_group
from .tmpfiles import sendsurf

UNO_CARDS = os.path.dirname(os.path.dirname(__file__))
UNO_CARDS = os.path.join(UNO_CARDS, 'resources', 'card_games', 'uno')
UNO_SIZE = UNO_WIDTH, UNO_HEIGHT = 241, 361

def unoimg(name):
	return os.path.join(UNO_CARDS, name + '.png')

class Card:
	SUITS = ('\u2660', '\u2663', '\u2665', '\u2666')
	NUMBERS = ('\U0001f1e6', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3',
		'6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f', '\U0001f1ef',
		'\U0001f1f6', '\U0001f1f0')

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

class UnoCard(Card):
	SUITS = ('red', 'yellow', 'green', 'blue')
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

def display_name(player):
	return player.name + '#' + player.discriminator

class Fish(Games):
	"""fish/cog-desc"""

	DECK = [Card(i, j) for i in range(4) for j in range(13)]

	async def do_fish(self, ctxs):
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
			okpids = [
				chr(48 + i) + chr(8419)
				for i in range(len(players))
			]
			msg = await dmx[pid].send(embed=embed(dmx[pid],
				title=('fish/fish-player-choice-title',),
				description='\n'.join(
					'{}: {}#{}'.format(
						chr(48 + i) + chr(8419),
						j.name, j.discriminator
					) for i, j in enumerate(players)
					if i != pid
				),
				footer=('fish/fish-player-choice',),
				color=0xffff00
			))
			for i in range(len(players)):
				if i == pid:
					continue
				await msg.add_reaction(chr(48 + i) + chr(8419))
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
				await dmx[pid].send(embed=embed(dmx[pid],
					title=('fish/fish-checkbooks-title',),
					description='\n'.join(
						' '.join(str(c) for c in b)
						for b in newbooks
					),
					color=0x55acee
				))
		for pid in range(len(players)):
			await checkbooks(pid)
		for i, dm in enumerate(dmx[1:]):
			await dm.send(embed=stats(i+1, 'fish/fish-m-wait'))
		pid = 0
		while all(hands) and deck and len(players) > 1:
			pid %= len(players)
			player = players[pid]
			matches = True
			await asyncio.gather(player2.send(embed=embed(player2,
				title=('fish/fish-turn-title',),
				description=(
					'fish/fish-turn',
					display_name(player)
				),
				color=0xffffff
			)) for player2 in players if player2 != player)
			await dmx[pid].send(embed=stats(
				pid, 'fish/fish-m-card'
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
					await player.send(embed=embed(dmx[pid],
						title=('fish/fish-timed-out-title',),
						description=('fish/fish-timed-out', 600),
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
				matches = [c for c in hands[chosen_pid] if c.number == num]
				count = len(matches)
				hands[chosen_pid] = [
					c
					for c in hands[chosen_pid]
					if c.number != num
				]
				if matches:
					await dmx[chosen_pid].send(embed=embed(dmx[chosen_pid],
						title=('fish/fish-card-taken-title',),
						description=(
							'fish/fish-card-taken',
							display_name(player),
							Card.NUMBERS[num],
							count
						),
						color=0xff0000
					))
					await asyncio.gather(dmx[pid2].send(embed=embed(dmx[pid2],
						title=('fish/fish-card-taken-title',),
						description=(
							'fish/fish-other-card-taken',
							display_name(player),
							display_name(players[chosen_pid]),
							Card.NUMBERS[num],
							count
						),
						color=0xff8080
					)) for pid2, player2 in enumerate(players)
					if pid2 not in {pid, chosen_pid})
				hands[pid].extend(matches)
				if matches:
					hands[pid].sort(key=lambda c: c.number)
					await checkbooks(pid)
					if not hands[pid]:
						break
					await dmx[pid].send(
						embed=stats(pid, 'fish/fish-m-card', (
							'fish/fish-card-got',
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
							if pid2 == pid:
								continue
							if pid2 != chosen_pid:
								await dmx[pid2].send(embed=embed(dmx[pid2],
									title=('fish/fish-card-missed-title',),
									description=(
										'fish/fish-other-card-missed-unsafe',
										display_name(player),
										display_name(players[chosen_pid]),
										Card.NUMBERS[num],
										count
									),
									color=0xff8080
								))
							else:
								await dmx[pid2].send(embed=embed(dmx[pid2],
									title=('fish/fish-card-missed-title',),
									description=(
										'fish/fish-card-missed-unsafe',
										display_name(player),
										Card.NUMBERS[num],
										count
									),
									color=0xff8080
								))
						await dmx[pid].send(embed=stats(pid,
							'fish/fish-m-card', (
								'fish/fish-fish-got',
								Card.NUMBERS[num]
							)
						))
					else:
						for pid2, player2 in enumerate(players):
							if pid2 == pid:
								continue
							if pid2 != chosen_pid:
								await dmx[pid2].send(embed=embed(dmx[pid2],
									title=('fish/fish-card-missed-title',),
									description=(
										'fish/fish-other-card-missed',
										display_name(player),
										display_name(players[chosen_pid]),
										Card.NUMBERS[num],
										count
									),
									color=0x55acee
								))
							else:
								await dmx[pid2].send(embed=embed(dmx[pid2],
									title=('fish/fish-card-missed-title',),
									description=(
										'fish/fish-card-missed',
										display_name(player),
										Card.NUMBERS[num],
										count
									),
									color=0x55acee
								))
						await dmx[pid].send(
							embed=stats(pid, 'fish/fish-m-wait', (
								'fish/fish-fish', draw
							))
						)
			if not timedout:
				pid += 1
		if not (len(players) > 1):
			await asyncio.gather(dm.send(embed=embed(dm,
				title=('fish/fish-all-timed-out-title',),
				description=('fish/fish-all-timed-out',),
				color=0xff0000
			)) for dm in dmx)
			return
		books = tuple(map(len, books))
		max_books = max(books)
		winners = [i for i, j in enumerate(books) if j == max_books]
		winners = tuple(players[i] for i in winners)
		await asyncio.gather(dm.send(embed=embed(dm,
			title=('fish/fish-winners-title',),
			description=(
				'fish/fish-winners',
				i18n(dm, 'comma-sep').join(
					display_name(player) for player in winners
				)
			),
			color=0x55acee
		)) for dm in dmx)

	name = 'Go Fish'
	maxim = 10
	minim = 2
	scn = 'fish start'
	jcn = 'fish join'

	@group(invoke_without_command=True, description='fish/fish-cmd-desc')
	@lone_group(True)
	async def fish(self, ctx):
		"""fish/fish-cmd-help"""
		pass

	@fish.command(name='join', description='fish/fish-join-desc')
	async def fish_join(self, ctx):
		await self._join_global_game(ctx, self.do_fish)

	@fish.command(name='leave', description='fish/fish-leave-desc')
	async def fish_leave(self, ctx):
		await self._unjoin_global_game(ctx)

	@fish.command(name='start', description='fish/fish-start-desc')
	async def fish_start(self, ctx):
		"""fish/fish-start-help"""
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

	async def do_uno(self, ctxs):
		players = [ctx.author for ctx in ctxs]
		deck = self.DECK[:]
		discard = [None]
		random.shuffle(deck)
		card = deck.pop()
		while card.worth == 10:
			deck.insert(random.randrange(108), card)
			card = deck.pop()
		discard[0] = card
		hands = [[deck.pop() for _ in range(7)] for _ in players]
		points = [0] * len(players)
		async def handsurf(pid):
			handlen = len(hands[pid])
			padding = UNO_WIDTH // 4
			surf = Surface(
				(UNO_WIDTH * handlen + UNO_WIDTH + padding, UNO_HEIGHT),
				SRCALPHA, 32
			)
			surf.fill((0, 0, 0, 0))
			for i, j in enumerate(hands[pid]):
				surf.blit(j.image, (UNO_WIDTH + padding + UNO_WIDTH * i, 0))
			surf.blit(discard[0].image, (0, 0))
			await sendsurf(
				players[pid].send, surf, 'uno', 'hand.png',
				embed=embed(players[pid],
					title=('uno/hand-title',),
					description=('uno/hand', points[pid]),
					fields=((
						('uno/card-numbers-title',),
						('uno/card-numbers',),
						False
					),),
					footer=('uno/waiting-for-card',) if can_turn(pid) else None,
					color=0xffffff
				).set_image(url='attachment://hand.png')
			)
		def can_card(card):
			if isinstance(card, SpecialUnoCard):
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
				if can_card(i):
					return True
			return False
		pid = 0
		dpid = 1
		while (deck or any(
			can_turn(i) for i in range(len(players))
		)) and len(players) > 1:
			pid %= len(players)
			player = players[pid]
			if not can_turn(pid):
				try:
					hands[pid].append(deck.pop())
				except IndexError:
					pass
			for hand in hands:
				hand.sort(key=lambda c: c.suit)
				hand.sort(key=lambda c: c.number)
			await handsurf(pid)
			if can_turn(pid):
				try:
					msg = await self.bot.wait_for('message', check=lambda m: (
						m.channel.id == player.dm_channel.id
						and m.author.id == player.id
						and m.content.strip().isdecimal()
						and 1 <= int(m.content) <= len(hands[pid])
						and can_card(hands[pid][int(m.content) - 1])
					), timeout=600.0)
					card = hands[pid].pop(int(msg.content) - 1)
					discard[0] = card
					if card.number > 9: #special function!
						if card.number == 10: #skip
							pid += dpid
						if card.number == 11: #reverse
							if len(players) <= 2: #reverse is a skip for 2p
								pid += dpid
							else:
								dpid = -dpid
						if card.number == 12: #draw2
							hands[
								(pid + dpid) % len(players)
							].extend([deck.pop(), deck.pop()])
							pid += dpid
						if card.number == 13: #wild of some sort
							msg = await player.send(embed=embed(player,
								title=('uno/choose-color-title',),
								description=('uno/choose-color',),
								color=0x55acee
							))
							HEARTS = '\u2764\U0001f49b\U0001f49a\U0001f499'
							for i in HEARTS:
								await msg.add_reaction(i)
							reaction, user = await self.bot\
								.wait_for('reaction_add', check=lambda r, u: (
									u.id == player.id
									and r.message.id == msg.id
									and str(r) in HEARTS
								))
							color = HEARTS.index(str(reaction))
							card.suit = color
							if card.draw4: #it's a draw4!
								hands[
									(pid + dpid) % len(players)
								].extend([deck.pop() for _ in range(4)])
				except asyncio.TimeoutError:
					await player.send(embed=embed(player,
						title=('uno/uno-timed-out-title',),
						description=('uno/uno-timed-out', 600),
						color=0xff0000
					))
					del players[pid]
					deck.extend(hands[pid])
					random.shuffle(deck)
					del hands[pid]
					del points[pid]
					continue
			if len(hands[pid]) == 1:
				await asyncio.gather(p.send(embed=embed(p,
					title=('uno/uno-title',),
					description=('uno/uno', display_name(player)),
					color=0xff8080
				)) for p in players if p != player)
			elif len(hands[pid]) <= 0:
				points[pid] += 10
				hands[pid].extend(deck.pop() for _ in range(min(len(deck), 7))
			pid += dpid
		for pid in range(len(players)):
			points[pid] -= sum(i.worth for i in hands[pid])
		max_points = max(points)
		winners = tuple(
			players[i]
			for i, j in enumerate(points)
			if j == max_points
		)
		await asyncio.gather(player.send(embed=embed(player,
			title=('fish/fish-winners-title',),
			description=(
				'fish/fish-winners',
				i18n(player, 'comma-sep').join(
					display_name(p) for p in winners
				)
			),
			color=0x55acee
		)) for player in players)

	name = 'Uno'
	maxim = float('inf')
	minim = 2
	scn = 'uno start'
	jcn = 'uno join'

	@group(invoke_without_command=True, description='uno/uno-cmd-desc')
	@lone_group(True)
	async def uno(self, ctx):
		"""uno/uno-cmd-help"""
		pass

	@uno.command(name='join', description='uno/uno-join-desc')
	async def uno_join(self, ctx):
		await self._join_global_game(ctx, self.do_uno)

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
