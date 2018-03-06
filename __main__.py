import discord as d
from discord.ext.commands import Bot
from .cogs.regex import setup_regex
from .cogs.games import setup_games

client = Bot(description="A testing Discord bot.", command_prefix=";")

setup_regex(client)
setup_games(client)

@client.event
async def on_ready(*_, **__):
	await client.change_presence(game=d.Game(name=';help'))

@client.command()
async def repeat(ctx, *, arg):
	"""Repeat what you say, right back at ya."""
	print('Repeating ' + arg)
	await ctx.send(arg)

@client.command()
async def hello(ctx):
	"""Test whether the bot is running! Simply says "Hello World!".
	Also checks permissions.
	"""
	print('Hello World!')
	await ctx.send('Hello World!')

@client.event
async def on_command_error(ctx, err):
	await ctx.send('```Error: {}```'.format(err.args[0]),)

@client.command()
async def hmmst(ctx):
	"""hmmst"""
	print('hmmst')
	await ctx.send('hmmst')

print('Defined stuff')

with open('login.txt') as f:
	token = f.read().strip()

client.run(token)
