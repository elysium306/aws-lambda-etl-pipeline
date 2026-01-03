.PHONY: install test run clean

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

test:
	python -m pytest -q

run:
	python scripts/run_local.py

clean:
	rm -rf .venv .pytest_cache __pycache__ data
	find . -name "*.pyc" -delete
	find . -type d -name "__pycache__" -type d -exec rm -rf {} +
