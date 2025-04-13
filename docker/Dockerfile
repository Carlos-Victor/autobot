FROM python:3.13.3-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk update && apk add build-base gcc libffi-dev libressl-dev cargo

COPY ./src .

RUN pip install -r requirements.txt

RUN rm requirements.txt

CMD python main.py
