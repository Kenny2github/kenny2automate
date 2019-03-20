import os
import re
import time
import json
import functools
import requests
import discord as d
from discord.ext import commands as c
from discord.ext.commands import command, has_permissions, Cog

db = None
i18ndir = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'i18n'
)
with open(os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'countrylangs.json'
))) as f:
    LANGS = json.load(f)

LANG = tuple(
    i[:-5]
    for i in os.listdir(i18ndir)
    if os.path.isfile(os.path.join(i18ndir, i))
)

def lang(ctx):
    """Get a language for a context."""
    res = db.execute(
        'SELECT lang FROM users WHERE user_id=?',
        (ctx.author.id,)
    ).fetchone()
    if res is None or res['lang'] is None:
        res = db.execute(
            'SELECT lang FROM channels WHERE channel_id=?',
            (ctx.channel.id,)
        ).fetchone()
        if res is None or res['lang'] is None:
            res = {'lang': 'en'}
    res = res['lang']
    return res

def i18n(ctx_or_lang, key, *params):
    """Return an i18n string by key, passing *params as format parameters."""
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
    e = d.Embed(
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

class I18n(Cog):
    """Internationalization control."""
    def __init__(self, bot, cur, deleters):
        global db
        self.bot = bot
        self.deleters = deleters
        db = cur

        INDICATOR_RANGE = range(0x1f1e6, 0x1f1ff)
        LETTERS = ''.join(chr(ord('A') + i) for i in range(26))
        globs = [time.time()]
        @self.bot.event
        @c.cooldown(1, 20.0)
        async def on_raw_reaction_add(event):
            emoji = event.emoji.name
            if not (
                len(emoji) == 2
                and ord(emoji[0]) in INDICATOR_RANGE
                and ord(emoji[1]) in INDICATOR_RANGE
            ):
                return
            if time.time() - globs[0] < 20.0:
                return
            globs[0] = time.time()
            code = LETTERS[INDICATOR_RANGE.index(ord(emoji[0]))] \
                + LETTERS[INDICATOR_RANGE.index(ord(emoji[1]))]
            lang = LANGS[code][0]
            channel = self.bot.get_channel(event.channel_id)
            text = (await channel.get_message(event.message_id)).content
            erroridx = 0
            while erroridx >= 0:
                try:
                    req = await self.bot.loop.run_in_executor(None, functools
                        .partial(requests.get,
                        'https://translate-service.scratch.mit.edu/translate',
                        params={'language': lang, 'text': text})
                    )
                    print(req.text)
                    text = req.json()['result']
                    erroridx = -1
                except KeyError:
                    print(lang)
                    if '-' in lang:
                        #cache failed locale
                        LANGS[code][erroridx] = LANGS[code][erroridx] \
                            .split('-')[0]
                        lang = LANGS[code][erroridx]
                    else:
                        erroridx += 1
                        try:
                            lang = LANGS[code][erroridx]
                        except IndexError:
                            return
            print('sending text:', text)
            if not text:
                await channel.send(embed=d.Embed(
                    title='Error',
                    description='Translate API returned a blank string',
                    color=0xff0000
                ))
            await channel.send(text)

    @command()
    async def ogham(self, ctx, *, text: str):
        """A fun little interpreter from English to Ogham."""
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

    @command()
    async def lang(self, ctx, *, lang: str = None):
        """Set your language."""
        if lang is None:
            with db.connection:
                db.execute(
                    'UPDATE users SET lang=NULL WHERE user_id=?',
                    (ctx.author.id,)
                )
            await ctx.send('Successfully reset language for {}'.format(
                ctx.author.mention
            ))
            return
        if (
            not os.path.isfile(os.path.join(i18ndir, lang + '.json'))
            and not lang == 'qqx'
        ):
            await ctx.send(
                'Unrecognized language: {}. Valid languages are:\n{}'.format(
                    lang, ', '.join(
                        i[:-5]
                        for i in os.listdir(i18ndir)
                        if i.endswith('.json')
                    )
                )
#this is special, the language command itself is not translated
            )
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
        await ctx.send('Successfully set language for {} to {}'.format(
            ctx.author.mention, lang
        ))

    @command()
    @has_permissions(administrator=True)
    async def channel_lang(
        self,
        ctx,
        lang: str = None,
        channel: d.TextChannel = None
    ):
        if channel is None:
            channel = ctx.channel
        if lang is None:
            with db.connection:
                db.execute(
                    'UPDATE channels SET lang=? WHERE channel_id=?',
                    (None, channel.id,)
                )
            await ctx.send('Successfully reset language for {}'.format(
                channel.mention
            ))
            return
        if (
            not os.path.isfile(os.path.join(i18ndir, lang + '.json'))
            and not lang == 'qqx'
        ):
            await ctx.send(
                'Unrecognized language: {}. Valid languages are:\n{}'.format(
                    lang, ', '.join(
                        i[:2]
                        for i in os.listdir(i18ndir)
                        if i.endswith('.json')
                    )
                )
#this is special, the language command itself is not translated
            )
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
        await ctx.send('Successfully set language for {} to {}'.format(
            channel.mention, lang
        ))

    @command(name='i18n')
    async def text(self, ctx, key: str, *params):
        await ctx.send(i18n(ctx, key, *params))

    @command(aliases=['t', 'trans'])
    @c.cooldown(1, 20.0)
    async def translate(self, ctx, lang = None, *, text = None):
        if not lang:
            res = db.execute(
                'SELECT lang FROM users WHERE user_id=?',
                (ctx.author.id,)
            ).fetchone()
            if res is None or res['lang'] is None:
                res = db.execute(
                    'SELECT lang FROM channels WHERE channel_id=?',
                    (ctx.channel.id,)
                ).fetchone()
                if res is None or res['lang'] is None:
                    res = {'lang': 'en'}
            lang = res['lang']
        if not text:
            arg = (await ctx.channel.history(limit=2).flatten())[1].content
        else:
            arg = text
        req = await self.bot.loop.run_in_executor(None, functools.partial(
            requests.get, 'https://translate-service.scratch.mit.edu/translate',
            params={'language': lang, 'text': arg},
            headers={
                'Origin': 'https://llk.github.io',
                'Referer': 'https://llk.github.io/scratch-gui/develop/',
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
            }
        ))
        msg = await ctx.send(list(req.json().values())[0] or '\1')
        deleters[ctx.message.id] = msg.id
