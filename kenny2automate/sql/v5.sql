CREATE TABLE IF NOT EXISTS monopolies (
  -- identifier based on time
  game_id integer PRIMARY KEY NOT NULL,
  -- player idx whose turn it is
  whose_turn integer NOT NULL,
  -- player info
  players pickle NOT NULL,
  -- property info
  properties pickle NOT NULL
);

ALTER TABLE users ADD COLUMN monopoly_game text;
