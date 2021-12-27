import os
import subprocess
from datetime import datetime

from db_layer.db_connection import DbConnection


class DbDump():
    def __init__(self, db_name):
        self.db_conn = DbConnection(db_name)

    def db_dump_command(self) -> None:
        created_on = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        path = './magic_number_dumps/'
        os.mkdir(path) if not os.path.isdir(path) else None

        subprocess.call(["sqlite3", f"{self.db_conn.db_name}.db",
        f".output {path}{self.db_conn.db_name}_{created_on}.sql", ".dump"])

    def dump_execute(self) -> None:
        self.db_conn.open_db_connection()
        self.db_dump_command()
        self.db_conn.close_db_connection()
