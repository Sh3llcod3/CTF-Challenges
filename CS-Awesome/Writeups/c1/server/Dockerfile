# This is a basic DockerFile, change and secure it as you see fit.
# You could also just get Flask & Gunicorn and deploy this on bare metal.
FROM python:3.9-buster

WORKDIR /app
RUN pip install flask gunicorn
ADD . /app

CMD gunicorn --bind 0.0.0.0:80 -w 8 main:app
