import os
import random
import json
from mahjong import Game
import discord
from discord.ext.commands import group
from .games import Games
from .i18n import embed
from .utils import DummyCtx, lone_group, background

with open(os.path.join('resources', 'mahjong', 'emojis.json')) as f:
    EMOJIS = json.load(f)

def tile(path):
    # if path is already string, it's unaffected
    # if it's a Tile, it's cast to a path
    suit, number = str(path).split('/')
    if number.isdecimal():
        number = int(number)
    return EMOJIS[suit][number]

def tiles(paths):
    if not isinstance(paths, (list, tuple)):
        paths = str(paths).split('|')
    return ''.join(tile(path) for path in paths)

class Mahjong(Games):
    """mahjong/cog-desc"""

    name = 'Mahjong'
    coro = '_mahjong'
    #maxim = minim = 4
    maxim = minim = 1
    jcn = 'mahjong join'

    @group(aliases=['mj'], invoke_without_command=True, description='mahjong/cmd-desc')
    @lone_group(True)
    async def mahjong(self, ctx):
        """mahjong/cmd-help"""
        pass

    @mahjong.command(description='mahjong/here-desc')
    async def here(self, ctx, against: discord.Member = None):
        try:
            players = await self._gather_multigame(ctx, against)
        except (TypeError, ValueError):
            return
        await self._mahjong(players, ())

    @mahjong.command(description='mahjong/join-desc')
    async def join(self, ctx):
        await self._join_global_game(ctx)

    @mahjong.command(description='mahjong/leave-desc')
    async def leave(self, ctx):
        await self._unjoin_global_game(ctx)

    def _state(self, discard, players, revealed, hand, player):
        revealed.sort()
        hand.sort()
        state = ''
        state += ''.join(tile(t) for t in discard[::-1])
        state += '\n'
        for i in range(len(players)):
            state += f'\n{i+1}\u20e3'
            if players[i] == player:
                state += ''.join(tile(t) for t in hand)
            else:
                state += ''.join(tile(t) for t in revealed[players[i]])
                state += EMOJIS['?'] * (13 - len(revealed[players[i]]))
        return state

    def _can_use(self, hand, tile):
        # returns list of usable melds
        pass

    async def _mahjong(self, ctxs, specs):
        players = [c.author for c in ctxs]
        wall = self._wall()
        discard = []
        hands = {}
        revealed = {}
        bonuses = {p: set() for p in players}
        for p in players:
            hands[p] = wall[:13]
            revealed[p] = []
            del wall[:13]
        for p in players:
            for t in iter(hands[p]):
                if t.startswith('jia/'):
                    bonuses[p].add(t)
                    hands[p].remove(t)
                    hands[p].append(wall.pop())
        while 1:
            for p in players:
                for p2 in players:
                    background(p2.send(self._state(
                        discard, players, revealed, hands[p2], p2
                    )))
                hand = hands[p]
                can = self._can_use(hand, discard[-1])
                if discard and can:
                    emb = embed(p,
                        title=('mahjong/can-use-title',),
                        description=('mahjong/can-use-' + self._meld_type(can),),
                        color=0xffff00
                    )
                    if await self._choice(p, emb):
                        hand.append(discard[-1])
                        revealed[p].append(discard[-1])
                        discard.pop()
                    else:
                        hand.append(wall.pop(0))
                else:
                    hand.append(wall.pop(0))
                background(p.send(embed=embed(p,
                    title=('mahjong/instructions-title',),
                    description=('mahjong/instructions',),
                    color=0x55acee
                )))
                msg = await self.bot.wait_for('message', check=lambda m: (
                    m.author.id == p.id
                    and isinstance(m.channel, discord.DMChannel)
                    and m.content.strip().isdecimal()
                    and 1 <= int(m.content) <= 14
                ))
                discard.append(hand.pop(int(msg.content)))
                try:
                    revealed[p].remove(discard[-1])
                except ValueError: #not in revealed
                    pass
                #TODO: skip logic
