import os
import re
import asyncio
import pygame
from chess import Board
import discord
from discord.ext.commands import group
from .games import Games
from .i18n import embed
from .utils import DummyCtx, lone_group, background
from .tmpfiles import sendsurf

# +x => right
# +y => down
# white starts on y 0

def img(name):
    return pygame.image.load(os.path.join('resources', 'chess', name + '.png'))

IMGS = {}
for i in ('Queen', 'King', 'Bishop', 'Rook', 'Knight', 'Pawn'):
    if i == 'Knight':
        IMGS[i[1].upper()] = img('white-' + i.lower())
        IMGS[i[1]] = img('black-' + i.lower())
    else:
        IMGS[i[0]] = img('white-' + i.lower())
        IMGS[i[0].lower()] = img('black-' + i.lower())

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
    jcn = 'chess join'

    @group(invoke_without_command=True, description='chess/cmd-desc')
    @lone_group(True)
    async def chess(self, ctx):
        """chess/cmd-help"""
        pass

    @chess.command(description='chess/here-desc')
    async def here(self, ctx, against: discord.Member = None):
        try:
            player1, player2 = await self._gather_game(ctx, against)
        except (TypeError, ValueError):
            return
        return await self._chess((DummyCtx(author=player1),
                                  DummyCtx(author=player2)))

    @chess.command(description='chess/join-desc')
    async def join(self, ctx):
        await self._join_global_game(ctx, self._chess)

    @chess.command(description='chess/leave-desc')
    async def leave(self, ctx):
        await self._unjoin_global_game(ctx)

    def new_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        def piece(cls, x, y, color):
            board[x][y] = cls((x, y), color)
        # pawns
        for i in range(8):
            piece(Pawn, i, 1, 'white')
        for i in range(8):
            piece(Pawn, i, 6, 'black')
        # rooks
        piece(Rook, 0, 0, 'white')
        piece(Rook, 7, 0, 'white')
        piece(Rook, 0, 7, 'black')
        piece(Rook, 7, 7, 'black')
        # knights
        piece(Knight, 1, 0, 'white')
        piece(Knight, 6, 0, 'white')
        piece(Knight, 1, 7, 'black')
        piece(Knight, 6, 7, 'black')
        # bishops
        piece(Bishop, 2, 0, 'white')
        piece(Bishop, 5, 0, 'white')
        piece(Bishop, 2, 7, 'black')
        piece(Bishop, 5, 7, 'black')
        # queens
        piece(Queen, 3, 0, 'white')
        piece(Queen, 3, 7, 'black')
        # kings
        piece(King, 4, 0, 'white')
        piece(King, 4, 7, 'black')
        return board

    def cls_from_letter(self, letter):
        if letter in {'', 'P'}:
            return Pawn
        if letter == 'B':
            return Bishop
        if letter == 'N':
            return Knight
        if letter == 'R':
            return Rook
        if letter == 'K':
            return King
        if letter == 'Q':
            return Queen

    def pos_from_alg(self, match, color, board):
        if match.group('kingside') is not None \
                or match.group('queenside') is not None:
            x1 = 4
            if match.group('kingside') is not None:
                x2 = 7
            elif match.group('queenside') is not None:
                x2 = 0
            if color == 'white':
                y1 = y2 = 0
            elif color == 'black':
                y1 = y2 = 7
            return [True, (x1, y1), (x2, y2), None]
        x1 = y1 = None
        if match.group('scol') is not None:
            x1 = ord(match.group('scol')) - 97
        if match.group('srow') is not None:
            y1 = int(match.group('srow')) - 1
        x2 = ord(match.group('col')) - 97
        y2 = int(match.group('row')) - 1
        piece = self.cls_from_letter(match.group('piece'))
        if piece is Pawn:
            promotion = match.group('promotion')
            if promotion is not None:
                promotion = self.cls_from_letter(promotion)
        else:
            promotion = None
        if x1 is not None and y1 is not None: #already enough info
            return [True, (x1, y1), (x2, y2), promotion]
        if x1 is not None and y1 is None:
            for i in range(8):
                p = board[x1][i]
                if p is not None and isinstance(p, piece) \
                        and p.color == color and p.move_valid((x2, y2), board):
                    if y1 is not None: #another valid piece
                        return [False, (x1, None), (x2, y2), promotion]
                    y1 = i
        if y1 is not None and x1 is None:
            for i in range(8):
                p = board[i][y1]
                if p is not None and isinstance(p, piece) \
                        and p.color == color and p.move_valid((x2, y2), board):
                    if x1 is not None: #another valid piece
                        return [False, (None, y1), (x2, y2), promotion]
                    x1 = i
        if x1 is y1 is None:
            for i in range(8):
                for j in range(8):
                    p = board[i][j]
                    if p is not None and isinstance(p, piece) \
                            and p.color == color and p.move_valid((x2, y2), board):
                        if x1 is not None: #another valid piece
                            return [False, (None, None), (x2, y2), promotion]
                        x1 = i
                        y1 = j
        if x1 is None or y1 is None:
            return [False, (x1, y1), (x2, y2), promotion]
        return [True, (x1, y1), (x2, y2), promotion]

    async def _chess(self, ctxs, specs):
        player1, player2 = ctxs[0].author, ctxs[1].author
        board = Board()
        def boardimg(bd, color):
            src = img(color + '-board')
            for x in range(8):
                for y in range(8):
                    square = x + y * 8
                    rx = x * 256 + 256
                    if color == 'white':
                        ry = 2048 - y * 256
                    elif color == 'black':
                        ry = y * 256 + 256
                    piece = board.piece_at(square)
                    if piece:
                        src.blit(IMGS[piece.symbol()], (rx, ry))
            return src
        async def sendboard(bd, turn, mov):
            surf1 = boardimg(bd, 'white')
            surf2 = boardimg(bd, 'black')
            await asyncio.gather(sendsurf(
                player1.send, surf1, 'chess', 'board.png',
                embed=embed(player1,
                    title=('chess/board-title',),
                    description=('chess/instructions',)
                        if turn == 'white'
                        else ('chess/waiting',),
                    footer=('chess/last-move', mov),
                    color=0xffffff * (turn == 'white')
                ).set_image(url='attachment://board.png')
            ), sendsurf(
                player2.send, surf2, 'chess', 'board.png',
                embed=embed(player2,
                    title=('chess/board-title',),
                    description=('chess/instructions',)
                        if turn == 'black'
                        else ('chess/waiting',),
                    footer=('chess/last-move', mov),
                    color=0xffffff * (turn == 'white')
                ).set_image(url='attachment://board.png')
            ))
        msg = DummyCtx(content='game start')
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
        surf = boardimg(board, 'white')
        if winner is None:
            for p in (player1, player2):
                background(sendsurf(
                    p.send, surf, 'chess', 'board.png',
                    embed=embed(p,
                        title=('chess/game-end-title',),
                        description=('chess/draw',),
                        footer=('chess/last-move', msg.content),
                        color=0x808080
                    ).set_image(url='attachment://board.png')
                ))
        else:
            for p in (player1, player2):
                background(sendsurf(
                    p.send, surf, 'chess', 'board.png',
                    embed=embed(p,
                        title=('chess/game-end-title',),
                        description=('chess/game-end', str(winner)),
                        footer=('chess/last-move', msg.content),
                        color=0xffffff if winner is player1 else 0
                    ).set_image(url='attachment://board.png')
                ))
