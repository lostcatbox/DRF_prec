FROM python:3.7.6

COPY . /app
RUN pip install -r /app/requirements.txt
WORKDIR /app

EXPOSE 8000

