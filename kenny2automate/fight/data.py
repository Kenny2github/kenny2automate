import random
import json
import os
import discord.ext.commands as c
from ..i18n import i18n
from ..utils import dataclass as _dataclass

@_dataclass
class Weapon(object):
    name: str
    damage: (int, type(lambda:None))
    price: int = None
    emoji: str = '\U0001f5e1'

    def nam(self, ctx):
        return '{} {}'.format(self.emoji, i18n(ctx, self.name))

    @classmethod
    async def convert(cls, ctx, argument):
        if argument not in weapons:
            raise c.BadArgument('{!r} is not a valid weapon'.format(argument))
        return weapons[argument]

class RandomWeapon(object):
    def __get__(self, instance, owner):
        if instance is None:
            return self
        instance.weapon = random.choice(list(weapons.values()))
        return instance.weapon

def fangs(user, opponent):
    """fight/weapon-fangs-damage"""
    user.health += 1
    if isinstance(opponent.armor.defense, int):
        damage = max(0, 2 - opponent.armor.defense)
    else:
        damage = 2
    opponent.health -= damage
    return damage

def bomb(user, opponent):
    """fight/weapon-bomb-damage"""
    if random.randint(1, 6) + random.randint(1, 6) >= 6:
        opponent.health -= 10
        return 10
    return 0

fns = {
    'fangs': fangs,
    'bomb': bomb
}

with open(os.path.join(os.path.dirname(__file__), 'weapons.json')) as f:
    weapons = json.load(f)
    for name, value in weapons.items():
        if isinstance(value['damage'], str):
            value['damage'] = fns[value['damage']]
        weapons[name] = Weapon(**value)

@_dataclass
class Armor(object):
    name: str
    defense: (int, type(lambda:None))
    price: int

    def nam(self, ctx):
        return '\U0001f6e1 {}'.format(i18n(ctx, self.name))

    @classmethod
    async def convert(cls, ctx, argument):
        if argument not in armors:
            raise c.BadArgument('{!r} is not a valid armor'.format(argument))
        return armors[argument]

def firesuit(user, opponent, damage):
    """fight/armor-firesuit-defense"""
    if opponent.weapon.name[13:] == 'fire':
        user.health += damage
        return 0
    return damage

fns = {
    'firesuit': firesuit
}

with open(os.path.join(os.path.dirname(__file__), 'armors.json')) as f:
    armors = json.load(f)
    for name, value in armors.items():
        if isinstance(value['defense'], str):
            value['defense'] = fns[value['defense']]
        armors[name] = Armor(**value)

@_dataclass
class Item(object):
    name: str
    action: type(lambda:None)
    price: int

    def nam(self, ctx):
        return i18n(ctx, self.name)

    @classmethod
    async def convert(cls, ctx, argument):
        if argument not in items:
            raise c.BadArgument('{!r} is not a valid item'.format(argument))
        return items[argument]

def bandages(user, enemy):
    """fight/item-bandages-action"""
    user.health += 5

def luck(user, opponent):
    """fight/item-luck-action"""
    if (random.randint(1, 6) + random.randint(1, 6)) <= 6:
        opponent.health -= 1
    else:
        opponent.health += 1

fns = {
    'bandages': bandages,
    'luck': luck
}

with open(os.path.join(os.path.dirname(__file__), 'items.json')) as f:
    items = json.load(f)
    for name, value in items.items():
        value['action'] = fns[value['action']]
        items[name] = Item(**value)

@_dataclass
class Enemy(object):
    name: str
    health: int
    reward: int
    weapon: Weapon = RandomWeapon()
    armor: Armor = armors['clothes']

    def nam(self, ctx):
        return i18n(ctx, self.name)

@_dataclass
class Player(object):
    name: str
    health: int
    gold: int = 0
    weapons: list = [weapons['fist']]
    armors: list = [armors['clothes']]
    items: list = []

    @property
    def weapon(self):
        return self.weapons[-1]

    @property
    def armor(self):
        return self.armors[-1]

    def nam(self, ctx):
        return self.name

with open(os.path.join(os.path.dirname(__file__), "monsters.json")) as f:
    monsters = json.load(f)
    for name, value in monsters.items():
        if 'weapon' in value:
            value['weapon'] = weapons[value['weapon']]
        if 'armor' in value:
            value['armor'] = armors[value['armor']]
        monsters[name] = Enemy(**value)
