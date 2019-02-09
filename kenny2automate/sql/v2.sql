CREATE TABLE IF NOT EXISTS server_sessions (
  -- session key
  session_id text PRIMARY KEY NOT NULL,
  -- session data
  session pickle
);
ALTER TABLE channels ADD COLUMN games_ping text;
ALTER TABLE users ADD COLUMN games_ping text;
