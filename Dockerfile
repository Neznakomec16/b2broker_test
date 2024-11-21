FROM python:3.12-alpine AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.1

RUN apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev \
    python3-dev \
    postgresql-dev \
    gcc \
    libc-dev \
    linux-headers \
    mariadb-dev \
    mariadb-connector-c \
    bash \
    git \
    curl \
    && curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

#----------------------------------------------------------------
FROM python:3.12-alpine

RUN addgroup -S appgroup && \
    adduser -S appuser -G appgroup -h /home/appuser -s /bin/sh

WORKDIR /app

COPY --from=base /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=base /usr/local/bin/ /usr/local/bin/

COPY . /app/
WORKDIR /app/wallet_api/

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 8000