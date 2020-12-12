'''
this code is an attribution from https://www.postgresqltutorial.com/postgresql-python/connect/
'''
import logging
from configparser import ConfigParser

def config(filename='./res/host_settings.ini', section='postgresql'):
    """! Parses the filename file configuration and loads the section of interest. 

    @param filenane The filename of the configuration file including path from project directory (Default: ./res/host_settings.ini).
    @param section The section to be read from the configuration file (Default: 'postgresql')
    @return The tuple of loaded elements with corresponding key values as in configuration file
    """

    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

if __name__ == '__main__':
    try:
        db = config(section='kafka')
    except(Exception) as error:
        logging.error(error)
        
