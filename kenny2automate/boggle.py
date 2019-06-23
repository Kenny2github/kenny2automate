import os
import random
from contextlib import ExitStack
import asyncio
import discord
from discord.ext.commands import group
from .games import Games
from .i18n import embed
from .utils import lone_group

CUBES = [
    ['A', 'N', 'A', 'E', 'E', 'G'],
    ['P', 'O', 'H', 'C', 'A', 'S'],
    ['I', 'D', 'R', 'X', 'E', 'L'],
    ['I', 'T', 'S', 'T', 'Y', 'D'],
    ['N', 'R', 'N', 'Z', 'L', 'H'],
    ['U', 'E', 'E', 'S', 'N', 'I'],
    ['J', 'B', 'O', 'A', 'O', 'B'],
    ['V', 'W', 'H', 'E', 'R', 'T'],
    ['O', 'U', 'M', 'C', 'I', 'T'],
    ['S', 'S', 'O', 'I', 'E', 'T'],
    ['F', 'P', 'K', 'A', 'F', 'S'],
    ['Q', 'N', 'M', 'I', 'H', 'U'],
    ['R', 'L', 'Y', 'T', 'E', 'T'],
    ['E', 'N', 'H', 'E', 'W', 'G'],
    ['O', 'W', 'T', 'O', 'A', 'T'],
    ['R', 'L', 'V', 'E', 'Y', 'D']
]

REGS = {chr(i): chr(j) for i, j in zip(
    range(ord('A'), ord('Z') + 1),
    range(ord('\U0001f1e6'), ord('\U0001f1e6') + 26)
)}

with open(os.path.join('kenny2automate', 'all_words.txt')) as f:
    ALL_WORDS = set(i for i in f.read().split() if len(i) >= 3)

class Boggle(Games):
    """boggle/cog-desc"""

    name = 'Boggle'
    maxim = float('inf')
    minim = 2
    scn = 'boggle start'
    jcn = 'boggle join'

    @group(invoke_without_command=True, description='boggle/boggle-desc')
    @lone_group(True)
    async def boggle(self, ctx):
        """boggle/boggle-help"""
        pass

    @boggle.command(description='boggle/join-desc')
    async def join(self, ctx):
        await self._join_global_game(ctx, self.do_boggle)

    @boggle.command(description='boggle/leave-desc')
    async def leave(self, ctx):
        await self._unjoin_global_game(ctx)

    @boggle.command(description='boggle/start-desc')
    async def start(self, ctx):
        await self._start_global_game(ctx)

    @staticmethod
    def board(matrix):
        return '\n'.join(' '.join(REGS[i] for i in row) for row in matrix)

    @staticmethod
    def new_board():
        leboard = [random.choice(i) for i in CUBES]
        random.shuffle(leboard)
        leboard = [[leboard[i * 4 + j] for j in range(4)] for i in range(4)]
        return leboard

    async def words(self, ctx, lewords, board):
        while 1:
            msg = await self.bot.wait_for('message', check=lambda m: (
                m.author.id == ctx.author.id
                and m.channel.id == ctx.author.dm_channel.id
            ))
            lewords.add(msg.content.strip().upper())
            asyncio.create_task(ctx.author.send(embed=discord.Embed(
                description=self.board(board),
                color=0xffffff
            )))

    @staticmethod
    async def mass_message(ctxs, **embed_args):
        await asyncio.gather(*(ctx.author.send(embed=embed(ctx,
            **embed_args
        )) for ctx in ctxs))

    def find_word(self, srow, scol, word, board, past_path):
        for row, col in (
            (srow + 1, scol + 1),
            (srow + 1, scol + 0),
            (srow + 1, scol - 1),
            (srow + 0, scol + 1),
            (srow + 0, scol - 1),
            (srow - 1, scol + 1),
            (srow - 1, scol + 0),
            (srow - 1, scol - 1)
        ):
            if row < 0 or row >= len(board):
                continue
            if col < 0 or col >= len(board[row]):
                continue
            if (row, col) in past_path:
                continue
            if board[row][col] == 'Q' and word.startswith('QU'):
                if len(word) == 2: #last letters
                    return True
                if self.find_word(
                    row, col, word[2:], board,
                    past_path + [(row, col)]
                ):
                    return True
            if board[row][col] == word[0]:
                if len(word) == 1: #last letter
                    return True
                if self.find_word(
                    row, col, word[1:], board,
                    past_path + [(row, col)]
                ):
                    return True
        return False

    def word_ok(self, word, board):
        for row, col in [(i, j) for i in range(4) for j in range(4)]:
            if board[row][col] == 'Q' and word.startswith('QU'):
                if self.find_word(row, col, word[2:], board, [(row, col)]):
                    return True
            if word[0] == board[row][col]:
                if self.find_word(row, col, word[1:], board, [(row, col)]):
                    return True
        return False

    async def do_boggle(self, ctxs):
        await self.mass_message(ctxs,
            title=('boggle/get-ready-title',),
            description=('boggle/get-ready', 3),
            color=0xffff00
        )
        board = self.new_board()
        await asyncio.sleep(3)
        lewords = [set() for i in range(len(ctxs))]
        tasks = [
            asyncio.create_task(self.words(ctx, words, board))
            for ctx, words in zip(ctxs, lewords)
        ]
        await self.mass_message(ctxs,
            title=('boggle/board-title',),
            description=('boggle/board', self.board(board)),
            color=0xffffff
        )
        await asyncio.sleep(180) # 3 minutes
        for task in tasks:
            task.cancel()
        await self.mass_message(ctxs,
            title=('boggle/verifying-words',),
            color=0x7289da
        )
        with ExitStack() as stack:
            for ctx in ctxs:
                stack.enter_context(ctx.author.typing())
            for leword in lewords:
                for word in list(leword):
                    if len(word) < 3:
                        leword.discard(word)
                        continue
                    if not self.word_ok(word, board):
                        leword.discard(word)
                        continue
                    if word.upper() not in ALL_WORDS:
                        leword.discard(word)
        await self.mass_message(ctxs,
            title=('boggle/eliminating-dupes',),
            color=0x7289da
        )
        dupes = set()
        for leword in lewords:
            for word in leword:
                for leword2 in lewords:
                    if leword2 is leword:
                        continue
                    if word in leword2:
                        dupes.add(word)
        sums = [sum(
            0
            if word in dupes
            else (
                11 if len(word) >= 8
                else {
                    3: 1,
                    4: 1,
                    5: 2,
                    6: 3,
                    7: 4
                }[len(word)]
            )
            for word in leword
        ) for leword in lewords]
        max_pts = max(sums)
        winners = {}
        for i, j in enumerate(sums):
            if j == max_pts:
                winners[ctxs[i].author.id] = '{0.name}#{0.discriminator}'.format(ctxs[i].author)
        await asyncio.gather(*(ctx.author.send(embed=embed(ctx,
            title=('boggle/results-title',),
            description=('boggle/results',),
            fields=tuple((
                '{0.name}#{0.discriminator}'.format(ctx2.author),
                (
                    'boggle/result', lesum,
                    '\n'.join(
                        (
                            '~~{}~~: {}'
                            if word in dupes
                            else '{}: {}'
                        ).format(
                            word,
                            0
                            if word in dupes
                            else (
                                11 if len(word) >= 8
                                else {
                                    3: 1,
                                    4: 1,
                                    5: 2,
                                    6: 3,
                                    7: 4
                                }[len(word)]
                            )
                        ) for word in leword
                    )
                ),
                False
            ) for ctx2, lesum, leword in zip(ctxs, sums, lewords))
            + ((('boggle/winner-title',), '\n'.join(winners.values()), False),),
            color=0x55acee if ctx.author.id in winners else 0x7289da
        )) for ctx in ctxs))
