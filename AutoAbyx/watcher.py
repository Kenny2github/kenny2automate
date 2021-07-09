import os
import asyncio
from discord.ext import commands
from .logger import getLogger

logger = getLogger('watcher')

mtimes: dict[str, float] = {}

def recurse_mtimes(dir: str, *path: str):
    for item in os.listdir(os.path.join(*path, dir)):
        fullitem = os.path.join(*path, dir, item)
        if os.path.isdir(fullitem):
            recurse_mtimes(item, *path, dir)
        elif item.endswith(('.py', '.sql', '.json')):
            mtimes[fullitem] = os.path.getmtime(fullitem)

async def stop_on_change(bot: commands.Bot, path: str):
    recurse_mtimes(path)
    await bot.wait_until_ready()
    while 1:
        for fn, mtime in mtimes.items():
            try:
                newmtime = os.path.getmtime(fn)
            except FileNotFoundError:
                logger.info("File '%s' deleted, closing client", fn)
                await bot.close()
                return
            if newmtime > mtime:
                logger.info("File '%s' modified, closing client", fn)
                await bot.close()
                return
        await asyncio.sleep(1)