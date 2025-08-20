.PHONY: all fmt test changelog

all: fmt test

fmt:
	ruff format
	ruff check --fix


test:
	pytest

dev:
	fastapi dev app.py --host 0.0.0.0

prod:
	fastapi run app.py

changelog:
	git-cliff -O CHANGELOG.md