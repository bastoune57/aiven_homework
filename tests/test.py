# import libraries
import unittest
import json

# import own modules
from homework.producer import Producer
from homework.consumer import Consumer
from homework.database import Database
from homework.helper_functions import generate_json_message, validate_record_format

class TestAssignment(unittest.TestCase):
    """
    class that will handle testing of the producer
    """
    
    def test_producer(self):
        """
        Test the instanciation and good working of the kafka producer
        """
        try:
            producer = Producer()
            producer.send()
        except (Exception) as error:
            print("\n\nProducer's connection to kafka failed with error: {}\n\n".format(error))
            assert(False)
    
    
    def test_consumer(self):
        """
        Test the instanciation and good working of the kafka consumer
        """
        try:
            consumer = Consumer()
            consumer.poll()
        except (Exception) as error:
            print("\n\nConsumer's connection to kafka failed with error: {}\n\n".format(error))
            assert(False)

    def test_db_connection(self):
        """
        Test the database connection by retrieving the server version
        """
        try:
            database = Database()
            database.get_server_version()
        except (Exception) as error:
            print("\n\nConnection to postgresql failed with error: {}\n\n".format(error))
            assert(False)

    def test_msg_generation(self):
        """
        Test that the function generating the message returns a json with 
        userId as a positive integer
        datestamp as float
        coordinates as tuple of float
        """
        try:
            record_str = generate_json_message()
            validate_record_format(record_str)
        except (Exception, ValueError) as error:
            print(error)
            assert(False)
            
    def test_sql_insertion(self):
        """
        Test that the sql insertion in the database works
        """
        #create a valid record
        try:
            # generate record as from kafka server
            record_str = generate_json_message()
            # create corresponding sql
            consumer = Consumer()
            sql_str = consumer.create_sql_command(record_str)
            # print SQL
            print(sql_str)
            # execute in db
            result = consumer.execute_sql(sql_str)
            # print all from table
            result = consumer.get_table_content()
            print(result)
            # XXX a better test would be to fetch the last element and compare with the generated one

        except (Exception, ValueError) as error:
            print(error)
            assert(False)

if __name__ == '__main__':
    unittest.main()
