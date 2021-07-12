import os
from time import time
from typing import Optional
from dataclasses import dataclass
from aiohttp import web, ClientSession
from ..config import config
from ..db import db
from ..logger import getLogger

DISCORD_API = 'https://discord.com/api/v8'
CLIENT_ID: int = config.client_id
CLIENT_SECRET: str = config.client_secret
REDIRECT_URI: str = config.redirect_uri
WEB_ROOT: str = config.web_root
FILE_ROOT: str = os.path.dirname(os.path.abspath(__file__))
SCOPES = 'identify guilds'
TOKEN_TYPE = 'Bearer'

logger = getLogger('server')

@dataclass
class Session:
    user_id: Optional[int]
    access_token: Optional[str]
    logged_in: Optional[float]
    token_expiry: Optional[int]

    session: ClientSession

class Handler:
    """Request handler class for the server."""

    sessions: dict[str, Session]

    def __init__(self):
        self.sessions = {}

    @staticmethod
    def path(self, filepath: str) -> str:
        return os.path.join(FILE_ROOT, filepath)

    async def load_sessions(self, session_id: str = None):
        """Load often-used session data into cache."""
        for row in await db.session_cache(session_id):
            headers = None
            if row['access_token'] is not None:
                headers = {'Authorization': f'%s %s' % (
                    TOKEN_TYPE, row['access_token'])}
            if row['session_id'] in self.sessions:
                await self.sessions[row['session_id']].session.close()
            self.sessions[row['session_id']] = Session(
                row['user_id'], row['access_token'],
                row['logged_in'], row['token_expiry'],
                ClientSession(headers=headers)
            )

    async def oauth_token(self, data: dict, session_id: str):
        """Update the session with token data."""
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        async with self.sessions[session_id].session.post(
            f'{DISCORD_API}/oauth2/token', data=data, headers=headers
        ) as req:
            req.raise_for_status()
            body = await req.json()
        async with self.sessions[session_id].session.get(
            f'{DISCORD_API}/users/@me'
        ) as req:
            req.raise_for_status()
            body['user_id'] = (await req.json())['id']
        await db.touch_user(body['user_id'])
        await db.session_response(session_id, body)
        await self.load_sessions(session_id)

    async def login_session(self, session_id: str, code: str):
        """Given an OAuth code, retrieve a refresh and access token."""
        data = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URI
        }
        await self.oauth_token(data, session_id)

    async def refresh_session(self, session_id: str):
        """Use a refresh token to continue OAuth access."""
        if self.sessions[session_id].user_id is None:
            raise RuntimeError('trying to refresh a non-logged-in session')
        data = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'grant_type': 'refresh_token',
            'refresh_token': await db.refresh_token(session_id)
        }
        await self.oauth_token(data, session_id)

    async def check_session_validity(self, session_id: str):
        """Check if a session needs refreshing, and do so if so."""
        session = self.sessions[session_id]
        if session.logged_in is None:
            return # no refreshing needed if not logged in
        if time() > session.logged_in + session.token_expiry:
            await self.refresh_session(session_id)

    async def create_session(self) -> str:
        """Generate a new (un-logged-in) session and return its ID."""
        session_id = await db.create_session()
        await self.load_sessions(session_id)
        return session_id
