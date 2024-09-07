#!/bin/bash

rm -rf ./env 
python3 -m venv env 
source env/bin/activate
pip install -r requirements.txt 

python manage.py run -h 0.0.0.0


# # in 2nd terminal run the 2 lines below
# python manage.py recreate_db
# python manage.py seed_db
