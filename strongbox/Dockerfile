FROM python:3.10.11-alpine3.17
RUN apk --update --upgrade add --no-cache gcc postgresql musl-dev postgresql-dev
RUN python -m pip install --upgrade pip

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

