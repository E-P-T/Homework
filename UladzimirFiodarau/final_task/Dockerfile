# syntax=docker/dockerfile:1
FROM python:3.9.13-slim-buster
LABEL maintainer='ufiodarau@gmail.com'

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /
WORKDIR /src
COPY ./src /src
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir


EXPOSE 8000