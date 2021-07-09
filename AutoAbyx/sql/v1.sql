-- main users table
CREATE TABLE IF NOT EXISTS users (
	-- user ID
	user_id integer PRIMARY KEY NOT NULL,
	-- i18n language
	lang text DEFAULT 'en',
	-- command prefix
	prefix text DEFAULT ';'
);

-- main channels table
CREATE TABLE IF NOT EXISTS channels (
	-- channel ID
	channel_id integer PRIMARY KEY NOT NULL,
	-- i18n language
	lang text DEFAULT 'en'
);

-- main guilds table
CREATE TABLE IF NOT EXISTS guilds (
	-- guild ID
	guild_id integer PRIMARY KEY NOT NULL,
	-- bad words (regex)
	words_censor text
);

-- one entry for every game to ping every channel for
-- to test if a channel should be pinged for a game,
-- check whether the following query returns any results:
-- SELECT * FROM channel_game_pings WHERE channel_id=? AND game=?;
CREATE TABLE IF NOT EXISTS channel_game_pings (
	-- channel ID
	channel_id integer NOT NULL,
	-- game to ping for (integer enum)
	game integer NOT NULL,
	-- keys
	PRIMARY KEY(channel_id, game),
	FOREIGN KEY(channel_id) REFERENCES channels(channel_id)
);

-- one entry for every game to (attempt to) ping every user for
-- to test if a user should be pinged for a game,
-- check whether the following query returns any results:
-- SELECT * FROM user_game_pings WHERE user_id=? AND game=?;
CREATE TABLE IF NOT EXISTS user_game_pings (
	-- user ID
	user_id integer NOT NULL,
	-- game to ping for (integer enum)
	game integer NOT NULL,
	-- keys
	PRIMARY KEY(user_id, game),
	FOREIGN KEY(user_id) REFERENCES users(user_id)
);

-- one entry for every word in the one-word-sentence
CREATE TABLE IF NOT EXISTS sentence (
	-- replacement for row ID
	word_id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	-- the word
	word text NOT NULL,
	-- the user who added it
	user_id integer NOT NULL,
	-- keys
	FOREIGN KEY(user_id) REFERENCES users(user_id)
);

-- user highscores for 2048
CREATE TABLE IF NOT EXISTS pow211_highscores (
	-- user ID
	user_id integer PRIMARY KEY NOT NULL,
	-- their highscore
	score integer NOT NULL,
	-- keys
	FOREIGN KEY(user_id) REFERENCES users(user_id)
);

-- TODO: server sessions