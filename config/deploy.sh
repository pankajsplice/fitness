#!/usr/bin/env bash

cd /opt/apps/gofit/
git pull origin master
source /home/admin/.virtualenvs/gofit/bin/activate
pip install -r /opt/apps/gofit/requirements.txt
/home/admin/.virtualenvs/gofit/bin/python manage.py migrate --shared
/home/admin/.virtualenvs/gofit/bin/python manage.py collectstatic --noinput
sudo supervisorctl stop gofit
kill $(lsof -t -i:8016)
sudo supervisorctl start gofit
