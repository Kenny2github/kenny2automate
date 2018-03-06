from setuptools import setup, find_packages

setup(
	name='kenny2automate',
	version='0.0',
	description='A Python Discord bot',
	url='https://github.com/Kenny2github/kenny2automate',
	author='Kenny2github',
	author_email='kenny2minecraft@gmail.com',
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Topic :: Communications :: Chat',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
	],
	keywords='discord bot fun',
	packages=find_packages(),
	install_requires=['discord.py'],
)
