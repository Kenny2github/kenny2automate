from discord import Forbidden
from discord.ext import commands
from .emoji import SEE_DM
from .i18n import i18n, embed

class Kenny2help(commands.HelpCommand):
	def get_destination(self):
		return self.context.author

	async def send_the_help(self, emb):
		try:
			await self.get_destination().send(embed=emb)
		except Forbidden as exc:
			if exc.code == 50007:
				await self.context.send(embed=embed(self.context,
					title=('error',),
					description=('cant-dm', self.context.author.mention),
					color=0xff0000
				))
			else:
				raise
		else:
			await self.context.message.add_reaction(SEE_DM)

	async def send_bot_help(self, mapping):
		ctx = self.context
		filtered = await self.filter_commands(ctx.bot.commands)
		categories = []
		for cmd in filtered:
			if cmd.cog not in categories:
				categories.append(cmd.cog)
		em = embed(ctx,
			description=(ctx.bot.description,),
			color=0x55acee,
			fields=tuple(
				(
					i.qualified_name,
					(i.description, ctx.prefix)
					if i.description else '\1',
					False
				)
				for i in categories
				if i is not None
			) + (
				('\1', ('help-cmds',), False),
			) + tuple(
				(
					self.command_string(i),
					(i.description, ctx.prefix)
					if i.description else '\1',
					False
				)
				for i in filtered
				if i.cog is None
			),
			footer=('help-footer', ctx.prefix)
		)
		await self.send_the_help(em)

	async def send_cog_help(self, cog):
		ctx = self.context
		filtered = await self.filter_commands(cog.get_commands())
		em = embed(ctx,
			description=(cog.description, ctx.prefix) if cog.description else None,
			color=0x55acee,
			fields=(
				(self.command_string(i), (i.description, ctx.prefix), False)
				for i in filtered
			)
		)
		await self.send_the_help(em)

	def command_string(self, cmd):
		ctx = self.context
		title = ctx.prefix + cmd.qualified_name
		title += ' ' + (i18n(ctx, cmd.usage) or cmd.signature)
		title = title.strip()
		return '`{}`'.format(title)

	async def send_group_help(self, group):
		ctx = self.context
		filtered = await self.filter_commands(group.commands)
		title = self.command_string(group)
		desc = i18n(ctx, group.description, ctx.prefix)
		if group.help:
			desc += '\n\n'
			desc += i18n(ctx, group.help, ctx.prefix)
		em = embed(ctx,
			title=title,
			description=desc,
			color=0x55acee,
			fields=(
				(self.command_string(i), (i.description, ctx.prefix), False)
				for i in filtered
			)
		)
		await self.send_the_help(em)

	async def send_command_help(self, command):
		ctx = self.context
		title = self.command_string(command)
		desc = i18n(ctx, command.description, ctx.prefix)
		if command.help:
			desc += '\n\n'
			desc += i18n(ctx, command.help, ctx.prefix)
		em = embed(ctx,
			title=title,
			description=desc,
			color=0x55acee
		)
		await self.send_the_help(em)
