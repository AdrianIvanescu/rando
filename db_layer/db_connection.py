import sqlite3


class DbConnection:
    def __init__(self, db_name):
        self._db_name = db_name

    @property
    def db_name(self):
        return self._db_name

    def open_db_connection(self):
        # connecting to sqlite
        self.conn = sqlite3.connect(f"{self._db_name}.db")

        # creating a cursor object using the cursor() method
        self.cursor = self.conn.cursor()

    def close_db_connection(self):
        # closing the connection
        self.conn.close()

    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print('An exception occured >>', e)

    def commit_db_change(self):
        # commit your changes in the database
        self.conn.commit()
