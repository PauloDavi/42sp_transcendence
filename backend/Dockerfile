FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

RUN chmod +x entrypoint.sh \
  && mkdir -p ./ssl \
  && openssl req -x509 -nodes -days 365 \
    -newkey rsa:2048 -keyout /app/ssl/django.key \
    -out ./ssl/django.crt \
    -subj "/C=BR/ST=SP/L=SP/O=42/CN=localhost"

ENTRYPOINT ["./entrypoint.sh"]
CMD ["gunicorn", "--certfile=/app/ssl/django.crt", "--keyfile=./ssl/django.key", "--bind", "0.0.0.0:443", "setup.wsgi:application"]
