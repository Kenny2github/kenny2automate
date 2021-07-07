from __future__ import annotations
import os
import json
from typing import Iterable, Union
import aiofiles
import discord
from discord.ext import commands

ROOT = 'l10n'
SUPPORTED_LANGS = set(
    fn[:-5] for fn in os.listdir(ROOT) if fn.endswith('.json'))

IDContext = Union[commands.Context, discord.abc.Snowflake]

class Msg:
    """Represents an i18n string by key."""

    unformatted: dict[str, dict[str, str]] = {}
    user_langs: dict[int, str] = {}
    channel_langs: dict[int, str] = {}

    def __init__(
        self,
        ctx: Union[commands.Context, str],
        key: str = None, *params: str,
        lang: str = None, **kwparams: str
    ):
        if lang is not None:
            self.lang = lang
            if key is not None:
                params = (key, *params)
            key = ctx # Msg(key, ..., lang=...)
        elif isinstance(ctx, commands.Context):
            self.set_lang(ctx)
        else:
            self.lang = None
            if key is not None:
                params = (key, *params)
            key = ctx # Msg(key, ...)
        self.key = key
        self.params = params
        self.kwparams = kwparams
        if self.lang is None:
            self.message = None
        else:
            self.set_message()

    def set_message(self):
        if self.lang == 'qqx':
            self.message = f'({self.default()})'
        else:
            self.message = self.unformatted[self.lang].get(self.key)
            if self.message is None:
                self.message = '\N{MATHEMATICAL LEFT ANGLE BRACKET}'
                self.message += self.default()
                self.message += '\N{MATHEMATICAL RIGHT ANGLE BRACKET}'

    def __str__(self) -> str:
        """Format the message and return it for use."""
        if self.message is None:
            if self.lang is None:
                return f'<Msg key={self.key} params={self.params} ' \
                    f'kwparams={self.kwparams}>'
            # lang is no longer None, finally get the string
            self.set_message()
        return self.message.format(*self.params, **self.kwparams)

    def __add__(self, other: str) -> str:
        return str(self) + str(other)

    def __radd__(self, other: str) -> str:
        return str(other) + str(self)

    def default(self) -> str:
        """Default message (without brackets) if no i18n available."""
        result = self.key
        if self.params or self.kwparams:
            result += ': '
        if self.params:
            result += ', '.join(
                f'{{{i}}}' for i in range(len(self.params)))
        if self.kwparams:
            if self.params:
                result += ', '
            result += ', '.join(
                f'{key}={{{key}}}' for key in self.kwparams)
        return result

    @classmethod
    async def load_state(cls):
        """Load translation strings and user/channel language data."""
        for lang in SUPPORTED_LANGS:
            async with aiofiles.open(os.path.join(ROOT, f'{lang}.json')) as f:
                data: dict = json.loads(await f.read())
            cls.unformatted.setdefault(lang, {}).update(data)
        for dirname in os.listdir(ROOT):
            if not os.path.isdir(os.path.join(ROOT, dirname)):
                continue
            for lang in SUPPORTED_LANGS:
                path = os.path.join(ROOT, dirname, f'{lang}.json')
                async with aiofiles.open(path) as f:
                    data: dict = json.loads(await f.read())
                for key, value in data.items():
                    cls.unformatted[lang][f'{dirname}/{key}'] = value
        # TODO: load user_langs and channel_langs from DB

    @classmethod
    def get_lang(cls, ctx: IDContext) -> str:
        """Get the correct language for the context."""
        if hasattr(ctx, 'id'):
            if ctx.id in cls.user_langs:
                return cls.user_langs[ctx.id]
        elif ctx.author.id in cls.user_langs:
            return cls.user_langs[ctx.author.id]
        if isinstance(ctx, commands.Context):
            if ctx.channel.id in cls.channel_langs:
                return cls.channel_langs[ctx.channel.id]
        return 'en'

    def set_lang(self, ctx: IDContext):
        """Set this message's language for this context."""
        self.lang = self.get_lang(ctx)

MsgStr = Union[Msg, str]

def cast(ctx: commands.Context, msg: MsgStr) -> str:
    """If a message is a plain string, return it.
    Otherwise, render the message in the context.
    """
    if isinstance(msg, str):
        return msg
    msg.set_lang(ctx)
    return str(msg)

def Embed(
    ctx: commands.Context,
    title: MsgStr = None,
    description: MsgStr = None,
    fields: Iterable[tuple[MsgStr, MsgStr, bool]] = None,
    footer: MsgStr = None,
    **kwargs
):
    """Return an Embed with internationalized data."""
    if title:
        kwargs['title'] = cast(ctx, title)
    if description:
        kwargs['description'] = cast(ctx, description)
    embed = discord.Embed(**kwargs)
    if footer:
        embed.set_footer(text=cast(ctx, footer))
    for name, value, inline in fields or ():
        embed.add_field(
            name=cast(ctx, name),
            value=cast(ctx, value),
            inline=inline
        )
    return embed
