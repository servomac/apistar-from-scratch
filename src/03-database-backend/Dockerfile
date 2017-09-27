FROM python:3.6

WORKDIR /app/
COPY requirements.txt /app/
COPY requirements-dev.txt /app/

RUN pip3 install -U pip \
    && pip3 install -r requirements.txt \
    && pip3 install -r requirements-dev.txt

ADD ./api/ /app/
