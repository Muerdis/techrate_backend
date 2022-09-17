FROM python:3.9

ARG APP_PORT

RUN mkdir /backend
WORKDIR /backend
ADD . /backend

EXPOSE $APP_PORT

RUN apt update

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install --no-cache-dir -r requirements.txt
