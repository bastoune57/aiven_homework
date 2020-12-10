# import libraries
import psycopg2
from kafka import KafkaConsumer

# import own modules
from config import config
from database import Database

class Consumer():
    """
    Wrapper for kafka consumer.
    This wrapper handles creating the instance, closing and sending messages to topic.
    """

    def __init__(self):
        """
        load kafka configuration settings from config file (default host_settings.ini)
        and create a kafka consumer instance
        """
        try:
            # read connection parameters
            kafka_config = config(section='kafka')
            # create producer instance
            self.consumer = KafkaConsumer(
                'routes',
                auto_offset_reset="earliest",
                client_id="demo-client-1",
                group_id="demo-group",
                security_protocol = "SSL",
                **kafka_config,
            )
        except (Exception) as error:
            print(error)


    def poll(self):
        """
        Poll records from the kafka server
        """

        # Call poll twice. First call will just assign partitions for our
        # consumer without actually returning anything
        for _ in range(2):
            raw_msgs = self.consumer.poll(timeout_ms=1000)
            for tp, msgs in raw_msgs.items():
                for msg in msgs:
                    try:
                        # here is the per message processing
                        validate_record_format()
                        print("Received: {}".format(msg.value))
                    except (Exception, ValueError) as error:
                        print(error)
                    #else:
                        # XXX save to db
                    
        # Commit offsets so we won't get the same messages again        
        self.consumer.commit()


if __name__ == '__main__':
    try:
        consumer = Consumer()
        consumer.poll()
    except (Exception) as error:
        print("\n\nConsumer's connection to kafka failed with error: {}\n\n".format(error))
