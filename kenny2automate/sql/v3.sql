CREATE TABLE IF NOT EXISTS guilds (
  -- guild ID
  guild_id integer PRIMARY KEY NOT NULL,
  -- bad words
  words_censor text,
  -- disabled commands
  guild_disabled_commands text,
  -- disabled cogs
  guild_disabled_cogs text
)
