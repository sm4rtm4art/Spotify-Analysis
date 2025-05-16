.PHONY: setup lint format test pre-commit help lint-notebooks

help:
	@echo "Available commands:"
	@echo "  make setup          - Install dependencies and set up pre-commit hooks"
	@echo "  make lint           - Run linting with ruff"
	@echo "  make format         - Run code formatting with ruff"
	@echo "  make lint-notebooks - Run linting on Jupyter notebooks with nbqa and ruff"
	@echo "  make test           - Run tests with pytest"
	@echo "  make pre-commit     - Install pre-commit hooks"

setup:
	uv sync
	pre-commit install

lint:
	ruff check .

format:
	ruff format .

lint-notebooks:
	nbqa ruff notebooks/

test:
	pytest tests/

pre-commit:
	pre-commit install
