format:
	isort *.py
	black .

lint:
	pylint schulze -d C0103

typecheck:
	mypy --no-strict-optional --ignore-missing-imports -p schulze

test:
	pytest --cov-report term-missing --cov=schulze -vv

check: lint typecheck test

all: format check
