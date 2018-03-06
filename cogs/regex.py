from discord.ext.commands import command
import re

class Regexes(object):
	"""Regex commands - Python flavored."""
	def __init__(self, bot):
		self.bot = bot

	@command()
	async def search(self, ctx, pattern, string, flags=None):
		"""Make a Python-flavored regex search! All groups are shown."""
		print('re.search')
		if flags is not None:
			exp = '(?' + flags.lower().replace('l', 'L') + ')(?:' + pattern + ')'
		else:
			exp = pattern
		try:
			m = re.search(exp, string)
		except Exception:
			m = False
		if m:
			result = '```\nGroups:\n' + m.group(0) + '\n'
			for group in m.groups():
				result += (group or '') + '\n'
			result += '```'
		elif m is False:
			result = '```\nError in flags or expression.\n```'
		else:
			result = '```\nNo match :(\n```'
		await ctx.send(result)

	@command()
	async def findall(self, ctx, pattern, string, flags=None):
		"""Use a Python-flavor regex to find all occurences of a pattern!"""
		print('re.findall')
		if flags is not None:
			exp = '(?' + flags.lower().replace('l', 'L') + ')(?:' + pattern + ')'
		else:
			exp = pattern
		gen = re.finditer(exp, string)
		result = '```\nResults:\n'
		try:
			for m in gen:
				result += m.group(0) + ('\t' if len(m.groups()) > 0 else '') + '\t'.join(m.groups()) + '\n'
		except Exception:
			result += 'Error in flags or expression.\n'
		if result == '```\nResults:\n':
			result += 'No results :(\n'
		if '\t' in result:
			ms = re.finditer('([^\t\n]*\t)+[^\t\n]*\n?', result)
			ms = [len(m.group(0).strip().split('\t')) for m in ms]
			ms = max(ms)
			result = result[:13] \
				 + '\t'.join(['Gp{}'.format(i) for i in range(ms-1)]) \
				 + '\n' + result[13:]
		result += '```'
		await ctx.send(result)

def setup_regex(client):
	client.add_cog(Regexes(client))
