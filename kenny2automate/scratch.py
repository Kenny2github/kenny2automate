import json
import random
import discord as d
from discord.ext.commands import group, Cog
import requests
from .i18n import embed

DGSWIKISERVER = 328938947717890058

class Scratch(Cog):
	"""scratch/cog-desc"""
	def __init__(self, bot):
		self.bot = bot

	def cog_check(self, ctx):
		if ctx.guild is None:
			return False
		return ctx.guild.id == DGSWIKISERVER

	async def req(self, url):
		resp = await self.bot.loop.run_in_executor(None, requests.get, url)
		result = None
		if resp.status_code < 400:
			result = resp.text
		return result

	@group(description='scratch/scratch-desc')
	async def scratch(self, ctx):
		pass

	@scratch.command(description='scratch/randomproject-desc')
	async def randomproject(self, ctx):
		async with ctx.channel.typing():
			count = json.loads(await self.req(
				'https://api.scratch.mit.edu/projects/count/all'
			))['count']
			comments = None
			while comments is None:
				pid = random.randint(1, count)
				comments = await self.req(
					'https://scratch.mit.edu/site-api/comments/project/'
					+ str(pid)
				)
			await ctx.send(embed=embed(ctx, description='[{}]({})'.format(
				i18n(ctx, 'scratch/randomproject-link'),
				'https://scratch.mit.edu/projects/' + str(pid)
			)))

	@scratch.command(description='scratch/messagecount-desc')
	async def messagecount(self, ctx, name=None):
		async with ctx.channel.typing():
			if name is not None:
				resp = await self.req(
					'https://api.scratch.mit.edu/users/{}/messages/count'
					.format(name)
				)
				username = name
			else:
				resp = None
				if ctx.author.nick is not None:
					resp = await self.req(
						'https://api.scratch.mit.edu/users/{}/messages/count'
						.format(ctx.author.nick)
					)
					username = ctx.author.nick
				if resp is None:
					resp = await self.req(
						'https://api.scratch.mit.edu/users/{}/messages/count'
						.format(ctx.author.name)
					)
					username = ctx.author.name
			if resp is None:
				await ctx.send(embed=embed(ctx,
					title=('error',),
					description=('scratch/messagecount-failed', username),
					color=0xff0000
				))
			else:
				await ctx.send(embed=embed(ctx,
					title=('scratch/messagecount-title',),
					description=(
						'scratch/messagecount',
						username,
						json.loads(resp)['count']
					),
					color=0xffffff
				))

	@scratch.command(description='scratch/news-desc')
	async def news(self, ctx):
		content = await self.req('https://api.scratch.mit.edu/news')
		content = json.loads(content)
		for new in content[:5]:
			await ctx.send(embed=d.Embed(
				title=new['headline'],
				description='[{copy}]({url})'.format(**new),
				color=0xffff00
			))
