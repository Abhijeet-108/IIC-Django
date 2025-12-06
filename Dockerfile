FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies needed by wkhtmltopdf
RUN apt-get update && apt-get install -y \
    curl \
    xz-utils \
    libfontconfig1 \
    libfreetype6 \
    libjpeg62-turbo \
    libpng16-16 \
    libx11-6 \
    libxext6 \
    libxrender1 \
    xfonts-75dpi \
    xfonts-base \
 && rm -rf /var/lib/apt/lists/*

# Install official generic wkhtmltopdf binary
WORKDIR /tmp

RUN curl -L -o wkhtmltopdf.tar.xz \
      https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.amd64.tar.xz \
 && tar -xf wkhtmltopdf.tar.xz \
 && mv wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf \
 && chmod +x /usr/local/bin/wkhtmltopdf \
 && rm -rf wkhtmltox wkhtmltopdf.tar.xz


# Your existing stuff from here ↓
WORKDIR /app
COPY . .

WORKDIR /app/IIC
RUN pip install --no-cache-dir -r requirements.txt

ENV WKHTMLTOPDF_CMD=/usr/local/bin/wkhtmltopdf
ENV PORT=8000
EXPOSE 8000

CMD ["sh", "-c", "gunicorn IIC.wsgi:application --bind 0.0.0.0:${PORT}"]
