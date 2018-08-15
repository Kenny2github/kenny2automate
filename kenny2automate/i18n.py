import os
import json
import sqlite3 as sql
import discord as d
from discord.ext.commands import command, has_permissions

db = None
i18ndir = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'i18n'
)

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
