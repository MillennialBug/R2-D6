import sqlite3

conn = sqlite3.connect('swrpg.db')
cur = conn.cursor()


def get_id(table, column, param):
    cur.execute(f'SELECT id from {table} WHERE {column}=?', (param,))
    t_id = cur.fetchone()
    if t_id is None:
        return None
    else:
        return int(t_id[0])


def get_next_id(table):
    cur.execute(f'SELECT MAX(id) FROM {table}')
    max_id = cur.fetchone()
    if max_id[0] is None:
        return 1
    else:
        return int(max_id[0]) + 1


def table_insert(table, values):
    try:
        cur.execute(f'INSERT INTO {table} VALUES {values};')
        conn.commit()
        return True
    except sqlite3.Error:
        return False


def set_active_char(char, user, guild):
    cur.execute('SELECT id FROM active_chars '
                'WHERE user_id=? AND guild_id=?', (user, guild))
    ac = cur.fetchone()

    if ac is not None:
        cur.execute('DELETE FROM active_chars WHERE id=?', ac[0])

    cur.execute('INSERT INTO active_chars (user_id, guild_id, char_id) VALUES (?, ?, ?)',
                (user, guild, char))
    conn.commit()
