import os
import random
import json
import discord
from discord.ext.commands import group
from .games import Games
from .i18n import embed
from .utils import DummyCtx, lone_group, background

with open(os.path.join('resources', 'mahjong', 'emojis.json')) as f:
    EMOJIS = json.load(f)

def tile(path, number=None):
    thing = EMOJIS
    for i in path.split('/'):
        if i.isdecimal():
            i = int(i) - 1
        thing = thing[i]
    if number is not None:
        thing = thing[number]
    return thing

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

    def _wall(self):
        wall = []
        for suit in ('zhu', 'tong', 'wan'):
            for num in range(1, 10):
                wall.extend([f'{suit}/{num}'] * 4)
        for wind in ('dong', 'nan', 'xi', 'bei'):
            wall.extend([f'feng/{wind}'] * 4)
        for dragon in ('zhong', 'fa', 'ban'):
            wall.extend([f'long/{dragon}'] * 4)
        for i in range(4):
            wall.append(f'jia/hua/{i}')
            wall.append(f'jia/gui/{i}')
        random.shuffle(wall)
        return wall

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

    def _meld_type(self, meld):
        # returns either 'chow', 'pong', 'kong', 'eyes', or None
        meld.sort()
        if len(meld) == 4: #kong
            return 'kong'
        if len(meld) == 2: #eyes
            return 'eyes'
        if meld[0][-1].isdecimal(): #ends with number, could be chow
            last, suit, stop = None, None, False
            for t in meld:
                nsuit, nlast = t.rsplit('/')[-2:]
                nlast = int(nlast)
                if last is not None:
                    if nsuit != suit or nlast != last + 1:
                        break
                suit, last = nsuit, nlast
            else:
                stop = True
            if stop:
                return 'chow'
        suit = None
        for t in meld:
            nsuit = [i for i in t.split('/') if not i.isdecimal()][-1]
            if suit is not None and nsuit != suit:
                break
            suit = nsuit
        else:
            return 'pong'
        return None

    async def _choice(self, user, emb):
        msg = await user.send(embed=emb)
        YEA, NAY = '\u2705\u274e'
        await msg.add_reaction(YEA)
        await msg.add_reaction(NAY)
        reaction, user = await self.bot.wait_for('reaction_add', check=lambda r, u: (
            str(r) in (YEA, NAY)
            and r.message.id == msg.id
            and u.id == user.id
        ))
        return str(reaction) == YEA

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
