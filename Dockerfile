FROM python:3.6

WORKDIR /app

RUN apt-get update && apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev
RUN pip install --upgrade pip && pip install tox
