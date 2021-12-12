import sqlite3

class DbConnection():
    def __init__(self,db_name):
        self.db_name = db_name

    def open_db_connection(self):
        # connecting to sqlite
        self.conn = sqlite3.connect(f"{self.db_name}.db")
        
        # creating a cursor object using the cursor() method
        self.cursor = self.conn.cursor()

    def close_db_connection(self):
        # closing the connection
        self.conn.close()