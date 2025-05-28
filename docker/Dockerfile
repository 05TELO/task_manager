FROM python:3.13-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

COPY ./pyproject.toml /pyproject.toml
RUN uv pip compile /pyproject.toml --group django --group dev -o /requirements.txt

FROM python:3.13-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apk add --no-cache curl

WORKDIR /app

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser


COPY --from=builder /requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./apps /app/apps
COPY ./core /app/core
COPY manage.py conftest.py pyproject.toml /app/
RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000