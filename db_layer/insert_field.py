from datetime import datetime

from db_layer.db_connection import DbConnection


class InsertField():
    def __init__(self, db_name, table_name):
        self.table_name = table_name
        self.db_conn = DbConnection(db_name)

    def insert_field(self, source, magic_number, number_of_tries, created_on):
        sql = f"""
        INSERT INTO {self.table_name} (source,magic_number,
        number_of_tries,created_on)
        VALUES ('{source}','{magic_number}','{number_of_tries}','{created_on}')
        """
        self.db_conn.execute_sql(sql)


def save_to_db(number, num_of_tries, source):
    created_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_info = InsertField('magic_number', 'run_times')
    save_info.db_conn.open_db_connection()
    save_info.insert_field(source, number, num_of_tries, created_on)
    save_info.db_conn.commit_db_change()
    save_info.db_conn.close_db_connection()
