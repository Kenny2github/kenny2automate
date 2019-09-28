import os
import re
import asyncio
import pygame
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

IMGS = {
    i: {
        'white': img('white-' + i.lower()),
        'black': img('black-' + i.lower())
    } for i in ('Queen', 'King', 'Bishop', 'Rook', 'Knight', 'Pawn')
}

class Piece:
    moves = 0

    def __init__(self, pos, color):
        self.x, self.y = pos
        self.color = color
        self.image = IMGS[type(self).__name__]

    def move_valid(self, newpos, board):
        """newpos: (x, y); board: Optional<Piece>[8][8]"""
        x, y = newpos
        there = board[x][y]
        if there is not None and there.color == self.color:
            return False
        return True

    def move(self, newpos, board):
        x, y = newpos
        board[self.x][self.y], board[x][y] = None, board[self.x][self.y]
        self.x, self.y = x, y
        self.moves += 1

    def __repr__(self):
        return '{!s}({!r}, {!r})'.format(
            type(self).__name__,
            (self.x, self.y),
            self.color
        )

    __str__ = __repr__

class Queen(Piece):
    def move_valid(self, newpos, board):
        if not super().move_valid(newpos, board):
            return False
        x, y = newpos
        dx, dy = x - self.x, y - self.y
        if abs(dx) != abs(dy) and not (dx == 0 or dy == 0):
            return False
        if dx == 0:
            for i in range(self.y + dy // abs(dy), y, dy // abs(dy)):
                if board[x][i] is not None:
                    return False
        elif dy == 0:
            for i in range(self.x + dx // abs(dx), x, dx // abs(dx)):
                if board[i][y] is not None:
                    return False
        else:
            for i, j in zip(
                    range(self.x + dx // abs(dx), x, dx // abs(dx)),
                    range(self.y + dy // abs(dy), y, dy // abs(dy))
            ):
                if board[i][j] is not None:
                    return False
        return True

class King(Piece):
    def is_checked(self, pos, board):
        for i in board:
            for piece in i:
                if piece is None:
                    continue
                if piece.color != self.color and piece.move_valid(pos, board):
                    return True
        return False
    def move_valid(self, newpos, board):
        x, y = newpos
        dx, dy = x - self.x, y - self.y
        if not super().move_valid(newpos, board):
            #castle is triggered by moving onto rook
            if self.moves == 0 and (y == 0 or y == 7) and dy == 0:
                #castle logic
                if isinstance(board[x][y], Rook) and board[x][y].moves == 0:
                    for i in range(self.x + dx // abs(dx), x, dx // abs(dx)):
                        if (
                            board[i][y] is not None
                            and (
                                abs(i - self.x) <= 2
                                and self.is_checked((i, y), board)
                            )
                        ):
                            return False
                    nrx = self.x + dx // abs(dx) #new rook x - king is moved later
                    board[x][y].move((nrx, y), board)
                    return True
                return False
            return False
        #ensure move does not place king in check
        if self.is_checked(newpos, board):
            return False
        return abs(self.x - x) <= 1 and abs(self.y - y) <= 1

    def move(self, newpos, board):
        #remember, this method assumes it's already valid
        x, y = newpos
        dx, dy = x - self.x, y - self.y
        if self.moves == 0 and (x == 0 or x == 7) and dy == 0:
            x = self.x + 2 * (dx // abs(dx)) #new king x
        super().move((x, y), board)

class Bishop(Piece):
    def move_valid(self, newpos, board):
        if not super().move_valid(newpos, board):
            return False
        x, y = newpos
        dx, dy = x - self.x, y - self.y
        if abs(dx) != abs(dy):
            return False
        for i, j in zip(
                range(self.x + dx // abs(dx), x, dx // abs(dx)),
                range(self.y + dy // abs(dy), y, dy // abs(dy))
        ):
            if board[i][j] is not None:
                return False
        return True

class Knight(Piece):
    def move_valid(self, newpos, board):
        if not super().move_valid(newpos, board):
            return False
        x, y = newpos
        dx, dy = x - self.x, y - self.y
        if abs(dx) == 2:
            return abs(dy) == 1
        if abs(dy) == 2:
            return abs(dx) == 1
        return False

class Rook(Piece):
    def move_valid(self, newpos, board):
        if not super().move_valid(newpos, board):
            return False
        x, y = newpos
        dx, dy = x - self.x, y - self.y
        if dx != 0 and dy != 0:
            return False
        if dx == 0:
            for i in range(self.y + dy // abs(dy), y, dy // abs(dy)):
                if board[x][i] is not None:
                    return False
        elif dy == 0:
            for i in range(self.x + dx // abs(dx), x, dx // abs(dx)):
                if board[i][y] is not None:
                    return False
        return True

class Pawn(Piece): #here we go
    def move_valid(self, newpos, board):
        if not super().move_valid(newpos, board):
            return False
        x, y = newpos
        dx, dy = x - self.x, y - self.y
        if self.moves == 0 and dx == 0 and abs(dy) == 2: #starting move
            return board[x][self.y + dy // abs(dy)] is None
        if dx != 0:
            if abs(dx) != 1 or abs(dy) != 1:
                return False
            if board[x][y] is not None: #pawn capture
                return True
            #en passant
            cx, cy = None, None
            if self.x > 0:
                possible = board[self.x - 1][self.y]
                if possible is not None and possible.color != self.color:
                    cx, cy = self.x - 1, self.y
                elif self.x < 7:
                    possible = board[self.x + 1][self.y]
                    if possible is not None and possible.color != self.color:
                        cx, cy = self.x + 1, self.y
            if cx is not None:
                board[cx][cy] = None
                return True
            return False
        return True

class Chess(Games):
    """chess/cog-desc"""

    COORD_REGEX = re.compile(r'^([a-h][0-8]|[0-8][a-h])'
                             r'[,\s]+([a-h][0-8]|[0-8][a-h])$', re.I)

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

    async def _chess(self, ctxs):
        player1, player2 = ctxs[0].author, ctxs[1].author
        board = self.new_board()
        def boardimg(bd, color):
            src = pygame.image.load(img(color + '-board'))
            for x, col in enumerate(bd):
                for y, row in enumerate(col):
                    if row is None:
                        continue
                    rx = x * 256 + 256
                    if color == 'white':
                        ry = 2048 - y * 256
                    elif color == 'black':
                        ry = y * 256 + 256
                    src.blit(row.image, (rx, ry))
            return src
        async def sendboard(bd, turn):
            surf1 = boardimg(bd, 'white')
            surf2 = boardimg(bd, 'black')
            await asyncio.gather(sendsurf(
                player1.send, surf1, 'chess', 'board.png',
                embed=embed(player1,
                    title=('chess/board-title',),
                    footer=('chess/instructions',)
                        if turn == 'white'
                        else ('chess/waiting',),
                    color=0xffffff * (turn == 'white')
                ).set_image(url='attachment://board.png')
            ), sendsurf(
                player2.send, surf2, 'chess', 'board.png',
                embed=embed(player2,
                    title=('chess/board-title',),
                    footer=('chess/instructions',)
                        if turn == 'black'
                        else ('chess/waiting',),
                    color=0xffffff * (turn == 'white')
                ).set_image(url='attachment://board.png')
            ))
        while 1:
            ### WHITE ###
            background(sendboard(board, 'white'))
            valid = False
            while not valid:
                try:
                    msg = await self.bot.wait_for('message', check=lambda m: (
                        (
                            self.COORD_REGEX.match(m.content)
                            or self.ALGEBRAIC.match(m.content)
                        )
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
                if ' ' in msg.content or ',' in msg.content:
                    (x1, y1), (x2, y2) = [(
                        ord(re.search('[a-h]', i).group(0).upper()) - 65,
                        int(re.search('[0-8]', i).group(0)) - 1
                    ) for i in re.split(r'[,\s]+', msg.content)[:2]]
                    promotion = None
                else:
                    valid, (x1, y1), (x2, y2), promotion = self.pos_from_alg(
                        self.ALGEBRAIC.match(msg.content),
                        'white', board
                    )
                    print(valid, x1, y1, x2, y2, promotion)
                    if not valid:
                        continue
                print('white:', x1, y1, x2, y2)
                if board[x1][y1] is not None:
                    valid = board[x1][y1].move_valid((x2, y2), board)
                    if valid:
                        print(board[x1][y1])
                else:
                    valid = False
            board[x1][y1].move((x2, y2), board)
            #pawn promotion
            if y2 == 7 and isinstance(board[x2][y2], Pawn): #7 is end for white
                if promotion is not None:
                    cls = promotion
                else:
                    background(player1.send(embed=embed(player1,
                        title=('chess/promotion-title',),
                        description=('chess/promotion',),
                        color=0xffffff
                    )))
                    try:
                        msg = await self.bot.wait_for('message', check=lambda m: (
                            m.content.casefold() in {
                                'queen', 'knight', 'rook', 'bishop'
                            }
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
                    cls = globals()[msg.content.title()]
                board[x2][y2] = cls((x2, y2), 'white')
            ### BLACK ###
            background(sendboard(board, 'black'))
            valid = False
            while not valid:
                try:
                    msg = await self.bot.wait_for('message', check=lambda m: (
                        (
                            self.COORD_REGEX.match(m.content)
                            or self.ALGEBRAIC.match(m.content)
                        )
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
                if ' ' in msg.content or ',' in msg.content:
                    (x1, y1), (x2, y2) = [(
                        ord(re.search('[a-h]', i).group(0).upper()) - 65,
                        int(re.search('[0-8]', i).group(0)) - 1
                    ) for i in re.split(r'[,\s]+', msg.content)[:2]]
                    promotion = None
                else:
                    valid, (x1, y1), (x2, y2), promotion = self.pos_from_alg(
                        self.ALGEBRAIC.match(msg.content),
                        'black', board
                    )
                    print(valid, x1, y1, x2, y2, promotion)
                    if not valid:
                        continue
                print('black:', x1, y1, x2, y2)
                if board[x1][y1] is not None:
                    valid = board[x1][y1].move_valid((x2, y2), board)
                    if valid:
                        print(board[x1][y1])
                else:
                    valid = False
            board[x1][y1].move((x2, y2), board)
            #pawn promotion
            if y2 == 0 and isinstance(board[x2][y2], Pawn): #0 is end for black
                if promotion is not None:
                    cls = promotion
                else:
                    background(player2.send(embed=embed(player2,
                        title=('chess/promotion-title',),
                        description=('chess/promotion',),
                        color=0xffffff
                    )))
                    try:
                        msg = await self.bot.wait_for('message', check=lambda m: (
                            m.content.casefold() in {
                                'queen', 'knight', 'rook', 'bishop'
                            }
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
                    cls = globals()[msg.content.title()]
                board[x2][y2] = cls((x2, y2), 'black')
