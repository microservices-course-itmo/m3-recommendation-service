FROM python:3

ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
EXPOSE 8000
# RUN ls
ENTRYPOINT bash -c "python src/manage.py migrate && python src/manage.py makemigrations && python src/manage.py runserver 0.0.0.0:8000"
