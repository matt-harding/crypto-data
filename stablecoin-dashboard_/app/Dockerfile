FROM python:3.9-slim-buster

WORKDIR /python-docker
RUN apt-get update
RUN apt-get install curl -y
COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app/. .

CMD [ "python3", "app.py"]