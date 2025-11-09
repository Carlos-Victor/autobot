FROM python:3.13.3-alpine as builder

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk update && apk add build-base gcc libffi-dev libressl-dev cargo

COPY ./src .

RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

RUN rm requirements.txt

FROM python:3.13-alpine
WORKDIR /app
COPY --from=builder /install /usr/local
COPY ./src .
CMD ["python", "main.py"]
