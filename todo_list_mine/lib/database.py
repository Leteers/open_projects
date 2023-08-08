import sqlite3
import pandas as pd
from .encoder import encoder as enc
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
            password=enc.encoding(self.count_users()+1,str(password),"encode")
            self.cursor.execute(f'''INSERT INTO users(login,password) VALUES ('{login}','{password}');''')
            self.connection.commit()
            return(True)
        
    def check_auth(self,login,password):
        self.cursor.execute(f'''SELECT * FROM users WHERE login='{login}'; ''')
        lst=self.cursor.fetchall()
        if lst:
            if password == enc.encoding(self.search_user_id(str(login)),lst[0][2],"decode"):
                return(True)
            else:
                return(False)
        else:
            return(False)
        
    def count_users(self):
        self.cursor.execute('''SELECT COUNT(*) FROM users;''')
        return(self.cursor.fetchall()[0][0])
    
    def search_user_id(self, login):
        self.cursor.execute(f'''SELECT id FROM users WHERE login="{login}";''')
        return(self.cursor.fetchall()[0][0])
    
if __name__ == "__main__":
    conn=Connection()
    conn.cursor.execute('''CREATE TABLE IF NOT EXISTS todos(id integer PRIMARY KEY, user_id INT, content TEXT, status TEXT)''')
    # conn.cursor.execute('''CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, login TEXT, password TEXT);''')    