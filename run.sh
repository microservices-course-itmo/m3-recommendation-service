#!/bin/sh


python ./src/manage.py migrate

python ./src/utils/kafka_consumers.py & \
python ./src/manage.py runserver 0.0.0.0:8000
