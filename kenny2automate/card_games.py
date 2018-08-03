import re
import random
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
	@bot_has_permissions(add_reactions=True, read_message_history=True)
	async def fish(self, ctx):
		"""Play Go Fish!"""
		players = await self._gather_multigame(ctx, 'Go Fish')
		if not players:
			print(players)
			return
		deck = [Card(i, j) for i in range(4) for j in range(13)]
		random.shuffle(deck)
		dmx = [player.dm_channel for player in players]
		hands = [[deck.pop() for _ in range(7)] for _ in players]
		for hand in hands:
			hand.sort(key=lambda c: c.number)
		books = [[] for _ in players]
		def stats(pid, footer):
			embed = d.Embed(
				title='Situation',
				description='Your hand and books.',
				color=0x0000FF,
			)
			embed.add_field(name='Hand', value=' '.join(str(c) for c in hands[pid]) or 'Empty', inline=False)
			embed.add_field(name='Books', value='\n'.join(' '.join(str(c) for c in b) for b in books[pid]) or 'None', inline=False)
			embed.add_field(name='Status', value=footer, inline=False)
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
					print('Wut? {} {} {}'.format(counts, newbooks, pid))
					newbook = [c for c in hands[pid] if c.number == num]
					newbook.sort(key=lambda c: c.suit)
					newbooks.append(newbook)
					books[pid].append(newbook)
					hands[pid] = [c for c in hands[pid] if c.number != num]
			if newbooks:
				await dmx[pid].send(embed=d.Embed(
					title='New books',
					description='\n'.join(' '.join(str(c) for c in b) for b in newbooks)
				))
		for pid in range(len(players)):
			await checkbooks(pid)
		M = {
			'card': 'Send a card number (e.g. Q or 10) to ask for it.',
			'wait': "Waiting for next player's question..."
		}
		for i, dm in enumerate(dmx[1:]):
			await dm.send(embed=stats(i+1, M['wait']))
		while all(hands) and deck:
			for pid, player in enumerate(players):
				matches = True
				print("{}'s turn".format(player.display_name))
				for pid2, player2 in enumerate(players):
					if player2 == player:
						continue
					await dmx[pid2].send("It is now {}'s turn.".format(player.display_name))
				await dmx[pid].send(embed=stats(pid, M['card']))
				while matches and hands[pid]:
					def checc(m):
						if m.channel.id != dmx[pid].id or m.author.id != player.id:
							return False
						if not re.fullmatch('(?:[JQKA2-9]|10)', m.content, re.I):
							return False
						num = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K').index(m.content.upper())
						for card in hands[pid]:
							if card.number == num:
								return True
						return False
					msg = await ctx.bot.wait_for('message', check=checc)
					num = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K').index(msg.content.upper().strip())
					matches = []
					for pid2, player2 in enumerate(players):
						if player2 == player:
							continue
						matches2 = [c for c in hands[pid2] if c.number == num]
						matches.extend(matches2)
						count = len(matches2)
						hands[pid2] = [c for c in hands[pid2] if c.number != num]
						if matches2:
							await dmx[pid2].send('{} asked for {}s - since you had {}, you were forced to hand them over.'.format(
								player.display_name,
								Card.NUMBERS[num],
								count
							))
							hands[pid].extend(matches)
					print('{}: {}'.format(player.display_name, hands[pid]))
					if matches:
						hands[pid].sort(key=lambda c: c.number)
						await checkbooks(pid)
						if not hands[pid]:
							break
						await dmx[pid].send(content='You got: {}'.format(' '.join(str(c) for c in matches)), embed=stats(pid, M['card']))
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
								await dmx[pid2].send('{} asked for {}s - although you had {}, you are not safe yet.'.format(
									player.display_name,
									Card.NUMBERS[num],
									count
								))
							await dmx[pid].send(
								content="Go fish! You got a {} - it's what you asked for!".format(Card.NUMBERS[num]),
								embed=stats(pid, M['card'])
							)
						else:
							for pid2, player2 in enumerate(players):
								if player2 == player:
									continue
								await dmx[pid2].send('{} asked for {}s - since you had {}, you are safe.'.format(
									player.display_name,
									Card.NUMBERS[num],
									count
								))
							await dmx[pid].send(content="Go fish! You got a {}.".format(draw), embed=stats(pid, M['wait']))
				if not (all(hands) and deck):
					break
		books = tuple(map(len, books))
		max_books = max(books)
		winners = [i for i, j in enumerate(books) if j == max_books]
		winners = tuple(players[i] for i in winners)
		if len(winners) > 1:
			embed = d.Embed(
				title='Winners',
				description='The winners are {}! Congratulations!'.format(
					', '.join(player.display_name for player in winners[:-1])
					+ ', and ' + winners[-1].display_name
				)
			)
		else:
			embed = d.Embed(
				title='Winner',
				description='The winner is {}! Congratulations!'.format(
					winners[0].display_name
				)
			)
		for dm in dmx:
			dm.send(embed=embed)
