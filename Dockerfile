FROM python:3.7
ADD . /src
WORKDIR /src
RUN apt-get update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt
