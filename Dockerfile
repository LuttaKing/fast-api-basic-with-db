FROM python:3.10.7

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt