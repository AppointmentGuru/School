FROM python:2.7
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code
WORKDIR /code

ADD requirements.txt /code/

RUN pip install -U pip
RUN pip install -r requirements.txt

ADD ./ansible /code