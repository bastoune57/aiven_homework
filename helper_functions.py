import json
import random
from datetime import datetime

def generate_json_message(userId=-1):
    """
    function that generate a json string with user id, datestamp and random coordinates information

    :param userID: indicates the userID (if not given, or a negative value, a random number between 0 and 9 will be chosen)
    :return json_str: a json formatted string with the ser id, datestamp and random coordinates information 
    """

    # get userID -> random (in range [0;9]) if not given
    if userId < 0:
        userId = random.randint(0,9)

    # get timestamp
    timestamp = datetime.timestamp(datetime.now())

    # get random latitute (in range [-90;+90]°) and longitude (in range [-180;+180]°) for positionning
    latitude = random.random() * 180 - 90
    longitude = (random.random() * 180 - 90) * 2
    
    # generate json string
    json_str = json.dumps({'timestamp': timestamp, 'userId':userId, 'coordinates':[latitude, longitude]})

    return json_str



def validate_record_format(record):
    """
    function that validates the format of the messages read from the kafka server and to be pushed to the postgresql db

    :param record: string of json format to be checked
    :return boolean of validity 
    """
    try:
        data = json.loads(record)
    except(ValueError) as error:
        raise Exception("The record is not from JSON format: {}".format(record))
        return False

    try:
        validate_userId (data)
        validate_timestamp (data)
        validate_coordinates (data)
    except(Exception) as error:
        print(error)
        return False
    
    return True



def validate_userId (record):
    """
    function that get the json decoded record to verify the userId content
    
    :param record: decoded json record
    """
    # check timestamp is in the record
    if 'userId' not in record:
        raise Exception ('userId missing from JSON string')

    userId = record['userId']
    
    # check timestamp is a float
    if not isinstance(userId, int):
        raise Exception ('userId invalid type {} (should be an integer)'.format(type(userId)))

    # check timestamp is >0
    if userId < 0: 
        raise Exception ('userId invalid value {} (should be a positive value)'.format(userId))



def validate_timestamp (record):
    """
    function that get the json decoded record to verify the timestamp content
    
    :param record: decoded json record
    """
    # check timestamp is in the record
    if 'timestamp' not in record:
        raise Exception ('timestamp missing from JSON string')

    timestamp = record['timestamp']
    
    # check timestamp is a float
    if not isinstance(timestamp, float):
        raise Exception ('timestamp invalid type {} (should be a float)'.format(type(timestamp)))

    # check timestamp is >0
    if timestamp < 0: 
        raise Exception ('timestamp invalid value {} (should be a positive value)'.format(timestamp))


def validate_coordinates (record):
    """
    function that get the json decoded record to verify the coordinates content

    :param record: decoded json record
    """

    # check coordinates is in the record
    if 'coordinates' not in record:
        raise Exception ('coordinates missing from JSON string')

    # check coordinates is a tuple
    if not isinstance(record['coordinates'], list):
        raise Exception ('coordinates invalid type {} (should be a list)'.format(type(record['coordinates'])))
    
    # check there are exactly 2 coordinates
    if len(record['coordinates']) != 2:
        raise Exception ('coordinates invalid length {} (should be a 2)'.format(len(record['coordinates'])))
    
    # get latitude
    latitude=record['coordinates'][0]

    # check latitude is a float
    if not isinstance(latitude, float):
        raise Exception ('latitude invalid type {} (should be a float)'.format(type(latitude)))
    
    # check that latitude value is between -90 and 90
    if latitude < -90 or latitude > 90:
        raise Exception ("Coordinate latitude is out of range: {} (should be between -90 and 90)".format(latitude))

    # get longitude
    longitude=record['coordinates'][1]

    # check latitude is a float
    if not isinstance(longitude, float):
        raise Exception ('longitude invalid type {} (should be a float)'.format(type(longitude)))
    
    # check that latitude value is between -90 and 90
    if longitude < -180 or longitude > 180:
        raise Exception ("Coordinate longitude is out of range: {} (should be between -180 and 180)".format(longitude))

    

if __name__ == '__main__':
    try:
        record = generate_json_message()
        validate_record_format(record)
        create_sql_command(record, 'routes_table1')
    except (Exception, ValueError) as error:
        print(error)

