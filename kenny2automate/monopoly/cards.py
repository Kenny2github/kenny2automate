__all__ = ['someones', 'nitros']

import math
import random
import re
from .player import PlayerState

def _changes(space_type, message, worth=0, space=None):
    async def action(ctx, player, dieroll, board):
        player.worth += worth
        if space is not None:
            if player.space > space:
                player.worth += 200 # passed GO
            player.space = space
        await send_action(
            ctx, space_type, message,
            0x55acee if worth > 0 else 0xff0000
        )
        return False

def _goj(space_type, message):
    async def action(ctx, player, dieroll, board):
        player.state |= PlayerState.HAS_GOJ
        await send_action(ctx, space_type, message, 0x55acee)
        return False

def _jail(space_type, message):
    async def action(ctx, player, dieroll, board):
        player.state |= PlayerState.JAILED1
        player.space = 10
        await send_action(ctx, space_type, message, 0xff0000)
        return False

def _houstel(space_type, message, house, hotel):
    async def action(ctx, player, dieroll, board):
        for p in board.spaces:
            if getattr(p, 'owner', None) == player.id:
                if p.houses < 5: #5th house is a hotel
                    player.worth -= p.houses * house
                else:
                    player.worth -= hotel
        await send_action(ctx, space_type, message, 0xff00000)
        return False

def _multipay(space_type, message, amount):
    async def action(ctx, player, dieroll, board):
        for p in board.players:
            player.worth += amount
            p.worth -= amount
        await send_action(
            ctx, space_type, message,
            0x55acee if amount > 0 else 0xff0000
        )
        return False

async def send_action(ctx, space_type, message, color=0):
    await ctx.author.send(embed=embed(ctx,
        title=('monopoly/{}-action-title'.format(space_type),),
        description=('monopoly/{}-action-{}'.format(space_type, message),),
        color=color
    ))

class Someones:
    _0 = _changes('someone', 0, 200, 0)
    _1 = _changes('someone', 1, 0, 24)
    _2 = _changes('someone', 2, 0, 11)
    async def _3(ctx, player, dieroll, board):
        first = 12
        second = 28
        dieroll = random.randint(1, 6) + random.randint(1, 6)
        await send_action(ctx, 'someone', 3)
        if 0 <= player.space < first or player.space > second:
            if player.space > second:
                player.worth += 200 #passed go
            player.space = first
        elif first < player.space < second:
            player.space = second
        if board.spaces[player.space].owner is None:
            return True
        old_level = board.spaces[player.space].houses
        board.spaces[player.space].houses = 1
        res = await board.spaces[player.space].action(ctx, player, dieroll)
        board.spaces[player.space].houses = old_level
        return res
    async def _4(ctx, player, dieroll, board):
        player.space = math.ceil((player.space + 5) / 10) * 10 - 5
        res = await board.spaces[player.space].action(ctx, player, dieroll)
        if not isinstance(res, bool):
            return (res[0], res[1] * 2)
        return res
    _5 = _4
    _6 = _changes('someone', 6, 50)
    _7 = _goj('someone', 7)
    async def _8(ctx, player, dieroll, board):
        player.space -= 3
        player.space %= 40
        await send_action(ctx, 'someone', 8)
        return False
    _9 = _jail('someone', 9)
    _10 = _houstel('someone', 10, 25, 100)
    _11 = _changes('someone', 11, -15)
    _12 = _changes('someone', 12, 0, 5)
    _13 = _changes('someone', 13, 0, 39)
    _14 = _multipay('someone', 14, -50)
    _15 = _changes('someone', 15, 150)
    _16 = _changes('someone', 16, 100)

class Nitros:
    _0 = _changes('nitro', 0, 200, 0)
    _1 = _changes('nitro', 1, 200)
    _2 = _changes('nitro', 2, -50)
    _3 = _changes('nitro', 3, 50)
    _4 = _goj('nitro', 4)
    _5 = _jail('nitro', 5)
    _6 = _multipay('nitro', 6, 50)
    _7 = _changes('nitro', 7, 100)
    _8 = _changes('nitro', 8, 20)
    _9 = _multipay('nitro', 9, 10)
    _10 = _changes('nitro', 10, 100)
    _11 = _changes('nitro', 11, -50)
    _12 = _changes('nitro', 12, -50)
    _13 = _changes('nitro', 13, 25)
    _14 = _houstel('nitro', 14, 40, 115)
    _15 = _changes('nitro', 15, 10)
    _16 = _changes('nitro', 16, 100)

someones = [getattr(Someones, i) for i in dir(Someones) if re.match(i, '_[0-9]+')]
nitros = [getattr(Nitros, i) for i in dir(Nitros) if re.match(i, '_[0-9]+')]
