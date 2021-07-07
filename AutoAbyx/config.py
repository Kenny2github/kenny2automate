import argparse
import json
from AutoAbyx.utils import AttrDict

with open('config.json') as f:
    config = AttrDict(json.load(f))

parser = argparse.ArgumentParser(description='Run AutoAbyx.')
parser.add_argument('-p', '--prefix', nargs='?', metavar='prefix',
                    help='the bot prefix')
parser.add_argument('-d', '--disable', nargs='*', metavar='disable',
                    default=[], help='modules not to run')
parser.add_argument('--stdout', action='store_true', default=False,
                    help='log to stdout instead of a file')
cmdargs = parser.parse_args()

PREFIX = cmdargs.prefix or config.get('prefix') or ';'
TOKEN = config.token