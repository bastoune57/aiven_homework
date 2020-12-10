# import libraries
import unittest
import json

# import own modules
from producer import Producer
from consumer import Consumer
from database import Database
from helper_functions import generate_json_message

class TestAssignement(unittest.TestCase):
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
            database.server_version()
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
            record = generate_json_message()
            validate_record_format(record)
        except (Exception, ValueError) as error:
            print(error)
            

if __name__ == '__main__':
    unittest.main()
