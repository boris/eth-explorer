FROM python:3.10-slim

RUN mkdir /app
EXPOSE 5000

RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY app /app

CMD flask --app ../app run --host=0.0.0.0
