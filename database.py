import psycopg2
from config import config

class Database:
    """
    Wrapper for the database connection
    It will create a connection to the DB and write to it
    """

    def __init__(self):
        """
        load postgresql configuration settings from config file (default host_settings.ini)
        and create a postgresql connection instance 
        """
        # read connection parameters
        pg_config = config(section='postgresql')
        
        # connect to db
        self.conn = psycopg2.connect(**pg_config)


    def server_version(self):
        """
        get server version from postgresql
        """
        # create a cursor
        cur = self.conn.cursor()
        
        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
        
        # close the communication with the PostgreSQL
        cur.close()

if __name__ == '__main__':
    try:
        db = Database()
        db.server_version()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
