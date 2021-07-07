import importlib
from discord.ext import commands
from .client import client
from .config import TOKEN, cmdargs
from .logger import getLogger
from .status import SetStatus
from .watcher import stop_on_change

MODULES = {
    'Miscellaneous Commands': ('misc_cmds', 'misc')
}

logger = getLogger('init')

def import_cog(bot: commands.Bot, name: str, fname: str):
    module = importlib.import_module('.' + fname, __name__)
    module.setup(bot)
    logger.info('Loaded %s', name)

globs = {}

def run():
    for name, (fname, cmdname) in MODULES.items():
        if cmdname in cmdargs.disable:
            logger.info('Not loading %s', name)
        else:
            import_cog(client, name, fname)
    globs['status'] = SetStatus(client)
    globs['wakeup'] = client.loop.create_task(stop_on_change(client, 'AutoAbyx'))
    globs['status'].start()
    client.loop.run_until_complete(client.start(TOKEN))

def done():
    try:
        if 'wakeup' in globs:
            globs['wakeup'].cancel()
        if 'status' in globs:
            globs['status'].cancel()
    except RuntimeError as exc:
        print(exc)
    client.loop.run_until_complete(client.close())
    client.loop.stop()
    client.loop.close()