FROM python:3.9.12-slim

WORKDIR /app

COPY . .

ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=0

RUN ["pip", "install", "-r", "requirements.txt"]

RUN rm requirements.txt
RUN rm Dockerfile

CMD ["python", "main.py"]