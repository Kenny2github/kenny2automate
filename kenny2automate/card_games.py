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

	def copy(self):
		return Card(self.suit, self.number)

class CardGames(PrivateGames):
#	@command()
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
			stack2 = await self.snr(qyoo, stack, whoami)
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

	@command()
	async def fish(self, ctx, against: d.Member = None):
		"""Play Go Fish! Do ;fish to let anyone join
		or ;fish @mention to get a specific person.
		"""
		try:
			player1, player2 = await self._gather_game(ctx, 'Go Fish', against)
		except (TypeError, ValueError):
			return
		deck = [Card(i, j) for i in range(4) for j in range(13)]
		random.shuffle(deck)
		dmx1 = player1.dm_channel
		dmx2 = player2.dm_channel
		hand1 = [deck.pop() for _ in range(7)]
		hand1.sort(key=lambda c: c.number)
		books1 = []
		hand2 = [deck.pop() for _ in range(7)]
		hand2.sort(key=lambda c: c.number)
		books2 = []
		async def stats(pid, footer):
			embed = d.Embed(
				title='Situation',
				description='Your hand and books.',
				color=0x0000FF,
			)
			embed.add_field(name='Hand', value=' '.join(str(c) for c in (hand1 if pid==1 else hand2)) or 'Empty', inline=False)
			embed.add_field(name='Books', value='\n'.join(' '.join(str(c) for c in b) for b in (books1 if pid==1 else books2)) or 'None', inline=False)
			embed.set_footer(text=footer)
			return embed
		def checc1(m):
			if m.channel.id != dmx1.id or m.author.id != player1.id:
				return False
			if not re.fullmatch('(?:[JQKA2-9]|10)', m.content, re.I):
				return False
			num = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K').index(m.content.upper())
			for card in hand1:
				if card.number == num:
					return True
			return False
		def checc2(m):
			if m.channel.id != dmx2.id or m.author.id != player2.id:
				return False
			if not re.fullmatch('(?:[JQKA2-9]|10)', m.content, re.I):
				return False
			num = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K').index(m.content.upper())
			for card in hand2:
				if card.number == num:
					return True
			return False
		async def checkbooks(pid):
			counts = {}
			newbooks = []
			for card in (hand1 if pid==1 else hand2):
				if card.number not in counts:
					counts[card.number] = 1
				else:
					counts[card.number] += 1
			for num, count in counts.items():
				if count >= 4:
					newbook = [c for c in (hand1 if pid==1 else hand2) if c.number == num]
					newbook.sort(lambda c: c.number)
					newbooks.append(newbook)
					(books1 if pid==1 else books2).append(newbook)
					tmp = [c for c in (hand1 if pid==1 else hand2) if c.number != num]
					(hand1 if pid==1 else hand2).clear()
					(hand1 if pid==1 else hand2).extend(tmp)
			if newbooks:
				await (dmx1 if pid==1 else dmx2).send(embed=d.Embed(
					title='New books',
					description='\n'.join(' '.join(c for c in b) for b in newbooks)
				))
		await checkbooks(1)
		await checkbooks(2)
		M = {
			'card': 'Send a card number (e.g. Q or 10) to ask for it.',
			'wait': "Waiting for opponent's question..."
		}
		await dmx2.send(stats(2, M['wait']))
		await dmx1.send(embed=stats(1, M['card']))
		while hand1 and hand2 and deck:
			matches = True
			while matches:
				msg = await ctx.bot.wait_for('message', check=checc1)
				num = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K').index(msg.content.upper().strip())
				matches = [c for c in hand2 if c.number == question]
				count = len(matches)
				hand2 = [c for c in hand2 if c.number != question]
				if matches:
					await dmx2.send('Your opponent asked for {}s - since you had {}, you were forced to hand them over.'.format(Card.NUMBERS[num], count))
					hand1.extend(matches)
					await dmx1.send(content='You got: {}'.format(' '.join(str(c) for c in matches)), embed=stats(1, M['card']))
				else:
					draw = deck.pop()
					hand1.append(draw)
					if draw.number == num:
						await dmx2.send('Your opponent asked for {}s - although you had {}, you are not safe yet.'.format(Card.NUMBERS[num], count))
						await dmx1.send(content="Go fish! You got a {} - it's what you asked for!", embed=stats(1, M['card']))
					else:
						await dmx2.send(
							content='Your opponent asked for {}s - since you had {}, you are safe.'.format(Card.NUMBERS[num], count),
							embed=stats(2, M['card'])
						)
						await dmx1.send(content="Go fish! You got a {}.".format(draw), embed=stats(1, M['wait']))
				await checkbooks(1)
			matches = True
			while matches:
				msg = await ctx.bot.wait_for('message', check=checc2)
				num = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K').index(msg.content.upper().strip())
				matches = [c for c in hand1 if c.number == question]
				count = len(matches)
				hand1 = [c for c in hand1 if c.number != question]
				if matches:
					await dmx1.send('Your opponent asked for {}s - since you had {}, you were forced to hand them over.'.format(Card.NUMBERS[num], count))
					hand2.extend(matches)
					await dmx2.send(content='You got: {}'.format(' '.join(str(c) for c in matches)), embed=stats(2, M['card']))
				else:
					draw = deck.pop()
					hand2.append(draw)
					if draw.number == num:
						await dmx1.send('Your opponent asked for {}s - although you had {}, you are not safe yet.'.format(Card.NUMBERS[num], count))
						await dmx2.send(content="Go fish! You got a {} - it's what you asked for!", embed=stats(2, M['card']))
					else:
						await dmx1.send(
                                                        content='Your opponent asked for {}s - since you had {}, you are safe.'.format(Card.NUMBERS[num], count),
                                                        embed=stats(2, M['card'])
                                                )
						await dmx2.send("Go fish! You got a {}.".format(draw))
				await checkbooks(2)
		books1 = len(books1)
		books2 = len(books2)
		if books1 > books2:
                        msg1 = 'You won! You had more books ({} > {})'
                        msg2 = 'You lost! You had less books ({} < {})'
                elif books1 < books2:
                        msg1 = 'You lost! You had less books ({} < {})'
                        msg2 = 'You won! You had more books ({} > {})'
                else:
                        msg1 = "It's a tie! You had the same number of books ({} = {})"
                        msg2 = msg1
                await dmx1.send(msg1.format(books1, books2))
                await dmx2.send(msg2.format(books1, books2))
