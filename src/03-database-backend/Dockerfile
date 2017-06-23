FROM python:3.6

WORKDIR /app/
COPY requirements.txt /app/

RUN pip3 install -U pip \
    && pip3 install -r requirements.txt

ADD ./api/ /app/
