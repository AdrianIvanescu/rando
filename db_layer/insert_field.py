from datetime import datetime

from db_layer.create_table import MagicTable


class InsertField(MagicTable):
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name

    def insert_field(self, source, magic_number, number_of_tries, created_on):
        sql = f"""
        INSERT INTO {self.table_name} (source,magic_number,
        number_of_tries,created_on)
        VALUES ('{source}','{magic_number}','{number_of_tries}','{created_on}')
        """
        self.execute_sql(sql)


def save_to_db(number, num_of_tries, source):
    created_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_info = InsertField('magic_number', 'run_times')
    save_info.open_db_connection()
    save_info.insert_field(source, number, num_of_tries, created_on)
    save_info.commit_db_change()
    save_info.close_db_connection()
