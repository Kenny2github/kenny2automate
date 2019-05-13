import re
from itertools import groupby
from discord.ext.commands import Cog, command
from datamuse import datamuse
import requests
from .i18n import i18n, embed
from .utils import q

class Words(Cog):
    """words/cog-description"""

    def __init__(self, bot, db):
        self.bot = bot
        self.db = db
        self.api = datamuse.Datamuse()

    @command(invoke_without_command=True, description='words/words-description')
    async def words(self, ctx, *, cmd):
        """words/words-help"""
        async def unknown(*_, **__):
            ctx.bot.help_command.context = ctx
            await ctx.bot.help_command.send_command_help(ctx.command)
        if ':' not in cmd:
            cmd, _, arg = cmd.rpartition(' ') #assume argument is one word
        else:
            cmd, _, arg = cmd.partition(':')
        cmd, arg = cmd.strip().replace(' ', '_'), arg.strip()
        await getattr(self, 'words_' + cmd, unknown)(ctx, word=arg)

    async def words_that_rhyme_with(self, ctx, *, word):
        async with ctx.channel.typing():
            perfect = await q(self.api.words, rel_rhy=word, md='s')
            near = await q(self.api.words, rel_nry=word, md='s')
        bad_words = self.censor(ctx)
        key = lambda i: i['numSyllables']
        perfect.sort(key=key)
        near.sort(key=key)
        joiner = i18n(ctx, 'comma-sep')
        fields = []
        for n, syll in groupby(perfect, key):
            fields.append((
                ('words/syllable-count', n),
                joiner.join(
                    i['word']
                    for i in syll
                    if not re.search(bad_words, i['word'], re.I)
                ),
                False
            ))
        await ctx.send(embed=embed(ctx,
            title=('words/perfect-rhymes',),
            description=None if fields else ('none-paren',),
            fields=fields,
            color=0x55acee
        ))
        fields = []
        for n, syll in groupby(near, key):
            fields.append((
                ('words/syllable-count', n),
                joiner.join(
                    i['word']
                    for i in syll
                    if not re.search(bad_words, i['word'], re.I)
                ),
                False
            ))
        await ctx.send(embed=embed(ctx,
            title=('words/near-rhymes',),
            description=None if fields else ('none-paren',),
            fields=fields,
            color=0xe67e22
        ))

    words_rhyme = words_rhy = words_nry = words_that_rhyme_with

    def censor(self, ctx):
        if ctx.guild is None:
            return '\1'
        else:
            res = self.db.execute(
                'SELECT words_censor FROM guilds WHERE guild_id=?',
                (ctx.guild.id,)
            ).fetchone()
            if res is None or res[0] is None:
                return '\1'
            return res[0] or '\1'

    def join_words_embed(self, ctx, title, lewords, word):
        bad_words = self.censor(ctx)
        return embed(ctx,
            title=(title, word),
            description=i18n(ctx, 'comma-sep').join(
                '{score}: {word}'.format(**i)
                for i in lewords
                if not re.search(bad_words, i['word'], re.I)
            ) or ('none-paren',),
            color=0x55acee
        )

    def _words(title, param, cmd=False, aliases=None, description=None):
        async def newfunc(self, ctx, *, word):
            async with ctx.channel.typing():
                lewords = await q(self.api.words, **{param: word})
            await ctx.send(embed=self.join_words_embed(
                ctx, 'words/' + title + '-title', lewords, word
            ))
        if cmd:
            return command(name=cmd, aliases=aliases or [title], description=(
                description or 'words/' + cmd + '-description'
            ))(newfunc)
        return newfunc

    words_means = words_ml = words_that_mean = _words('means', 'ml')
    words_sounds = words_sl = words_that_sound_like = _words('sounds', 'sl')
    words_spelled = words_sp = words_spelled_like = _words('spelled', 'sp')
    words_jja = words_modified_by = _words('jja', 'rel_jja')
    words_modifying = words_jjb = words_that_modify = _words('jjb', 'rel_jjb')
    synonyms = _words('syn', 'rel_syn', 'synonyms')
    words_triggered_by = words_trg = words_associated_with \
        = _words('trg', 'rel_trg')
    antonyms = _words('ant', 'rel_ant', 'antonyms')
    hypernyms = _words('spc', 'rel_spc', 'hypernyms')
    hyponyms = _words('gen', 'rel_gen', 'hyponyms')
    holonyms = _words('com', 'rel_com', 'holonyms')
    meronyms = _words('par', 'rel_par', 'meronyms')
    words_following = words_after = words_bga = words_that_follow \
        = _words('bga', 'rel_bga')
    words_preceding = words_before = words_bgb = words_that_precede \
        = _words('bgb', 'rel_bgb')
    homophones = _words('hom', 'rel_hom', 'homophones')
    words_matching_consonants_with = words_cns \
        = words_that_match_consonants_with = _words('cns', 'rel_cns')

    @command(aliases=['define'], description='words/word-description')
    async def word(self, ctx, *, leword):
        async with ctx.channel.typing():
            lewords = await q(
                requests.get,
                'https://api.datamuse.com/words',
                params={
                    'qe': 'sp',
                    'sp': leword,
                    'md': 'dpsrf',
                    'ipa': '1',
                    'max': 1,
                }
            )
            lewords = lewords.json()
        if 'defs' not in lewords[0]:
            return await ctx.send(embed=embed(ctx,
                title=('error',),
                description=('words/no-def', leword),
                color=0xff0000
            ))
        deeta = lewords[0]
        tags = deeta['tags']
        poss = set()
        for i in tags:
            if i.startswith('ipa_pron:'):
                pron = i[len('ipa_pron:'):]
            elif i.startswith('f:'):
                freq = i[len('f:'):]
            elif i != 'query' and ':' not in i:
                poss.add(i)
        numSyllables = deeta['numSyllables']
        defs = deeta['defs']
        defHeadword = deeta.get('defHeadword', leword)
        await ctx.send(embed=embed(ctx,
            title=('words/word-info', leword),
            description=('words/word-root', defHeadword),
            fields=(
                (('words/word-pronunciation',), pron, True),
                (('words/word-syllables',), str(numSyllables), True),
                (
                    ('words/word-parts-of-speech',),
                    i18n(ctx, 'comma-sep').join(poss),
                    True
                ),
                (('words/word-frequency',), str(freq), True),
                (('words/word-definitions',), '\n'.join(
                    '{}. {}'.format(i + 1, j.replace('\t', '\xa0\xa0\xa0\xa0'))
                    for i, j in enumerate(defs)
                ), False)
            ),
            color=0xffffff
        ))
