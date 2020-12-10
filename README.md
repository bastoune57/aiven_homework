# Aiven Homework
In the recruiting process for Aiven, a homework is given. This repository is the source code for the assignment. 

## installation
The project is written in Python3 and pip environment is required. (install pip following https://pip.pypa.io/en/stable/installing/). It is recommended to create a virtual environment (https://docs.python.org/3/tutorial/venv.html).
Then load the pip configuration:
```bash
pip3 install -r requirements.txt
```

## usage
The project will have a kafka producer (producer.py) and a consumer (consumer.py) that will interact with a kafka server and a postgresql database that are both hosted by Aiven. 

Starting the producer will send 3 records to the kafka server
```bash
python3 producer.py
```

Starting the consumer will read available records from the kafka server then push it to a postgresql database
```bash
python3 consumer.py
```

## Licenses
* [GNU] https://www.psycopg.org/docs/license.html
* [Kafka] Apache License, v2.0. 

### Assignment
Software Engineer in Support
This exercise is meant as a recruiting homework for candidate’s applying for a technical position within Aiven. As Aiven is a Database As a Service vendor which takes great pride in the easy setup of our services, we’d like to see a homework regarding the use of our services in a demo application. This will help familiarize the applicant with our offered technology stack and help us evaluate the candidate’s proficiency in using the services Aiven offers.

#### Exercise

The exercise should be relatively fast to complete. You can spend as much time as you want to. If all this is very routine stuff for you, this should not take more than a few hours. If there are many new things, a few evenings should already be enough time.
As part of the demo application you must be able to send events to a Kafka topic (a producer) which will then be read by a Kafka consumer application that you’ve written.

The consumer application must then store the consumed data to an Aiven PostgreSQL database.
Even though this is a small concept program, returned homework should include tests and proper packaging. If your tests require Kafka and PostgreSQL services, for simplicity your tests can assume those are already running, instead of integrating Aiven service creation and deleting.

To complete the homework please register to Aiven at https://console.aiven.io/signup.html at which point you’ll automatically be given $300 worth of credits to play around with. This should be enough for a few hours use of our services. If you need more credits to complete your homework, please contact us.

We accept homework exercises written in Python, Go, Java and Node.JS. Aiven predominantly uses Python itself, so we give out bonus points for candidates completing the homework in Python.
Automatic tests for the application are not mandatory, but again we’d like to see at least a description of how the application could be tested.

#### Submission 

The completed homework should be stored in a git repository on GitHub for easy access, please return the link to the exercise repository via email.
Besides the source code, the Git repository should also contain a README file describing how the application can be compiled/run/tested.

#### Criteria for evaluation 
* Code formatting and clarity. We value readable code written for other developers, not for a tutorial, or as one-off hack.
* We appreciate demonstrating your experience and knowledge, but also utilizing existing libraries. There is no need to re-invent the wheel.
* Practicality of testing. 100% test coverage may not be practical, and also having 100% coverage but having no test validation is not very useful.
* Attribution. If you take code from Google results, examples etc., add attributions. We all know new things are often written based on search results.
* “Open source ready” repository. It’s very often a good idea to pretend the homework assignment in Github is used by random people (in practice, if you want to, you can delete/hide the repository as soon as we have seen it).
