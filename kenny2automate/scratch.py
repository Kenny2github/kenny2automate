import json
import random
from discord.ext.commands import group
import requests
from .i18n import i18n

DGSWIKISERVER = 328938947717890058

class Scratch(object):
	def __init__(self, bot):
		self.bot = bot

	def __local_check(self, ctx):
		if ctx.guild is None:
			return False
		return ctx.guild.id == DGSWIKISERVER

	async def req(self, url):
		resp = await self.bot.loop.run_in_executor(None, requests.get, url)
		result = None
		if resp.status_code < 400:
			result = resp.text
		return result

	@group()
	async def scratch(self, ctx):
		"""Scratch-related commands. Run `;help scratch`."""
		pass

	@scratch.command()
	async def randomproject(self, ctx):
		"""Get a random project link!"""
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
			await ctx.send('https://scratch.mit.edu/projects/' + str(pid))

	@scratch.command()
	async def messagecount(self, ctx, name=None):
		"""How many messages do you have on Scratch?"""
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
				await ctx.send(i18n(
					ctx, 'scratch/messagecount-failed', username
				))
			else:
				await ctx.send(i18n(
					ctx,
					'scratch/messagecount',
					username,
					json.loads(resp)['count']
				))

	@scratch.command()
	async def news(self, ctx):
		"""Get Scratch news."""
		content = await self.req('https://api.scratch.mit.edu/news')
		content = json.loads(content)
		for new in content[:5]:
			await ctx.send(
				'**' + new['headline'] + '**'
				+ '\n' + new['copy'] + '\n' + new['url']
			)
