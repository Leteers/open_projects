import sqlite3
import pandas as pd

class Connection:
    def __init__(self):
        self.connection = sqlite3.connect("prod.db")
        self.cursor = self.connection.cursor()
    def create_user(self,login, password):
        self.cursor.execute(f'''SELECT * FROM users WHERE login='{login}'; ''')
        lst=self.cursor.fetchall()
        if lst:
            return('userexists')
        elif len(password) < 7 :
            return('plen')
        else:
            self.cursor.execute(f'''INSERT INTO users(login,password) VALUES ('{login}','{password}');''')
            self.connection.commit()
            return(True)
        
    def check_auth(self,login,password):
        self.cursor.execute(f'''SELECT * FROM users WHERE login='{login}'; ''')
        lst=self.cursor.fetchall()
        if lst:
            if password == lst[0][2]:
                return(True)
            else:
                return(False)
        else:
            return(False)
if __name__ == "__main__":
    conn=Connection()
    conn.cursor.execute('''CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, login TEXT, password TEXT);''')    