from functools import wraps
from typing import Optional, TypeVar
from discord.ext import commands

T = TypeVar('T')

class AttrDict:
    """Access data by key or attribute."""
    def __init__(self, attrs: dict[str, T]):
        self.__dict__.update(attrs)
    def __getitem__(self, key: str) -> T:
        return self.__dict__[key]
    def __setitem__(self, key: str, value: T):
        self.__dict__[key] = value
    def __repr__(self) -> str:
        return repr(self.__dict__)
    def __str__(self) -> str:
        return str(self.__dict__)
    def get(self, key: str, default: T = None) -> Optional[T]:
        return self.__dict__.get(key, default)

def lone_group(func):
    """Send group help if the group itself is invoked."""
    @wraps(func)
    async def newfunc(*args):
        for arg in args:
            if isinstance(arg, commands.Context):
                ctx = arg
                break
        else:
            return
        if ctx.invoked_subcommand is not None:
            return
        await ctx.send_help(ctx.command)
    return newfunc