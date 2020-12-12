# import libraries
import logging
import unittest

# add homework path to system path
import sys
import os
my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../homework/')

# import own code
from producer import Producer
from consumer import Consumer
from database import Database
from helper_functions import generate_json_message, validate_record_format


class TestHomework(unittest.TestCase):
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
            logging.error("\n\nProducer's connection to"
                        "kafka failed with error: {}\n\n".format(error))
            assert(False)

    def test_consumer(self):
        """
        Test the instanciation and good working of the kafka consumer
        """
        try:
            consumer = Consumer()
            consumer.poll()
        except (Exception) as error:
            logging.error("\n\nConsumer's connection to"
                        "kafka failed with error: {}\n\n".format(error))
            assert(False)

    def test_db_connection(self):
        """
        Test the database connection by retrieving the server version
        """
        try:
            database = Database()
            database.get_server_version()
        except (Exception) as error:
            logging.error("\n\nConnection to postgresql"
                    " failed with error: {}\n\n".format(error))
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
        except (Exception, ValueError) as error:
            print(error)
            assert(False)
        assert(validate_record_format(record_str))

    def test_sql_insertion(self):
        """
        Test that the sql insertion in the database works
        """
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
            for res in result:
                print(res)
            # XXX a better test would be to fetch the
            # last element and compare with the generated one

        except (Exception, ValueError) as error:
            logging.error(error)
            assert(False)


if __name__ == '__main__':
    unittest.main()
