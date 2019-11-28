import os
import re
import json
import asyncio
from chess import Board
import discord
from discord.ext.commands import group
from .games import Games
from .i18n import embed, i18n
from .utils import DummyCtx, lone_group, background

# +x => right
# +y => down
# white starts on y 0

with open(os.path.join('resources', 'chess', 'emojis.json')) as f:
    EMOJIS = json.load(f)

def emote(p):
    piece = {
        'q': 'queen',
        'k': 'king',
        'b': 'bishop',
        'r': 'rook',
        'n': 'knight',
        'p': 'pawn'
    }[p.lower()]
    if p.isupper():
        color = 'white'
    else:
        color = 'black'
    return f'<:{color}{piece}:{EMOJIS[color][piece]}>'

class Chess(Games):
    """chess/cog-desc"""

    ALGEBRAIC = re.compile(r"^(?:(?P<piece>[BNRKQP]?)" #what piece moved, can be blank
                           r"(?P<scol>[a-h])?(?P<srow>[0-8])?" #from where, if necessary
                           r"(?P<captureq>x)?" #if present, a capture was probably made
                           r"(?P<col>[a-h])(?P<row>[0-8])" #to where, mandatory
                           r"[=/]?(?P<promotion>[BNRQ])?" #pawn got promoted
                           r"|(?P<kingside>[0O]-[0O])" #OR, kingside castling
                           r"|(?P<queenside>[0O]-[0O]-[0O]))" #queenside
                           r"(?:(?P<check>\+\+?|\u2020)" #check
                           r"|(?P<checkmate>[#\u2021\u2260]))?$") #checkmate

    name = 'Chess'
    coro = '_chess'
    maxim = minim = 2
    specs = float('inf')
    spec = True
    jcn = 'chess join'

    @group(invoke_without_command=True, description='chess/cmd-desc')
    @lone_group(True)
    async def chess(self, ctx):
        """chess/cmd-help"""
        pass

    @chess.command(description='chess/here-desc')
    async def here(self, ctx, against: discord.Member = None):
        try:
            player1, player2, specs = await self._gather_game(ctx, against)
        except (TypeError, ValueError):
            return
        await self._chess((DummyCtx(author=player1),
                           DummyCtx(author=player2)), specs)

    @chess.command(description='chess/join-desc')
    async def join(self, ctx):
        await self._join_global_game(ctx)

    @chess.command(description='chess/leave-desc')
    async def leave(self, ctx):
        await self._unjoin_global_game(ctx)

    @chess.command(description='chess/start-desc')
    async def start(self, ctx):
        await self._start_global_game(ctx)

    @chess.command(aliases=['spec'], description='chess/spectate-desc')
    async def spectate(self, ctx):
        await self._spec_global_game(ctx)

    async def _chess(self, ctxs, specs):
        player1, player2 = ctxs[0].author, ctxs[1].author
        board = Board()
        def boardimg(bd, color):
            BLACK, WHITE, SPACE = '\u2b1b\u2b1c\u200b'
            rows = []
            caps = BLACK + '\u200b' + '\u200b'.join(chr(i + 0x1f1e6) for i in range(8)) + '\u200b' + BLACK
            result = '\n'
            for x in range(8):
                rows.append([f'{x+1}\u20e3']) #20e3 is number emoji char
                for y in range(8):
                    square = y + x * 8
                    piece = board.piece_at(square)
                    if piece:
                        rows[-1].append(emote(piece.symbol()))
                    else:
                        rows[-1].append((BLACK, WHITE)[(x % 2) ^ (y % 2)])
                rows[-1].append(f'{x+1}\u20e3')
            if color == 'white':
                rows = reversed(rows)
            result += caps + '\n'
            result += '\n'.join('\u200b'.join(row) for row in rows)
            result += '\n' + caps
            return result
        async def sendboard(bd, turn, mov):
            cont1 = boardimg(bd, 'white')
            cont2 = boardimg(bd, 'black')
            await asyncio.gather(player1.send(embed=embed(player1,
                title=('chess/board-title',),
                description=cont1,
                fields=((('chess/status-title',), (
                    'chess/instructions'
                    if turn == 'white'
                    else 'chess/waiting',
                ), False),),
                footer=('chess/last-move', mov),
                color=0xfffffe if turn == 'white' else 0x0
            )), player2.send(embed=embed(player2,
                title=('chess/board-title',),
                description=cont2,
                fields=((('chess/status-title',), (
                    'chess/instructions'
                    if turn == 'white'
                    else 'chess/waiting',
                ), False),),
                footer=('chess/last-move', mov),
                color=0xfffffe if turn == 'white' else 0x0
            )), *(p.send(embed=embed(p,
                title=('chess/board-title',),
                description=cont1,
                footer=('chess/last-move', mov),
                color=0xfffffe if turn == 'white' else 0x0
            )) for p in specs))
        msg = DummyCtx(content=i18n(player1, 'chess/game-start'))
        while not board.is_game_over():
            ### WHITE ###
            background(sendboard(board, 'white', msg.content))
            while True:
                try:
                    msg = await self.bot.wait_for('message', check=lambda m: (
                        self.ALGEBRAIC.match(m.content)
                        and m.author.id == player1.id
                        and isinstance(m.channel, discord.DMChannel)
                    ), timeout=600.0)
                except asyncio.TimeoutError:
                    for p in (player1, player2):
                        background(p.send(embed=embed(p,
                            title=('games/game-timeout-title',),
                            description=('chess/timed-out',),
                            color=0xff0000
                        )))
                    return
                try:
                    board.push_san(msg.content)
                except ValueError:
                    continue
                else:
                    break
            if board.is_game_over():
                break
            ### BLACK ###
            background(sendboard(board, 'black', msg.content))
            while True:
                try:
                    msg = await self.bot.wait_for('message', check=lambda m: (
                        self.ALGEBRAIC.match(m.content)
                        and m.author.id == player2.id
                        and isinstance(m.channel, discord.DMChannel)
                    ), timeout=600.0)
                except asyncio.TimeoutError:
                    for p in (player1, player2):
                        background(p.send(embed=embed(p,
                            title=('games/game-timeout-title',),
                            description=('chess/timed-out',),
                            color=0xff0000
                        )))
                    return
                try:
                    board.push_san(msg.content)
                except ValueError:
                    continue
                else:
                    break
        result = board.result()
        winner = player1 if result == '1-0' else (
            player2 if result == '0-1' else None
        )
        cont = boardimg(board, 'white')
        if winner is None:
            for p in (player1, player2) + specs:
                background(p.send(embed=embed(p,
                    title=('chess/game-end-title',),
                    description=cont,
                    fields=((('chess/status-title',), (
                        'chess/draw',
                    ), False),),
                    footer=('chess/last-move', msg.content),
                    color=0x808080
                )))
        else:
            for p in (player1, player2) + specs:
                background(p.send(embed=embed(p,
                    title=('chess/game-end-title',),
                    description=cont,
                    fields=((('chess/status-title',), (
                        'chess/game-end', str(winner)
                    ), False),),
                    footer=('chess/last-move', msg.content),
                    color=0xfffffe if winner is player1 else 0x0
                )))
