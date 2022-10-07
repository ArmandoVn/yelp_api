# syntax=docker/dockerfile:1
FROM python:3.10

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

WORKDIR /src

COPY ./Pipfile ./Pipfile.lock /src/
RUN pipenv install

COPY ./yelp /src/yelp
WORKDIR /src/yelp

ENTRYPOINT ["pipenv", "run"]
