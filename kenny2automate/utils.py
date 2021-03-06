import asyncio
from functools import wraps, partial
from discord.ext import commands

class DummyCtx(object):
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)

def dataclass(cls):
    def __init__(self, *args, **kwargs):
        taken_care_of = set()
        len_annos = len(cls.__annotations__)
        len_args = len(args)
        if len_annos < len_args:
            raise TypeError('__init__() takes '
                            '{} positional arguments but {} were given'.format(
                                len_annos, len_args
                            ))
        for name, arg in zip(cls.__annotations__.keys(), args):
            if not isinstance(arg, cls.__annotations__[name]):
                raise TypeError('argument {!r} is not of type {!r}'.format(
                    name, cls.__annotations__[name].__name__
                ))
            setattr(self, name, arg)
            taken_care_of.add(name)
        for name, value in kwargs.items():
            if name in taken_care_of:
                raise TypeError('__init__() got multiple values for argument '
                                '{!r}'.format(name))
            if not isinstance(value, cls.__annotations__.get(name, object)):
                raise TypeError('argument {!r} is not of type {!r}'.format(
                    name, cls.__annotations__[name].__name__
                ))
            taken_care_of.add(name)
            setattr(self, name, value)
        for name in cls.__annotations__:
            if name not in taken_care_of and not hasattr(cls, name):
                raise TypeError('__init__() missing 1 required argument: '
                                '{!r}'.format(name))
            #weird memory stuff
            elif hasattr(cls, name) \
                    and cls.__annotations__[name] in {list, set, dict}:
                setattr(self, name, cls.__annotations__[name]())
    def copy(self):
        return cls(**self.__dict__)
    def __eq__(self, other):
        if not isinstance(other, cls):
            return False
        for name, value in self.__dict__.items():
            if isinstance(value, type(lambda:None)):
                continue
            if isinstance(getattr(other, name), type(lambda:None)):
                continue
            if getattr(other, name) != value:
                return False
        return True
    cls.__init__ = __init__
    cls.copy = copy
    cls.__eq__ = __eq__
    return cls

def lone_group(in_cls=True):
	def wrapper(func):
		@wraps(func)
		async def newfunc(*args):
			for arg in args:
				if isinstance(arg, commands.Context):
					ctx = arg
					break
			else:
				return
			ctx.bot.help_command.context = ctx
			await ctx.bot.help_command.send_group_help(ctx.command)
		return newfunc
	return wrapper

async def q(call, *args, **kwargs):
	return await asyncio.get_event_loop().run_in_executor(
		None, partial(call, *args, **kwargs)
	)
background = asyncio.create_task
