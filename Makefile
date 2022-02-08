install:
	poetry install
lint:
	poetry run flake8 gen_diff
test:
	poetry run pytest
test-coverage:
	poetry run pytest --cov=gen_diff --cov-report xml tests/
