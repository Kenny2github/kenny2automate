import asyncio
import os
from typing import Optional
import aiofiles
import aiosqlite
from .logger import getLogger

__all__ = [
    'db',
    'Database'
]

logger = getLogger('db')

class Database:
    """Represents the database connection."""

    _inst = None
    DB_FILE = 'autoabyx.db'
    DB_VERSION = 1 # latest version
    SQL_DIR = os.path.join('AutoAbyx', 'sql')

    conn: Optional[aiosqlite.Connection] = None
    cur: Optional[aiosqlite.Cursor] = None
    lock = asyncio.Lock()

    def __new__(cls):
        """The database connection is a singleton."""
        if cls._inst is None:
            cls._inst = super().__new__(cls)
        return cls._inst

    async def init(self):
        """Open a connection to the database and create schema if necessary.
        The Database is usable from this point forward.
        """
        self.conn = await aiosqlite.connect(self.DB_FILE)
        self.conn.row_factory = aiosqlite.Row
        self.cur = await self.conn.cursor()
        async with self.lock:
            await self.cur.execute('PRAGMA user_version')
            current_version = (await self.cur.fetchone())[0]
        if current_version == self.DB_VERSION:
            logger.info('Latest database version (%s) matches current (%s)',
                        current_version, self.DB_VERSION)
            return
        if current_version > self.DB_VERSION:
            raise RuntimeError(
                f'Outdated DB version: ours is {self.DB_VERSION}, '
                f'saved is {current_version}')
        logger.info('Database is outdated, upgrading from %s to %s',
                    current_version, self.DB_VERSION)
        for ver in range(current_version + 1, self.DB_VERSION + 1):
            sqlfile = os.path.join(self.SQL_DIR, f'v{ver}.sql')
            if not os.path.isfile(sqlfile):
                logger.info('  No script for v%s, skipping', ver)
                continue
            async with aiofiles.open(sqlfile) as f:
                logger.info('  v%s -> v%s', ver - 1, ver)
                try:
                    await self.cur.executescript(await f.read())
                except aiosqlite.OperationalError:
                    logger.exception('    Upgrading failed:')
        # can't use quoting with PRAGMA statements, so I have to do
        # something very illegal here and directly substitute a value
        query = f'PRAGMA user_version = {self.DB_VERSION}'
        logger.info(query)
        await self.cur.execute(query)

    async def stop(self):
        """Commit and close the connection to the database.
        The Database is unusable from this point forward.
        """
        await self.conn.commit()
        await self.conn.close()
        self.conn = self.cur = None

    async def asterisk_langs(self, asterisk: str) -> dict[int, str]:
        """Get * i18n language settings."""
        langs: dict[int, str] = {}
        query = f'SELECT {asterisk}_id, lang FROM {asterisk}s'
        async with self.lock:
            await self.cur.execute(query)
            async for row in self.cur:
                langs[row[f'{asterisk}_id']] = row['lang']
        return langs

    async def user_langs(self) -> dict[int, str]:
        """Get user i18n language settings."""
        return await self.asterisk_langs('user')

    async def channel_langs(self) -> dict[int, str]:
        """Get channel i18n language settings."""
        return await self.asterisk_langs('channel')

    async def set_lang(self, asterisk: str, obj_id: int, lang: Optional[str]):
        """Set the language for a *."""
        query = f'INSERT INTO {asterisk}s ({asterisk}_id, lang) VALUES (?, ?) ' \
            f'ON CONFLICT({asterisk}_id) DO UPDATE SET lang=excluded.lang'
        await self.cur.execute(query, (obj_id, lang))

    async def set_user_lang(self, user_id: int, lang: Optional[str]):
        """Set the language for a user."""
        await self.set_lang('user', user_id, lang)

    async def set_channel_lang(self, channel_id: int, lang: Optional[str]):
        """Set the language for a channel."""
        await self.set_lang('channel', channel_id, lang)

db: Database = Database()
