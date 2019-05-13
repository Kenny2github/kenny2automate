from os.path import dirname, join
from enum import IntFlag
from json import load
from ..i18n import embed

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
            player.worth -= amount
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
        await ctx.author.send('{} landed on Community Chest'.format(player)) #TODO

class Chance(Special):
    name = '@someone'
    space: int
    async def action(self, ctx, player, dieroll):
        await ctx.author.send('{} landed on Chance'.format(player)) #TODO

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

    def __init__(self):
        spaceclasses = self.spaces
        spaces = []
        releases = iter(data['releases']['names'])
        taxes = iter(data['tax'])
        teams = iter(data['teams']['names'])
        properties = (p for g in data['groups'] for p in g['properties'])
        groups = (g['name'] for g in data['groups'] for p in g['properties'])
        i = 0
        for s in spaceclasses:
            if issubclass(s, Special):
                spaces.append(s(space=i))
                if s is Jail:
                    Jail.space = i
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

class PlayerState(IntFlag):
    NOTHING = 0b0000
    JAILED1 = 0b0001
    JAILED2 = 0b0010
    JAILED3 = 0b0100
    HAS_GOJ = 0b1000
    IN_JAIL = 0b0111

class Player:
    def __init__(
        self, name, id, token,
        owned=None, on=0, worth=1500,
        state=PlayerState.NOTHING
    ):
        self.name = name
        self.id = id
        self.token = token
        self.owned = owned or set()
        self.on = on
        self.worth = worth
        self.state = state

    name: str #player name
    id: int #player ID
    token: int #token number

    def __repr__(self):
        return self.name

    #dynamic
    owned: set = set() #set of int spaces
    on: int = 0 #int space that the player is on
    worth: int = 1500 #net worth
    state: PlayerState = PlayerState.NOTHING
