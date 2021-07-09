from __future__ import annotations
import os
import json
from typing import Iterable, Union
import aiofiles
import discord
from discord.ext import commands
from .chars import LABR, RABR, DONE
from .db import db
from .logger import getLogger
from .utils import lone_group

ROOT = 'l10n' # TODO: change to i18n
SUPPORTED_LANGS = set(
    fn[:-5] for fn in os.listdir(ROOT) if fn.endswith('.json'))

logger = getLogger('i18n')

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
                self.message = self.unformatted['en'].get(self.key)
            if self.message is None:
                self.message = LABR + self.default() + RABR

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
                if not os.path.isfile(path):
                    if lang != 'qqx': # qqx only has one file
                        logger.warning('No %s i18n for %s', lang, dirname)
                    continue
                async with aiofiles.open(path) as f:
                    data: dict = json.loads(await f.read())
                for key, value in data.items():
                    cls.unformatted[lang][f'{dirname}/{key}'] = value
        cls.user_langs.update(await db.user_langs())
        cls.channel_langs.update(await db.channel_langs())
        logger.info('Loaded i18n cache')

    @classmethod
    def get_lang(cls, ctx: IDContext) -> str:
        """Get the correct language for the context."""
        if not isinstance(ctx, commands.Context):
            # None may
            if cls.user_langs.get(ctx.id, None) is not None:
                return cls.user_langs[ctx.id]
        elif cls.user_langs.get(ctx.author.id, None) is not None:
            return cls.user_langs[ctx.author.id]
        if isinstance(ctx, commands.Context):
            if cls.channel_langs.get(ctx.channel.id, None) is not None:
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
    fields: Iterable[tuple[MsgStr, MsgStr, bool]] = (),
    footer: MsgStr = None,
    **kwargs
) -> discord.Embed:
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

class LanguageConverter(commands.Converter):
    async def convert(self, ctx: commands.Context, argument: str) -> str:
        """Convert a language argument or fail with BadArgument."""
        language = argument.strip().strip('`').casefold()
        if language not in SUPPORTED_LANGS:
            raise commands.BadArgument(str(Msg(
                ctx, 'i18n/unsupported-lang', language)))
        return language

class Internationalization(commands.Cog):
    """i18n/cog-desc"""

    @commands.is_owner()
    @commands.command(brief='i18n/r24n-desc')
    async def r25n(self, ctx: commands.Context):
        await Msg.load_state()
        await ctx.message.add_reaction(DONE)

    @commands.group(brief='i18n/lang-desc')
    @lone_group
    async def lang(self, ctx):
        pass

    @lang.command(name='get', brief='i18n/lang-get-desc')
    async def user_get(self, ctx: commands.Context):
        if Msg.user_langs.get(ctx.author.id, None) is None:
            await ctx.send(embed=Embed(
                ctx, description=Msg('i18n/lang-get-null'),
                color=discord.Color.red()
            ))
        else:
            await ctx.send(embed=Embed(
                ctx, description=Msg(
                    'i18n/lang-get',
                    Msg.user_langs[ctx.author.id]),
                color=discord.Color.blue()
            ))

    @lang.command(name='set', brief='i18n/lang-set-desc')
    async def user_set(
        self, ctx: commands.Context,
        *, language: LanguageConverter
    ):
        Msg.user_langs[ctx.author.id] = language
        await db.set_user_lang(ctx.author.id, language)
        await ctx.send(embed=Embed(
            ctx, description=Msg('i18n/lang-set', language),
            color=discord.Color.blue()
        ))

    @lang.command(name='reset', brief='i18n/lang-reset-desc')
    async def user_reset(self, ctx: commands.Context):
        Msg.user_langs.pop(ctx.author.id, None)
        await db.set_user_lang(ctx.author.id, None)
        await ctx.send(embed=Embed(
            ctx, description=Msg('i18n/lang-reset'),
            color=discord.Color.blue()
        ))

    @commands.has_permissions(manage_channels=True)
    @lang.group(brief='i18n/lang-channel-desc')
    @lone_group
    async def channel(self, ctx):
        pass

    @channel.command(name='get', brief='i18n/lang-channel-get-desc')
    async def channel_get(self, ctx: commands.Context):
        if Msg.channel_langs.get(ctx.channel.id, None) is None:
            await ctx.send(embed=Embed(
                ctx, description=Msg('i18n/lang-channel-get-null'),
                color=discord.Color.red()
            ))
        else:
            await ctx.send(embed=Embed(
                ctx, description=Msg(
                    'i18n/lang-channel-get',
                    Msg.channel_langs[ctx.channel.id]),
                color=discord.Color.blue()
            ))

    @channel.command(name='set', brief='i18n/lang-channel-set-desc')
    async def channel_set(
        self, ctx: commands.Context,
        *, language: LanguageConverter
    ):
        Msg.channel_langs[ctx.channel.id] = language
        await db.set_channel_lang(ctx.channel.id, language)
        await ctx.send(embed=Embed(
            ctx, description=Msg('i18n/lang-channel-set', language),
            color=discord.Color.blue()
        ))

    @channel.command(name='reset', brief='i18n/lang-channel-reset-desc')
    async def channel_reset(self, ctx: commands.Context):
        Msg.channel_langs.pop(ctx.channel.id, None)
        await db.set_channel_lang(ctx.channel.id, None)
        await ctx.send(embed=Embed(
            ctx, description=Msg('i18n/lang-channel-reset'),
            color=discord.Color.blue()
        ))

def setup(bot: commands.Bot):
    bot.add_cog(Internationalization())
