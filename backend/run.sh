#!/bin/bash

rm -rf ./env 
python3 -m venv env 
source env/bin/activate
pip install -r requirements.txt 

python manage.py run -h 0.0.0.0
