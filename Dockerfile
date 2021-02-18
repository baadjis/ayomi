FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /ayomi
ADD requirements.txt /ayomi/
RUN pip install -r requirements.txt
ADD . /ayomi/