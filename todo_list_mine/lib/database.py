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
    
    def insert_to_do(self,user_id,text,status):
        self.cursor.execute(f'''INSERT INTO todos(user_id,content,status) VALUES ({user_id},"{text}","{status}");''')
        self.connection.commit()

    def get_to_dos(self,user_id):
        self.cursor.execute(f'''SELECT * FROM todos WHERE status <>"closed" and user_id = {user_id};''')
        return(self.cursor.fetchall())
    
    def update_to_do_status_to_close(self,id):
        self.cursor.execute(f'''UPDATE todos SET status="closed" WHERE id={id}''')
        self.connection.commit()
        

    def select_all(self):
        self.cursor.execute('''SELECT count(*) FROM todos;''')
        return(self.cursor.fetchall())
    

if __name__ == "__main__":
    conn=Connection()
    
    conn.cursor.execute('''CREATE TABLE IF NOT EXISTS todos(id integer PRIMARY KEY, user_id INT, content TEXT, status TEXT)''')
    # conn.cursor.execute('''DROP TABLE users;''')
    conn.cursor.execute('''CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, login TEXT, password TEXT, status TEXT);''')    