#!/bin/bash
echo 'Activating virtual env...'
. /vagrant/venv/bin/activate

echo 'Starting project'
python /vagrant/main.py

echo 'Project running'
