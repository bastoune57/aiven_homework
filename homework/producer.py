# import libraries
from kafka import KafkaProducer

# import own modules
from homework.config import config 
from homework.helper_functions import generate_json_message

class Producer:
    """
    Wrapper for kafka producer.
    This wrapper handles creating the instance, closing and sending messages to topic.
    """

    def __init__ (self):
        """
        load kafka configuration settings from config file (default host_settings.ini)
        and create a kafka producer instance 
        """
        # load connection parameters
        kafka_config = config(section='kafka')
        # create producer instance
        self.connection = KafkaProducer(
            security_protocol = "SSL",
            **kafka_config,
        )



    def send (self):
        """
        Create messages and send them to the kafka server 
        """
        # first check connection was succesful
        for i in range(1, 4):
            message = generate_json_message(i)
            print("Sending: {}".format(message))
            self.connection.send('routes', message.encode("utf-8"))
        
        # Force sending of all messages        
        self.connection.flush()


if __name__ == '__main__':
    try:
        producer = Producer()
        producer.send()
    except (Exception) as error:
        print("\n\nProducer's connection to kafka failed with error: {}\n\n".format(error))
