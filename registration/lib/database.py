import sqlite3
import pandas as pd

# connection = sqlite3.connect("prod.db")
# cursor =connection.cursor()
# cursor.execute('''create table if not exists users(id integer PRIMARY KEY, winner TEXT, moves_amount INTEGER, position TEXT)''')
# cursor.execute('''create table if not exists game_instance(id integer PRIMARY KEY, '1' TEXT, '2' TEXT, '3' TEXT,  '4' TEXT, '5' TEXT, '6' TEXT, '7' TEXT, '8' TEXT, '9' TEXT)''')

class Connection:
    def __init__(self):
        self.connection = sqlite3.connect("tic_tac_toe.db")
        self.cursor = self.connection.cursor()
    def add_game_to_db(self, winner, moves_amount, position):
        query=f'''INSERT INTO games(winner,moves_amount,position) VALUES ('{winner}',{moves_amount},'{position}')'''
        self.cursor.execute(query)
        self.connection.commit()
    def game_instance(self):
        try:
            query='''SELECT * FROM games WHERE id=(SELECT max(id) FROM games);'''
            self.cursor.execute(query)
            df = pd.DataFrame(self.cursor.fetchall())
            query=f'''INSERT INTO game_instance(id) VALUES ('{df[0][0]}')'''
        except:
            pass
    def add_move(self, position, simbol):
        try:
            query='''SELECT * FROM game_instance WHERE id=(SELECT max(id) FROM game_instance);'''
            self.cursor.execute(query)
            df = pd.DataFrame(self.cursor.fetchall())
            query=f'''UPDATE game_instance SET '{position}'= {simbol} WHERE id = {df[0][0]}'''
        except:
            pass
