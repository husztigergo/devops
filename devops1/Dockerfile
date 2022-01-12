FROM python:3.10.0-bullseye

WORKDIR /app
COPY main.py /app

RUN chmod +x /app/main.py

RUN pip install mysql-connector-python requests

ENTRYPOINT python3 /app/main.py