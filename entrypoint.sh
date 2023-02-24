#!/usr/bin/env sh

python manage.py migrate

python manage.py loaddata dump.json

#gunicorn --bind 0.0.0.0:8000 djangochannels.asgi -w 4 -k uvicorn.workers.UvicornWorker
python manage.py runserver 0:8000
