FROM python:3.9

RUN mkdir /backend
WORKDIR /backend
ADD . /backend

EXPOSE 8000

RUN apt update
RUN apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install --no-cache-dir -r requirements.txt
