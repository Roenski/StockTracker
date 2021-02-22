import configparser
import psycopg2
from add_trans import Transaction


class Database():

    # filename = .ini file for the database
    # status_func = function, what to print status messages with
    def __init__(self, filename, status_func=print):
        self.conn = None
        self.cur = None
        self.ini_file = filename
        self.status_func = status_func

    def config(self):
        parser = configparser.ConfigParser()
        parser.read(self.ini_file)

        section = 'postgresql'

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, self.ini_file))

        return db

    def insert(self, sql_msg):
        self.cur.execute(sql_msg)
        self.conn.commit()

    def select_all(self, num, offset=0):
        sql_msg = "SELECT * FROM transactions " \
        + "ORDER BY tid ASC LIMIT {} OFFSET {}".format(num, offset)
        self.cur.execute(sql_msg)
        return self.cur.fetchall()

    def delete_entry(self, tid):
        sql_msg = "DELETE FROM transactions WHERE tid={}".format(tid)
        self.cur.execute(sql_msg)
        self.conn.commit()

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
