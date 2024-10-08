FROM python:3.11.4-slim as base

WORKDIR /app

COPY . /app

RUN python3 -m pip install -r requirements.txt

EXPOSE 8080

CMD python3 -m flask run --host=0.0.0.0 --port=8080
