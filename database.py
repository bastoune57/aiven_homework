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

        try:
            # read connection parameters
            pg_config = config(section='postgresql')
    
            # connect to db
            conn = psycopg2.connect(**pg_config)
       
            # create a cursor
            cur = conn.cursor()
    
            # execute a statement
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')
    
            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            print(db_version)
    
            # close the communication with the PostgreSQL
            cur.close()
    
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

db = Database()
