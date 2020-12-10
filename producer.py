from kafka import KafkaProducer
from config import config 

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
        try:
            # load connection parameters
            kafka_config = config(section='kafka')
            # create producer instance
            self.producer = KafkaProducer(
                security_protocol = "SSL",
                **kafka_config,
            )
        except (Exception) as error:
            print(error)


    def send (self):
        """
        Create messages and send them to the kafka server 
        """
        for i in range(1, 4):
            message = "message number {}".format(i)
            print("Sending: {}".format(message))
            self.producer.send('routes', message.encode("utf-8"))
        
        # Force sending of all messages        
        self.producer.flush()


producer = Producer()
producer.send()
