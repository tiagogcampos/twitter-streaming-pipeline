FROM python:3.9.12-slim AS py
FROM openjdk:8-jdk-slim

WORKDIR /app

COPY --from=py / /

COPY . .

ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=0

RUN ["pip", "install", "-r", "requirements.txt"]

RUN ["rm", "requirements.txt"]

ARG JARS_DIRECTORY "./jars/*"

COPY ${JARS_DIRECTORY} "/usr/local/lib/python3.9/site-packages/pyspark/jars/"

RUN rm -rf $JARS_DIRECTORY
RUN rm Dockerfile

CMD ["python", "main.py"]