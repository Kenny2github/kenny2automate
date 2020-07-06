import asyncio
import discord
from discord.ext.commands import group
from .emoji import (
    BLUE_CIRCLE as BLUE, RED_CIRCLE as RED,
    BLACK_SQUARE as BLACK, CR0SS as NEIN, NUMBERS
)
from .games import Games
from .i18n import i18n, embed
from .utils import lone_group, background, DummyCtx

DOWN = '\N{DOWNWARDS BLACK ARROW}'
REGA, REGB, REGC, REGD, REGE, REGF, REGG = REGS = NUMBERS[1:8]

class Connect4(Games):
    """connect4/cog-desc"""

    async def connect4_global(self, ctxs, specs):
        """Global connect4 coroutine!"""
        _ctx1, _ctx2 = ctxs
        ctx1, ctx2 = _ctx1.author, _ctx2.author
        regs = REGS[:]
        board = self.genboard()
        redwon, bluewon = False, False
        checkwin = self.checkwin
        constructboard = self.constructboard

        boardmsg1 = await ctx1.send('_ _')
        boardmsg2 = await ctx2.send('_ _')
        boardmsg1 = await ctx1.fetch_message(boardmsg1.id)
        boardmsg2 = await ctx2.fetch_message(boardmsg2.id)
        specbds = await asyncio.gather(*(c.author.send('_ _') for c in specs))
        reaction, user = None, None

        while not (redwon or bluewon):
            if reaction is None:
                for reg in regs:
                    background(boardmsg1.add_reaction(reg))
                background(boardmsg1.add_reaction(DOWN))
                for reg in regs:
                    background(boardmsg2.add_reaction(reg))
                background(boardmsg2.add_reaction(DOWN))
            boardmsgcont1 = constructboard(_ctx1, board, (ctx1, ctx2), 0)
            boardmsgcont2 = constructboard(_ctx2, board, (ctx1, ctx2), 0)
            boardmsgconts = (constructboard(c, board, (ctx1, ctx2), 0)
                             for c in specs)
            for m, c, b in zip(specbds, specs, boardmsgconts):
                background(m.edit(embed=embed(c,
                    title=('connect4/board-title',),
                    description=b,
                    color=0xff0000
                )))
            background(boardmsg1.edit(embed=embed(ctx1,
                title=('connect4/board-title',),
                description=boardmsgcont1 + i18n(
                    ctx1, 'connect4/board-you-are', RED
                ),
                color=0xff0000
            )))
            background(boardmsg2.edit(embed=embed(ctx2,
                title=('connect4/board-title',),
                description=boardmsgcont2 + i18n(
                    ctx2, 'connect4/board-you-are', BLUE
                ),
                color=0xff0000
            )))
            reaction = DOWN
            while str(reaction) == DOWN:
                try:
                    reaction, user = await self.bot.wait_for(
                        'reaction_remove',
                        check=lambda r, u: (
                            r.message.id == boardmsg1.id
                            and str(r) in regs
                            and str(r) != NEIN
                            and u.id == ctx1.id
                            or r.message.id in (boardmsg1.id, boardmsg2.id)
                            and str(r) == DOWN
                            and u.id in (ctx1.id, ctx2.id)
                        ),
                        timeout=600.0
                    )
                except asyncio.TimeoutError:
                    for r in boardmsg1.reactions:
                        background(r.remove(self.bot.user))
                    background(boardmsg1.edit(embed=embed(ctx1,
                        title=('hangman/timeout-title',),
                        description=('connect4/game-timeout', 600),
                        color=0xff0000
                    )))
                    for r in boardmsg2.reactions:
                        background(r.remove(self.bot.user))
                    background(boardmsg2.edit(embed=embed(ctx2,
                        title=('hangman/timeout-title',),
                        description=('connect4/game-timeout', 600),
                        color=0xff0000
                    )))
                    for c in specs:
                        background(specbds[i].edit(embed=embed(c,
                            title=('hangman/timeout-title',),
                            description=('connect4/game-timeout', 600),
                            color=0xff0000
                        )) for i in range(len(specs)))
                    return
                if str(reaction) == DOWN:
                    whose = int(ctx2.id == user.id)
                    msg = await user.send(embed=embed(ctxs[whose],
                        title=('connect4/board-title',),
                        description=(boardmsgcont1, boardmsgcont2)[whose] + i18n(
                            ctxs[whose], 'connect4/board-you-are', (RED, BLUE)[whose]
                        ),
                        color=0xff0000
                    ))
                    msg = await user.fetch_message(msg.id)
                    for reg in regs:
                        background(msg.add_reaction(reg))
                    background(msg.add_reaction(DOWN))
                    if whose:
                        boardmsg2 = msg
                    else:
                        boardmsg1 = msg
                    background(reaction.message.delete())
            idx = regs.index(str(reaction))
            hit = False
            for rown in range(len(board[idx])):
                if board[idx][rown] != BLACK:
                    board[idx][rown-1] = RED
                    hit = True
                    break
            if not hit:
                board[idx][-1] = RED
            if board[idx].count(BLACK) == 0:
                regs[idx] = NEIN
            redwon, bluewon = checkwin(board, RED), checkwin(board, BLUE)
            if redwon or bluewon:
                break
            boardmsgcont1 = constructboard(_ctx1, board, (ctx1, ctx2), 1)
            boardmsgcont2 = constructboard(_ctx2, board, (ctx1, ctx2), 1)
            boardmsgconts = (constructboard(c, board, (ctx1, ctx2), 1)
                             for c in specs)
            for m, c, b in zip(specbds, specs, boardmsgconts):
                background(m.edit(embed=embed(c,
                    title=('connect4/board-title',),
                    description=b,
                    color=0x55acee
                )))
            background(boardmsg1.edit(embed=embed(ctx1,
                title=('connect4/board-title',),
                description=boardmsgcont1 + i18n(
                    ctx1, 'connect4/board-you-are', RED
                ),
                color=0x55acee
            )))
            background(boardmsg2.edit(embed=embed(ctx2,
                title=('connect4/board-title',),
                description=boardmsgcont2 + i18n(
                    ctx2, 'connect4/board-you-are', BLUE
                ),
                color=0x55acee
            )))
            reaction = DOWN
            while str(reaction) == DOWN:
                try:
                    reaction, user = await self.bot.wait_for(
                        'reaction_remove',
                        check=lambda r, u: (
                            r.message.id == boardmsg2.id
                            and str(r) in regs
                            and str(r) != NEIN
                            and u.id == ctx2.id
                            or r.message.id in (boardmsg1.id, boardmsg2.id)
                            and str(r) == DOWN
                            and u.id in (ctx1.id, ctx2.id)
                        ),
                        timeout=600.0
                    )
                except asyncio.TimeoutError:
                    for r in boardmsg1.reactions:
                        background(r.remove(self.bot.user))
                    background(boardmsg1.edit(embed=embed(ctx1,
                        title=('hangman/timeout-title',),
                        description=('connect4/game-timeout', 600),
                        color=0xff0000
                    )))
                    for r in boardmsg2.reactions:
                        background(r.remove(self.bot.user))
                    background(boardmsg2.edit(embed=embed(ctx2,
                        title=('hangman/timeout-title',),
                        description=('connect4/game-timeout', 600),
                        color=0xff0000
                    )))
                    for c in specs:
                        background(specbds[i].edit(embed=embed(c,
                            title=('hangman/timeout-title',),
                            description=('connect4/game-timeout', 600),
                            color=0xff0000
                        )) for i in range(len(specs)))
                    return
                if str(reaction) == DOWN:
                    whose = int(ctx2.id == user.id)
                    msg = await user.send(embed=embed(ctxs[whose],
                        title=('connect4/board-title',),
                        description=(boardmsgcont1, boardmsgcont2)[whose] + i18n(
                            ctxs[whose], 'connect4/board-you-are', (RED, BLUE)[whose]
                        ),
                        color=0x55acee
                    ))
                    msg = await user.fetch_message(msg.id)
                    for reg in regs:
                        background(msg.add_reaction(reg))
                    background(msg.add_reaction(DOWN))
                    if whose == 0:
                        boardmsg1 = msg
                    else:
                        boardmsg2 = msg
                    background(reaction.message.delete())
            idx = regs.index(str(reaction))
            hit = False
            for rown in range(len(board[idx])):
                if board[idx][rown] != BLACK:
                    board[idx][rown-1] = BLUE
                    hit = True
                    break
            if not hit:
                board[idx][-1] = BLUE
            if board[idx].count(BLACK) == 0:
                regs[idx] = NEIN
            redwon, bluewon = checkwin(board, RED), checkwin(board, BLUE)
        boardmsgcont1 = constructboard(_ctx1, board, (ctx1, ctx2), int(bluewon))
        boardmsgcont2 = constructboard(_ctx2, board, (ctx1, ctx2), int(bluewon))
        boardmsgconts = (constructboard(c, board, (ctx1, ctx2), int(bluewon))
                         for c in specs)
        for m, c, b in zip(specbds, specs, boardmsgconts):
            background(m.edit(embed=embed(c,
                title=('connect4/board-title',),
                description=b,
            )))
        background(boardmsg1.edit(embed=embed(ctx1,
            title=('connect4/board-title',),
            description=boardmsgcont1
        )))
        background(boardmsg2.edit(embed=embed(ctx2,
            title=('connect4/board-title',),
            description=boardmsgcont2
        )))
        if redwon and bluewon:
            embed1 = embed(ctx1,
                title=('connect4/game-over-title',),
                description=('connect4/game-over-tied',)
            )
            embed2 = embed(ctx2,
                title=('connect4/game-over-title',),
                description=('connect4/game-over-tied',)
            )
            embeds = (embed(c.author,
                title=('connect4/game-over-title',),
                description=('connect4/game-over-tied',),
            ) for c in specs)
        else:
            embed1 = embed(ctx1,
                title=('connect4/game-over-title',),
                description=('connect4/game-over-description',
                    RED if redwon else BLUE, f'({ctx1 if redwon else ctx2})',
                    RED if bluewon else BLUE, f'({ctx1 if bluewon else ctx2})'),
                color=0xff0000 if redwon else 0x55acee
            )
            embed2 = embed(ctx2,
                title=('connect4/game-over-title',),
                description=('connect4/game-over-description',
                    RED if redwon else BLUE, f'({ctx1 if redwon else ctx2})',
                    RED if bluewon else BLUE, f'({ctx1 if bluewon else ctx2})'),
                color=0xff0000 if redwon else 0x55acee
            )
            embeds = (embed(c.author,
                title=('connect4/game-over-title',),
                description=('connect4/game-over-description',
                    RED if redwon else BLUE, f'({ctx1 if redwon else ctx2})',
                    RED if bluewon else BLUE, f'({ctx1 if bluewon else ctx2})'),
                color=0xff0000 if redwon else 0x55acee
            ) for c in specs)
        embed1.description += '\n' + i18n(ctx1, 'games/rematch')
        embed2.description += '\n' + i18n(ctx2, 'games/rematch')
        for c, e in zip(specs, embeds):
            background(c.author.send(embed=e))
        msg1 = await ctx1.send(embed=embed1)
        msg2 = await ctx2.send(embed=embed2)
        await self._rematch((msg1, msg2), (_ctx1, _ctx2))

    @staticmethod
    def genboard():
        return [[BLACK for _ in range(7)] for _ in range(7)]

    @staticmethod
    def checkwin(board, tile):
        BH = len(board[0])
        BW = len(board)
        #check -
        for y in range(BH):
            for x in range(BW - 3):
                if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                    return True
        #check |
        for x in range(BW):
            for y in range(BH - 3):
                if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                    return True
        #check \
        for x in range(BW - 3):
            for y in range(3, BH):
                if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                    return True
        #check /
        for x in range(BW - 3):
            for y in range(BH - 3):
                if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                    return True
        #check + because if it's full and no 4s everyone won
        for row in board:
            for i in row:
                if i == BLACK:
                    return False
        #all full and no rows
        return True

    def constructboard(self, ctx, board, players, whose):
        boardmsgcont = ''
        boardmsgcont += RED + ' = ' + str(players[0]) + '\n'
        boardmsgcont += BLUE + ' = ' + str(players[1]) + '\n'
        boardmsgcont += "".join(REGS) + '\n'
        for row in zip(*board):
            for column in row:
                boardmsgcont += column
            boardmsgcont += '\n'
        boardmsgcont += i18n(
            ctx, (
                'connect4/board-turn'
                if ctx.author in players
                else 'connect4/board-turn-spec'
            ), (
                (RED, BLUE)[whose]
            ), self.bot.command_prefix()
        )
        return boardmsgcont

    name = 'Connect 4'
    coro = 'connect4_global'
    jcn = 'connect4 join'
    scn = 'connect4 start'
    maxim = minim = 2
    specs = float('inf')
    spec = True

    @group(aliases=['c4'], invoke_without_command=True, description='connect4/connect4-desc')
    @lone_group(True)
    async def connect4(self, ctx):
        """connect4/connect4-help"""
        pass

    @connect4.command(description='connect4/here-desc')
    async def here(self, ctx, against: discord.Member = None):
        try:
            player1, player2, specs = await self._gather_game(ctx, against)
        except (TypeError, ValueError):
            return
        await self.connect4_global((DummyCtx(author=player1),
                                    DummyCtx(author=player2)), specs)

    @connect4.command(description='connect4/join-desc')
    async def join(self, ctx):
        await self._join_global_game(ctx)

    @connect4.command(description='connect4/start-desc')
    async def start(self, ctx):
        try:
            await self._start_global_game(ctx)
        except:
            import traceback
            traceback.print_exc()
            raise

    @connect4.command(aliases=['spec'], description='connect4/spectate-desc')
    async def spectate(self, ctx):
        await self._spec_global_game(ctx)

    @connect4.command(description='connect4/leave-desc')
    async def leave(self, ctx):
        await self._unjoin_global_game(ctx)
