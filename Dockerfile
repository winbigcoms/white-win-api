FROM python:3.10.9

WORKDIR /white-win-api

COPY . /white-win-api

RUN pip3 install -r requirements.txt
