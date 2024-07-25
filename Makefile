# Projeto

srcdir = fast_zero
testdir = tests
migratedir = migrate


# Run

.PHONY: run

run:
	poetry run fastapi dev $(srcdir)/app.py


# Init

.PHONY: init init-python

init: init-python

init-python:
	poetry install --sync


# Format

.PHONY: fmt

fmt:
	poetry run ruff check --fix $(srcdir) $(testdir) $(migratedir)
	poetry run ruff format $(srcdir) $(testdir) $(migratedir)


# Lint

.PHONY: lint lint-poetry lint-ruff-format lint-ruff-check

lint: lint-poetry lint-ruff-format lint-ruff-check

lint-poetry:
	poetry check --lock

lint-ruff-format:
	poetry run ruff format --diff $(srcdir) $(testdir) $(migratedir)

lint-ruff-check:
	poetry run ruff check --diff $(srcdir) $(testdir) $(migratedir)


# Test

.PHONY: test test-pytest coverage-html

test: test-pytest

test-pytest:
	poetry run pytest $(testdir)

coverage-html: test-pytest
	poetry run coverage html


# Database

.PHONY: db-gen-migrate db-migrate

db-gen-migrate:
	poetry run alembic revision --autogenerate

db-migrate:
	poetry run alembic upgrade head


# Clean

.PHONY: clean

clean:
	find $(srcdir) $(testdir) $(migratedir) -name __pycache__ -exec rm -rf {} +
	find $(srcdir) $(testdir) $(migratedir) -type d -empty -delete
	rm -rf dist .ruff_cache .pytest_cache .coverage .coverage.* htmlcov
