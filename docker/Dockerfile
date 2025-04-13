FROM python:3.14.0a7-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk update && apk add build-base gcc libffi-dev libressl-dev
COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

RUN rm requirements.txt

RUN python main.py
