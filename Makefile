.PHONY: test
test:
	pytest

.PHONY: lint
lint:
	mypy .
	flake8 .
	black --check .
	isort --recursive --check-only --diff .

.PHONY: fix_lint
fix_lint:
	black .
	isort --recursive .

.PHONY: test_and_lint
test_and_lint: test lint
