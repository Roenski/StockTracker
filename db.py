import configparser
import psycopg2


class Database():

    def __init__(self, filename):
        self.conn = None
        self.cur = None
        self.ini_file = filename

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

    def connect(self, status_func):
        try:
            params = self.config()

            status_func('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(**params)

            self.cur = self.conn.cursor()

            status_func("PostgreSQL database version:")
            self.cur.execute("SELECT version()")

            db_version = self.cur.fetchone()
            status_func(str(db_version))
            
            self.cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            status_func(error)
        finally:
            if self.conn is not None:
                self.conn.close()
                status_func('Database connection closed.')