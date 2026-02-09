# Variables
PYTHON=python3
PIP=pip3
APP=main.py

.PHONY: all install lint format test coverage clean run dist check

# Default target
all: install lint test coverage

# Install dependencies
install:
	$(PIP) install -r requirements.txt

# Run linters
lint:
	flake8 .
	
# Auto-format code
format:
	black .

# Run tests
test:
	pytest tests/

# Run tests with coverage
coverage:
	coverage run -m pytest
	coverage report -m
	coverage html

# Remove cache and temporary files
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .mypy_cache .coverage dist/ build/ *.egg-info coverage.html htmlcov/

# Run the main app
run:
	$(PYTHON) $(APP)

# Package distribution
dist:
	$(PYTHON) setup.py sdist bdist_wheel

# Run everything needed before commit
check: format lint test coverage
