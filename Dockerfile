FROM python:3.12-slim AS builder
ENV PYTHONUNBUFFERED=1

WORKDIR /app/
COPY pyproject.toml poetry.lock ./

RUN pip install --disable-pip-version-check --no-cache-dir poetry poetry-plugin-export

RUN poetry export -f requirements.txt -o requirements.txt


# Imagem

FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /app/
COPY --from=builder /app/requirements.txt ./
RUN pip install --disable-pip-version-check --no-cache-dir -r requirements.txt

COPY fast_zero ./fast_zero
COPY migrate ./migrate
COPY scripts/run-with-migrate.sh alembic.ini ./
RUN python -m compileall fast_zero migrate -f -j 0

EXPOSE 8000
CMD ["./run-with-migrate.sh"]
