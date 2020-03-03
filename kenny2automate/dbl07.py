import asyncio
import discord
from discord.ext.commands import group
from .games import Games
from .i18n import embed
from .utils import background, lone_group

class Dbl07(Games):
    """007/cog-desc"""

    name = '007'
    coro = '_dbl07'
    maxim = 2
    minim = 2
    jcn = '007 join'

    @group(name='007', invoke_without_command=True, description='007/cmd-desc')
    @lone_group(True)
    async def dbl07(self, ctx):
        """007/cmd-help"""
        pass

    @dbl07.command(description='007/join-desc')
    async def join(self, ctx):
        await self._join_global_game(ctx)

    @dbl07.command(description='007/leave-desc')
    async def leave(self, ctx):
        await self._unjoin_global_game(ctx)

    @dbl07.command(description='007/here-desc')
    async def here(self, ctx, against: discord.Member = None):
        try:
            player1, player2 = await self._gather_game(ctx, against)
        except (TypeError, ValueError):
            return
        await self._dbl07((DummyCtx(author=player1),
                           DummyCtx(author=player2)), ())

    async def _dbl07(self, ctxs, specs):
        LOAD, FIRE, PROTECT = ACTIONS = '\U0001f4e5\U0001f52b\U0001f6e1'
        players = tuple(i.author for i in ctxs)
        deeta = tuple({'shields': 0, 'ammo': 0} for _ in range(2))
        async def action(player):
            msg = await player.send(embed=embed(player,
                title=('007/action-title',),
                description=('007/action', *ACTIONS),
                color=0xffff00
            ))
            await asyncio.gather(*(msg.add_reaction(i) for i in ACTIONS))
            r, u = await self.bot.wait_for('reaction_add', check=lambda r, u: (
                r.emoji in ACTIONS
                and u.id == player.id
                and r.message.id == msg.id
            ))
            return r.emoji
        def ret_winner(acts, idx):
            if actions[idx] == FIRE:
                if deeta[idx]['ammo'] <= 0:
                    return None
                # note: idx-1 can be negative,
                # but it still ends up being
                # whichever is the other item
                # in a 2-tuple
                if acts[idx-1] == LOAD:
                    ret = idx
                if acts[idx-1] == FIRE:
                    if deeta[idx]['ammo'] > deeta[idx-1]['ammo']:
                        ret = idx
                    elif deeta[idx]['ammo'] < deeta[idx-1]['ammo']:
                        ret = idx-1
                    else:
                        ret = None # tie, continue
                    deeta[idx-1]['ammo'] = 0
                if acts[idx-1] == PROTECT:
                    if deeta[idx]['ammo'] > deeta[idx-1]['shields']:
                        ret = idx
                    else:
                        ret = None
                    deeta[idx-1]['shields'] = max(0, deeta[idx-1]['shields']
                                                     - deeta[idx]['ammo'])
                deeta[idx]['ammo'] = 0
                return ret
            if acts[idx] == LOAD:
                deeta[idx]['ammo'] += 1
            if acts[idx] == PROTECT:
                deeta[idx]['shields'] += 1
            return None
        def fields(pid):
            return sum(((
                (('007/player-' + ('you' if i == pid else 'them'),), actions[i], True),
                (('007/ammo-title',), str(deeta[i]['ammo']), True),
                (('007/shields-title',), str(deeta[i]['shields']), True)
            ) for i, play in enumerate(players)), ())
        actions = (('none',),) * 2
        for pid, player in enumerate(players):
            background(player.send(embed=embed(player,
                title=('007/start-title',),
                description=('007/start',),
                fields=fields(pid),
                color=0xee00ee
            )))
        winner = None
        while winner is None:
            actions = await asyncio.gather(*(action(i) for i in players))
            if actions[1] == PROTECT: #shield comes first
                first, second = 1, 0
            else:
                first, second = 0, 1
            winner = ret_winner(actions, first)
            if winner is not None:
                break
            winner = ret_winner(actions, second)
            if winner is not None:
                break
            for pid, player in enumerate(players):
                background(player.send(embed=embed(player,
                    title=('007/round-title',),
                    description=('007/round',),
                    fields=fields(pid),
                    color=0xfffffe
                )))
        winner %= 2
        msgs = await asyncio.gather(*(player.send(embed=embed(player,
            title=('007/game-over-title',),
            description=('007/you-' + ('lost' if winner != pid else 'won'),),
            fields=fields(pid),
            color=0xff0000 if winner != pid else 0x55acee,
            footer=('games/rematch',)
        )) for pid, player in enumerate(players)))
        await self._rematch(msgs, ctxs)
