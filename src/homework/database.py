import json
import psycopg2
from config import config

class Database:
    """! Wrapper for the database connection

    It gives the possibility to connect to the postgresql server and interact with it executing sql commands such as: create and list tables, list table content...
    """

    def __init__(self):
        """! The Database class initializer.

        Load postgresql configuration settings from config file (default host_settings.ini)
        and create a postgresql connection instance.
        """
        # read connection parameters
        pg_config = config(section='postgresql')
        
        # connect to db
        self.conn = psycopg2.connect(**pg_config)
        
        # create a cursor
        self.cur = self.conn.cursor()

    def __del__(self):
        """! The Database class deleter

        Closes the postgresql connection
        """
        self.cur.close()
        self.conn.close()


    def execute_sql(self, sql_string):
        """! The Database execute_sql function.

        It executes a sql command in the database server
        @param sql_string The string containig the command to be executed.
        """
        try:
            # execute the sql
            self.cur.execute( sql_string )
            self.conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print("\nexecute_sql() error:", error)
            self.conn.rollback()


    def create_table(self, table_name):
        """! Creates a table with table_name if not already existing
        
        @param table_name String name of the table to be created
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
        """! Lists tables from database

        @return Result from selecting all available tables
        """
        # create sql command
        s = "SELECT table_schema, table_name FROM information_schema.tables"
        s += " WHERE ( table_schema = 'public' ) ORDER BY table_schema, table_name;"
        return self.get_execute_sql(s)

    def get_table_content(self):
        """! Lists table content

        @return sql result from selecting all table content
        """
        # create sql
        s = "SELECT * from {};".format(self.table_name)
        return self.get_execute_sql(s)

    def get_execute_sql(self, sql_str):
        """! Executes sql command and return result

        @parmam sql_str String containing a verified sql command
        @return Results from sql in postgresql
        """
        # execute command
        self.execute_sql(sql_str)
        # fetch response 
        result = self.cur.fetchall()
        
        return result


    def create_sql_command (self, record_str):
        """! Function that creates the sql command to insert the received verified records
        
        @param record_str The json string of received verified record
        @return The string corresponding to the sql command
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
