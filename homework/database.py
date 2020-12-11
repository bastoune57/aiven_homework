import json
import psycopg2
from homework.config import config

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
        
        # create a cursor
        self.cur = self.conn.cursor()

    def __del__(self):
        """
        delete postgresql connection instance 
        """
        self.cur.close()
        self.conn.close()


    def execute_sql(self, sql_string):
        """
        excecute a sql command
        """
        try:
            # execute the sql
            self.cur.execute( sql_string )
            self.conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print("\nexecute_sql() error:", error)
            self.conn.rollback()


    def create_table(self, table_name):
        """
        Create a table with our settings with given name
        
        :param table_name: string name of the table to be created
        """
        # create sql command
        s = 'CREATE TABLE IF NOT EXISTS {} ('.format(table_name)
        s += " user_id INT NOT NULL, "
        s += " timestamp DOUBLE PRECISION NOT NULL, "
        s += " latitude DOUBLE PRECISION NOT NULL,"
        s += " longitude DOUBLE PRECISION NOT NULL);"
        # execute command
        self.execute_sql(s)
        print("table initialised")


    def list_tables(self):
        """
        list tables from database

        :return result from selecting all available tables
        """
        # create sql command
        s = "SELECT table_schema, table_name FROM information_schema.tables"
        s += " WHERE ( table_schema = 'public' ) ORDER BY table_schema, table_name;"
        return self.get_execute_sql(s)

    def get_table_content(self):
        """
        list table content

        :return sql result from selecting all table content
        """
        # create sql
        s = "SELECT * from {};".format(self.table_name)
        return self.get_execute_sql(s)

    def get_execute_sql(self, sql_str):
        """
        execute sql and return results

        :parmam sql_str: str containing a verified sql command
        :return results: results from sql in postgresql
        """
        # execute command
        self.execute_sql(sql_str)
        # fetch response 
        result = self.cur.fetchall()
        
        return result


    def create_sql_command (self, record_str):
        """
        function that creates the sql command to insert the received verified records
        
        :param record_str: the json string of received verified record
        :return sql_str: the string corresponding to the sql command
        """
        record = json.loads(record_str)
        sql_string = 'INSERT INTO {} '.format( self.table_name )
        sql_string += "( user_id, timestamp, latitude, longitude )\nVALUES ("
        sql_string += "{}, {}, {}, {});".format(record['userId'], record['timestamp'],record['coordinates'][0], record['coordinates'][1])
        
        return sql_string


    def get_server_version(self):
        """
        get server version from postgresql
        """
        # execute a statement
        print('PostgreSQL database version:')
        self.cur.execute('SELECT version()')
        
        # display the PostgreSQL database server version
        db_version = self.cur.fetchone()
        print(db_version)
        

if __name__ == '__main__':
    try:
        db = Database()
        #db.create_table("routes_table")
        print(db.list_tables())
        db.get_server_version()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
