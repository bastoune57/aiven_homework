.PHONY: init create_venv install_pkg_homework install_venv upgrade_venv start_producer start_consumer start_database start_homework

## declare variable name
path_to_venv=./venv
python_version=python3
homework_path=src/homework
tests_path=src/tests

## declare commands

install_venv:
	pip3 install virtualenv

create_venv:
	python3 -m venv $(path_to_venv)

upgrade_venv:
	$(path_to_venv)/bin/pip install -r requirements.txt

install_pkg_homework:
	$(path_to_venv)/bin/$(python_version) setup.py install

init: create_venv install_venv upgrade_venv

start_producer:
	$(path_to_venv)/bin/$(python_version) $(homework_path)/producer.py

start_consumer:
	$(path_to_venv)/bin/$(python_version) $(homework_path)/consumer.py

start_database:
	$(path_to_venv)/bin/$(python_version) $(homework_path)/database.py

run_homework: start_producer start_consumer

run_all_tests: 
	$(path_to_venv)/bin/$(python_version) -m unittest -v $(tests_path)/test.py
