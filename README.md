# Aiven Recruiting Homework
In the recruiting process for Aiven, a homework is given. This repository is the source code for the assignment. 

## Prerequisite

The project is written in Python3 using pip and virtual environment. Here are links to help with their installation:
* **pip:** https://pip.pypa.io/en/stable/installing/
* **virtualenv:** https://virtualenv.pypa.io/en/stable/installation.html

To be able to connect to the Aiven servers you need to create a "res" folder in the source directory with the required files as follow:
```
+-- _res
|   +-- host_settings.ini
|   +-- _ssl
|   |	+-- ca.pem
|   |	+-- service.key
|   |	+-- service.cert
```

In total there are 4 files: 
* host\_settings.ini
* ca.pem
* service.cert
* service.key

In order to obtain these files please contact the project manager at bastien.hamet@gmail.com.

## installation

Once downloaded from git you can prepare the project using:
```bash
make init
```

## Code structure 
Folder architecture is as follow:

```
.
+-- _src
|   +-- _homework
|   |      +-- __init__.py
|   |      +-- config.py
|   |      +-- consumer.py
|   |      +-- database.py
|   |      +-- helper_functions.py
|   |      +-- producer.py
|   +-- _tests
|   |      +-- test.py
+-- _res
|   +-- host_settings.ini
|   +-- _ssl
|   |	+-- ca.pem
|   |	+-- service.key
|   |	+-- service.cert
+-- doxy_config
+-- LICENSE
+-- Makefile
+-- README.md
+-- requirements.txt
+-- setup.py
```
The source code is mainly located in the **homework** package and it contains:
* **config.py:** a module that reads .ini files using the **configParser**
* **consumer.py:** a class that handles reading records from a kafka server and storing it after validation in a PostgreSQL server.
* **database.py:** a class that handles interaction with the PostgreSQL server.
* **producer.py:** a class that handles creating and sending records to the kafka server.
* **helper\_functions.py:** functions used from all project parts like validation functions and generating JSON strings from records. Ideally it should move to a utils library.

## Homework Functionality

The project will have a kafka producer (producer.py) and a consumer (consumer.py) that will interact with a kafka server and a postgreSQL database that are both hosted by Aiven. 
The homework producer sends some randomly JSON generated records to the kafka server. 
Those are then polled by the homework consumer, validated and writen in the PostgreSQL database. 

A record is composed of:
* userID: as an integer value
* timestamp: as a float value
* coordinates: as a list of 2 values:
	* latitude: as a float value going from -90° to 90°
 	* longitude: as a float value going from -180° to 180°

In PostgreSQL the database is called **routes** and the table **routes\_table**. 

## Usage
Start the homework using:
```bash
make run_homework
```

Start the test ptocedures using:
```bash
make run_tests
```

## Documentation
Documentation is generated with Doxygen. 

To install Doxygen on Ubuntu:
```bash
sudo apt install doxygen graphviz
```

To generate the documentation:
```bash
make docs
```

Use your browser to load the generated index.html from the generated folder: ./docs/html/index.html


## Third party software

The homework is made using several already existing libraries which are:
* **json:** used as a decoder and encoder for JSON format (https://docs.python.org/3/library/json.html)
* **kafka:** used as kafka adapter for Python (https://pypi.org/project/kafka-python/)
* **psycopg2:** used as a PostgreSQL adapter for Python (https://pypi.org/project/psycopg2/)
* **logging:** used for non application outcome console output 
* **configParser:** used to read and parse configuration files
* **random:** used to generate random numbers 
* **datetime:** used to work with timestamps 

## Attributions

The following attributions were made:
* **Aiven article:** Producer and consumer classes are inspired from the Aiven article on getting started with Aiven kafka (https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka)
* **PostgreSQL tutorial:** Config module to connect parse configuration files is taken from (https://www.postgresqltutorial.com/postgresql-python/connect/) 

## Project next steps
In order to continue working with this project the next steps would be to:
* **Continous integration:** Update to the git with a runner that automatically builds and test the code, update the docs...
* **Make a utils library:** Move all modules that are used from the different classes to a utils library.
* **Improve integration testing:** Running a test with the full homework application and compare the generated records from the producer to the written data in the PostgreSQL database.
* **Continuous application**: Update the application to run continuously until it is stopped. 
* **Up-scaling**: Increase the amount of consumers, producers, types of messages, tables etc...

## Licenses
See LICENSE file

