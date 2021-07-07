import sys
import os
import time
import logging
from .config import cmdargs

FORMAT = '{levelname}\t{asctime}: {name}:\t{message}'
TIME = '%Y-%m-%d'

os.makedirs('logs', exist_ok=True)

if cmdargs.stdout:
    handler = logging.StreamHandler(sys.stdout)
else:
    handler = logging.FileHandler(
        'logs/%s.log' % time.strftime(TIME), 'a', 'utf8')

logging.basicConfig(
    format=FORMAT, style='{', level=logging.INFO, handlers=[handler])

def getLogger(name: str) -> logging.Logger:
    return logging.getLogger('AutoAbyx.' + name)

logging.getLogger('discord').setLevel(logging.WARNING)