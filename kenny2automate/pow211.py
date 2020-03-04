import random
import asyncio
from discord.ext.commands import command
from .games import Games
from .i18n import embed, i18n
from .utils import background

class Pow211(Games):
    """2048/cog-desc"""

    @command(name='2048', description='2048/cmd-desc')
    async def pow211(self, ctx):
        ARROWS = LEFT, RIGHT, UP, DOWN = '\u2b05\u27a1\u2b06\u2b07'
        board = [[None] * 4 for _ in range(4)]
        highscore = self.db.execute('SELECT score FROM pow211_highscores WHERE \
user_id=?', (ctx.author.id,)).fetchone()
        if highscore is None:
            highscore = 0
        elif highscore[0] is None:
            highscore = 0
        else:
            highscore = highscore[0]
        def ended():
            lost = True
            for row in board:
                for tile in row:
                    if tile == 2048:
                        return True
                    if tile is None:
                        lost = False
            if lost:
                for x in range(1, 3):
                    for y in range(1, 3):
                        if any((
                            board[x][y] == board[x+1][y],
                            board[x][y] == board[x-1][y],
                            board[x][y] == board[x][y+1],
                            board[x][y] == board[x][y-1]
                        )):
                            return False
            else:
                return False
            return True
        def random_slot():
            pos = []
            for x in range(4):
                for y in range(4):
                    if board[x][y] is None:
                        pos.append((x, y))
            try:
                return random.choice(pos)
            except IndexError:
                return None
        def add_random_tile():
            value = 2 if random.random() < 0.9 else 4
            try:
                x, y = random_slot()
            except TypeError:
                return
            board[x][y] = value
        def boardtxt():
            sep = '\n\u255f\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\
\u2500\u253c\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2562\n'
            #top border
            cont = '\u2554\u2550\u2550\u2550\u2550\u2564\u2550\u2550\u2550\
\u2550\u2564\u2550\u2550\u2550\u2550\u2564\u2550\u2550\u2550\u2550\u2557\n'
            cont += sep.join('\u2551' + '\u2502'.join(
                str(tile or '').center(4) for tile in row
            ) + '\u2551' for row in board)
            #bottom border
            cont += '\n\u255a\u2550\u2550\u2550\u2550\u2567\u2550\u2550\u2550\
\u2550\u2567\u2550\u2550\u2550\u2550\u2567\u2550\u2550\u2550\u2550\u255d'
            cont = f'```{cont}```'
            return cont
        add_random_tile()
        add_random_tile()
        emb = embed(ctx,
            title=('2048/board-title',),
            fields=((('2048/points-title',), ('2048/points',
                                              0, highscore), False),),
            footer=('2048/board-footer',),
            color=0xffff00
        )
        msg = await ctx.send('_ _')
        background(msg.add_reaction(LEFT))
        background(msg.add_reaction(UP))
        background(msg.add_reaction(DOWN))
        background(msg.add_reaction(RIGHT))
        points = 0
        while not ended():
            #board
            cont = boardtxt()
            emb.description = cont
            emb.set_field_at(0,
                name=emb.fields[0].name,
                value=i18n(ctx, '2048/points', points, highscore),
                inline=emb.fields[0].inline
            )
            background(msg.edit(embed=emb))
            try:
                r, u = await self.bot.wait_for('reaction_remove', check=lambda r, u: (
                    r.message.id == msg.id
                    and u.id == ctx.author.id
                ), timeout=60.0)
            except asyncio.TimeoutError:
                await ctx.send(embed=embed(ctx,
                    title=('error',),
                    description=('2048/timed-out',),
                    color=0xff0000
                ))
                return
            # 0 = left, 1 = right, 2 = up, 3 = down
            direc = ARROWS.index(r.emoji)
            changed = 2
            moved = set()
            while changed:
                changed = 0
                if direc == 0:
                    #fall
                    for x in range(4):
                        board[x].sort(key=lambda i: bool(i), reverse=True)
                    if changed == 1:
                        break
                    #merge
                    for x in range(4):
                        for y in range(1, 4):
                            if board[x][y] is None or (x, y) in moved:
                                continue
                            if board[x][y] == board[x][y-1]:
                                board[x][y-1] *= 2
                                board[x][y] = None
                                points += board[x][y-1]
                                changed = 1
                                moved.add((x, y-1))
                                moved.add((x, y))
                if direc == 1:
                    #fall
                    for x in range(4):
                        board[x].sort(key=lambda i: bool(i))
                    if changed == 1:
                        break
                    #merge
                    for x in range(4):
                        for y in range(2, -1, -1):
                            if board[x][y] is None or (x, y) in moved:
                                continue
                            if board[x][y] == board[x][y+1]:
                                board[x][y+1] *= 2
                                board[x][y] = None
                                points += board[x][y+1]
                                changed = 1
                                moved.add((x, y+1))
                                moved.add((x, y))
                if direc == 2:
                    #fall
                    for y in range(4):
                        col = [board[x][y] for x in range(4)]
                        col.sort(key=lambda i: bool(i), reverse=True)
                        for x in range(4):
                            board[x][y] = col[x]
                    if changed == 1:
                        break
                    #merge
                    for x in range(1, 4):
                        for y in range(4):
                            if board[x][y] is None or (x, y) in moved:
                                continue
                            if board[x][y] == board[x-1][y]:
                                board[x-1][y] *= 2
                                board[x][y] = None
                                points += board[x-1][y]
                                changed = 1
                                moved.add((x-1, y))
                                moved.add((x, y))
                if direc == 3:
                    #fall
                    for y in range(4):
                        col = [board[x][y] for x in range(4)]
                        col.sort(key=lambda i: bool(i))
                        for x in range(4):
                            board[x][y] = col[x]
                    if changed == 1:
                        break
                    #merge
                    for x in range(2, -1, -1):
                        for y in range(4):
                            if board[x][y] is None or (x, y) in moved:
                                continue
                            if board[x][y] == board[x+1][y]:
                                board[x+1][y] *= 2
                                board[x][y] = None
                                points += board[x+1][y]
                                changed = 1
                                moved.add((x+1, y))
                                moved.add((x, y))
            add_random_tile()
        #board
        cont = boardtxt()
        emb.description = cont
        emb.set_field_at(0,
            name=emb.fields[0].name,
            value=i18n(ctx, '2048/points', points, highscore),
            inline=emb.fields[0].inline
        )
        background(msg.edit(embed=emb))
        won = False
        newhigh = points > highscore
        if newhigh:
            self.db.execute('INSERT OR REPLACE INTO pow211_highscores \
(user_id, score) VALUES (?, ?)', (ctx.author.id, points))
        for row in board:
            for col in row:
                if col == 2048:
                    won = True
                    break
            if won:
                break
        if won:
            await ctx.send(embed=embed(ctx,
                title=('2048/won-title',),
                description=('2048/won' + ('-high' if newhigh else ''), points),
                color=0x55acee
            ))
        else:
            await ctx.send(embed=embed(ctx,
                title=('2048/lost-title',),
                description=('2048/lost' + ('-high' if newhigh else ''), points),
                color=0x0
            ))
