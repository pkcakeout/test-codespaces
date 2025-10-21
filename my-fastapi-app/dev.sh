#!/bin/bash

pipenv install -r requirements.txt

pipenv run bash -c 'cd src ; uvicorn main:app --reload --host 0.0.0.0 --port 8000'
