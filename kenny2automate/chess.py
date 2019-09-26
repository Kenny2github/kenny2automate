import asyncio
import discord
from discord.ext.commands import command
from .games import Games
from .i18n import embed
from .utils import DummyCtx, lone_group

# +x => right
# +y => down
# white starts on y 0

class Piece:
    moves = 0

    def __init__(self, pos, color):
        self.x, self.y = pos
        self.color = color

    def move_valid(self, newpos, board):
        """newpos: (x, y); board: Optional<Piece>[8][8]"""
        x, y = newpos
        there = board[x][y]
        if there is not None and there.color == self.color:
            return False
        return True

    def move(self, newpos):
        x, y = newpos
        board[self.x][self.y], board[x][y] = board[x][y], board[self.x][self.y]
        self.x, self.y = x, y
        self.moves += 1

class Queen(Piece):
    def move_valid(self, newpos, board):
        if not super().move_valid(newpos, board):
            return False
        x, y = newpos
        dx, dy = x - self.x, y - self.y
        if abs(dx) != abs(dy) and not (dx == 0 or dy == 0):
            return False
        if dx == 0:
            for i in range(self.y + 1, y, dy // abs(dy)):
                if board[x][i] is not None:
                    return False
        elif dy == 0:
            for i in range(self.x + 1, x, dx // abs(dx)):
                if board[i][y] is not None:
                    return False
        else:
            for i, j in zip(
                    range(self.x + 1, x, dx // abs(dx)),
                    range(self.y + 1, y, dy // abs(dy))
            ):
                if board[i][j] is not None:
                    return False
        return True

class King(Piece):
    def is_checked(self, pos, board):
        for i in len(board):
            for j in len(i):
                piece = board[i][j]
                if piece.color != self.color and piece.move_valid(pos, board):
                    return True
        return False
    def move_valid(self, newpos, board):
        if not super().move_valid(newpos, board):
            return False
        x, y = newpos
        dx, dy = x - self.x, y - self.y
        #ensure move does not place king in check
        if self.is_checked(newpos, board):
            return False
        #castle is triggered by moving onto rook
        if self.moves == 0 and (x == 0 or x == 7) and dy == 0:
            dx = x - self.x
            #castle logic
            if isinstance(board[x][y], Rook) and board[x][y].moves == 0:
                for i in range(self.x + 1, x, dx // abs(dx)):
                    if (
                        board[i][y] is not None
                        or abs(i - self.x) <= 2
                        and self.is_checked((i, y), board)
                    ):
                        return False
                nrx = self.x + dx // abs(dx) #new rook x - king is moved later
                board[nrx][y], board[x][y] = board[x][y], board[nrx][y]
        return abs(self.x - x) <= 1 and abs(self.y - y) <= 1

    def move(self, newpos):
        #remember, this method assumes it's already valid
        x, y = newpos
        dx, dy = x - self.x, y - self.y
        if self.moves == 0 and (x == 0 or x == 7) and dy == 0:
            x = self.x + 2 * (dx // abs(dx)) #new king x
        super().move((x, y))

class Bishop(Piece):
    def move_valid(self, newpos, board):
        if not super().move_valid(newpos, board):
            return False
        x, y = newpos
        dx, dy = x - self.x, y - self.y
        if abs(dx) != abs(dy):
            return False
        for i, j in zip(
                range(self.x + 1, x, dx // abs(dx)),
                range(self.y + 1, y, dy // abs(dy))
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
            for i in range(self.y + 1, y, dy // abs(dy)):
                if board[x][i] is not None:
                    return False
        elif dy == 0:
            for i in range(self.x + 1, x, dx // abs(dx)):
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

    name = 'Chess'
    maxim = minim = 2
    scn = 'chess start'
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

    @chess.command(description='chess/start-desc')
    async def start(self, ctx):
        await self._start_global_game(ctx)

    def board(self):
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
        piece(Queen, 3, 6, 'black')
        # kings
        piece(King, 4, 0, 'white')
        piece(King, 4, 0, 'black')
        return board

    async def _chess(self, ctxs):
        player1, player2 = ctxs[0].author, ctxs[1].author
        await player1.send('Hello Chess!')
        await player2.send('Hello Chess!')
        board = self.board()
