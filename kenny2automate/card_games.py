import re
import random
from itertools import accumulate
from bisect import bisect
import asyncio as a
import discord as d
from discord.ext.commands import command
from discord.ext.commands import bot_has_permissions
from .pm_games import PrivateGames

class Card(object):
	SUITS = tuple('\u2660 \u2663 \u2665 \u2666'.split(' '))
	NUMBERS = tuple('\U0001f1e6 2\u20e3 3\u20e3 4\u20e3 5\u20e3 6\u20e3 7\u20e3 8\u20e3 9\u20e3 \U0001f51f \U0001f1ef \U0001f1f6 \U0001f1f0'.split(' '))

	suit = SUITS[0]
	number = NUMBERS[0]

	def __init__(self, suit=SUITS[0], number=NUMBERS[0]):
		self.suit = suit
		self.number = number

	def __repr__(self):
		return self.NUMBERS[self.number] + self.SUITS[self.suit]

	__str__ = __repr__

	def __hash__(self):
		return hash(repr(self))

	def __eq__(self, other):
		return hash(self) == hash(other)

class CardGames(PrivateGames):
	@command()
	async def blackjack(self, ctx, against: d.Member = None):
		GO, NO = '\u2705 \u274e'.split(' ')
		async def player_coro(ctx, player, qyoo, *, deck, whoami):
			dmx = await ctx.bot.get_context((await player.dm_channel.history(limit=1).flatten())[0])
			stack = 0
			pot = 0
			while 1:
				qyoo.put_nowait('player{}'.format(whoami))
				hand = [deck.pop(), deck.pop()]
				while 1:
					if deck and sum(c.number for c in hand) <= 21:
						msg = await dmx.send('[{}] Your hand: {}\nDo you want a card?'.format(whoami, '`;`'.join(str(c) for c in hand)))
						await msg.add_reaction(GO)
						await msg.add_reaction(NO)
						try:
							reaction, user = await ctx.bot.wait_for('reaction_add',
								check=lambda r, u:
									r.emoji in (GO, NO) \
									and r.message.id == msg.id \
									and u.id == player.id,
								timeout=600.0
							)
						except a.TimeoutError:
							await dmx.send("You didn't make a move for 10 minutes! The game has been cancelled.")
							raise
						if reaction.emoji == GO:
							hand.append(deck.pop())
						else:
							break
					else:
						break
				await dmx.send('[{}] Your hand: {}\nWaiting for the other player to finish...'.format(whoami, '`;`'.join(str(c) for c in hand)))
				self.unblock_me(qyoo)
				await qyoo.join()
				hand2 = await self.snr(qyoo, hand, whoami)
				await dmx.send('[{}] Other\'s hand: {}'.format(whoami, '`;`'.join(str(c) for c in hand2)))
				total = sum(c.number + 1 for c in hand)
				total2 = sum(c.number + 1 for c in hand2)
				if total > 21:
					won1 = False
				elif total > total2:
					won1 = True
				else:
					won1 = False
				if total2 > 21:
					won2 = False
				elif total2 > total:
					won2 = True
				else:
					won2 = False
				if not (won1 or won2):
					await dmx.send('[{}] Both players lost! The cards go to the pot.'.format(whoami))
					pot += total + total2
				elif won1 and won2:
					await dmx.send('[{}] Both players won! The cards go to the pot.'.format(whoami))
					pot += total + total2
				elif won1:
					await dmx.send('[{}] You won this round! Well done.'.format(whoami))
					stack += total + total2 + pot
					pot = 0
				elif won2:
					await dmx.send('[{}] You lost this round. Better luck next round!'.format(whoami))
					pot = 0
				if not deck:
					break
			stack2 = await self.snr(stack)
			if stack > stack2:
				await ctx.send('[{}] You won {} to {}! Congratulations!'.format(whoami, stack, stack2))
			elif stack < stack2:
				await ctx.send('[{}] You lost {} to {}... Better luck next game.'.format(whoami, stack, stack2))
			else:
				await ctx.send('[{}] Tie, {} even! Interesting.'.format(whoami, (stack + stack2) // 2))
		async def coro1(ctx, player, qyoo, *, deck):
			await player_coro(ctx, player, qyoo, deck=deck, whoami=1)
		async def coro2(ctx, player, qyoo, *, deck):
			await player_coro(ctx, player, qyoo, deck=deck, whoami=2)
		deck = [Card(i, j) for i in range(4) for j in range(13)]
		random.shuffle(deck)
		await self._game(ctx, 'Blackjack', against, coro1, coro2, deck=deck)
