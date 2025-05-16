.PHONY: setup lint format test pre-commit help

help:
	@echo "Available commands:"
	@echo "  make setup      - Install dependencies and set up pre-commit hooks"
	@echo "  make lint       - Run linting with ruff"
	@echo "  make format     - Run code formatting with ruff"
	@echo "  make test       - Run tests with pytest"
	@echo "  make pre-commit - Install pre-commit hooks"

setup:
	uv sync
	pre-commit install

lint:
	ruff check .

format:
	ruff format .

test:
	pytest tests/

pre-commit:
	pre-commit install
