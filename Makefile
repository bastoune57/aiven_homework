.PHONY: init docs create_venv install_pkg_homework upgrade_venv start_producer start_consumer start_database start_homework

## declare variable name
path_to_venv=./venv
python_version=python3
homework_path=src/homework
tests_path=src/tests

########
# useful commands to prepare the project
########

# create virtual environment
create_venv:
	python3 -m venv $(path_to_venv)

# install pip requirement to venv
upgrade_venv:
	$(path_to_venv)/bin/pip install -r requirements.txt

# create and install pip package from project
install_pkg_homework:
	$(path_to_venv)/bin/$(python_version) setup.py install

# prepare the project after downloading from git
init: create_venv upgrade_venv

########
# Some helpers function for development
#######

# start the producer script
start_producer:
	$(path_to_venv)/bin/$(python_version) $(homework_path)/producer.py

# start the producer script
start_consumer:
	$(path_to_venv)/bin/$(python_version) $(homework_path)/consumer.py

start_database:
	$(path_to_venv)/bin/$(python_version) $(homework_path)/database.py

########
# Run command for the application or for tests
########

run_homework: start_producer start_consumer

run_tests: 
	$(path_to_venv)/bin/$(python_version) -m unittest -v $(tests_path)/test.py

########
# Others 
########

# create doc with doxygen
docs:
	$(path_to_venv)/bin/doxygen doxy_config

########
# Commands to run some of the tests individually 
########

test_database:
	$(path_to_venv)/bin/$(python_version) $(tests_path)/test.py TestHomework.test_db_connection

test_consumer:
	$(path_to_venv)/bin/$(python_version) $(tests_path)/test.py TestHomework.test_consumer

test_producer:
	$(path_to_venv)/bin/$(python_version) $(tests_path)/test.py TestHomework.test_producer

