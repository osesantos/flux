#!/bin/bash

set -e

echo "Starting the application..."

python3 -m venv venv
source venv/bin/activate

echo "Installing dependencies..."

pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt > /dev/null 2>&1

export PYTHONPATH="${PYTHONPATH}:/home/osesantos/git/flux/src"

echo "Running the application..."

uvicorn src.main:app --reload --host 0.0.0.0 --port 5544
