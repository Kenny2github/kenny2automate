import re
import random
import functools
from urllib.parse import quote
import asyncio as a
import discord as d
from discord.ext.commands import command
from discord.ext import commands as c
import requests

class DummyCtx(object):
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)

DGSWIKISERVER = 328938947717890058

class Wiki(object):
	def __init__(self, bot, logger, loop, server):
		self.bot = bot
		self.logger = logger
		self.loop = loop
		self.serverid = server

	def __local_check(self, ctx):
		if ctx.guild is None:
			return False
		return ctx.guild.id == DGSWIKISERVER

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
		params['format'] = 'json'
		resp = await self.bot.loop.run_in_executor(
			None,
			functools.partial(
				requests.get,
				Wiki.WIKIS[wiki] + '/w/api.php',
				params=params
			)
		)
		return resp.json()

	@command()
	async def page(self, ctx, *, title):
		"""Get the contents of a page."""
		self.logger.info('Wiki.page: ' + title, extra={'ctx': ctx})
		async with ctx.channel.typing():
			try:
				content = await self.req({
					'action': 'query',
					'prop': 'revisions',
					'titles': title,
					'rvlimit': 1,
					'rvprop': 'content',
				})
			except Exception as exc:
				self.logger.error('Fetching page content failed: ' + str(exc),
					extra={'ctx': DummyCtx(author=DummyCtx(name='Wiki.page'))})
				await ctx.send('Fetching page content failed. Sorry!')
				return
		content = list(content['query']['pages'].values())[0]['revisions'][0]['*']
		content = content.splitlines()
		contents = ['```html\n']
		i = 0
		for line in content:
			if len(contents[i]) + 11 > 2000:
				contents.append('```html\n')
				temp = contents[i][:1997].rsplit('\n', 1)
				contents[i], contents[i+1] = temp[0], temp[1] + contents[i][1997:]
				contents[i] += '```'
				i += 1
				contents[i] = '```html\n' + contents[i]
			contents[i] += line + '\n'
		contents[-1] += '```'
		for msg in contents:
			await ctx.send(msg)

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

	@command()
	@c.cooldown(8, 64800.0, type=c.BucketType.guild)
	async def analyzega(self, ctx, wiki):
		"""Do some analysis of a wiki's GA stats"""
		self.logger.info('Wiki.analyzega: ' + wiki, extra={'ctx': ctx})
		async with ctx.channel.typing():
			try:
				data = await self.req({
					'action': 'query',
					'prop': 'revisions',
					'titles': 'User:InterwikiBot/GA Stats',
					'rvlimit': '1',
					'rvprop': 'ids|content'
				}, wiki)
			except Exception as exc:
				self.logger.error('Fetching wiki stats failed: ' + str(exc), extra={'ctx': DummyCtx(author=DummyCtx(name='Wiki.analyzega'))})
				await ctx.send('Fetching stats failed. You likely specified a nonexistent wiki.')
				return
		data = list(data['query']['pages'].values())[0]['revisions'][0]
		content = data['*']
		revid = data['revid']

		MASTER_VIEWS = [
			(m.group(1).replace('_', ' '), int(m.group(2)))
			for m in re.finditer(r'\n#\s*\[\[([^\]]+)\]\]\s*\((\d+) views\)', content)
		]
		print(MASTER_VIEWS)
		MASTER_VIEWS.sort(key=lambda i: i[1], reverse=True) #sanity check
		views_unnamed = [j for i, j in MASTER_VIEWS]
		count = len(views_unnamed)
		print('# ===Total stats===')
		# ;Average pageviews per page
		average_pageviews = sum(views_unnamed) / count
		# ;Median pageviews per page
		median_pageviews = (views_unnamed[count // 2]
			if count % 2
			else ((views_unnamed[count // 2]
				+ views_unnamed[count // 2 - 1])
				/ 2))

		diffs = [i - views_unnamed[n+1] for n, i in enumerate(views_unnamed[:-1])]
		diffcount = len(diffs)
		# ;Average difference between pageviews
		average_diff = sum(diffs) / diffcount
		# ;Median difference between pageviews
		median_diff = (diffs[diffcount // 2]
			if diffcount % 2
			else ((diffs[diffcount // 2]
				+ diffs[diffcount // 2 - 1])
				/ 2))
		mults = [i / views_unnamed[n+1] for n, i in enumerate(views_unnamed[:-1])]
		multcount = len(mults)
		# ;Average multiple of one page's views to the next highest page's views
		average_mult = sum(mults) / multcount
		# ;Median multiple of one page's views to the next highest page's views
		median_mult = (mults[multcount // 2]
			if multcount % 2
			else ((mults[multcount // 2]
				+ mults[multcount // 2 - 1])
				/ 2))
		# ;Total pageviews
		total = sum(views_unnamed)

		print('# ===Stats for highest datapoint: ...')
		# ;Views
		highest_title, highest_views = MASTER_VIEWS[0]
		avg_wo_high = sum(views_unnamed[1:]) / len(views_unnamed[1:])
		# ;Pulls up average viewcount by
		diff_avg_from_high = average_pageviews - avg_wo_high
		next_high_title = MASTER_VIEWS[1][0]
		# ;Difference to next highest, {next_high_title}
		diff_next_high = diffs[0]
		avg_diff_wo_high = sum(diffs[1:]) / len(diffs[1:])
		# ;Pulls up average difference by
		diff_avg_diff_from_high = average_diff - avg_diff_wo_high
		# ;Multiple if next highest, {next_high_title}
		mult_next_high = mults[0]

		print('# ===Stats for lowest datapoint: ...')
		# ;Views
		lowest_title, lowest_views = MASTER_VIEWS[-1]
		avg_wo_low = sum(views_unnamed[:-1]) / len(views_unnamed[:-1])
		# ;Pulls down average viewcount by
		diff_avg_from_low = avg_wo_low - average_pageviews # pulls DOWN
		next_low_title = MASTER_VIEWS[-2][0]
		# ;Difference to next lowest, {next_low_title}
		diff_next_low = diffs[-1]
		avg_diff_wo_low = sum(diffs[:-1]) / len(diffs[:-1])
		# ;Pulls down average difference by
		diff_avg_diff_from_low = avg_diff_wo_low - average_diff # pulls DOWN
		# ;Fraction of next lowest, {next_low_title}
		mult_next_low = mults[-1]

		print('# ===Stats for median datapoints: ...')
		if count % 2:
			# ;Views
			median_title, median_views = MASTER[count // 2]
			views_wo_median = views_unnamed[:]
			views_wo_median.pop(count // 2)
			avg_wo_median = sum(views_wo_median) / (count - 1)
			# ;Changes average viewcount by
			diff_avg_from_median = average_pageviews - avg_wo_median
			diffs_wo_median = diffs[:]
			diffs_wo_median.pop(diffcount // 2 - 1)
			diffs_wo_median.pop(diffcount // 2 - 1)
			avg_diff_wo_median = sum(diffs_wo_median) / (diffcount - 2)
			# ;Changes average difference by
			diff_avg_diff_from_median = average_diff - avg_diff_wo_median
			mults_wo_median = mults[:]
			mults_wo_median.pop(multcount // 2 - 1)
			mults_wo_median.pop(multcount // 2 - 1)
			avg_mult_wo_median = sum(mults_wo_median) / (multcount - 2)
			# ;Changes average multiple by
			diff_avg_mult_from_median = average_mult - avg_mult_wo_median
		else:
			# ;Views
			(median_title, median_views), (median2_title, median2_views) = MASTER_VIEWS[
				count // 2 - 1], MASTER_VIEWS[count // 2]
			views_wo_median = views_unnamed[:]
			views_wo_median.pop(count // 2 - 1)
			views_wo_median.pop(count // 2 - 1)
			avg_wo_median = sum(views_wo_median) / (count - 2)
			# ;Changes average viewcount by
			diff_avg_from_median = average_pageviews - avg_wo_median
			diffs_wo_median = diffs[:]
			diffs_wo_median.pop(diffcount // 2)
			avg_diff_wo_median = sum(diffs_wo_median) / (diffcount - 1)
			# ;Changes average difference by
			diff_avg_diff_from_median = average_diff - avg_diff_wo_median
			mults_wo_median = mults[:]
			mults_wo_median.pop(multcount // 2)
			avg_mult_wo_median = sum(mults_wo_median) / (multcount - 1)
			# ;Changes average multiple by
			diff_avg_mult_from_median = average_mult - avg_mult_wo_median
		print('generate')
		embed = d.Embed(title='Total stats', description='Total statistics overall')
		embed.add_field(name='Average pageviews per page', value='{} views'.format(average_pageviews))
		embed.add_field(name='Median pageviews per page', value='{} views'.format(median_pageviews))
		embed.add_field(name='Average difference between pageviews', value='{} views per 2 pages'.format(average_diff))
		embed.add_field(name='Median difference between pageviews', value='{} views'.format(median_diff))
		embed.add_field(name='Average multiple of views', value='{} times per 2 pages'.format(average_mult))
		embed.add_field(name='Median multiple of views', value='{} times'.format(median_mult))
		embed.add_field(name='Total pageviews', value='{} views'.format(total))
		await ctx.send(embed=embed)
		embed = d.Embed(title='Stats for highest datapoint: {}'.format(highest_title), description='Stats for the highest-ranked page')
		embed.add_field(name='Views', value=str(highest_views))
		embed.add_field(name='Pulls up average viewcount by', value='{} views'.format(diff_avg_from_high))
		embed.add_field(name='Difference to next highest, {}'.format(next_high_title), value='{} views'.format(diff_next_high))
		embed.add_field(name='Pulls up average difference by', value='{} views per 2 pages'.format(diff_avg_diff_from_high))
		embed.add_field(name='Multiple of next highest, {}'.format(next_high_title), value='{} is {} times more popular'.format(highest_title, mult_next_high))
		await ctx.send(embed=embed)
		embed = d.Embed(title='Stats for lowest datapoint: {}'.format(lowest_title), description='Stats for the lowest-ranked page')
		embed.add_field(name='Views', value=str(lowest_views))
		embed.add_field(name='Pulls down average viewcount by', value='{} views'.format(diff_avg_from_low))
		embed.add_field(name='Difference to next lowest, {}'.format(next_low_title), value='{} views'.format(diff_next_low))
		embed.add_field(name='Pulls down average difference by', value='{} views per 2 pages'.format(diff_avg_diff_from_low))
		embed.add_field(name='Fraction of next lowest, {}'.format(next_low_title), value='{} is {} times more popular'.format(next_low_title, mult_next_low))
		await ctx.send(embed=embed)
		if count % 2:
			embed = d.Embed(title='Stats for median datapoint: {}'.format(median_title), description='Stats for the middle-ranked page')
			embed.add_field(name='Views', value=str(median_views))
		else:
			embed = d.Embed(title='Stats for median datapoints: {} and {}'.format(median_title, median2_title), description='Stats for the middle-ranked pages')
			embed.add_field(name='Views', value='{} and {}'.format(median_views, median2_views))
		embed.add_field(name='Changes average viewcount by', value='{} views'.format(diff_avg_from_median))
		embed.add_field(name='Changes average difference by', value='{} views per 2 pages'.format(diff_avg_diff_from_median))
		embed.add_field(name='Changes average multiple by', value='{} times'.format(diff_avg_mult_from_median))
		print('generated')
		await ctx.send(embed=embed)
		print('sent?')
