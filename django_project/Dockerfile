FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD /wait-for-it/wait-for-it.sh .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /code/
