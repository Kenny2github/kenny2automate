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
)
