# Use a stable Python base image
FROM python:3.12-slim

# Prevent Python from writing .pyc files and use unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install wkhtmltopdf and system dependencies
RUN apt-get update && \
    apt-get install -y wkhtmltopdf && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy everything from repo into the container
COPY . .

# Go into the Django project folder that has manage.py
WORKDIR /app/IIC

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Environment variable for pdfkit/wkhtmltopdf
ENV WKHTMLTOPDF_CMD=/usr/bin/wkhtmltopdf

# Render provides PORT; default to 8000 for local tests
ENV PORT=8000

# Expose the port (mainly for local docker run; Render uses PORT env)
EXPOSE 8000

# Start Django with gunicorn
CMD ["sh", "-c", "gunicorn IIC.wsgi:application --bind 0.0.0.0:${PORT}"]
