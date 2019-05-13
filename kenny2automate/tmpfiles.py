from os import path, remove
import time
from contextlib import contextmanager

tmpdir = path.join(path.dirname(path.dirname(__file__)), 'temp')

INDEX = 0

def tmpfile(prefix='', suffix=''):
    global INDEX
    INDEX += 1
    return path.join(
        tmpdir,
        '{}{}-{}{}'.format(
            prefix,
            time.time(),
            INDEX,
            suffix
        )
    )

@contextmanager
def tmpf(*args, **kwargs):
    name = tmpfile(*args, **kwargs)
    try:
        yield name
    finally:
        remove(name)
