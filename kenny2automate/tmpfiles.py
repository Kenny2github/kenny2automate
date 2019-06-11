from os import path, remove, mkdir
import time
from contextlib import contextmanager

tmpdir = path.join(path.dirname(path.dirname(__file__)), 'temp')
if not path.isdir(tmpdir):
    if path.exists(tmpdir):
        remove(tmpdir)
    else:
        mkdir(tmpdir)

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
