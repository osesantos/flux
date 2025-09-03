#!/bin/bash

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

export PYTHONPATH="${PYTHONPATH}:/home/osesantos/git/flux/src"

uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
