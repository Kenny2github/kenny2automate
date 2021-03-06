import subprocess
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	reqs = f.read()
reqs = reqs.strip().splitlines()

VERSION = subprocess.check_output(
    "cd kenny2automate && git rev-parse --short HEAD",
    shell=True
).decode('ascii').strip()

setup(
	name='kenny2automate',
	version='19.0a' + VERSION,
	description='A Python Discord bot',
	url='https://github.com/Kenny2github/kenny2automate',
	author='Kenny2github',
	author_email='kenny2minecraft@gmail.com',
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Topic :: Communications :: Chat',
		'Topic :: Games/Entertainment :: Turn Based Strategy',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Natural Language :: Chinese (Traditional)',
		'Natural Language :: Japanese',
		'Natural Language :: Russian',
		'Natural Language :: French',
		'Operating System :: Microsoft :: Windows :: Windows 10',
		'Operating System :: POSIX :: Linux',
		'Programming Language :: Python :: 3 :: Only',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: SQL',
	],
	keywords='discord bot fun',
	packages=find_packages(),
	install_requires=reqs,
	python_requires='>=3.7',
)
