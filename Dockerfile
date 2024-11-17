# Set Python runtime
FROM python:3.11.5-slim-bookworm AS backend_base

# Set maintainer
LABEL maintainer="Sean O'Leary <seamicole@gmail.com>"

# Set build-time environment variables
ARG BACKEND_SECRET_KEY
ENV BACKEND_SECRET_KEY=${BACKEND_SECRET_KEY}

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install PostgreSQL 16 client tools and other dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    libpq-dev \
    git \
    wget \
    gnupg2

# Add PostgreSQL APT repository to install the 16.x version of the client
RUN echo "deb http://apt.postgresql.org/pub/repos/apt bookworm-pgdg main" > /etc/apt/sources.list.d/pgdg.list \
    && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
    && apt-get update \
    && apt-get install -y postgresql-client-16

# Clean up APT when done
RUN rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man && apt-get clean

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Delete requirements.txt
RUN rm -f requirements.txt

# Copy the project files into the container
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Add and run as non-root user
RUN adduser --disabled-password --gecos '' appuser
RUN chown -R appuser:appuser /app

# Configure entrypoint
COPY entrypoints/beat.sh /usr/local/bin/
COPY entrypoints/web.sh /usr/local/bin/
COPY entrypoints/worker.sh /usr/local/bin/
