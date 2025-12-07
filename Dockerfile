FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y wkhtmltopdf && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

WORKDIR /app/IIC
RUN pip install --no-cache-dir -r requirements.txt

ENV WKHTMLTOPDF_CMD=/usr/local/bin/wkhtmltopdf
ENV PORT=8000
EXPOSE 8000

CMD ["sh", "-c", "gunicorn IIC.wsgi:application --bind 0.0.0.0:${PORT}"]
