import sqlite3
import pandas as pd

# connection = sqlite3.connect("prod.db")
# cursor =connection.cursor()
# cursor.execute('''create table if not exists users(id integer PRIMARY KEY, winner TEXT, moves_amount INTEGER, position TEXT)''')
# cursor.execute('''create table if not exists game_instance(id integer PRIMARY KEY, '1' TEXT, '2' TEXT, '3' TEXT,  '4' TEXT, '5' TEXT, '6' TEXT, '7' TEXT, '8' TEXT, '9' TEXT)''')

class Connection:
    def __init__(self):
        self.connection = sqlite3.connect("prod.db")
        self.cursor = self.connection.cursor()
if __name__ == "__main__":
    conn=Connection()
    conn.cursor.execute('''CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, login TEXT, password TEXT)''')    