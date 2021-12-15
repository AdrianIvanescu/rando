from colorama.ansi import Fore, Style
from db_layer.db_connection import DbConnection
from db_layer.db_dump import DbDump


class DropTable(DbDump):
    def __init__(self, db_name, table_name):
        self.table_name = table_name
        self.db_conn = DbConnection(db_name)

    def drop_execute(self) -> None:
        sql = f"DROP TABLE IF EXISTS {self.table_name}"
        self.db_conn.open_db_connection()
        self.db_dump_command()
        self.db_conn.execute_sql(sql)
        self.db_conn.close_db_connection()
        print(
            f'''>> The table {Fore.GREEN}{self.table_name}{Style.RESET_ALL} \
was drop successfully...'''
        )