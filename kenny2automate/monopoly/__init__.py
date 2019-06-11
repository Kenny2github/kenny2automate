import asyncio
import time
import random
import os
import pickle
import sqlite3 as sql
import pygame.image
import pygame.draw
import discord
from discord.ext.commands import group, CheckFailure
from ..i18n import embed, i18n
from ..games import Games
from ..tmpfiles import tmpf
from ..utils import lone_group, DummyCtx
from .data import Board, Player, PlayerState, Jail

sql.register_adapter(Board, pickle.dumps)

MY_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    'resources', 'monopoly'
)
def f(name):
    return os.path.join(MY_DIR, name)

def roll():
    return (random.randint(1, 6), random.randint(1, 6))

BOARD = None#pygame.image.load(f('board.png'))
GAMES = 0

class Monopoly(Games):
    """monopoly/cog-desc"""

    @staticmethod
    async def _sendsurf(meth, surf, **kwargs):
        with tmpf('monopoly-', '.png') as name:
            pygame.image.save(surf, name)
            file = discord.File(name, 'image.png')
            await meth(file=file, **kwargs)

    @group(invoke_without_command=True, aliases=[
        'mnply', 'monop'
    ], description='monopoly/monopoly-desc')
    @lone_group(True)
    async def monopoly(self, ctx):
        """monopoly/monopoly-help"""
        pass

    name = 'Monopoly'
    maxim = 4
    minim = 2
    scn = 'monopoly start'
    jcn = 'monopoly join'
    singleton = True

    @monopoly.command(description='monopoly/join-desc')
    async def join(self, ctx, against: discord.Member = None):
        await self._join_global_game(ctx, self._create_monopoly)

    @monopoly.command(description='monopoly/leave-desc')
    async def leave(self, ctx):
        await self._unjoin_global_game(ctx)

    @monopoly.command(description='monopoly/start-desc')
    async def start(self, ctx):
        await self._start_global_game(ctx)

    async def _create_monopoly(self, ctxs):
        global BOARD, GAMES
        #remove players already playing
        for i in iter(ctxs):
            res = self.db.execute(
                'SELECT monopoly_game FROM users WHERE user_id=?',
                (i.author.id,)
            ).fetchone()
            if res and res[0]:
                ctxs.remove(i)
                await i.author.dm_channel.send(embed=embed(i,
                    title=('error',),
                    description=('monopoly/already-playing',),
                    color=0xff0000
                ))
        if BOARD is None:
            BOARD = pygame.image.load(f('board.png'))
        tokens = list(map(lambda i: i + 1, range(len(os.listdir(f('tokens'))))))
        random.shuffle(tokens)
        players = [
            Player(
                name=i.author.name,
                id=i.author.id,
                token=tokens.pop(0)
            )
            for i in ctxs
        ]
        board = Board()
        game_id = round(time.time()) + GAMES
        GAMES += 1
        self.db.execute(
            'INSERT INTO monopolies VALUES (?, ?, ?, ?)',
            (game_id, 0, players, board)
        )
        self.db.executemany(
            'UPDATE users SET monopoly_game=? WHERE user_id=?',
            ((game_id, i.author.id) for i in ctxs)
        )
        asyncio.create_task(self._play_monopoly(game_id))

    async def _play_monopoly(self, game_id):
        try:
            while 1:
                try:
                    players
                except NameError:
                    game_id, players, board = await self._load_monopoly(None, game_id)
                for whose_turn, player in enumerate(players):
                    #breakpoint()
                    game_id, players, board = await self._load_monopoly(None, game_id)
                    dbl = True
                    dbls = 0
                    while dbl:
                        dbl = await self._turn_monopoly(game_id, player, players, board)
                        if dbl:
                            dbls += 1
                        if dbls >= 3:
                            dbl = False
                            player.on = Jail.space
                            player.state |= PlayerState.JAILED1
                            ctx = DummyCtx(
                                author=self.bot.get_user(player.id),
                                channel=DummyCtx(id=0)
                            )
                            await ctx.author.send(embed=embed(ctx,
                                title=('monopoly/speeding-title',),
                                description=('monopoly/speeding',),
                                color=0
                            ))
                    self._save_monopoly(game_id, players, board, whose_turn)
        finally:
            try:
                self.db.execute('DELETE FROM monopolies WHERE game_id=?', (game_id,))
                self.db.execute(
                    'UPDATE users SET monopoly_game=NULL WHERE monopoly_game=?',
                    (game_id,)
                )
                self._done_global_game(players)
            except sql.ProgrammingError:
                os.system('py "delet monop.py"')

    async def _choice(self, ctx, emb):
        msg = await ctx.author.send(embed=emb)
        YEA, NAY = '\u2705\u274e'
        await msg.add_reaction(YEA)
        await msg.add_reaction(NAY)
        reaction, user = await self.bot.wait_for('reaction_add', check=lambda r, u: (
            str(r) in (YEA, NAY)
            and r.message.id == msg.id
            and u.id == ctx.author.id
        ))
        return str(reaction) == YEA

    async def _turn_monopoly(self, game_id, player, players, board):
        author = self.bot.get_user(player.id)
        ctx = DummyCtx(author=author, channel=DummyCtx(id=0))
        #die1, die2 = roll()
        die1, die2 = map(int, (
            await self.bot.wait_for(
                'message', check=lambda m: m.author.id == player.id
            )
        ).content.split(', '))
        await self._sendsurf(ctx.author.send, BOARD, embed=embed(ctx,
            title=('monopoly/rolled-title',),
            description=('monopoly/rolled', die1, die2, player.worth),
            color=0xffffff
        ))
        if player.state & PlayerState.IN_JAIL:
            if die1 == die2: #doubles :)
                player.state &= ~PlayerState.IN_JAIL # clear all jail flags
            elif player.state & PlayerState.JAILED3: #already the third time
                player.worth -= 50
                player.state &= ~PlayerState.IN_JAIL
            else:
                if player.state & PlayerState.HAS_GOJ:
                    if (await self._choice(ctx, embed(ctx,
                            title=('monopoly/use-goj?-title',),
                            description=('monopoly/use-goj?',),
                            color=0xffff00
                    ))):
                        player.state &= ~(PlayerState.HAS_GOJ | PlayerState.IN_JAIL)
                elif player.worth >= 50:
                    if (await self._choice(ctx, embed(ctx,
                            title=('monopoly/jail-fine-title',),
                            description=('monopoly/jail-fine',),
                            color=0xffff00
                    ))):
                        player.worth -= 50
                        player.state &= ~PlayerState.IN_JAIL
                else:
                    player.state <<= 1
                    return False
        player.on += die1 + die2
        space = board.spaces[player.on]
        print('{} is now on {} ({})'.format(player.name, player.on, space.name))
        action = (await space.action(ctx, player, die1 + die2))
        if (
                action is True #for sale to this worth
                and (await self._choice(ctx, embed(ctx,
                    title=('monopoly/buy-prop?-title',),
                    description=('monopoly/buy-prop?', space.name),
                    color=0xffff00
                ))) #chosen to
        ):
            player.worth -= space.cost
            space.owner = player.id
            player.owned.add(space.space)
            group = tuple(board.get_properties_by_group(space.group))
            if space.group in {'releases', 'teams'}:
                count = 0
                for p in group:
                    if p.owner == player.id:
                        count += 1
                for p in group:
                    if p.owner == player.id:
                        p.houses = count
            else:
                owns_all = True
                for p in group:
                    if p.owner != player.id:
                        owns_all = False
                        break
                if owns_all:
                    for p in group:
                        if not p.houses:
                            p.houses = -1
        elif (
                action is True #chose no
                or bool(action) is False #or all taken care of
        ):
            pass
        else:
            for p in players:
                if p.id == action[0]:
                    p.worth += action[1]
                    break
        if player.worth < 0: # :(
            await self._maybe_bankrupt(ctx, player, players, board)
        return die1 == die2

    async def _load_monopoly(self, ctx, real_game_id=None):
        if real_game_id is None:
            res = self.db.execute(
                'SELECT monopoly_game FROM users WHERE user_id=?',
                (ctx.author.id,)
            ).fetchone()
            if res is None or res[0] is None:
                await ctx.author.send(embed=embed(ctx,
                    title=('error',),
                    description=('monopoly/not-in-game',),
                    color=0xff0000
                ))
                raise CheckFailure
            game_id = res[0]
        else:
            game_id = real_game_id
        res = self.db.execute(
            'SELECT players, properties FROM monopolies WHERE game_id=?',
            (game_id,)
        ).fetchone()
        if real_game_id is None:
            if res is None or res[0] is None:
                self.db.execute(
                    'UPDATE users SET monopoly_game=? WHERE user_id=?',
                    (None, ctx.author.id)
                )
                await ctx.author.send(embed=embed(ctx,
                    title=('error',),
                    description=('monopoly/not-in-game',),
                    color=0xff0000
                ))
                raise CheckFailure
            for p in res['players']:
                if p.id == ctx.author.id:
                    player = p
            try:
                player
            except NameError:
                self.db.execute(
                    'UPDATE users SET monopoly_game=? WHERE user_id=?',
                    (None, ctx.author.id)
                )
                await ctx.author.send(embed=embed(ctx,
                    title=('error',),
                    description=('monopoly/not-in-game',),
                    color=0xff0000
                ))
                raise CheckFailure
            return (game_id, player, res['players'], res['properties'])
        return (game_id, res['players'], res['properties'])

    def _save_monopoly(self, game_id, players, board, whose_turn):
        with self.db.connection:
            self.db.execute(
                'UPDATE monopolies SET players=?, properties=?, whose_turn=? \
WHERE game_id=?',
                (players, board, whose_turn, game_id)
            )

    async def not_enough_money(self, ctx):
        await ctx.author.send(embed=embed(ctx,
            title=('error',),
            description=('monopoly/not-enough-money',),
            color=0xff0000
        ))

    @monopoly.command(description='monopoly/give-desc')
    async def give(self, ctx, who: discord.User, *, thing=None):
        game_id, player, players, board = await self._load_monopoly(ctx)
        for p in players:
            if p.id == who.id:
                other = p
        try:
            other
        except NameError:
            return await ctx.author.send(embed=embed(ctx,
                title=('error',),
                description=('monopoly/unknown-player',),
                color=0xff0000
            ))
        if thing is None:
            if not (player.state & PlayerState.HAS_GOJ):
                return await ctx.author.send(embed=embed(ctx,
                    title=('error',),
                    description=('monopoly/no-goj',),
                    color=0xff0000
                ))
            given = 'gojf'
            other.state |= PlayerState.HAS_GOJ
            player.state &= ~PlayerState.HAS_GOJ
        else:
            prop = board.get_property_by_name(thing)
            if prop is None:
                try:
                    amount = int(thing)
                except ValueError:
                    return await ctx.author.send(embed=embed(ctx,
                        title=('error',),
                        description=('monopoly/unknown-property', thing),
                        color=0xff0000
                    ))
                else:
                    given = 'muns'
                    other.worth += amount
                    player.worth -= amount
                    if player.worth < 0:
                        return await self.not_enough_money(ctx)
            else:
                given = 'prop'
                prop.owner = other.id
                other.owned.add(prop.space)
                player.owned.remove(prop.space)
        self._save_monopoly(game_id, players, board)
        await ctx.author.send(embed=embed(ctx,
            title=('success',),
            description=(
                'monopoly/item-given',
                (
                    thing or i18n(ctx, 'monopoly/goj-given')
                    if given != 'muns'
                    else thing + ' ' + i18n(ctx, 'monopoly/currency')
                )
            ),
            color=0x55acee
        ))

    @monopoly.command(description='monopoly/unmortgage-desc')
    async def unmortgage(self, ctx, *, property_name):
        game_id, player, players, board = await self._load_monopoly(ctx)
        prop = board.get_property_by_name(property_name)
        if prop is None:
            return await ctx.author.send(embed=embed(ctx,
                title=('error',),
                description=('monopoly/unknown-property', property_name),
                color=0xff0000
            ))
        player.worth -= prop.mort * 1.1
        prop.mortgaged = False
        if player.worth < 0:
            ## let it be known that this
            ## was the first lack of worth
            ## coded into the game.
            return await self.not_enough_money(ctx) #w/o saving
        self._save_monopoly(game_id, players, board)
        await ctx.author.send(embed=embed(ctx,
            title=('success',),
            description=('monopoly/unmortgaged', prop.name),
            color=0x55acee
        ))
