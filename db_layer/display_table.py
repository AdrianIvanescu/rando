from db_layer.db_connection import DbConnection


class DisplayTable():
    def __init__(self, db_name, table_name):
        self.table_name = table_name
        self.db_conn = DbConnection(db_name)

    def show_table(self):
        # create table as per requirement
        sql = f"""
        select * from {self.table_name}
        """
        self.db_conn.open_db_connection()
        self.db_conn.execute_sql(sql)
        self.print_table(sql)
        self.db_conn.cursor.description
        self.db_conn.close_db_connection

    def print_table(self, sql):
        rows = self.db_conn.cursor.fetchall()
        dash = '-' * 62
        print(dash)
        headers = ['ID', 'SOURCE', 'NUMBER', 'TRIES#', 'CREATED_ON']
        for header in headers:
            print(f'{header:10}', end=" ")
        print(f'\n{dash}')
        for row in rows:
            print(f'{row[0]}\t   {row[1]:10}\t{row[2]}\t {row[3]}\t  {row[4]}')
        print(dash)
