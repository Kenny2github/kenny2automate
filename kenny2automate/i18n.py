import os
import re
import json
import functools
import typing
import asyncio
import discord
from discord.ext.commands import (
    command, group, has_permissions, Cog,
    Converter, BadArgument
)
from googletrans import Translator, LANGUAGES
from .utils import DummyCtx, lone_group, background

db = None
i18ndir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'i18n')
with open(os.path.join(
    os.path.dirname(i18ndir), 'kenny2automate', 'countrylangs.json'
)) as f:
    LANGS = json.load(f)

LANG = tuple(
    i[:-5]
    for i in os.listdir(i18ndir)
    if os.path.isfile(os.path.join(i18ndir, i))
)

def lang(ctx):
    """Get a language for a context."""
    if hasattr(ctx, 'id'):
        leid = ctx.id
    else:
        leid = ctx.author.id
    res = db.execute(
        'SELECT lang FROM users WHERE user_id=?',
        (leid,)
    ).fetchone()
    if res is None or res['lang'] is None:
        if not hasattr(ctx, 'id') and not isinstance(ctx, DummyCtx):
            leid = ctx.channel.id
        res = db.execute(
            'SELECT lang FROM channels WHERE channel_id=?',
            (leid,)
        ).fetchone()
        if res is None or res['lang'] is None:
            res = {'lang': 'en'}
    res = res['lang']
    return res

def i18n(ctx_or_lang, key, *params):
    """Return an i18n string by key, passing *params as format parameters."""
    if key is None:
        return None
    if not isinstance(ctx_or_lang, str):
        res = lang(ctx_or_lang)
    else:
        res = ctx_or_lang
    dirq, key = os.path.split(key)
    if res == 'qqx':
        return (
            '({})'.format(os.path.join(dirq, key))
            if not params
            else '({}: {})'.format(
                os.path.join(dirq, key),
                ', '.join(map(str, params))
            )
        )
    try:
        with open(
            os.path.join(i18ndir, dirq, res + '.json'),
            encoding='utf8'
        ) as f:
            i18njson = json.load(f)
    except FileNotFoundError:
        i18njson = {}
    if key not in i18njson:
        try:
            with open(os.path.join(i18ndir, dirq, 'en.json')) as f:
                i18njson = json.load(f)
        except FileNotFoundError:
            i18njson = {}
        if key not in i18njson:
            return (
                '|{}|'.format(os.path.join(dirq, key))
                if not params
                else '|{}: {}|'.format(
                    os.path.join(dirq, key),
                    ', '.join(map(str, params))
                )
            )
        return i18njson[key].format(*params)
    return i18njson[key].format(*params)

def embed(ctx, title=None, description=None, fields=None, footer=None, **kwargs):
    """Return an Embed with internationalized data.

    ``title`` and ``description``, if specified, must be strings or iterables.
    If strings, they will be directly passsed through. If iterables, the first
    element must be the i18n key, and all remaining elements will be passed as
    parameters. (This string-or-iterable union is known as an "i18n object".)
    ``fields``, if specified, must be an iterable of (name, value, ?inline)
    3-tuples, where name and value are i18n objects and inline is a boolean.
    Any fields will be added in the same order as they come in the iterable.
    """
    e = discord.Embed(
        title=(
            title
            if isinstance(title, (str, type(None)))
            else i18n(ctx, *title)
        ),
        description=(
            description
            if isinstance(description, (str, type(None)))
            else i18n(ctx, *description)
        ),
        **kwargs
    )
    if footer is not None:
        e.set_footer(text=(
            footer
            if isinstance(footer, (str, type(None)))
            else i18n(ctx, *footer)
        ))
    if not fields:
        return e
    for name, value, inline in fields:
        e.add_field(
            name=(
                name
                if isinstance(name, str)
                else i18n(ctx, *name)
            ),
            value=(
                value
                if isinstance(value, str)
                else i18n(ctx, *value)
            ),
            inline=inline
        )
    return e

class Lang(Converter):
    async def convert(self, ctx, argument):
        if argument not in LANGUAGES and argument != '*':
            raise BadArgument(i18n(ctx, 'i18n/invalid-lang', repr(argument)))
        return argument

class I18n(Cog):
    """i18n/cog-desc"""
    def __init__(self, bot, cur, deleters):
        global db
        self.bot = bot
        self.deleters = deleters
        self.trans = Translator()
        db = cur

        INDICATOR_RANGE = range(0x1f1e6, 0x1f1ff)
        LETTERS = ''.join(chr(ord('A') + i) for i in range(26))
        @self.bot.event
        async def on_raw_reaction_add(event):
            emoji = event.emoji.name
            if not (
                len(emoji) == 2
                and ord(emoji[0]) in INDICATOR_RANGE
                and ord(emoji[1]) in INDICATOR_RANGE
            ):
                return
            code = LETTERS[INDICATOR_RANGE.index(ord(emoji[0]))] \
                + LETTERS[INDICATOR_RANGE.index(ord(emoji[1]))]
            erroridx = 0
            while 1:
                lang = LANGS[code][erroridx]
                if lang in LANGUAGES:
                    break
                if '-' in lang:
                    lang = lang.split('-', 1)[0]
                if lang in LANGUAGES:
                    break
                erroridx += 1
            guild = self.bot.get_guild(event.guild_id)
            channel = self.bot.get_channel(event.channel_id)
            user = self.bot.get_user(event.user_id)
            if channel is None:
                await user.create_dm()
                channel = user.dm_channel
            message = await channel.fetch_message(event.message_id)
            ctx = DummyCtx(
                guild=guild,
                channel=channel,
                message=message,
                author=user
            )
            text = message.clean_content
            await self._translate(ctx, 'auto', lang, text, message.jump_url)

    @command(description='i18n/ogham-desc')
    async def ogham(self, ctx, *, text: str):
        OGHAM = {
            32: 5760,
            97: 5776,
            98: 5761,
            99: 5769,
            100: 5767,
            101: 5779,
            102: 5763,
            103: 5772,
            104: 5766,
            105: 5780,
            107: 5781,
            108: 5762,
            109: 5771,
            110: 5765,
            111: 5777,
            112: 5786,
            113: 5770,
            114: 5775,
            115: 5764,
            116: 5768,
            117: 5778,
            118: 5763,
            120: 5781,
            122: 5774,
        }
        await ctx.send(
            '\u169b'
            + re.sub('[^a-ik-vxz ]', '', text.lower())
            .translate(OGHAM)
            + '\u169c'
        )

    @command(description='i18n/lang-desc')
    async def lang(self, ctx, *, lang: str = None):
        if lang is None:
            with db.connection:
                db.execute(
                    'UPDATE users SET lang=NULL WHERE user_id=?',
                    (ctx.author.id,)
                )
            await ctx.send(embed=embed(ctx,
                title=('success',),
                description=('i18n/lang-success-reset', ctx.author.mention),
                color=0x55acee
            ))
            return
        if (
            lang not in LANG
            and not lang == 'qqx'
        ):
            await ctx.send(embed=embed(ctx,
                title=('error',),
                description=('i18n/unknown-lang', lang, ', '.join(LANG)),
                color=0xff0000
            ))
            return
        res = db.execute(
            'SELECT lang FROM users WHERE user_id=?',
            (ctx.author.id,)
        ).fetchone()
        with db.connection:
            if res is None:
                db.execute(
                    'INSERT INTO users (user_id, lang) VALUES (?, ?)',
                    (ctx.author.id, lang)
                )
            else:
                db.execute(
                    'UPDATE users SET lang=? WHERE user_id=?',
                    (lang, ctx.author.id)
                )
        await ctx.send(embed=embed(ctx,
            title=('success',),
            description=('i18n/lang-success', ctx.author.mention, lang),
            color=0x55acee
        ))

    @command(description='i18n/channel_lang-desc')
    @has_permissions(administrator=True)
    async def channel_lang(
        self,
        ctx,
        lang: str = None,
        channel: discord.TextChannel = None
    ):
        if channel is None:
            channel = ctx.channel
        if lang is None:
            with db.connection:
                db.execute(
                    'UPDATE channels SET lang=? WHERE channel_id=?',
                    (None, channel.id,)
                )
            await ctx.send(embed=embed(ctx,
                title=('success',),
                description=('i18n/lang-success-reset', channel.mention),
                color=0x55acee
            ))
            return
        if (
            lang not in LANG
            and not lang == 'qqx'
        ):
            await ctx.send(embed=embed(ctx,
                title=('error',),
                description=('i18n/unknown-lang', lang, ', '.join(LANG)),
                color=0xff0000
            ))
            return
        res = db.execute(
            'SELECT lang FROM channels WHERE channel_id=?',
            (channel.id,)
        ).fetchone()
        with db.connection:
            if res is None:
                db.execute(
                    'INSERT INTO channels (channel_id, lang) VALUES (?, ?)',
                    (channel.id, lang)
                )
            else:
                db.execute(
                    'UPDATE channels SET lang=? WHERE channel_id=?',
                    (lang, channel.id)
                )
        await ctx.send(embed=embed(ctx,
            title=('success',),
            description=('lang-success', channel.mention, lang),
            color=0x55acee
        ))

    @command(name='i18n', description='i18n/i18n-desc')
    async def text(self, ctx, key: str, *params):
        await ctx.send(i18n(ctx, key, *params))

    @command(aliases=['t', 'trans'], description='i18n/translate-desc')
    async def translate(self, ctx, fromlanguage: typing.Optional[Lang] = 'auto',
                        language: typing.Optional[Lang] = None,
                        count: typing.Optional[int] = 1, *, text=None):
        if not language and fromlanguage == 'auto':
            _lang = lang(ctx)
        elif not language:
            _lang = fromlanguage
            fromlanguage = 'auto'
        else:
            _lang = language
        url = ctx.message.jump_url
        if not text:
            msg = (await ctx.channel.history(limit=count+1).flatten())[:0:-1]
            url = msg[0].jump_url
            text = '\n\n'.join(m.clean_content for m in msg)
        await self._translate(ctx, fromlanguage, _lang, text, url)

    async def _translate(self, ctx, sl, tl, q, url, error_if_same=True):
        q = q.strip()
        # get bad words for guild
        if ctx.guild is None:
            bad_words = '\1'
        else:
            res = db.execute(
                'SELECT words_censor FROM guilds WHERE guild_id=?',
                (ctx.guild.id,)
            ).fetchone()
            if res is None or res[0] is None:
                bad_words = '\1'
            else:
                bad_words = res[0] or '\1' #res[0] could still be empty
        # get translated text
        trans = await self.bot.loop.run_in_executor(None, functools.partial(
            self.trans.translate, q, src=sl, dest=tl
        ))
        if trans.src == trans.dest:
            if error_if_same:
                background(ctx.send(embed=embed(ctx,
                    title=('error',),
                    description=('i18n/translation-same',),
                    color=0xff0000
                )))
            return
        if trans.text.casefold() == trans.origin.casefold():
            if error_if_same:
                background(ctx.send(embed=embed(ctx,
                    title=('error',),
                    description=('i18n/translation-failed',),
                    color=0xff0000
                )))
            return
        if re.search(bad_words, trans.text, re.I):
            background(ctx.send(embed=embed(ctx,
                title=('error',),
                description=('i18n/translation-censored',),
                color=0xff0000
            )))
            return
        msg = await ctx.channel.send(embed=embed(ctx, #channel cuz DummyCtx
            description=i18n(ctx, 'i18n/message-translation',
                             trans.src, trans.dest, url)
                + '\n' + trans.text,
            color=0x36393f,
            footer=('i18n/translation-requested-by', str(ctx.author)),
            url=url,
        ))
        self.deleters[ctx.message.id] = msg.id

    autolangs = {}

    @group(
        aliases=['at', 'autotrans'],
        description='i18n/autotranslate-desc',
        invoke_without_command=True,
    )
    @lone_group(True)
    async def autotranslate(self, ctx):
        pass

    @autotranslate.command(description='i18n/at-on-desc')
    async def on(self, ctx, *_lang: Lang):
        _lang = list(_lang)
        if not _lang:
            _lang.append(lang(ctx))
        alangs = self.autolangs.setdefault(ctx.channel.id, set())
        _lang = [la for la in _lang if la not in alangs]
        if not _lang:
            background(ctx.send(embed=embed(ctx,
                title=('error',),
                description=('i18n/already-autoing'),
                color=0xff0000
            )))
            return
        for la in _lang:
            background(self._at(la, ctx))

    async def _at(self, lang, ctx):
        self.autolangs[ctx.channel.id].add(lang)
        background(ctx.send(embed=embed(ctx,
            title=('i18n/at-on-title',),
            description=('i18n/at-on', lang),
            color=0x55acee
        )))
        while lang in self.autolangs[ctx.channel.id]:
            try:
                msg = await self.bot.wait_for('message', check=lambda m: (
                    m.channel.id == ctx.channel.id
                    and not m.author.bot # skip bots
                    and not m.content.startswith(
                        self.bot.command_prefix(None, m)
                    ) # skip commands
                ), timeout=2.0) # check for stoppage every 2 secs
            except asyncio.TimeoutError:
                pass
            else:
                background(self._translate(
                    ctx, 'auto', lang, msg.clean_content,
                    msg.jump_url, False
                ))
        background(ctx.send(embed=embed(ctx,
            title=('i18n/autolang-ended-title',),
            description=('i18n/autolang-ended', lang),
            color=0x55acee
        )))

    @autotranslate.command(description='i18n/at-off-desc')
    async def off(self, ctx, *_lang: Lang):
        alangs = len(self.autolangs.get(ctx.channel.id, set()))
        if len(_lang) == 1 and _lang[0] == '*':
            _lang = list(self.autolangs[ctx.channel.id])
        elif not _lang and alangs == 1:
            _lang = list(self.autolangs[ctx.channel.id])
        elif not _lang:
            _lang = [lang(ctx)]
        for la in _lang:
            try:
                self.autolangs.get(ctx.channel.id, set()).remove(la)
            except KeyError:
                background(ctx.send(embed=embed(ctx,
                    title=('error',),
                    description=('i18n/at-off-not-on', _lang),
                    color=0xff0000
                )))
