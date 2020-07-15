FROM python:3.7.6

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY . /app
RUN pip install -r /app/requirements.txt
WORKDIR /app

EXPOSE 8000

CMD ["python","manage.py","makemigrations"]
CMD ["python","manage.py","migrate"]
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
