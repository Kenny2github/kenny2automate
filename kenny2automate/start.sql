CREATE TABLE IF NOT EXISTS gcf_guilds (
	-- guild ID
	guild_id integer PRIMARY KEY NOT NULL,
	-- channel ID in that guild for global connect4
	channel_id integer unsigned NOT NULL,
	-- role ID to mention for new games
	role_id integer unsigned
);

CREATE TABLE IF NOT EXISTS channels (
	-- channel ID
	channel_id integer PRIMARY KEY NOT NULL,
	-- occupied in crudehangman?
	ch_occupied boolean DEFAULT 0,
	-- language
	lang char(2)
);

CREATE TABLE IF NOT EXISTS users (
	-- user ID
	user_id integer PRIMARY KEY NOT NULL,
	-- language
	lang char(2),
	-- command prefix
	prefix char(1),
	-- fight health
	fight_health integer unsigned,
	-- fight weapon
	fight_weapons text,
	-- fight armor
	fight_armors text,
	-- fight gold
	fight_gold integer unsigned,
	-- fight items, stringified list
	fight_items text
);
