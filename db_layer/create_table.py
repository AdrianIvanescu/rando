from colorama.ansi import Fore
from colorama.ansi import Style

from db_layer.db_connection import DbConnection


class MagicTable(DbConnection):
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name

    def commit_db_change(self):
        # commit your changes in the database
        self.conn.commit()

    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print('An exception occured >>', e)

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
        self.execute_sql(sql)
        print(
            f'''>> The table {Fore.GREEN}{self.table_name}{Style.RESET_ALL} \
created successfully...'''
        )

    def drop_table(self):
        # drop table if already exists.
        sql = f"DROP TABLE IF EXISTS {self.table_name}"
        self.execute_sql(sql)
        print(
            f'''>> The table {Fore.GREEN}{self.table_name}{Style.RESET_ALL} \
was drop successfully...'''
        )
