import re
import random
import functools
from urllib.parse import quote
import asyncio as a
import discord as d
from discord.ext.commands import command
from discord.ext import commands as c
import requests
from .i18n import i18n

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
	@c.cooldown(1, 3600.0, c.BucketType.guild)
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
				await ctx.send(i18n(ctx, 'wiki/page-failed'))
				return
		content = list(content['query']['pages']
			.values())[0]['revisions'][0]['*']
		content = content.splitlines()
		contents = ['```html\n']
		i = 0
		for line in content:
			if len(contents[i]) + 11 > 2000:
				contents.append('```html\n')
				temp = contents[i][:1997].rsplit('\n', 1)
				contents[i], contents[i+1] = \
					temp[0], temp[1] + contents[i][1997:]
				contents[i] += '```'
				i += 1
				contents[i] = '```html\n' + contents[i]
			contents[i] += line + '\n'
		contents[-1] += '```'
		for msg in contents:
			await ctx.send(msg)

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
				await ctx.send(i18n(ctx, 'wiki/iwstats-failed'))
				return
			content = list(content['query']['pages']
				.values())[0]['revisions'][0]['*']
		exp = re.compile(r"""\|-
\|(?P<time>[^\|]+)
\|(?P<pages>[0-9]+)
\|(?P<articles>[0-9]+)
\|(?P<edits>[0-9]+)
\|(?P<images>[0-9]+)
\|(?P<users>[0-9]+)
\|(?P<activeusers>[0-9]+)
\|(?P<admins>[0-9]+)
""")
		for match in re.finditer(
			r'(?P<cont>==\s*(?P<code>[a-z][a-z])\s*==[\s\S]+?\|\})',
			content,
			re.I | re.S
		):
			embed = d.Embed(
				title=i18n(ctx, 'wiki/iwstats-title', match.group('code')),
				description=i18n(
					ctx, 'wiki/iwstats-description', match.group('code')
				),
				color=random.randint(0, 0xffffff)
			)
			for fieldtitle, value in list(
					re.finditer(exp, match.group('cont'))
					)[-1].groupdict().items():
				embed.add_field(
					name=i18n(ctx, 'wiki/iwstats-' + fieldtitle),
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
				await ctx.send(i18n(ctx, 'wiki/wikistats-failed'))
				return
		data = data['query']['statistics']
		embed = d.Embed(
			title=i18n(ctx, 'wiki/iwstats-title', wiki),
			description=i18n(ctx, 'wiki/iwstats-description', wiki),
		)
		for fieldtitle, value in data.items():
			embed.add_field(
				name=i18n(ctx, 'wiki/iwstats-' + fieldtitle),
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
				await ctx.send(i18n(ctx, 'wiki/wikistats-failed'))
				return
		data = list(data['query']['pages'].values())[0]['revisions'][0]
		content = data['*']

		MASTER_VIEWS = [
			(m.group(1).replace('_', ' '), int(m.group(2)))
			for m in re.finditer(
				r'\n#\s*\[\[([^\]]+)\]\]\s*\((\d+) views\)',
				content
			)
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

		diffs = [i - views_unnamed[n+1]
			for n, i in enumerate(views_unnamed[:-1])]
		diffcount = len(diffs)
		# ;Average difference between pageviews
		average_diff = sum(diffs) / diffcount
		# ;Median difference between pageviews
		median_diff = (diffs[diffcount // 2]
			if diffcount % 2
			else ((diffs[diffcount // 2]
				+ diffs[diffcount // 2 - 1])
				/ 2))
		mults = [i / views_unnamed[n+1]
			for n, i in enumerate(views_unnamed[:-1])]
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
			median_title, median_views = MASTER_VIEWS[count // 2]
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
			(median_title, median_views), (median2_title, median2_views) \
				= MASTER_VIEWS[count // 2 - 1], MASTER_VIEWS[count // 2]
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
		embed = d.Embed(
			title=i18n(ctx, 'wiki/analyzega-total-title'),
			description=i18n(ctx, 'wiki/analyzega-total-description')
		)
		embed.add_field(name=i18n(ctx, 'wiki/analyzega-total-appp'),
			value=i18n(ctx, 'wiki/analyzega-views', average_pageviews))
		embed.add_field(name=i18n(ctx, 'wiki/analyzega-total-mppp'),
			value=i18n(ctx, 'wiki/analyzega-views', median_pageviews))
		embed.add_field(name=i18n(ctx, 'wiki/analyzega-total-adbp'),
			value=i18n(ctx, 'wiki/analyzega-views-per-pages', average_diff))
		embed.add_field(name=i18n(ctx, 'wiki/analyzega-total-mdbp'),
			value=i18n(ctx, 'wiki/analyzega-views', median_diff))
		embed.add_field(name=i18n(ctx, 'wiki/analyzega-total-amov'),
			value=i18n(ctx, 'wiki/analyzega-times-per-pages', average_mult))
		embed.add_field(name=i18n(ctx, 'wiki/analyzega-total-mmov'),
			value=i18n(ctx, 'wiki/analyzega-times', median_mult))
		embed.add_field(name=i18n(ctx, 'wiki/analyzega-total-tp'),
			value=i18n(ctx, 'wiki/analyzega-views', total))
		await ctx.send(embed=embed)
		embed = d.Embed(
			title=i18n(ctx, 'wiki/analyzega-highest-title', highest_title),
			description=i18n(ctx, 'wiki/analyzega-highest-description')
		)
		embed.add_field(name=i18n(ctx, 'wiki/analyzega-views-title'),
			value=str(highest_views))
		embed.add_field(name=i18n(ctx, 'wiki/analyzega-highest-puavb'),
			value=i18n(ctx, 'wiki/analyzega-views', diff_avg_from_high))
		embed.add_field(name=i18n(ctx, 'wiki/analyzega-highest-dtnh',
			next_high_title),
			value=i18n(ctx, 'wiki/analyzega-views', diff_next_high))
		embed.add_field(name=i18n(ctx, 'wiki/analyzega-highest-puadb'),
			value=i18n(ctx, 'wiki/analyzega-views-per-pages',
				diff_avg_diff_from_high))
		embed.add_field(name=i18n(ctx, 'wiki/analyzega-highest-monh',
			next_high_title),
			value=i18n(ctx, 'wiki/analyzega-highest-monh-value', highest_title,
				mult_next_high))
		await ctx.send(embed=embed)
		embed = d.Embed(
			title=i18n(ctx, 'wiki/analyzega-lowest-title', lowest_title),
			description=i18n(ctx, 'wiki/analyzega-lowest-description')
		)
		embed.add_field(name=i18n(ctx, 'wiki/analyzega-views-title'),
			value=str(lowest_views))
		embed.add_field(name=i18n(ctx, 'wiki/analyzega-lowest-pdavb'),
			value=i18n(ctx, 'wiki/analyzega-views', diff_avg_from_low))
		embed.add_field(name=i18n(ctx, 'wiki/analyzega-lowest-dtnl', next_low_title),
			value=i18n(ctx, 'wiki/analyzega-views', diff_next_low))
		embed.add_field(name=i18n(ctx, 'wiki/analyzega-lowest-pdadb'),
			value=i18n(ctx, 'wiki/analyzega-views-per-pages',
				diff_avg_diff_from_low))
		embed.add_field(name=i18n(ctx, 'wiki/analyzega-lowest-fonl', next_low_title),
			value=i18n(ctx, 'wiki/analyzega-lowest-fonl-value', next_low_title,
				mult_next_low))
		await ctx.send(embed=embed)
		if count % 2:
			embed = d.Embed(
				title=i18n(ctx, 'wiki/analyzega-median-title1', median_title),
				description=i18n(ctx, 'wiki/analyzega-median-description1')
			)
			embed.add_field(name=i18n(ctx, 'wiki/analyzega-views-title'),
				value=str(median_views))
		else:
			embed = d.Embed(
				title=i18n(ctx, 'wiki/analyzega-median-title2', median_title,
					median2_title),
				description=i18n(ctx, 'wiki/analyzega-median-description2')
			)
			embed.add_field(name=i18n(ctx, 'wiki/analyzega-views-title'),
				value=i18n(ctx, 'wiki/analyzega-median-views', median_views,
					median2_views))
		embed.add_field(name=i18n(ctx, 'wiki/analyzega-median-cavb'),
			value=i18n(ctx, 'wiki/analyzega-views', diff_avg_from_median))
		embed.add_field(name=i18n(ctx, 'wiki/analyzega-median-cadb'),
			value=i18n(ctx, 'wiki/analyzega-views-per-pages',
				diff_avg_diff_from_median))
		embed.add_field(name=i18n(ctx, 'wiki/analyzega-median-camb'),
			value=i18n(ctx, 'wiki/analyzega-views', diff_avg_mult_from_median))
		print('generated')
		await ctx.send(embed=embed)
		print('sent?')
