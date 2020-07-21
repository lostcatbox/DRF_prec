FROM python:3.7.6

COPY . /app
RUN pip install -r /app/requirements.txt
RUN chmod +x /app/start.sh
WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["/app/start.sh"]
