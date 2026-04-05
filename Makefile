.PHONY: all fmt qa deps test changelog

all: fmt qa  deps test

fmt:
	ruff format
	ruff check --fix

qa:
	ruff check
	ty check

deps:
	pip-audit

test:
	pytest

dev:
	MUSICLIBRARY_DB=musiclibrary.db fastapi dev app.py --host 0.0.0.0

prod:
	fastapi run app.py

changelog:
	git-cliff -o CHANGELOG.md
