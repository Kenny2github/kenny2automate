import os
import time
import json
import functools
import sqlite3 as sql
import requests
import discord as d
from discord.ext import commands as c
from discord.ext.commands import command, has_permissions

db = None
i18ndir = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'i18n'
)
with open(os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'countrylangs.json'
))) as f:
    LANGS = json.load(f)

def i18n(ctx, key, *params):
    res = db.execute(
        'SELECT lang FROM user_langs WHERE user_id=?',
        (ctx.author.id,)
    ).fetchone()
    if res is None:
        res = db.execute(
            'SELECT lang FROM channel_langs WHERE channel_id=?',
            (ctx.channel.id,)
        ).fetchone()
        if res is None:
            res = {'lang': 'en'}
    res = res['lang']
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

class I18n(object):
    """Internationalization control."""
    def __init__(self, bot, logger, cur):
        global db
        self.bot = bot
        self.logger = logger
        db = cur

        INDICATOR_RANGE = range(0x1f1e6, 0x1f1ff)
        LETTERS = ''.join(chr(ord('A') + i) for i in range(26))
        globs = [time.time()]
        @self.bot.event
        @c.cooldown(1, 20.0)
        async def on_raw_reaction_add(event):
            emoji = event.emoji.name
            if not all((
                len(emoji) == 2,
                ord(emoji[0]) in INDICATOR_RANGE,
                ord(emoji[1]) in INDICATOR_RANGE
            )):
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
                    ttext = req.json()['result']
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
            print('sending text')
            await channel.send(text)

    @command()
    async def lang(self, ctx, *, lang: str = None):
        """Set your language."""
        self.logger.info('I18n.lang: ' + str(lang), extra={'ctx': ctx})
        if lang is None:
            db.execute(
                'DELETE FROM user_langs WHERE user_id=?',
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
            'SELECT lang FROM user_langs WHERE user_id=?',
            (ctx.author.id,)
        ).fetchone()
        if res is None:
            db.execute(
                'INSERT INTO user_langs VALUES (?, ?)',
                (ctx.author.id, lang)
            )
        else:
            db.execute(
                'UPDATE user_langs SET lang=? WHERE user_id=?',
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
        self.logger.info(
            'I18n.channel_lang: ' + str(lang),
            extra={'ctx': ctx}
        )
        if channel is None:
            channel = ctx.channel
        if lang is None:
            db.execute(
                'DELETE FROM channel_langs WHERE channel_id=?',
                (channel.id,)
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
            'SELECT lang FROM channel_langs WHERE channel_id=?',
            (channel.id,)
        ).fetchone()
        if res is None:
            db.execute(
                'INSERT INTO channel_langs VALUES (?, ?)',
                (channel.id, lang)
            )
        else:
            db.execute(
                'UPDATE channel_langs SET lang=? WHERE channel_id=?',
                (lang, channel.id)
            )
        await ctx.send('Successfully set language for {} to {}'.format(
            channel.mention, lang
        ))

    @command(name='i18n')
    async def text(self, ctx, key: str, *params):
        self.logger.info('I18n.text: ' + str(key), extra={'ctx': ctx})
        await ctx.send(i18n(ctx, key, *params))

    @command(aliases=['t', 'trans'])
    @c.cooldown(1, 20.0)
    async def translate(self, ctx, lang = None, *, text = None):
        if not lang:
            res = db.execute(
                'SELECT lang FROM user_langs WHERE user_id=?',
                (ctx.author.id,)
            ).fetchone()
            if res is None:
                res = db.execute(
                    'SELECT lang FROM channel_langs WHERE channel_id=?',
                    (ctx.channel.id,)
                ).fetchone()
                if res is None:
                    res = {'lang': 'en'}
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
        await ctx.send(req.json()['result'])
