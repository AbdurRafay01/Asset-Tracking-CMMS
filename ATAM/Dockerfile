FROM python:3.10

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /ATAM/requirements.txt
RUN pip install -r /ATAM/requirements.txt

COPY . /ATAM/
WORKDIR /ATAM/

EXPOSE 8000
