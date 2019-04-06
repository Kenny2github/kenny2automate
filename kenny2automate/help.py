from discord.ext import commands
from .i18n import i18n, embed

class Kenny2help(commands.HelpCommand):
	def get_destination(self):
		return self.context.author

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
				(i.qualified_name, (i.description, ctx.prefix) if i.description else '\1', False)
				for i in categories
				if i is not None
			) + (
				('\1', ('help-cmds',), False),
			) + tuple(
				(i.name, (i.description, ctx.prefix) if i.description else '\1', False)
				for i in filtered
				if i.cog is None
			),
			footer=('help-footer', ctx.prefix)
		)
		await self.get_destination().send(embed=em)

	async def send_cog_help(self, cog):
		ctx = self.context
		filtered = await self.filter_commands(cog.get_commands())
		em = embed(ctx,
			description=(cog.description, ctx.prefix) if cog.description else None,
			color=0x55acee,
			fields=(
				(i.qualified_name, (i.description, ctx.prefix), False)
				for i in filtered
			)
		)
		await self.get_destination().send(embed=em)

	async def send_group_help(self, group):
		ctx = self.context
		filtered = await self.filter_commands(group.commands)
		desc = i18n(ctx, group.description, ctx.prefix)
		if group.help:
			desc += '\n\n'
			desc += i18n(ctx, group.help, ctx.prefix)
		em = embed(ctx,
			description=desc,
			color=0x55acee,
			fields=(
				(i.name, (i.description, ctx.prefix), False)
				for i in filtered
			)
		)
		await self.get_destination().send(embed=em)

	async def send_command_help(self, command):
		ctx = self.context
		desc = i18n(ctx, command.description, ctx.prefix)
		if command.help:
			desc += '\n\n'
			desc += i18n(ctx, command.help, ctx.prefix)
		em = embed(ctx,
			description=desc,
			color=0x55acee
		)
		await self.get_destination().send(embed=em)
