import json
import random
from discord.ext.commands import command
import requests

DGSWIKISERVER = 328938947717890058

class Scratch(object):
	def __init__(self, bot, logger, loop):
		self.bot = bot
		self.logger = logger
		self.loop = loop

	async def req(self, url):
		resp = await self.bot.loop.run_in_executor(None, requests.get, url)
		result = None
		if resp.status_code < 400:
			result = resp.text
		return result

	@command()
	async def randomproject(self, ctx):
		"""Get a random project link!"""
		self.logger.info('Scratch.randomproject', extra={'ctx': ctx})
		async with ctx.channel.typing():
			count = json.loads(await self.req('https://api.scratch.mit.edu/projects/count/all'))['count']
			comments = None
			while comments is None:
				pid = random.randint(1, count)
				comments = await self.req('https://scratch.mit.edu/site-api/comments/project/' + str(pid))
			await ctx.send('https://scratch.mit.edu/projects/' + str(pid))

	@command()
	async def messagecount(self, ctx, name=None):
		"""How many messages do you have on Scratch?"""
		async with ctx.channel.typing():
			if name is not None:
				self.logger.info('Scratch.messagecount: ' + name, extra={'ctx': ctx})
				resp = await self.req('https://api.scratch.mit.edu/users/' + name + '/messages/count')
				username = name
			else:
				resp = None
				if ctx.author.nick is not None:
					self.logger.info('Scratch.messagecount: ' + ctx.author.nick, extra={'ctx': ctx})
					resp = await self.req('https://api.scratch.mit.edu/users/' + ctx.author.nick + '/messages/count')
					username = ctx.author.nick
				if resp is None:
					self.logger.info('Scratch.messagecount: ' + ctx.author.name, extra={'ctx': ctx})
					resp = await self.req('https://api.scratch.mit.edu/users/' + ctx.author.name + '/messages/count')
					username = ctx.author.name
			if resp is None:
				await ctx.send("Couldn't get message count for " + username)
			else:
				await ctx.send('{} has {} message(s)'.format(
					username,
					json.loads(resp)['count']
				))

	@command()
	async def news(self, ctx):
		"""Get Scratch news."""
		self.logger.info('Scratch.news', extra={'ctx': ctx})
		content = await self.req('https://api.scratch.mit.edu/news')
		content = json.loads(content)
		for new in content[:5]:
			await ctx.send(
				'**' + new['headline'] + '**'
				+ '\n' + new['copy'] + '\n' + new['url']
			)
