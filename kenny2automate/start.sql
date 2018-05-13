CREATE TABLE IF NOT EXISTS ch_channels_occupied (
	-- channel ID
	channel_id integer unsigned NOT NULL
);

CREATE TABLE IF NOT EXISTS gcf_guilds (
	-- guild ID
	guild_id integer unsigned NOT NULL,
	-- channel ID in that guild for global connect4
	channel_id integer unsigned NOT NULL,
	-- role ID to mention for new games
	role_id integer unsigned NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS user_prefixes (
	-- user ID
	user_id integer unsigned NOT NULL,
	-- prefix
	prefix char(1) NOT NULL
);
