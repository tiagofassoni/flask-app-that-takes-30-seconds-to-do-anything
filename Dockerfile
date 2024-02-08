FROM python:3.11-bookworm

WORKDIR /code

COPY code/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
