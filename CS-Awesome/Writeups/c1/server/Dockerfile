FROM python:3.9-buster

WORKDIR /app
RUN pip install flask gunicorn
ADD . /app

CMD gunicorn --bind 0.0.0.0:80 -w 8 main:app
