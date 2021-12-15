from colorama.ansi import Fore
from colorama.ansi import Style

from db_layer.db_connection import DbConnection


class CreateTable():
    def __init__(self, db_name, table_name):
        self.table_name = table_name
        self.db_conn = DbConnection(db_name)

    def create_table(self):
        # create table as per requirement
        sql = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name}(
        row_id INTEGER PRIMARY KEY AUTOINCREMENT,
        source CHAR(10) NOT NULL,
        magic_number INT(3) NOT NULL,
        number_of_tries INT(2) NOT NULL,
        created_on text
        );
        """
        self.db_conn.open_db_connection()
        self.db_conn.execute_sql(sql)
        self.db_conn.commit_db_change()
        self.db_conn.close_db_connection
        print(
            f'''>> The table {Fore.GREEN}{self.table_name}{Style.RESET_ALL} \
created successfully...'''
        )
