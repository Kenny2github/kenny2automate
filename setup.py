from setuptools import setup, find_packages

setup(
	name='kenny2automate',
	version='2.0',
	description='A Python Discord bot',
	url='https://github.com/Kenny2github/kenny2automate',
	author='Kenny2github',
	author_email='kenny2minecraft@gmail.com',
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Topic :: Communications :: Chat',
		'Topic :: Games/Entertainment :: Turn Based Strategy'
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Natural Language :: Chinese (Traditional)',
		'Natural Language :: Japanese',
		'Operating System :: Microsoft :: Windows :: Windows 10',
		'Operating System :: POSIX :: Linux'
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: SQL'
	],
	keywords='discord bot fun',
	packages=find_packages(),
	install_requires=['discord.py', 'requests', 'mw-api-client'],
	python_requires='>=3.6',
)
