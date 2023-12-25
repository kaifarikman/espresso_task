import sqlite3


def get_connection():
    conn = sqlite3.connect('coffee.sqlite')
    return conn


def start_session():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS coffee( 
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        degree_of_roasting TEXT NOT NULL,
        type TEXT NOT NULL,
        about TEXT NOT NULL,
        price INTEGER NOT NULL,
        volume INTEGER NOT NULL
        )''')
        conn.commit()


def get_all_coffee():
    with get_connection() as conn:
        cur = conn.cursor()
        coffee_list = cur.execute('SELECT * FROM coffee').fetchall()
        return coffee_list


def get_coffee_by_name(name_):
    with get_connection() as conn:
        cur = conn.cursor()
        coffee_list = cur.execute('SELECT * FROM coffee WHERE name=?', (name_,))
        return coffee_list


def add_coffee(data_):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            '''INSERT INTO coffee (name, degree_of_roasting, type, about, price, volume)
             VALUES (?,?,?,?,?,?)''',
            data_
        )
        conn.commit()


def edit_coffee(id_, data_):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            f'''UPDATE coffee SET name=?, degree_of_roasting=?, type=?, about=?, price=?, volume=?
            WHERE id={id_}''', data_[1:]
        )
        conn.commit()
