.PHONY: init create_venv install_pkg_homework install_venv upgrade_venv start_producer start_consumer start_database start_homework

## declare variable name
path_to_venv=./venv
python_version=python3
pkg_name=homework

## declare commands

install_venv:
	pip3 install virtualenv

create_venv:
	python3 -m venv $(path_to_venv)

upgrade_venv:
	$(path_to_venv)/bin/pip install -r requirements.txt

install_pkg_homework:
	python setup.py install

init: create_venv install_venv upgrade_venv install_pkg_homework

start_producer:
	$(path_to_venv)/bin/$(python_version) $(pkg_name)/producer.py

start_consumer:
	$(path_to_venv)/bin/$(python_version) $(pkg_name)/consumer.py

start_database:
	$(path_to_venv)/bin/$(python_version) $(pkg_name)/database.py

run_homework: start_producer start_consumer

run_all_tests: 
	python -m unittest -v tests/test.py
