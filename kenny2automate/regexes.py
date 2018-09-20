import re
from discord.ext.commands import command
from .i18n import i18n

class Regexes(object):
	"""Regex commands - Python flavored."""
	@command()
	async def search(self, ctx, pattern, string, flags=None):
		"""Make a Python-flavored regex search! All groups are shown."""
		if flags is not None:
			exp = '(?' + flags.lower().replace('l', 'L') + ')(?:' + pattern + ')'
		else:
			exp = pattern
		try:
			m = re.search(exp, string)
		except Exception:
			m = False
		if m:
			result = i18n(
				ctx,
				'regexes/search-result',
				m.group(0),
				'\n'.join(group or '' for group in m.groups())
			)
		elif m is False:
			result = i18n(ctx, 'regexes/search-error')
		else:
			result = i18n(ctx, 'regexes/search-result-nomatch')
		await ctx.send(result)

	@command()
	async def findall(self, ctx, pattern, string, flags=None):
		"""Use a Python-flavor regex to find all occurences of a pattern!"""
		if flags is not None:
			exp = '(?' + flags.lower().replace('l', 'L') + ')(?:' + pattern + ')'
		else:
			exp = pattern
		gen = re.finditer(exp, string)
		result = i18n(ctx, 'regexes/findall-result', '{0}')
		result2 = ''
		try:
			for m in gen:
				result2 += m.group(0) + ('\t' if len(m.groups()) > 0 else '') + '\t'.join(m.groups()) + '\n'
		except Exception:
			result = result.format(i18n(ctx, 'regexes/findall-error'))
		if not result2:
			result = result.format(i18n(ctx, 'regexes/findall-result-none'))
		if result2:
			ms = result2.split('\n')
			ms = [len(m.strip().split('\t')) for m in ms]
			ms = max(ms)
			gpstr = i18n(ctx, 'regexes/findall-gp', '{0}') #manual format
			result2 = '\t'.join([gpstr.format(i) for i in range(ms)]) \
				+ '\n' + result2
			result = result.format(result2)
		await ctx.send(result)
