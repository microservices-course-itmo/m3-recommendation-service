FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY requirements.txt ./
COPY src/download_data.py ./src/

RUN pip install -r requirements.txt

RUN mkdir ./ml && python ./src/download_data.py

COPY . .

RUN python ./src/manage.py collectstatic --noinput

EXPOSE 8080

CMD [ "./run.sh" ]
