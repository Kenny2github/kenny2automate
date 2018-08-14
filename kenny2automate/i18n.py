import json
import sqlite3 as sql

dbw = sql.connect('k2a_i18n.db')
dbw.row_factory = sql.Row
db = dbw.cursor()
with open(os.path.join(os.path.dirname(__file__), 'i18n.sql')) as f:
    db.executescript(f.read())
i18ndir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'i18n')

def i18n(ctx, key, *params):
    res = db.execute(
        'SELECT lang FROM user_langs WHERE user_id=?',
        (ctx.author.id,)
    ).fetchone()
    if res is None:
        res = {'lang': 'en'}
    res = res['lang']
    with open(os.path.join(i18ndir, res + '.json')) as f:
        i18njson = json.load(f)
    if key not in i18njson:
        with open(os.path.join(i18ndir, 'en.json')) as f:
            i18njson = json.load(f)
        if key not in i18njson:
            return None
        return i18njson[key].format(*params)
    return i18njson[key].format(*params)

class I18n(object):
    """Internationalization control."""
    def __init__(self, bot, logger):
        self.bot = bot
        self.logger = logger

    @command()
    async def lang(self, ctx, *, lang: str):
        """Set your language."""
        logger.info('I18n.lang: ' + str(lang), extra={'ctx': ctx})
        if not os.path.isfile(os.path.join(i18ndir, lang + '.json')):
            await ctx.send(
                'Unrecognized language: {}. Valid languages are:\n{}'.format(
                    lang, ', '.join(i[:2] for i in os.listdir(i18ndir))
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
    @command(name='i18n')
    async def text(self, ctx, *, key: str, *params):
        await ctx.send(i18n(ctx, key, *params))
