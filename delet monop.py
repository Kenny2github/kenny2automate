import sqlite3 as sql
dbw = sql.connect('kenny2automate.db')
dbw.execute('DELETE FROM monopolies').execute('UPDATE users SET monopoly_game=NULL')
dbw.executemany('UPDATE users SET games_games=? WHERE user_id=?', (
    (','.join(set(row[0].split(',')) - {'Monopoly'}), row[1])
    for row in dbw.execute("SELECT games_games, user_id FROM users WHERE games_games LIKE '%Monopoly%'").fetchall()
))
dbw.commit()
dbw.close()
