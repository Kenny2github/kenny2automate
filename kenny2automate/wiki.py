import re
import random
from urllib.parse import quote
import asyncio as a
import discord as d
from discord.ext.commands import command
import aiohttp

class DummyCtx(object):
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)

class Wiki(object):
	def __init__(self, bot, logger, loop, server):
		self.bot = bot
		self.logger = logger
		self.loop = loop
		self.serverid = server

	session = None

	WIKIS = {
		'de': 'https://scratch-dach.info',
		'en': 'https://en.scratch-wiki.info',
		'id': 'https://scratch-indo.info',
		'nl': 'https://nl.scratch-wiki.info',
		'hu': 'https://hu.scratch-wiki.info',
		'ru': 'https://scratch-ru.info',
		'fr': 'https://fr.scratch-wiki.info',
		'ja': 'https://ja.scratch-wiki.info',
		'test': 'https://test.scratch-wiki.info',
	}

	async def req(self, params, wiki='en'):
		if self.session is None:
			self.session = aiohttp.ClientSession()
		params['format'] = 'json'
		resp = await self.session.get(Wiki.WIKIS[wiki] + '/w/api.php', params=params)
		cont = await resp.json()
		resp.close()
		return cont

	@command()
	async def page(self, ctx, *, title):
		"""Get a link to the contents of a page."""
		title = title.replace(' ', '_')
		ns, name = title.split(':', 1)
		ns = ns[:1].upper() + ns[1:]
		name = name[:1].upper() + name[1:]
		title = ns + ':' + name
		title = quote(title, safe='/:')
		await ctx.send('https://en.scratch-wiki.info/w/index.php?title={}&action=edit'.format(title))
		self.logger.info('Wiki.page: ' + title, extra={'ctx': ctx})

	@command()
	async def recentchanges(self, ctx, limit=50):
		"""Get recent changes on the Wiki."""
		self.logger.info('Wiki.recentchanges: ' + str(limit), extra={'ctx': ctx})
		twenties, limit = divmod(limit, 20)
		async with ctx.channel.typing():
			result = ['']
			changes = []
			start = 'now'
			for i in [20 for j in range(twenties)] + [limit]:
				resp = await self.req({
					'action': 'query',
					'list': 'recentchanges',
					'rcprop': 'user|timestamp|comment|title|sizes|flags',
						'rctype': 'edit|new',
					'rclimit': i,
					'rcstart': start
				})
				changes.extend(resp['query']['recentchanges'])
				start = resp['query']['recentchanges'][-1]['timestamp']
			i = 0
			for ch in changes:
				change = '\n'
				change += ch['timestamp']
				change += ': '
				change += ch['title']
				change += '; '
				sizechange = ch['newlen'] - ch['oldlen']
				if sizechange <= -500 or sizechange >= 500:
					change += '**'
				change += '('
				if sizechange <= 0:
					change += str(sizechange)
				if sizechange > 0:
					change += '+' + str(sizechange)
				change += ')'
				if sizechange <= -500 or sizechange >= 500:
					change += '**'
				change += ' . . '
				change += ch['user']
				change += ' _('
				change += ch['comment'].replace('*', '\\*').replace('_', '\\_').replace('`', '\\`')
				change += ')_'
				result[i] += change
				if len(result[i]) > 2000:
					result.append('')
					result[i], result[i+1] = result[i].rsplit('\n', 1)
					i += 1
			for r in result:
				await ctx.send(r)

	@command()
	async def randompage(self, ctx):
		"""Get a link to a random Wiki page!"""
		self.logger.info('Wiki.randompage', extra={'ctx': ctx})
		rn = await self.req({
			'action': 'query',
			'list': 'random',
			'rnlimit': '1',
			'rnnamespace': '0'
		})
		title = rn['query']['random'][0]['title']
		title = title.replace(' ', '_')
		title = quote(title, safe='/:')
		await ctx.send('https://en.scratch-wiki.info/wiki/' + title)

	@command()
	async def iwstats(self, ctx):
		"""Get statistics for the international wikis!"""
		self.logger.info('Wiki.wikistats', extra={'ctx': ctx})
		async with ctx.channel.typing():
			try:
				content = await self.req({
					'action': 'query',
					'prop': 'revisions',
					'titles': 'User:InterwikiBot/International Stats',
					'rvlimit': '1',
					'rvprop': 'content',
				})
			except Exception as exc:
				self.logger.error('Fetching wiki stats failed: ' + str(exc), extra={'ctx': DummyCtx(author=DummyCtx(name='Wiki.wikistats'))})
				await ctx.send('Fetching stats failed. Oops!')
				return
			content = list(content['query']['pages'].values())[0]['revisions'][0]['*']
		exp = re.compile(r"""\|-
\|(?P<Time>[^\|]+)
\|(?P<Pages>[0-9]+)
\|(?P<Articles>[0-9]+)
\|(?P<Edits>[0-9]+)
\|(?P<Images>[0-9]+)
\|(?P<Users>[0-9]+)
\|(?P<ActiveUsers>[0-9]+)
\|(?P<Admins>[0-9]+)
""")
		for match in re.finditer(r'(?P<cont>==\s*(?P<code>[a-z][a-z])\s*==[\s\S]+?\|\})', content, re.I|re.S):
			embed = d.Embed(
				title='{}wiki Stats'.format(match.group('code')),
				description='Here are stats for the {}wiki.'.format(match.group('code')),
				color=random.randint(0, 0xffffff)
			)
			for fieldtitle, value in list(
					re.finditer(exp, match.group('cont'))
					)[-1].groupdict().items():
				embed.add_field(
					name=re.sub('([a-z])([A-Z])', r'\1 \2', fieldtitle),
					value=value,
					inline=True
				)
			await ctx.send(embed=embed)
			await a.sleep(1)

	@command()
	async def wikistats(self, ctx, wiki):
		"""Get stats for the ``wiki``wiki."""
		async with ctx.channel.typing():
			try:
				data = await self.req({
					'action': 'query',
					'meta': 'siteinfo',
					'siprop': 'statistics'
				}, wiki)
			except Exception as exc:
				self.logger.error('Fetching wiki stats failed: ' + str(exc), extra={'ctx': DummyCtx(author=DummyCtx(name='Wiki.wikistats'))})
				await ctx.send('Fetching stats failed. You likely specified a nonexistent wiki.')
				return
			data = data['query']['statistics']
			embed = d.Embed(
				title='{}wiki Stats'.format(wiki),
				description='Here are some statistics for the {}wiki.'.format(wiki),
			)
			for fieldtitle, value in data.items():
				embed.add_field(
					name='Active Users' if fieldtitle == 'activeusers' else fieldtitle.title(),
					value=str(value),
				)
			await ctx.send(embed=embed)

	def __del__(self):
		if self.session is None:
			return
		self.loop.create_task(self.session.close())
