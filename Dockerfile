FROM python:3.11.4-slim as base

RUN python3 -m pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python3 -m flask run --host=0.0.0.0 --port=8000
