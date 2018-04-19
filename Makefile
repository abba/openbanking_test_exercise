PHONY: start_server stop_server test activate_venv

# SHELL := /bin/bash

start_server:
	python3 obtest.py &

stop_server:
	lsof -P | grep ':5000' | awk '{print $$2}' | xargs kill -9 

test: start_server
	pytest -v

# activate_venv:
# 	source venv/bin/activate

