ALTER TABLE users ADD COLUMN evol_self pickle;

CREATE TABLE evol_unnamed_children (
  -- entry ID, autoincrement to avoid reusing deleted row IDs
  entry_id integer PRIMARY KEY AUTOINCREMENT,
  -- child
  child pickle
);
