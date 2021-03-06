import configparser
import psycopg2
from table import TransactionTable, StockTable


class Database:

    def __init__(self, name, filename, status_func=print):
        self.conn = None
        self.cur = None
        self.name = name
        self.ini_file = filename
        self.status_func = status_func
        self.transactions = TransactionTable()
        self.stocks = StockTable()

    def insert(self, sql_msg):
        self.connect_db()
        self.cur.execute(sql_msg)
        self.conn.commit()
        self.close()

    def query(self, sql_msg):
        self.connect_db()
        self.cur.execute(sql_msg)
        ans = self.cur.fetchall()
        self.close()
        return ans

    def config(self):
        parser = configparser.ConfigParser()
        parser.read(self.ini_file)

        section = self.name

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, self.ini_file))

        return db

    def connect_db(self):
        try:
            params = self.config()

            self.status_func('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(**params)

            self.cur = self.conn.cursor()

            self.status_func("PostgreSQL database version:")
            self.cur.execute("SELECT version()")

            db_version = self.cur.fetchone()
            self.status_func(str(db_version))
            
        except (Exception, psycopg2.DatabaseError) as error:

            self.status_func(error)

    def close(self):
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.close()
            self.status_func("Database connection closed.")



