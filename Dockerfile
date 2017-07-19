FROM python:2.7
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code/ansible
WORKDIR /code

ADD requirements.txt /code/

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY ./ansible/*.yml /code/ansible/
COPY ./ansible/roles/ /etc/ansible/roles/
COPY ./ansible/inventory/digital_ocean.py /etc/ansible/inventory/digital_ocean.py
COPY ./ansible/library/ /etc/ansible/library/
