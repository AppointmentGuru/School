FROM python:3.4

RUN mkdir -p /code
WORKDIR /code

ADD requirements.txt /code/

RUN pip install -U pip
RUN pip install -r requirements.txt

ADD ./ansible /code