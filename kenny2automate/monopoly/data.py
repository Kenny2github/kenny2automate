from os.path import dirname, join
import random
from json import load
from ..i18n import embed
from .cards import someones, nitros
from .player import Player, PlayerState

with open(join(dirname(__file__), 'data.json'), 'r') as f:
    data = load(f)

class Space:
    def __repr__(self):
        return self.name
    async def action(self, ctx, player, dieroll):
        pass
    space: int = None

class Property(Space):
    def __init__(
        self, cost: int, rent: list, mort: int,
        name: str, group: str, space: int, hous: int,
        owner: int = None, mortgaged: bool = False,
        houses: int = 0
    ):
        self.cost = cost
        self.rent = rent
        self.mort = mort
        self.name = name
        self.group = group
        self.space = space
        self.hous = hous
        self.owner = owner
        self.mortgaged = mortgaged
        self.houses = houses

    cost: int
    rent: list
    hous: int = 0
    mort: int
    name: str
    group: str
    space: int

    def real_rent(self, level, dieroll) -> int:
        if level == -1:
            return self.rent * 2
        return self.rent[level]

    async def action(self, ctx, player, dieroll):
        if self.owner:
            if player.id == self.owner:
                await ctx.author.send(embed=embed(ctx,
                    title=('monopoly/own-prop-title',),
                    description=('monopoly/own-prop', self.name),
                    color=0x55acee
                ))
                return False
            if self.mortgaged:
                return False
            amount = self.real_rent(self.houses, dieroll)
            await ctx.author.send(embed=embed(ctx,
                title=('monopoly/rent-title',),
                description=('monopoly/rent-paid', amount, self.name),
                color=0xff8080
            ))
            return (self.owner, amount)
        else:
            return player.worth >= self.cost

    #dynamic
    owner: int = None
    mortgaged: bool = False
    houses: int = 0

class Release(Property):
    def __init__(
        self, name: str, space: int,
        owner: int = None, mortgaged: bool = False,
        houses: int = 0
    ):
        super().__init__(
            name=name,
            space=space,
            cost=self.cost,
            rent=self.rent,
            mort=self.mort,
            group=self.group,
            hous=None,
            owner=owner,
            mortgaged=mortgaged,
            houses=houses
        )
    name: str
    space: int
    cost = data['releases']['cost']
    rent = data['releases']['rent']
    mort = data['releases']['mort']
    group: str = 'releases'

    #dynamic
    owner: int = None
    mortgaged: bool = False
    houses: int = 0

class Team(Release):
    name: str
    space: int
    cost = data['teams']['cost']
    rent = data['teams']['rent']
    mort = data['teams']['mort']
    group: str = 'teams'

    def real_rent(self, level, dieroll):
        return self.rent[level] * dieroll

    owner: int = None
    mortgaged: bool = False
    houses: int = None

class Tax(Space):
    def __init__(self, name: str, space: int, tax: int):
        self.name = name
        self.space = space
        self.tax = tax

    name: str
    space: int
    tax: int

    async def action(self, ctx, player, dieroll):
        player.worth -= self.tax
        await ctx.author.send(embed=embed(ctx,
            title=('tax-paid-title',),
            description=('tax-paid', self.name, self.tax),
            color=0xff8080
        ))

class Special(Space):
    name: str
    space: int
    def __init__(self, space):
        self.space = space
    async def action(self, ctx, player, dieroll):
        raise NotImplementedError

class GO(Special):
    name = 'GO'
    space: int = 0
    async def action(self, ctx, player, dieroll):
        player.worth += 200
        await ctx.author.send(embed=embed(
            title=('monopoly/go-title',),
            description=('monopoly/passed-go',),
            color=0x55acee
        ))

class Community(Special):
    name = 'Gifted Nitro'
    space: int
    async def action(self, ctx, player, dieroll):
        self.deck.insert(0, self.deck.pop(-1))
        return await self.deck[0].action(ctx, player, dieroll, self.board)

class Chance(Community):
    name = '@someone'
    space: int

class Jail(Special):
    name = 'Banned/Just Furry'
    space: int = 10
    async def action(self, ctx, player, dieroll):
        await ctx.author.send(embed=embed(ctx,
            title=('monopoly/nothing-happens-title',),
            description=('monopoly/nothing-happens', self.name),
        ))

class Parking(Special):
    name = 'Discord Job'
    space: int = 20
    action = Jail.action

class GoToJail(Special):
    name = 'Get Banned'
    space: int = 30
    async def action(self, ctx, player, dieroll):
        player.on = Jail.space
        player.state |= PlayerState.JAILED1
        # to free: player.state &= ~PlayerState.IN_JAIL
        await ctx.author.send(embed=embed(ctx,
            title=('monopoly/go-to-jail-title',),
            description=('monopoly/go-to-jail',),
            color=0
        ))

class Board:
    spaces = [
        GO,
        Property,
        Community,
        Property,
        Tax,
        Release,
        Property,
        Chance,
        Property,
        Property,
        Jail,
        Property,
        Team,
        Property,
        Property,
        Release,
        Property,
        Community,
        Property,
        Property,
        Parking,
        Property,
        Chance,
        Property,
        Property,
        Release,
        Property,
        Property,
        Team,
        Property,
        GoToJail,
        Property,
        Property,
        Community,
        Property,
        Release,
        Chance,
        Property,
        Tax,
        Property
    ]
    someone_deck: list
    nitro_deck: list

    def __init__(self, players):
        self.players = players
        spaceclasses = self.spaces
        spaces = []
        releases = iter(data['releases']['names'])
        taxes = iter(data['tax'])
        teams = iter(data['teams']['names'])
        properties = (p for g in data['groups'] for p in g['properties'])
        groups = (g['name'] for g in data['groups'] for p in g['properties'])
        i = 0
        self.someone_deck = someones[:]
        self.nitro_deck = nitros[:]
        random.shuffle(self.someone_deck)
        random.shuffle(self.nitro_deck)
        for s in spaceclasses:
            if issubclass(s, Special):
                spaces.append(s(space=i))
                if s is Jail:
                    Jail.space = i
                elif s is Chance:
                    spaces[-1].deck = self.someone_deck
                elif s is Community:
                    spaces[-1].deck = self.nitro_deck
                if issubclass(s, Community):
                    spaces[-1].board = self
            elif s is Property:
                spaces.append(s(**next(properties), group=next(groups), space=i))
            elif s is Release:
                spaces.append(s(next(releases), space=i))
            elif s is Team:
                spaces.append(s(next(teams), space=i))
            elif s is Tax:
                spaces.append(s(**next(taxes), space=i))
            i += 1
        self.spaces = spaces

    def get_property_by_name(self, name):
        for p in self.spaces:
            if p.name == name:
                return p
        return None

    def get_properties_by_group(self, name):
        for p in self.spaces:
            if getattr(p, 'group', None) == name:
                yield p
