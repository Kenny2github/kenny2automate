import re
import random
import functools
import asyncio as a
import discord as d
from discord.ext.commands import group
from discord.ext import commands as c
import mw_api_client as mwc
from .i18n import i18n, embed as _embed
from .utils import DummyCtx

DGSWIKISERVER = 328938947717890058

WIKI_URLS = {
	'de': 'https://scratch-dach.info/w/api.php',
	'en': 'https://en.scratch-wiki.info/w/api.php',
	'id': 'https://scratch-indo.info/w/api.php',
	'nl': 'https://nl.scratch-wiki.info/w/api.php',
	'hu': 'https://hu.scratch-wiki.info/w/api.php',
	'ru': 'https://scratch-ru.info/w/api.php',
	'fr': 'https://fr.scratch-wiki.info/w/api.php',
	'ja': 'https://ja.scratch-wiki.info/w/api.php',
	'test': 'https://test.scratch-wiki.info/w/api.php',
}
WIKIS = {k: mwc.Wiki(v) for k, v in WIKI_URLS.items()}

class Wiki(object):
	def __init__(self, bot, logger, server):
		self.bot = bot
		self.logger = logger
		self.serverid = server

	def __local_check(self, ctx):
		return ctx.guild is None or ctx.guild.id == DGSWIKISERVER

	async def q(self, call, *args, **kwargs):
		return await self.bot.loop.run_in_executor(
			None,
			functools.partial(call, *args, **kwargs)
		)

	sessions = {}

	@group()
	async def wiki(self, ctx):
		"""Wiki-related commands. Run `;help wiki`."""
		pass

	@wiki.command()
	async def login(self, ctx, wiki, username, *, password):
		"""Login to a Wiki. MUST BE IN DMS."""
		if ctx.guild is not None:
			try:
				await ctx.message.delete()
			except d.Forbidden:
				await ctx.send(embed=_embed(ctx,
					title=('error',),
					description=('wiki/login-notdm-nodelete',),
					color=0xff0000
				))
			else:
				msg = await ctx.send(embed=_embed(ctx,
					title=('error',),
					description=('wiki/login-notdm',),
					color=0xff0000
				))
				await a.sleep(2)
				await msg.delete()
			finally:
				return
		async with ctx.channel.typing():
			try:
				self.sessions[ctx.author.id] = await self.q(
					mwc.Wiki, WIKI_URLS[wiki]
				)
			except KeyError:
				await ctx.send(embed=_embed(ctx,
					title=('error',),
					description=('wiki/login-notwiki',),
					color=0xff0000
				))
				return
			w = self.sessions[ctx.author.id]
			try:
				await ctx.send(embed=_embed(ctx,
					title=('wiki/login-status-title',),
					description=(
						'wiki/login-status',
						(await self.q(
							w.clientlogin, username, password
						))['status']
					),
					color=0xffff00
				))
			except mwc.WikiError as exc:
				await ctx.send(embed=_embed(ctx,
					title=('error',),
					description=('wiki/login-failed', str(exc)),
					color=0xff0000
				))
				del self.sessions[ctx.author.id]
				return

	async def notloggedin(self, ctx):
		await ctx.send(embed=_embed(ctx,
			title=('error',),
			description=('wiki/notloggedin',),
			color=0xff0000
		))

	@wiki.command()
	@c.check(lambda ctx: ctx.guild is None)
	async def edit(self, ctx, *, title):
		"""Edit a Wiki page."""
		if ctx.author.id not in self.sessions:
			return await self.notloggedin(ctx)
		await ctx.send(embed=_embed(ctx,
			title=('battleship/instructions-title',),
			description=('wiki/edit-instructions',),
			color=0xffff00
		))
		msg = await self.bot.wait_for('message', check=lambda m: (
			m.channel.id == ctx.channel.id
			and m.author.id == ctx.author.id
			and ((
				m.content.strip().startswith('```')
				and m.content.strip().endswith('```')
			) or m.content == 'EOF')
		))
		content = ''
		while msg.content != 'EOF':
			content += msg.content.strip('`').strip() + '\n'
			msg = await self.bot.wait_for('message', check=lambda m: (
				m.channel.id == ctx.channel.id
				and m.author.id == ctx.author.id
				and ((
					m.content.strip().startswith('```')
					and m.content.strip().endswith('```')
				) or m.content == 'EOF')
			))
		await ctx.send(i18n(ctx, 'wiki/edit-summary'))
		msg = await self.bot.wait_for('message', check=lambda m: (
			m.channel.id == ctx.channel.id
			and m.author.id == ctx.author.id
		))
		summary = msg.content.strip()
		async with ctx.channel.typing():
			await ctx.send(embed=_embed(ctx,
				title=('wiki/edit-result-title',),
				description=(
					'wiki/edit-result',
					(await self.q(
						self.sessions[ctx.author.id].page(title).edit,
						content,
						summary
					))['edit']['result']
				),
				color=0xffff00
			))

	@wiki.command()
	@c.check(lambda ctx: ctx.guild is None)
	async def page(self, ctx, *, title):
		"""Get the contents of a page."""
		async with ctx.channel.typing():
			try:
				content = await self.q((
					WIKIS['en']
					if ctx.author.id not in self.sessions
					else self.sessions[ctx.author.id]
				).page(title).read)
			except Exception as exc:
				self.logger.error('Fetching page content failed: ' + str(exc),
					extra={'ctx': DummyCtx(author=DummyCtx(name='Wiki.page'))})
				await ctx.send(embed=_embed(ctx,
					title=('error',),
					description=('wiki/page-failed',),
					color=0xff0000
				))
				return
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

	@wiki.command()
	async def randompage(self, ctx):
		"""Get a link to a random Wiki page!"""
		rn = list(await self.q((
			WIKIS['en']
			if ctx.author.id not in self.sessions
			else self.sessions[ctx.author.id]
		).random, 1))[0]
		title = rn.title
		await ctx.send(title)

	@wiki.command()
	async def iwstats(self, ctx):
		"""Get statistics for the international wikis!"""
		async with ctx.channel.typing():
			try:
				content = await self.q(
					WIKIS['en'].page(
						'User:InterwikiBot/International Stats'
					).read
				)
			except Exception as exc:
				self.logger.error('Fetching wiki stats failed: ' + str(exc), extra={'ctx': DummyCtx(author=DummyCtx(name='Wiki.wikistats'))})
				await ctx.send(embed=_embed(ctx,
					title=('error',),
					description=('wiki/iwstats-failed',),
					color=0xff0000
				))
				return
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
			embed = _embed(ctx,
				title=('wiki/iwstats-title', match.group('code')),
				description=(
					'wiki/iwstats-description', match.group('code')
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

	@wiki.command()
	async def stats(self, ctx, wiki):
		"""Get stats for the ``wiki``wiki."""
		async with ctx.channel.typing():
			try:
				data = await self.q(
					WIKIS[wiki].meta.siteinfo,
					prop='statistics'
				)
			except Exception as exc:
				self.logger.error('Fetching wiki stats failed: ' + str(exc), extra={'ctx': DummyCtx(author=DummyCtx(name='Wiki.wikistats'))})
				await ctx.send(embed=_embed(ctx,
					title=('error',),
					description=('wiki/wikistats-failed',),
					color=0xff0000
				))
				return
		embed = _embed(ctx,
			title=('wiki/iwstats-title', wiki),
			description=('wiki/iwstats-description', wiki),
			color=0xffffff
		)
		for fieldtitle, value in data.items():
			embed.add_field(
				name=i18n(ctx, 'wiki/iwstats-' + fieldtitle),
				value=str(value),
			)
		await ctx.send(embed=embed)

	@wiki.group()
	async def analyzega(self, ctx):
		"""Analysis of GA stats."""
		pass

	@analyzega.command(name='en')
	@c.cooldown(1, 64800.0, type=c.BucketType.guild)
	async def analyzega_en(self, ctx):
		"""Analysis of English GA stats."""
		await self._analyzega(ctx, 'en')
	@analyzega.command(name='de')
	@c.cooldown(1, 64800.0, type=c.BucketType.guild)
	async def analyzega_de(self, ctx):
		"""Analysis of German GA stats."""
		await self._analyzega(ctx, 'de')
	@analyzega.command(name='id')
	@c.cooldown(1, 64800.0, type=c.BucketType.guild)
	async def analyzega_id(self, ctx):
		"""Analysis of Indonesian GA stats."""
		await self._analyzega(ctx, 'id')
	@analyzega.command(name='fr')
	@c.cooldown(1, 64800.0, type=c.BucketType.guild)
	async def analyzega_fr(self, ctx):
		"""Analysis of French GA stats."""
		await self._analyzega(ctx, 'fr')
	@analyzega.command(name='ru')
	@c.cooldown(1, 64800.0, type=c.BucketType.guild)
	async def analyzega_ru(self, ctx):
		"""Analysis of Russian GA stats."""
		await self._analyzega(ctx, 'ru')
	@analyzega.command(name='nl')
	@c.cooldown(1, 64800.0, type=c.BucketType.guild)
	async def analyzega_nl(self, ctx):
		"""Analysis of Dutch GA stats."""
		await self._analyzega(ctx, 'nl')
	@analyzega.command(name='hu')
	@c.cooldown(1, 64800.0, type=c.BucketType.guild)
	async def analyzega_hu(self, ctx):
		"""Analysis of Hungarian GA stats."""
		await self._analyzega(ctx, 'hu')
	@analyzega.command(name='ja')
	@c.cooldown(1, 64800.0, type=c.BucketType.guild)
	async def analyzega_ja(self, ctx):
		"""Analysis of Japanese GA stats."""
		await self._analyzega(ctx, 'ja')
	@analyzega.command(name='test')
	@c.cooldown(1, 64800.0, type=c.BucketType.guild)
	async def analyzega_test(self, ctx):
		"""Analysis of Test wiki GA stats."""
		await self._analyzega(ctx, 'test')

	async def _analyzega(self, ctx, wiki):
		"""Do some analysis of a wiki's GA stats"""
		async with ctx.channel.typing():
			try:
				content = await self.q(
					WIKIS[wiki].page('User:InterwikiBot/GA Stats').read
				)
			except Exception as exc:
				self.logger.error('Fetching wiki stats failed: ' + str(exc), extra={'ctx': DummyCtx(author=DummyCtx(name='Wiki.analyzega'))})
				await ctx.send(embed=_embed(ctx,
					title=('error',),
					description=('wiki/wikistats-failed',),
					color=0xff0000
				))
				return

		MASTER_VIEWS = [
			(m.group(1).replace('_', ' '), int(m.group(2)))
			for m in re.finditer(
				r'\n#\s*\[\[([^\]]+)\]\]\s*\((\d+) views\)',
				content
			)
		]
		MASTER_VIEWS.sort(key=lambda i: i[1], reverse=True) #sanity check
		views_unnamed = [j for i, j in MASTER_VIEWS]
		count = len(views_unnamed)
		# ===Total stats===
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

		# ===Stats for highest datapoint: ...
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

		# ===Stats for lowest datapoint: ...
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

		# ===Stats for median datapoints: ...
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
		#generate
		embed = _embed(ctx,
			title=('wiki/analyzega-total-title',),
			description=('wiki/analyzega-total-description',),
			color=0x55acee
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
		embed = _embed(ctx,
			title=('wiki/analyzega-highest-title', highest_title),
			description=('wiki/analyzega-highest-description',),
			color=0xffffff
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
		embed = _embed(ctx,
			title=('wiki/analyzega-lowest-title', lowest_title),
			description=('wiki/analyzega-lowest-description',),
			color=0
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
			embed = _embed(ctx,
				title=('wiki/analyzega-median-title1', median_title),
				description=('wiki/analyzega-median-description1',),
				color=0x808080
			)
			embed.add_field(name=i18n(ctx, 'wiki/analyzega-views-title'),
				value=str(median_views))
		else:
			embed = _embed(ctx,
				title=('wiki/analyzega-median-title2', median_title,
					median2_title),
				description=('wiki/analyzega-median-description2',),
				color=0x808080
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
		await ctx.send(embed=embed)
