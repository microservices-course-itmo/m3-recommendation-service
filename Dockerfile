FROM python:3.8

ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
# RUN pip install requests
# RUN python src/download_data.py
EXPOSE 8000

# ENTRYPOINT bash -c 'ls /code/ml'

ENTRYPOINT bash -c "python src/download_data.py && python src/manage.py migrate && python src/manage.py makemigrations && python src/manage.py collect static && python src/manage.py runserver 0.0.0.0:8000 && nohup python src/utils/kafka_consumers &"
