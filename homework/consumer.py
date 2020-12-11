# import libraries
import psycopg2
from kafka import KafkaConsumer

# import own modules
from config import config
from database import Database
from helper_functions import validate_record_format

class Consumer(Database):
    """
    Wrapper for kafka consumer.
    This wrapper handles creating the instance, closing and sending messages to topic.
    """

    def __init__(self):
        """
        load kafka configuration settings from config file (default host_settings.ini)
        and create a kafka consumer instance
        Then load postgresql configuration settings from config file (default host_settings.ini)
        and create a postgresql connection instance
        Check if the table of interest is in or create it
        """
        # inheritance handling 
        Database.__init__(self)

        self.table_name = "routes_table2"

        try:
            # read kafka connection parameters
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

        # if our table does not exist yet then create it
        self.create_table(self.table_name)


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
                        record_str = msg.value.decode('ascii')
                        print("Received: {}".format(record_str))
                        # check the record's content integrity
                        if validate_record_format(record_str):
                            # generate according sql
                            sql_str = self.create_sql_command(record_str)
                            # execute sql
                            self.execute_sql(sql_str)
                            print("Consumer: record written to database")
                    except (Exception, ValueError) as error:
                        print(error)
                    
        # Commit offsets so we won't get the same messages again        
        self.consumer.commit()


if __name__ == '__main__':
    try:
        consumer = Consumer()
        consumer.poll()
        #print(consumer.get_table_content())
    except (Exception) as error:
        print("\n\nConsumer's connection to kafka failed with error: {}\n\n".format(error))