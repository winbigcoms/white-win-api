FROM python:3.6.8

WORKDIR /white-win-api

COPY . /white-win-api

RUN pip3 install -r requirements.txt
