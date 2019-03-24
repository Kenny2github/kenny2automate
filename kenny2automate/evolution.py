import random
import pickle
import sqlite3 as sql
import discord as d
from discord.ext.commands import group, Cog
from .i18n import i18n, embed
from .utils import dataclass, DummyCtx

#Strength, Constitution, Dexterity, Intelligence, Wisdom, Charisma, Sex
db = None

@dataclass
class Gene(object):
    str: (int, float)
    con: (int, float)
    dex: (int, float)
    chr: (int, float)
    wis: (int, float)
    int: (int, float)
    sex: str

    @staticmethod
    def _combstat(one, two):
        if one < 0 and two < 0:
            if one == two:
                return 1
            else:
                return min(one, two)
        elif one < 0:
            return abs(one) * two
        elif two < 0:
            return abs(two) * one
        else:
            return max(one, two)

    def combine(self, other):
        if not isinstance(other, Gene):
            return NotImplemented
        return Gene(
            self._combstat(self.str, other.str),
            self._combstat(self.con, other.con),
            self._combstat(self.dex, other.dex),
            self._combstat(self.chr, other.chr),
            self._combstat(self.wis, other.wis),
            self._combstat(self.int, other.int),
            self.sex if sum(map(abs, (
                self.str, self.con, self.dex,
                self.chr, self.wis, self.int
            ))) > sum(map(abs, (
                other.str, other.con, other.dex,
                other.chr, other.wis, other.int
            ))) else other.sex
        )

    __or__ = __add__ = __mul__ = combine

    def __repr__(self):
        def mult(thing):
            if thing < 0:
                return 'x{:.1f}'.format(abs(thing))
            return '{:.1f}'.format(thing)
        return 'str: {} con: {} dex: {} chr: {} wis: {} int: {} sex: {}'.format(
            mult(self.str), mult(self.con), mult(self.dex),
            mult(self.chr), mult(self.wis), mult(self.int),
            self.sex
        )

@dataclass
class Entity(object):
    soul: int
    genes: tuple
    children: set = set()
    parents: frozenset = frozenset()

    @property
    def dominant(self):
        return self.genes[0] | self.genes[1]

    def procreate(self, other):
        if not isinstance(other, Entity):
            return NotImplemented
        if not (self.soul or other.soul):
            #nameless entities cannot reproduce
            return NotImplemented
        new = Entity(0, ( #claiming is done afterwards
            random.choice(self.genes), random.choice(other.genes)
        ), parents=frozenset((self.soul, other.soul)))
        db.execute(
            'INSERT INTO evol_unnamed_children (child) VALUES (?)',
            (new,)
        )
        claim = db.execute('SELECT entry_id FROM evol_unnamed_children ORDER BY \
entry_id DESC').fetchone()[0]
        self.children.add(claim | 2**128)
        other.children.add(claim | 2**128)
        return new

    __mul__ = __add__ = __or__ = procreate

sql.register_adapter(Entity, pickle.dumps)

class Evolution(Cog):
    """evolution/cog-desc"""
    def __init__(self, bot, db_):
        self.bot = bot
        global db
        db = db_

    def cog_check(self, ctx):
        return ctx.guild is None

    async def load_player(self, ctx):
        res = db.execute(
            'SELECT evol_self FROM users WHERE user_id=?',
            (ctx.author.id,)
        ).fetchone()
        if res is None or res[0] is None:
            await ctx.send(embed=embed(ctx,
                title=('evolution/claiming-soul-title',),
                description=('evolution/claiming-soul',),
                color=0x808080
            ))
            try:
                entry_id, husk = db.execute('SELECT entry_id, child FROM \
evol_unnamed_children ORDER BY entry_id ASC').fetchone()
            except TypeError: #was None
                gene1 = Gene(
                    *(random.choice((
                        random.randint(
                            3, random.randint(3, 18)
                        ), random.randint(3, 5) * -0.5
                    )) for _ in range(6)),
                    random.choice(('X', 'Y'))
                )
                gene2 = Gene(
                    *(random.choice((
                        random.randint(
                            3, random.randint(3, 18)
                        ), random.randint(3, 5) * -0.5
                    )) for _ in range(6)),
                    random.choice(('X', 'Y'))
                )
                new = Entity(ctx.author.id, (gene1, gene2), parents=frozenset())
                if res is None:
                    db.execute(
                        'INSERT INTO users (user_id, evol_self) VALUES (?, ?)',
                        (ctx.author.id, new)
                    )
                else:
                    db.execute(
                        'UPDATE users SET evol_self=? WHERE user_id=?',
                        (new, ctx.author.id)
                    )
                await ctx.send(embed=embed(ctx,
                    title=('evolution/no-new-souls-title',),
                    description=(
                        'evolution/no-new-souls',
                        repr(new.dominant)
                    ),
                    color=0
                ))
                return new
            husk.soul = ctx.author.id
            if res is None:
                db.execute(
                    'INSERT INTO users (user_id, evol_self) VALUES (?, ?)',
                    (ctx.author.id, husk)
                )
            else:
                db.execute(
                    'UPDATE users SET evol_self=? WHERE user_id=?',
                    (husk, ctx.author.id)
                )
            db.execute(
                'DELETE FROM evol_unnamed_children WHERE entry_id=?',
                (entry_id,)
            )
            for parent in husk.parents:
                u = self.bot.get_user(parent)
                if u.dm_channel is None:
                    await u.create_dm()
                dmx = DummyCtx(
                    author=u, channel=u.dm_channel, send=u.dm_channel.send
                )
                p = await self.load_player(dmx)
                for c in p.children:
                    if c & 2**128-1 == entry_id:
                        p.children.remove(c)
                        p.children.add(ctx.author.id)
                        break
                self.save_player(p)
                await dmx.send(embed=embed(dmx,
                    title=('evolution/birth-title',),
                    description=(
                        'evolution/birth',
                        ctx.author.name, ctx.author.discriminator,
                        repr(husk.dominant)
                    ),
                    color=0x55acee
                ))
            await ctx.send(embed=embed(ctx,
                title=('evolution/claimed-soul-title',),
                description=(
                    'evolution/claimed-soul', repr(husk.dominant)
                ),
                color=0x55acee
            ))
            res = (husk,)
        me = res[0]
        return me

    def save_player(self, player):
        db.execute(
            'UPDATE users SET evol_self=? WHERE user_id=?',
            (player, player.soul)
        )

    @group(description='evolution/evol-desc')
    async def evol(self, ctx):
        pass

    @evol.command(description='evolution/adopt-desc')
    async def adopt(self, ctx):
        """evolution/adopt-help"""
        me = await self.load_player(ctx)
        gene1 = Gene(
            *(random.choice((
                random.randint(
                    3, random.randint(3, 18)
                ), random.randint(3, 5) * -0.5
            )) for _ in range(6)),
            random.choice(('X', 'Y'))
        )
        gene2 = Gene(
            *(random.choice((
                random.randint(
                    3, random.randint(3, 18)
                ), random.randint(3, 5) * -0.5
            )) for _ in range(6)),
            random.choice(('X', 'Y'))
        )
        new = Entity(0, (gene1, gene2), parents=frozenset((me.soul,)))
        db.execute(
            'INSERT INTO evol_unnamed_children (child) VALUES (?)',
            (new,)
        )
        claim = db.execute('SELECT entry_id FROM evol_unnamed_children ORDER BY \
entry_id DESC').fetchone()[0]
        me.children.add(claim | 2**128)
        self.save_player(me)
        await ctx.send(embed=embed(ctx,
            title=('evolution/adopted-title',),
            description=('evolution/adopted',),
            color=0x55acee
        ))

    @evol.command(description='evolution/propose-desc')
    async def propose(self, ctx, other: d.User, *, message: str):
        """evolution/propose-help"""
        if other.dm_channel is None:
            await other.create_dm()
        dmx = DummyCtx(
            send=other.dm_channel.send,
            channel=other.dm_channel,
            author=other
        )
        await self.load_player(ctx) #make sure they exist
        await self.load_player(dmx)
        msg = await dmx.send(embed=embed(dmx,
            title=('evolution/proposal-title',),
            description=(
                'evolution/proposal',
                ctx.author.name, ctx.author.discriminator,
                message
            ),
            color=0xff0000
        ))
        await msg.add_reaction('\u2705') #check
        await msg.add_reaction('\u274c') #cross
        await ctx.send(embed=embed(ctx,
            title=('evolution/proposed-title',),
            description=('evolution/proposed',),
            color=0xff0000
        ))
        @self.bot.listen()
        async def on_reaction_add(reaction, user):
            if reaction.emoji not in '\u2705\u274c' or user.id != dmx.author.id:
                return
            self.bot.remove_listener(on_reaction_add, 'on_reaction_add')
            if reaction.emoji == '\u274c':
                await ctx.send(embed=embed(ctx,
                    title=('evolution/proposal-rejected-title',),
                    description=(
                        'evolution/proposal-rejected',
                        dmx.author.name, dmx.author.discriminator
                    ),
                    color=0xff0000
                ))
                await dmx.send(embed=embed(dmx,
                    title=('evolution/rejected-proposal-title',),
                    description=(
                        'evolution/rejected-proposal',
                        ctx.author.name, ctx.author.discriminator
                    ),
                    color=0
                ))
                return
            if reaction.emoji == '\u2705':
                me = await self.load_player(ctx)
                you = await self.load_player(dmx)
                me * you
                await ctx.send(embed=embed(ctx,
                    title=('evolution/proposal-accepted-title',),
                    description=(
                        'evolution/proposal-accepted',
                        dmx.author.name, dmx.author.discriminator
                    ),
                    color=0x55acee
                ))
                await dmx.send(embed=embed(dmx,
                    title=('evolution/accepted-proposal-title',),
                    description=(
                        'evolution/accepted-proposal',
                        ctx.author.name, ctx.author.discriminator
                    ),
                    color=0x55acee
                ))
                self.save_player(me)
                self.save_player(you)

    @evol.command(description='evolution/profile-desc')
    async def profile(self, ctx):
        me = await self.load_player(ctx)
        await ctx.send(embed=embed(ctx,
            color=0xffffff,
            fields=(
                (
                    ('evolution/your-genes',),
                    repr(me.dominant),
                    False
                ), (
                    ('evolution/your-parents',),
                    '\n'.join(
                        '@{0.name}#{0.discriminator}'.format(
                            self.bot.get_user(i)
                        ) for i in me.parents
                    ) or ('evolution/no-parents',),
                    True
                ), (
                    ('evolution/your-children',),
                    '\n'.join(
                        '@{0.name}#{0.discriminator}'.format(
                            self.bot.get_user(i)
                        ) if not i & 2**128 else i18n(
                            ctx, 'evolution/husk'
                        )
                        for i in me.children
                    ) or ('evolution/no-children',),
                    True
                )
            )
        ))
