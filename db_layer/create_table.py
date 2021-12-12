import sqlite3
from sqlite3.dbapi2 import SQLITE_FUNCTION, Error

from colorama.ansi import Fore, Style

class MagicTable:
    def __init__(self,db_name,table_name):
        self.db_name = db_name
        self.table_name = table_name
    
    def open_db_connection(self):
        # connecting to sqlite
        self.conn = sqlite3.connect(f"{self.db_name}.db")
        
        # creating a cursor object using the cursor() method
        self.cursor = self.conn.cursor()

    def commit_db_change(self):
        # commit your changes in the database
        self.conn.commit()

    def close_db_connection(self):
        # closing the connection
        self.conn.close()

    def execute_sql(self,sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print ('An exception occured', e)

    def create_table(self):
        # create table as per requirement
        sql = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name}(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source CHAR(10) NOT NULL,
        magic_number INT(3) NOT NULL,
        was_guess INT(1),
        initial_guess INT(30) NOT NULL,
        number_of_tries INT(2) NOT NULL
        )
        """
        self.execute_sql(sql)
        print(
            f">> The table {Fore.GREEN}{self.table_name}{Style.RESET_ALL} created successfully..."
        )

    def drop_table(self):
        # drop table if already exists.
        sql = f"DROP TABLE IF EXISTS {self.table_name}"
        self.execute_sql(sql)
        print(
            f">> The table {Fore.GREEN}{self.table_name}{Style.RESET_ALL} was drop successfully..."
        )