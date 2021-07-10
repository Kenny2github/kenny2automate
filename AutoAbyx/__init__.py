import importlib
from discord.ext import commands
from .client import client
from .config import TOKEN, cmdargs
from .db import db
from .disabling import Disabling
from .i18n import Msg
from .logger import getLogger
from .prefix import Prefix
from .status import SetStatus
from .watcher import stop_on_change

MODULES = {
    'Miscellaneous Commands': ('misc_cmds', 'misc'),
    'Unit Conversions': ('units', 'units'),
    'Internationalization': ('i18n', 'i18n'),
    'Prefix': ('prefix', 'prefix'),
    'Command Disabling': ('disabling', 'disabling'),
}

logger = getLogger('init')

def import_cog(bot: commands.Bot, name: str, fname: str):
    """Load a module and run its setup function."""
    module = importlib.import_module('.' + fname, __name__)
    module.setup(bot)
    logger.info('Loaded %s', name)

globs = {}

def run():
    """Run the bot."""
    client.loop.run_until_complete(db.init())
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
    """Cleanup and shutdown the bot."""
    try:
        if 'wakeup' in globs:
            globs['wakeup'].cancel()
        if 'status' in globs:
            globs['status'].cancel()
    except RuntimeError as exc:
        print(exc)
    client.loop.run_until_complete(client.close())
    if db.conn is not None:
        client.loop.run_until_complete(db.stop())
    client.loop.stop()
    client.loop.close()