# Projeto

srcdir = fast_zero
testdir = tests


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
	poetry run ruff check --fix $(srcdir) $(testdir)
	poetry run ruff format $(srcdir) $(testdir)


# Lint

.PHONY: lint lint-poetry lint-ruff-format lint-ruff-check

lint: lint-poetry lint-ruff-format lint-ruff-check

lint-poetry:
	poetry check --lock

lint-ruff-format:
	poetry run ruff format --diff $(srcdir) $(testdir)

lint-ruff-check:
	poetry run ruff check --diff $(srcdir) $(testdir)


# Test

.PHONY: test test-pytest coverage-html

test: test-pytest

test-pytest:
	poetry run pytest $(testdir)

coverage-html: test-pytest
	poetry run coverage html


# Clean

.PHONY: clean

clean:
	find $(srcdir) $(testdir) -name __pycache__ -exec rm -rf {} +
	find $(srcdir) $(testdir) -type d -empty -delete
	rm -rf dist .ruff_cache .pytest_cache .coverage .coverage.* htmlcov
