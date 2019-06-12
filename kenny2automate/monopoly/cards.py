import re

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
    _6 = _changes('someone', 6, 50)
    async def _8(ctx, player, dieroll, board):
        player.space -= 3
        player.space %= 40
        await send_action(ctx, 'someone', 8)
    _11 = _changes('someone', 11, -15)
    _12 = _changes('someone', 12, 0, 5)
    _13 = _changes('someone', 13, 0, 39)
    _15 = _changes('someone', 15, 150)
    _16 = _changes('someone', 16, 100)

class Nitros:
    _0 = _changes('nitro', 0, 200, 0)
    _1 = _changes('nitro', 1, 200)
    _2 = _changes('nitro', 2, -50)
    _3 = _changes('nitro', 3, 50)
    async def _5(ctx, player, dieroll, board):
        player.state |= 1 #JAILED1
        player.on = 10 #jail
        await send_action(ctx, 'nitro', 5)
    _7 = _changes('nitro', 7, 100)
    _8 = _changes('nitro', 8, 20)
    _10 = _changes('nitro', 10, 100)
    _11 = _changes('nitro', 11, -50)
    _12 = _changes('nitro', 12, -50)
    _13 = _changes('nitro', 13, 25)
    _15 = _changes('nitro', 15, 10)
    _16 = _changes('nitro', 16, 100)

someones = [getattr(Someones, i) for i in dir(Someones) if re.match(i, '_[0-9]+')]
nitros = [getattr(Nitros, i) for i in dir(Nitros) if re.match(i, '_[0-9]+')]
