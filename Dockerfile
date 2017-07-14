FROM python:2.7
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code/ansible
WORKDIR /code

ADD requirements.txt /code/

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY ./ansible/*.yml /code/ansible/
COPY ./ansible/roles/ /etc/ansible/roles/
COPY ./ansible/library/ /etc/ansible/library/
COPY ./ansible/templates/ /etc/ansible/templates/
